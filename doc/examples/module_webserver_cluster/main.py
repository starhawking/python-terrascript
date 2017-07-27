# Here the PROD variable is hard-coded. In a real setup this could be
# a command line argument.
#
PROD=False

from terrascript import *
import terrascript.aws.r as r
import terrascript.aws.d as d

USER_DATA = """#!/bin/bash

cat > index.html <<EOF
<h1>Hello, World</h1>
EOF

nohup busybox httpd -f -p "{{}}" &
"""


def webserver_cluster(cluster_name, instance_type='t2.micro', server_port=8080, 
                      min_size=2, max_size=2):
    """webserver_cluster module."""

    # Security Group for Elastic Load Balanacer
    #
    sg_elb = r.aws_security_group('elb', name='{}-elb'.format(cluster_name))

    r.aws_security_group_rule('allow_http_inbound', security_group_id=sg_elb.id,
                              type='ingress', from_port=80, to_port=80,
                              protocol='tcp', cidr_blocks = ["0.0.0.0/0"])

    r.aws_security_group_rule('allow_all_outbound', security_group_id=sg_elb.id,
                              type='egress', from_port=0, to_port=0,
                              protocol='-1', cidr_blocks = ["0.0.0.0/0"])

    # Security Group for EC2 instance
    #
    sg_inst =  r.aws_security_group('instance', name='{}-instance'.format(cluster_name))

    r.aws_security_group_rule('allow_server_http_inbound', security_group_id=sg_inst.id,
                              type='ingress', from_port=server_port, to_port=server_port,
                              protocol='tcp', cidr_blocks = ["0.0.0.0/0"])

    # Render user_data.
    #
    template_file = USER_DATA.format(server_port)


    # Launch configuration
    #
    launch_config = r.aws_launch_configuration('example', image_id='ami-40d28157',
                                               instance_type=instance_type,
                                               security_groups=[sg_inst.id],
                                               user_data=template_file,
                                               lifecycle={
                                                   'create_before_destroy': True
                                               })


    # Availability zones
    #
    az = d.aws_availability_zones('all')


    # Elsatic Load Balancar
    #
    elb = r.aws_elb('example', name=cluster_name,
                    availability_zones=[az.names],
                    security_groups=[sg_elb.id],
                    listener=[{
                        'lb_port': 80,
                        'lb_protocol': 'HTTP',
                        'instance_port': server_port,
                        'instance_protocol': 'HTTP'
                    }],
                    health_check=[{
                        'healthy_threshold': 2,
                        'unhealthy_threshold': 2,
                        'timeout': 3,
                        'interval': 30,
                        'target': 'HTTP:{}/'.format(server_port)
                    }])


    # Autoscaling Group
    #
    asg = r.aws_autoscaling_group('example', launch_configuration=launch_config.id,
                                  availability_zones=[az.names],
                                  load_balancers=[elb.name],
                                  health_check_type='ELB',
                                  min_size=min_size,
                                  max_size=max_size,
                                  tag=[{
                                      'key': 'Name',
                                      'value': cluster_name,
                                      'propagate_at_launch': True
                                  }])


    return elb, asg, sg_elb



terraform(required_version='>=0.9')

provider('aws', region='us-east-1')

if PROD:
    cluster_name = 'webservers-prod'
    instance_type = 'm4.large'
    min_size = 2
    max_size = 10
else:
    cluster_name = 'webservers-stage'
    instance_type = 't2.micro'
    min_size = 2
    max_size = 2

# Call the "module"
#
elb, asg, sg_elb = webserver_cluster(cluster_name, instance_type=instance_type,
                                     min_size=min_size, max_size=max_size)


if PROD:

    r.aws_autoscaling_schedule('scale_out_during_business_hours',
                               scheduled_action_name='scale_out_during_business_hours',
                               min_size=2,
                               max_size=10,
                               desired_capacity=10,
                               recurrence='0 9 * * *',
                               autoscaling_group_name=asg.name)

    r.aws_autoscaling_schedule('scale_in_at_night',
                               scheduled_action_name='scale_in_at_night',
                               min_size=2,
                               max_size=10,
                               desired_capacity=2,
                               recurrence='0 17 * * *',
                               autoscaling_group_name=asg.name)

else:

    r.aws_security_group_rule('allow_testing_inbound',
                              type='ingress',
                              security_group_id=sg_elb.id,
                              from_port=12345,
                              to_port=12345,
                              protocol='tcp',
                              cidr_blocks=['0.0.0.0/0'])

# Output
#
output('elb_dns_name', value=elb.dns_name)

print(dump())

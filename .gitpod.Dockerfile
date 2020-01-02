FROM gitpod/workspace-full:latest

USER root

# Fetch Terraform binary
RUN curl -O /tmp/terraform.zip https://releases.hashicorp.com/terraform/0.12.18/terraform_0.12.18_linux_amd64.zip \
    unzip /tmp/terraform.zip \
    install -m 0755 /tmp/terraform /usr/local/bin/terraform

USER gitpod

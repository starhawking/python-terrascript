#!/usr/bin/env python3

"""Auto-generate terrascript/PROVIDER/{r,d}.py files."""

import glob
import collections
import os
import os.path
import sys
import time

PREFIX = 'terrascript'

thisdir = os.path.abspath('.')
if not os.path.isdir(os.path.join(thisdir, PREFIX)):
    print('Script must be run from python-terrascript folder')
    sys.exit(1)

paths = [p for p in glob.glob('terraform-providers/*/*/*.go')
        if not p.endswith('test.go') and ('/resource_' in p or '/data_source_' in p)]

paths.sort()

# Dictionary as {PROVIDER: ([RESOURCE, ...],[DATA, ...])}
data = collections.defaultdict(lambda : ([],[]))

for path in paths:
    
    # Split path into components, e.g.
    # 'terraform-providers/aws/aws/resource_aws_instance.go' -> provider='aws', class_='resource_aws_instance.go'
    x,y,provider,class_ = path.split('/')

    # Strip '.go' suffix
    class_ = class_.split('.')[0]
    
    # Split the class_ and name (type_) of the resource/data source.
    # 'resource_arm_dns_zone' -> ('resource', 'dns_zone')
    # 'data_source_arm_client_config' -> ('data', 'client_config')
    if class_.startswith('resource'):
        class_, type_ = class_.split('_')[0], '_'.join(class_.split('_')[2:])
    else:
        class_, type_ = class_.split('_')[0], '_'.join(class_.split('_')[3:])

    if class_ == 'resource':
        data[provider][0].append(type_)
    else:
        data[provider][1].append(type_)
        
    # if class_.startswith('resource_'):
    #     class_ = class_[len('resource_'):]
    #     if not class_.startswith(provider + '_'):
    #         class_ = provider + '_' + class_
    #     data[provider][0].append(class_)
    # else:
    #     class_ = class_[len('data_source_'):]
    #     if not class_.startswith(provider + '_'):
    #         class_ = provider + '_' + class_
    #     data[provider][1].append(class_)

# Create Python modules
#
for provider,v in data.items():
    provider_path = os.path.join(thisdir, PREFIX, provider)
    provider_init_path = os.path.join(thisdir, PREFIX, provider, '__init__.py')
    resource_path = os.path.join(provider_path, 'r.py')
    data_path = os.path.join(provider_path, 'd.py')

    if not os.path.exists(provider_path):
        os.mkdir(provider_path)

    with open(provider_init_path, 'w') as fp:
        fp.write('"""' + time.strftime('%Y-%m-%d %H:%M:%S') + '"""' + '\n')

    print(resource_path)
    with open(resource_path, 'w') as fp:
        fp.write('from terrascript import _resource\n')
        for type_ in v[0]:
            fp.write('class {}_{}(_resource): pass\n'.format(provider, type_))
            fp.write('{} = {}_{}\n\n'.format(type_, provider, type_))
            
    print(data_path)
    with open(data_path, 'w') as fp:
        fp.write('from terrascript import _data\n')
        for type_ in v[1]:
            fp.write('class {}_{}(_data): pass\n'.format(provider, type_))
            fp.write('{} = {}_{}\n\n'.format(type_, provider, type_))


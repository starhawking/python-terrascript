#!/usr/bin/env python3 

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
    x,y,provider,klass = path.split('/')

    # Strip '.go' suffix
    klass = klass.split('.')[0]

    if klass.startswith('resource_'):
        klass = klass[len('resource_'):]
        if not klass.startswith(provider + '_'):
            klass = provider + '_' + klass
        data[provider][0].append(klass)
    else:
        klass = klass[len('data_source_'):]
        if not klass.startswith(provider + '_'):
            klass = provider + '_' + klass
        data[provider][1].append(klass)

# Create Python modules
#
for provider,v in data.items():
    provider_path = os.path.join(thisdir, PREFIX, provider)
    provider_init_path = os.path.join(thisdir, PREFIX, provider, '__init__.py')
    resource_path = os.path.join(provider_path, 'r.py')
    data_path = os.path.join(provider_path, 'd.py')

    if not os.path.exists(provider_path):
        os.mkdir(provider_path)
        # TODO: create __init__.py

    with open(provider_init_path, 'w') as fp:
        fp.write('"""' + time.strftime('%Y-%m-%d %H:%M:%S') + '"""' + '\n')

    print(resource_path)
    with open(resource_path, 'w') as fp:
        fp.write('from terrascript import _resource\n')
        for resource in v[0]:
            fp.write('class {}(_resource): pass\n'.format(resource))
            fp.write('{} = {}\n\n'.format(resource[len(provider)+1:], resource))

    print(data_path)
    with open(data_path, 'w') as fp:
        fp.write('from terrascript import _data\n')
        for data in v[1]:
            fp.write('class {}(_data): pass\n'.format(data))
            fp.write('{} = {}\n\n'.format(data[len(provider)+1:], data))

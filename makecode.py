#!/usr/bin/env python3

"""Auto-generate terrascript/PROVIDER/{r,d}.py files."""

import glob
import collections
import os
import os.path
import sys
import time
import re
import github3
import base64

PREFIX = 'terrascript'
REPO_OWNER = 'terraform-providers'
PROVIDERS = [
    'aws',
    'azurerm',
    'google',
    'template'
]
PROVIDERS.sort()


REGEX = re.compile(b'".*?_(?P<type_>.+)":\s+(?P<class_>resource|data)')
#"azurerm_traffic_manager_profile":   resourceArmTrafficManagerProfile(),

try:
    # Travis-CI
    TOKEN = os.environ['GITHUB_TOKEN']
except KeyError:
    # @home
    TOKEN = open('GITHUB_TOKEN').read().strip()

thisdir = os.path.abspath('.')
if not os.path.isdir(os.path.join(thisdir, PREFIX)):
    print('Script must be run from python-terrascript folder')
    sys.exit(1)


gh = github3.login(token=TOKEN)
for provider in PROVIDERS:
    print(provider)
    reponame = 'terraform-provider-{}'.format(provider)
    repo = gh.repository(REPO_OWNER, reponame)
    branch = repo.branch(repo.default_branch)
    commit = branch.commit
    tree = repo.tree(commit.sha)

    regex = re.compile('^'+provider+'/provider.go')
    provider_go_hash = [h for h in tree.recurse().tree
                       if regex.match(h.path)][0]

    provider_go_blob = repo.blob(provider_go_hash.sha)
    decoded = base64.b64decode(provider_go_blob.content)

    provider_path = os.path.join(thisdir, PREFIX, provider)
    provider_init_path = os.path.join(thisdir, PREFIX, provider, '__init__.py')
    resource_path = os.path.join(provider_path, 'r.py')
    data_path = os.path.join(provider_path, 'd.py')

    if not os.path.exists(provider_path):
        os.mkdir(provider_path)

    with open(provider_init_path, 'w') as fp:
        fp.write('"""' + time.strftime('%Y-%m-%d %H:%M:%S') + '"""' + '\n')

    with open(resource_path, 'w') as fpr:
        fpr.write('from terrascript import _resource\n')

        with open(data_path, 'w') as fpd:
            fpd.write('from terrascript import _data\n')

            for m in REGEX.finditer(decoded):
                type_ = m.group('type_').decode('utf-8')
                class_ = m.group('class_').decode('utf-8')

                if class_ == 'resource':
                    fpr.write('class {}_{}(_resource): pass\n'.format(provider, type_))
                    fpr.write('{} = {}_{}\n\n'.format(type_, provider, type_))
                else:
                    fpd.write('class {}_{}(_data): pass\n'.format(provider, type_))
                    fpd.write('{} = {}_{}\n\n'.format(type_, provider, type_))


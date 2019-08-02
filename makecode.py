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
PROVIDERS = [p.strip() for p in open('PROVIDERS').read().split('\n') if p]
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
    provider_snake_case = provider.replace('-', '_')
    reponame = 'terraform-provider-{}'.format(provider)
    repo = gh.repository(REPO_OWNER, reponame)
    branch = repo.branch(repo.default_branch)
    commit = branch.commit
    tree = repo.tree(commit.sha)

    regex = re.compile('^'+provider+'/provider.go')

    recursed_tree = tree.recurse().tree
    provider_go_hash = [h for h in recursed_tree
                        if regex.match(h.path)][0]
    generated_go_hashes = [h for h in recursed_tree if h.path.endswith("_gen.go") and h.path.startswith(provider + '/')]

    provider_go_blob = repo.blob(provider_go_hash.sha)
    generated_go_blobs = [repo.blob(hash_.sha) for hash_ in generated_go_hashes]
    decoded = base64.b64decode(provider_go_blob.content) + b''.join(base64.b64decode(g.content) for g in generated_go_blobs)

    provider_path = os.path.join(thisdir, PREFIX, provider_snake_case)
    provider_init_path = os.path.join(thisdir, PREFIX, provider_snake_case, '__init__.py')
    resource_path = os.path.join(provider_path, 'r.py')
    data_path = os.path.join(provider_path, 'd.py')

    if not os.path.exists(provider_path):
        os.mkdir(provider_path)

    with open(provider_init_path, 'w') as fp:
        fp.write('"""' + time.strftime('%Y-%m-%d %H:%M:%S') + '"""' + '\n')

    with open(resource_path, 'w') as fpr:
        fpr.write('from terrascript import Resource\n')

        with open(data_path, 'w') as fpd:
            fpd.write('from terrascript import Data\n')

            for m in REGEX.finditer(decoded):
                type_ = m.group('type_').decode('utf-8')
                class_ = m.group('class_').decode('utf-8')

                if provider == 'google-beta':
                    block_name = 'google_{}'.format(type_)
                else:
                    block_name = '{}_{}'.format(provider_snake_case, type_)

                if class_ == 'resource':
                    fpr.write('class {}(Resource):\n'.format(block_name))
                    fpr.write("    def __init__(self, _label, **kwargs): super().__init__('{}', _label, **kwargs)\n".format(block_name))
                    fpr.write('{} = {}\n\n'.format(type_, block_name))
                else:
                    fpd.write('class {}(Data):\n'.format(block_name))
                    fpd.write("    def __init__(self, _label, **kwargs): super().__init__('{}', _label, **kwargs)\n".format(block_name))
                    fpd.write('{} = {}\n\n'.format(type_, block_name))

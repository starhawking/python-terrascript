"""Functions shared by all test modules."""

import json
import os

def assert_equals_json(object, path):
    """Compare a (dictionary) object with the content of a JSON file.

       Comparison is actually done by comparing two JSON string based on
       https://medium.com/@stschindler/comparing-nested-python-dictionaries-with-no-hassle-9ffe35ae076e
       
       Normally one must not sort the keys (``sort_keys=True``) as this may
       result in code Terraform will reject. In this case for the purpose of
       simple string conversion sorting of dictionary keys is necessary.

       Indentation is not strictly necessary but makes debugging easier when
       running ``nosetests`` with the ``--pdb`` option.

           (Pdb) print(s1)
           (Pdb) print(s2)

    """

    # Convert `object` into JSON string with sorted keys.
    s1 = json.dumps(object, sort_keys=True, indent=2)
    s1 = str(object)

    # Convert content of `path` into JSON string with sorted keys.
    with open(os.path.join('tests', 'configs', path), 'rt') as fp:
        s2 = json.dumps(json.load(fp), sort_keys=True, indent=2)

    assert s1 == s2
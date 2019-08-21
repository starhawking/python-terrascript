"""Functions shared by all test modules."""

import json
import os

def assert_equals_json(object, path):
    """Compare a (dictionary) object with the content of a JSON file.

       Comparison is actually done by comparing two JSON string based on
       https://medium.com/@stschindler/comparing-nested-python-dictionaries-with-no-hassle-9ffe35ae076e

       Indentation is not strictly necessary but makes debugging easier when
       running ``nosetests`` with the ``--pdb`` option.

           (Pdb) print(s1, '\n---\n', s2)

    """

    # Convert `object` into JSON string with sorted keys.
    s1 = json.dumps(object, sort_keys=True, indent=2)

    # Convert content of `path` into JSON string with sorted keys.
    with open(os.path.join('tests', 'configs', path), 'rt') as fp:
        s2 = json.dumps(json.load(fp), sort_keys=True, indent=2)

    assert s1 == s2
"""Functions shared by all test modules."""

import deepdiff
import json
import os
import sys


if sys.version_info >= (3, 5):
    # JSONDecodeError was introduced in python 3.5
    # https://docs.python.org/3/library/json.html#json.JSONDecodeError
    JSONDecodeError = json.decoder.JSONDecodeError
else:
    JSONDecodeError = ValueError


def assert_deep_equal(t1, t2):
    """Compare ``t1`` with the JSON structure parsed from ``path``.

       Comparison is performed through the DeepDiff Python package
       (https://github.com/seperman/deepdiff).

       The ``diffs`` variable will contain any differences which
       can be displayed in the debugger.

           (Pdb) pp(diffs)

    """

    t1 = json.loads(str(t1))

    try:
        t2 = json.loads(t2)
    except JSONDecodeError:
        with open(os.path.join('tests', 'configs', t2), 'rt') as fp:
            t2 = json.load(fp)

    diffs = deepdiff.DeepDiff(t1, t2)

    assert diffs == {}


# For tests where the call has not been renamed yet.
assert_equals_json = assert_deep_equal

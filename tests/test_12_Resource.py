
import json

from terrascript import *

from nose.tools import *


class Test_Resource(object):
    def setup(self):
        self.resource = Resource('dummy', 'label', arg1='val1', arg2='val2')

    def test_instanceResource(self):
        assert isinstance(self.resource, Resource)

    def test_labels(self):
        assert self.resource._labels == ('dummy', 'label')

    def test_args(self):
        assert self.resource._args == {'arg1': 'val1', 'arg2': 'val2'}

    def test_str(self):
        assert json.loads(str(self.resource)) == self.resource._args


@raises(TypeError)
def test_resource_missing_label():
    Resource(arg1='arg1', arg2='arg2')

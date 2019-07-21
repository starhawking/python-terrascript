
import collections.abc

import json

from terrascript import *

from nose.tools import *


class Test_Block(object):
    def setup(self):
        self.block = Block('label1', 'label2', arg1='val1', arg2='val2')

    def test_instance_MutableMapping(self):
        assert isinstance(self.block, collections.abc.MutableMapping)
        
    def test_MutableMapping_getitem(self):
        assert self.block['arg1'] == 'val1'
        
    def test_MutableMapping_setitem(self):
        self.block['arg3'] = 'val3'
        assert self.block['arg3'] == 'val3'
        
    ##@raises(KeyError)
    def test_MutableMapping_delitem(self):
        del(self.block['arg1'])
        assert 'arg1' not in self.block
        
    def test_MutableMapping_len(self):
        len(self.block) == 2
        
    def test_MutableMapping_iter(self):
        for arg in self.block:
            arg in ('arg1', 'arg2',)
            
    def test_MutableMapping_keys(self):
        for arg in ('arg1', 'arg2'):
            assert arg in self.block.keys()
        
    def test_MutableMapping_values(self):
        for val in ('val1', 'val2'):
            assert val in self.block.values()
            
    def test_MutableMapping_items(self):
        # TODO: How to test dict_items([('arg2', 'val2'), ('arg1', 'val1')]) ???
        assert self.block.items() is not None

    def test_instance_Block(self):
        assert isinstance(self.block, Block)
        assert hasattr(self.block, '_labels')
        
    def test_labels(self):
        assert isinstance(self.block._labels, tuple)
        assert len(self.block._labels) == 2
        assert self.block._labels == ('label1', 'label2', )

    def test_args(self):
        assert isinstance(self.block, dict)
        assert self.block == {'arg1': 'val1', 'arg2': 'val2'}

    def test_len(self):
        len(self.block) == 2
        
    def test_str(self):
        assert json.loads(str(self.block)) == self.block

import json

from terrascript import Terrascript, Data


class Test_Data:
    def setup(self):
        self.config = Terrascript()

    def test_repr(self):
        assert repr(Data('foo', 'bar')) == 'data.foo.bar'

    def test_data(self):
        data = Data('foo', 'bar', baz='qux')
        self.config += data
        assert dict(self.config) == {
            'data': {
                'foo': {
                    'bar': {
                        'baz': 'qux'
                    }
                }
            }
        }

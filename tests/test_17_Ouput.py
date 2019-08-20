import json

from terrascript import Terrascript, Output


class Test_Output:
    def setup(self):
        self.config = Terrascript()

    def test_output(self):
        output = Output('foo', 'bar')
        self.config += output
        assert dict(self.config) == {
            'output': {
                'foo': {
                    'value': 'bar'
                }
            }
        }

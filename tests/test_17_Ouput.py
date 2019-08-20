import json

from terrascript import Terrascript, Output


class Test_Output:
    def setup(self):
        self.config = Terrascript()

    def test_output(self):
        output = Output('foo', 'bar')
        self.config += output
        assert str(self.config) == json.dumps({
            'output': {
                'foo': {
                    'value': 'bar'
                }
            }
        })

import sys
import tempfile

class Base(object):
    def setup(self):
        sys.stdout = self._stdout = tempfile.NamedTemporaryFile('w+', delete=False,
                                                                prefix='terrascript.')

        sys.stderr.write(self._stdout.name + ' ')

    def teardown(self):
        self._stdout.close()
        sys.stdout = sys.__stdout__

    @property
    def stdout(self):
        self._stdout.seek(0)
        return self._stdout.read()[:-1]    # Remove trailing \n:w

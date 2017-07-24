"""
Terraform interpolation functions.

"""

class _function(object):
    
    def __init__(self, *args):
        self.args = args
        
    def __repr__(self):
        return '${{{}({})}}'.format(self.__class__.__name__, ','.join([str(i).lstrip('$').lstrip('{').rstrip('}') for i in self.args]))


class lookup(_function):
    pass

class file(_function):
    pass

from abc import ABC, abstractproperty


class ReferenceMixin(ABC):
    @abstractproperty
    def ref_list(self):
        ...

    def __repr__(self):
        ref_list = list(self.ref_list)
        return self.interpolated if ref_list[0] == 'var' else self.fullname

    @property
    def fullname(self):
        return '.'.join(self.ref_list)

    @property
    def interpolated(self):
        """The object in interpolated syntax: ``${...}``."""
        return '${{{}}}'.format(self.fullname)

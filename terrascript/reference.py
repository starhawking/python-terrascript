from abc import ABC, abstractproperty


class ReferenceMixin(ABC):

    @abstractproperty
    def ref_list(self):
        ...

    @property
    def is_var(self):
        return next(iter(self.ref_list)) == 'var'

    def __repr__(self):
        return self.interpolated if self.is_var else self.fullname

    @property
    def fullname(self):
        return '.'.join(self.ref_list)

    @staticmethod
    def _interpolate(s):
        """Interpolated syntax: ``${...}``."""
        return '${{{}}}'.format(s)

    @property
    def interpolated(self):
        """The object in interpolated syntax: ``${...}``."""
        return self._interpolate(self.fullname)

    def __getattr__(self, item):
        """Get the terraform attribute of the object,
        e.g. ``google_compute_address.my_address.ip_version``
        """
        s = "{}.{}".format(self.fullname, item)
        return self._interpolate(s) if self.is_var else s

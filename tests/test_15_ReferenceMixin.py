from terrascript import Resource, Terrascript
from terrascript.reference import ReferenceMixin


class Variable(ReferenceMixin):
    @property
    def ref_list(self):
        return ["var", "foo"]


class Data(ReferenceMixin):
    @property
    def ref_list(self):
        return ["data", "foo", "bar"]


class Test_ReferenceMixin:
    def setup(self):
        self.config = Terrascript()

    def test_reference_mixin(self):
        data = Data()
        assert data.interpolated == "${data.foo.bar}"
        assert data.fullname == "data.foo.bar"
        assert repr(data) == data.fullname

    def test_reference_mixin_variable(self):
        var = Variable()
        assert var.interpolated == "${var.foo}"
        assert var.fullname == "var.foo"
        assert repr(var) == var.interpolated

    def test_depends_on(self):
        r = Resource("type", "name")
        self.config += r
        self.config += Resource("type", "name2", depends_on=[r])
        assert self.config["resource"]["type"]["name2"]["depends_on"] == [repr(r)]

    def test_get_attr(self):
        assert Data().some_attr == "data.foo.bar.some_attr"

    def test_get_attr_variable(self):
        assert Variable().some_attr == "${var.foo.some_attr}"

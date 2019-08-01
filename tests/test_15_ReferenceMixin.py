from typing import Iterable

from terrascript import Terrascript, ReferenceMixin, Resource


class Test_ReferenceMixin:
    def setup(self):
        self.config = Terrascript()

    def test_reference_mixin(self):
        class Data(ReferenceMixin):
            @property
            def ref_list(self) -> Iterable[str]:
                return ["data", "foo", "bar"]

        data = Data()
        assert data.interpolated == "${data.foo.bar}"
        assert data.fullname == "data.foo.bar"
        assert repr(data) == data.fullname

    def test_reference_mixin_variable(self):
        class Variable(ReferenceMixin):
            @property
            def ref_list(self) -> Iterable[str]:
                return ["var", "foo"]

        var = Variable()
        assert var.interpolated == "${var.foo}"
        assert var.fullname == "var.foo"
        assert repr(var) == var.interpolated

    def test_depends_on(self):
        r = Resource("type", "name")
        self.config += r
        self.config += Resource("type", "name2", depends_on=[r])
        assert self.config["resource"]["type"]["name2"]["depends_on"] == [repr(r)]

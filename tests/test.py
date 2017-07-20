
from base import Base

from  terrascript.aws import r


TEST_STRING = """
resource "aws_instance" "NAME" {
  argument = "STRING"
}
"""

TEST_BOOL = """
resource "aws_instance" "NAME" {
  argument = false
}
"""

TEST_INT = """
resource "aws_instance" "NAME" {
  argument = 10
}
"""

TEST_FLOAT = """
resource "aws_instance" "NAME" {
  argument = 3.1415
}
"""

TEST_LIST = """
resource "aws_instance" "NAME" {
  argument = ["a", "b", "c"]
}
"""

TEST_DICT = """
resource "aws_instance" "NAME" {
  argument = {
    a = "a"
    b = "b"
  }
}
"""

# The exact output depends on the 
TEST_MIXED = """
resource "aws_instance" "NAME" {
  argument = {
    int = 10
    list = ["a", "b", "c"]
    float = 3.1415
    bool = true
    string = "STRING"
  }
}
"""

class TestTypes(Base):

    def test_string(self):
        r.aws_instance("NAME", argument='STRING')
        assert self.stdout.strip() == TEST_STRING.strip()

    def test_bool(self):
        r.aws_instance("NAME", argument=False)
        assert self.stdout.strip() == TEST_BOOL.strip()

    def test_int(self):
        r.aws_instance("NAME", argument=10)
        assert self.stdout.strip() == TEST_INT.strip()

    def test_float(self):
        r.aws_instance("NAME", argument=3.1415)
        assert self.stdout.strip() == TEST_FLOAT.strip()

    def test_list(self):
        r.aws_instance("NAME", argument=['a', 'b', 'c'])
        assert self.stdout.strip() == TEST_LIST.strip()

    def test_dict(self):
        r.aws_instance("NAME", argument={'a': 'a', 'b': 'b'})
        assert self.stdout.strip() == TEST_DICT.strip()

    def test_mixed(self):
        a = {'string': 'STRING',
             'bool': True,
             'int': 10,
             'float': 3.1415,
             'list': ['a', 'b', 'c'],
             # 'dict' not supported!
             }
        r.aws_instance("NAME", argument=a)
        assert self.stdout.strip() == TEST_MIXED.strip()

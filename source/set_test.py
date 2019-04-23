#!python3

from set import MySet as InheritSet
import unittest

class SetTest(unittest.TestCase):
    def test_init_with_elements(self):
        names = ["Winnie", "Kojin", "Brian", "Nabil", "Julia", "Alex", "Nick"]
        s = InheritSet()
        # assert s.size == 0
        s = InheritSet(names)
        # assert s.size == 7
        assert (names[0] in s) is True
        assert (names[2] in s) is True
        assert (names[5] in s) is True
    
    def test_init_without_elements(self):
        s = InheritSet()
        # assert s.size == 0
        s.add('hello')
        assert ('hello' in s) is True

    def test_contains(self):
        pass

        

#!python3

from set import MySet as mySet
import unittest

class SetTest(unittest.TestCase):
    def test_init_with_elements(self):
        names = ["Winnie", "Kojin", "Brian", "Nabil", "Julia", "Alex", "Nick"]
        s = mySet()
        assert s.size == 0
        s = mySet(names)
        assert s.size == 7
        assert (names[0] in s) is True
        assert (names[2] in s) is True
        assert (names[5] in s) is True
    
    def test_init_without_elements(self):
        s = mySet()
        assert s.size == 0
        assert len(s.container) == 0

    def test_contains(self):
        names = ["Winnie", "Kojin", "Brian", "Nabil", "Julia", "Alex", "Nick"]
        s = mySet()
        assert s.size == 0
        s = mySet(names)
        assert s.size == 7
        assert (names[0] in s) is True
        assert (names[2] in s) is True
        assert (names[5] in s) is True

    def test_add(self):
        s = mySet()
        assert s.size == 0
        assert len(s.container) == 0
        s.add("something")
        assert s.size == 1
        self.assertCountEqual(s.container.keys(), ["something"])
        s.add("another")
        assert s.size == 2
        self.assertCountEqual(s.container.keys(), ["something", "another"])
        
    def test_remove(self):
        names = ["Winnie", "Kojin", "Brian", "Nabil", "Julia", "Alex", "Nick"]
        s = mySet(names)
        assert s.size == 7
        s.remove("Winnie")
        assert s.size == 6
        assert ("Winnie" in s) is False
        
    def test_intersection(self):
        names = ["Winnie", "Kojin", "Brian", "Nabil", "Julia", "Alex", "Nick"]
        names2 = ["Jack", "Jeremy", "Jake", "Jayce", "Julia", "Alex"]
        s1 = mySet(names)
        s2 = mySet(names2)
        assert s1.size == 7
        assert s2.size == 6
        s1_s2_inter = s1.intersection(s2)
        assert s1_s2_inter.size == 2
        assert ("Julia" in s1_s2_inter) is True
        assert ("Alex" in s1_s2_inter) is True
        assert ("Jeremy" in s1_s2_inter) is False
        assert ("Jayce" in s1_s2_inter) is False
        assert ("Winnie" in s1_s2_inter) is False
        assert ("Brian" in s1_s2_inter) is False

    def test_union(self):
        names = ["Winnie", "Kojin", "Brian", "Nabil", "Julia", "Alex", "Nick"]
        names2 = ["Jack", "Jeremy", "Jake", "Jayce", "Julia", "Alex"]
        s1 = mySet(names)
        s2 = mySet(names2)
        assert s1.size == 7
        assert s2.size == 6
        union = s1.union(s2)
        assert union.size == 11     
        assert ("Julia" in union) is True
        assert ("Jeremy" in union) is True
        assert ("Jayce" in union) is True
        assert ("Winnie" in union) is True
        assert ("Brian" in union) is True
    
    def test_difference(self):
        names = ["Winnie", "Kojin", "Brian", "Nabil", "Julia", "Alex", "Nick"]
        names2 = ["Jack", "Jeremy", "Jake", "Jayce", "Julia", "Alex"]
        s1 = mySet(names)
        s2 = mySet(names2)
        diff1 = s1.difference(s2)
        diff2 = s2.difference(s1)
        assert diff1.size == 5
        assert diff2.size == 4
        assert ("Julia" in diff1) is False
        assert ("Winnie" in diff1) is True
        assert ("Kojin" in diff1) is True

        assert ("Alex" in diff2) is False
        assert ("Jeremy" in diff2) is True
        assert ("Jayce" in diff2) is True
    
    def test_is_subset(self):
        names = ["Winnie", "Kojin", "Brian", "Nabil", "Julia", "Alex", "Nick"]
        names2 = ["Jack", "Jeremy", "Jake", "Jayce", "Julia", "Alex"]
        s1 = mySet(names)
        s2 = mySet(names2)
        assert s1.size == 7
        assert s2.size == 6
        union = s1.union(s2)
        assert union.size == 11     
        assert s1.is_subset(union) is True
        assert s2.is_subset(union) is True
        names3 = ["this", "that", "thing"]
        s3 = mySet(names3)
        assert s3.is_subset(union) is False

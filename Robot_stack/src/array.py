'''
Created on 22 Jul 2017

@author: annub
'''
import unittest
from src.Stack import stack

class TestArrayStack(unittest.TestCase):

    def test_get_top(self):
        a = stack(7,[1,3,5,4,3,2])
        a.get_top()
        self.assertTrue(a.get_top()==2)
        
    def test_pushing(self):
        a = stack(7,[1,3,5,4,3,2])
        a.pushing(9)
        self.assertTrue(a.get_top()==9)
        
    def test_popping(self):
        a = stack(5,[12,2,43,1])
        a.poping()
        self.assertTrue(a.get_top()==43)
        
    def test_get_stack(self):
        a = stack(7,[1,3,5,4,3,2])
        self.assertTrue(a.get_stack()==[1,3,5,4,3,2])
        
    
        
    
if __name__ == '__main__':
    unittest.main()
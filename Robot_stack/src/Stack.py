'''
Created on 22 Jul 2017

@author: annub
'''
class stack():
    
    def __init__(self,size):
        my_array=[]
        m=len(my_array)
        if(m>=1):
            self.__first = my_array[m-1]
            self.__bottom=my_array[0]
        else:
            self.__first=None
            self.__bottom=None
        self.__my_stack = my_array
        self.__size=size
        self.__length= len(self.__my_stack)


    def get_top(self):
        return self.__first
    
    def get_length(self):
        return self.__length
    
    def pushing(self, node):
        if(self.__size==self.__length):
            print("The stack is full")
        else:
            self.__my_stack.append(node)
            self.__length= len(self.__my_stack)
            self.__first = node
        
    def poping(self):
        if(self.__my_stack==None):
            print("Error: the stack is empty")
        else:
            del self.__my_stack[-1]
            if(self.__my_stack==0):
                self.__first = None
            else:
                self.__first = self.__my_stack[-1]
            self.__length= len(self.__my_stack)
            return self

    def get_stack(self):
        return list(self.__my_stack)
  
s=stack(100)
s.pushing(10)
s.pushing(20)
s.pushing(30)
s.pushing(10)
s.pushing(20)
s.pushing(30)
s.pushing(10)
s.pushing(20)
s.pushing(30)
s.pushing(10)
s.pushing(20)
s.pushing(30)
print(s.get_stack())
print(s.get_top())
print(s.get_length())

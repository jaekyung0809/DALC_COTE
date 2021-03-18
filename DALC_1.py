#!/usr/bin/env python
# coding: utf-8

# In[5]:


sum2 = 0
for i in range(1, 10+1):
    sum2 += i
sum2


# In[3]:


sum3= sum(i for i in range(1,10+1))
print(sum3)


# In[4]:


sum4 = sum(range(1,10+1))
sum4


# In[6]:


def are_equal(a,b):
    return a==b
are_equal(10, 10.0)


# In[7]:


from typing import TypeVar

T = TypeVar('T')
U = TypeVar('U')

def are_equal(a:T, b:U) -> bool:
    return a==b

are_equal(10, 10.0)


# In[8]:


foo = ['A','B','C']
for f in foo:
    print(f)


# In[10]:


from collections import namedtuple
MyStruct = namedtuple("MyStruct","field1 field2 field3")

m = MyStruct("foo","bar","baz")
m


# In[11]:


from dataclasses import dataclass

@dataclass
class Product:
    weight: int = None
    price : float = None
        
apple = Product()
apple.price = 10


# In[13]:


from dataclasses import dataclass
@dataclass
class Rectangle:
    width: int
    height: int
    
    def area(self):
        return self.width * self.height
rect = Rectangle(3,4)
print(rect.area())


# In[ ]:





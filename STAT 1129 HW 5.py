#!/usr/bin/env python
# coding: utf-8

# In[2]:


class Human:
    species = "Homo sapiens"
    language = "Spanish"
    hair_color = "black"
    eye_color = "brown"

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
        self.height = None
        self.weight = None
A = Human("Francesca", 19, "female")
B = Human("Nico", 20, "male")


# In[4]:


import math
class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    def distance(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)
p = Point(6, 7)
print(p.distance()) 


# In[5]:


print("The answer for #3 is 'A'")


# In[7]:


def main():
    print("hello", end="")
try:
    if __name__ == "__main__":
        main()
except:
    print("name")
finally:
    print("world")


# In[8]:


print("The answer for #5 is 'C'")


# In[10]:


x = "hello"
if not type(x) is int:
    raise TypeError("Only integers are allowed")


# In[ ]:





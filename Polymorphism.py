#!/usr/bin/env python
# coding: utf-8

# # Implementation of the types of polymorphism

# Ducktyping

# In[5]:


class duck:
    def walk(self):
        print("duck is walking")
    def talk(self):
        print("quack quack")
class dog:
    def walk(self):
        print("dog is walking")
    def talk(self):
        print("bow bow")
def obj(a):
    a.walk()
    a.talk()
du=duck()
obj(du)
d=dog()
obj(d)


# If any of the method not present in class then leads to error so you need to confirm

# In[6]:


class duck:
    def walk(self):
        print("duck is walking")
    def talk(self):
        print("quack quack")
class dog:
    def walk(self):
        print("dog is walking")
    
def obj(a):
    a.walk()
    if hasattr(a,'talk'):
        a.talk()
du=duck()
obj(du)
d=dog()
obj(d)


# Method overloading

# In[7]:


def sum(a,b,c=None):
    if c==None:
        return a+b
    else:
        return a+b+c
print(sum(4,5))
print(sum(5,6,7))


# In[8]:


def sum(a,b):
    return a+b
def sum(a,b,c):
    return a+b+c
    
print(sum(4,5))
print(sum(5,6,7))


# In[9]:


class s:
    def sum(self,a,b):
        return a+b
    def sum(self,a,b,c):
        return a+b+c
a=s()
a.sum(3,4)
a.sum(1,2,3)


# In[15]:


class s:
    def sum(self,a,b,c=None):
        if c==None:
            return a+b
        else:
            return a+b+c
a=s()
print(a.sum(3,4))
print(a.sum(4,5,6))


# method overloading

# In[18]:


class p:
    def pp(self):
        print("parent")
class c(p):
    def pp(self):
        super().pp()
        print("child")
a=c()
a.pp()


# Operator Overloading

# In[19]:


class comp:
    def __init__(self,a,b):
        self.real=a
        self.img=b
    def __add__(self,other):
        return str(c1.real+c2.real)+'+'+str(c1.img+c2.img)+'i'
c1=comp(1,2)
c2=comp(1,2)
print(c1+c2)
        


# Abstract class

# In[21]:


from abc import ABC,abstractmethod
class a(ABC):
    def p(self):
        pass
    def p1(self):
        print("parent")
class b(a):
    def p(self):
        print('child')
obj=b()
obj.p()
obj.p1()


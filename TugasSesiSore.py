#!/usr/bin/env python
# coding: utf-8

# In[1]:


def divisible(m,n):
    if m % n == 0:
        return True
    return False

print(divisible(2,3))
print(divisible(4,2))


# In[ ]:


def menu():
    print("1. Soup and salad")
    print("2. Pasta with meat sauce")
    print("3. Chef's spesial")
    inp = int(input("Which your would you like to order? "))
    
    if inp == 1:
        print("One Soup and salad coming right up!")
    elif inp == 2:
        print("One Pasta with meat sauce coming right up!")
    elif inp == 3:
        print("One Chef's spesial coming right up!")
    else:
        print("Sorry, that is not a valid choice.")

menu()


# In[ ]:


import random

def rand_divis_3():
    number = random.randint(1,100)
    if number % 3 == 0:
        return True
    return False

print(rand_divis_3())


# In[ ]:


def isNotEqual(a,b):
    return (a > b) or (b > a)

a = 100
b = 10
print(isNotEqual(a,b))


# In[ ]:


# variable name adalah variable lokal dari fungsi ask_name()
# sehingga variable name tidak bisa di akses di luar fungsi ask_name()
def ask_name():
    name = input("Enter your name: ")
    print("your name is",name)

ask_name()


# In[ ]:





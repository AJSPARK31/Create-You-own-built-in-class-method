#!/usr/bin/env python
# coding: utf-8

# In[11]:


# Write a Python class to implement pow(x, n)



class get_power_of_given_number():
    
    def __init__(self,num,power):
        self.num=num
        self.power=power
    def get_power(self):
        result=self.num**self.power
        return result
    
result_1=get_power_of_given_number(10,2)
result_1.get_power()


# In[ ]:





# In[ ]:





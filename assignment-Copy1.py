#!/usr/bin/env python
# coding: utf-8

# ###Asignment

# In[1]:


def is_even (integer):
    
    result =integer % 2
    
    if result == 0:
        
        return True
    else:
        return False
    


# In[3]:


is_even(3)


# In[18]:


def calculate_grade (studentscore):
    
    if studentscore >= 90:
        
        return 'A'
    
    elif studentscore >= 80:
        
        return 'B'
    
    elif studentscore >= 70:
        
        return 'C'
    
    elif studentscore >=60:
        
        return 'D'
    
    else:
        
        return 'F'
    
        
        
    


# In[6]:


calculate_grade(79)


# In[ ]:





# In[9]:


def calculate_area (lenght, width):
    
    Area = lenght * width
    
    return Area

    


# In[11]:


calculate_area(10, 4)


# ### if a triangle has the side lengths a, b, and c, then theorem says the inequality,: a+b > c, a+c > b, and b+c > a must be satisfied

# In[13]:


def is_triangle(a,b,c):
    
    if (a+b)>c and (a+c)>b and (b+c)>a:
        
        return True
    else:
        
        return False


# In[ ]:





# In[15]:


is_triangle(4,2,3)


# In[ ]:





# In[16]:


def max_of_three(num1, num2, num3):
    
    if (num1 >= num2) and (num1 >= num3):
        
        return num1
    
    elif(num2 >= num1) and (num2 >= num3):
        
        return num2
    
    
    else:
        
        return num3
    
    


# In[19]:


max_of_three(7,8,9)


# In[20]:


def reverse_string(s):
    return s[::-1]


# In[22]:


reverse_string('hello')


# In[ ]:





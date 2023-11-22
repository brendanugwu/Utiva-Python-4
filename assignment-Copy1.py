

# ###Asignment

Ques 1

def is_even (integer):
    
    result =integer % 2
    
    if result == 0:
        
        return True
    else:
        return False
    
Ques 2

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
    
        
    Ques 3

def calculate_area (lenght, width):
    
    Area = lenght * width
    
    return Area


Ques 4

# ### if a triangle has the side lengths a, b, and c, then theorem says the inequality,: a+b > c, a+c > b, and b+c > a must be satisfied

def is_triangle(a,b,c):
    
    if (a+b)>c and (a+c)>b and (b+c)>a:
        
        return True
    else:
        
        return False


Ques 5

def max_of_three(num1, num2, num3):
    
    if (num1 >= num2) and (num1 >= num3):
        
        return num1
    
    elif(num2 >= num1) and (num2 >= num3):
        
        return num2
    
    
    else:
        
        return num3
    
    
Addedum question

def reverse_string(s):
    return s[::-1]







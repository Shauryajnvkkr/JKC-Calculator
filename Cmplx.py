#!/usr/bin/env python
# coding: utf-8

# In[1]:


import sys
import math
import cmath
x="y"
from os import system, name 
  
# import sleep to show output for some time period 
from time import sleep 
  
# define our clear function 
def clear(): 
  
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
  
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear') 
  
  

    

    
while True:
    if x=="n" or x=="no":
        break
    E= ''' A Program to find log[use "ln" for natural log];{or hyperbola} and cos[or tan] or exponential[e]<arc or inverse {use"a" before every trigonomerty function}> or sin(🌐🌏🎯🗿) and power{💪💪🎲ł function =: '''
    print(E)
    B=(input('Which function do you want to perform ='))
    def n():
    
        if(B=='cos'):
            A=eval(input('Provide tetha {ø} ='))    
            C=cmath.cos(A) 
            print(C)
        else:
            if(B=='sin'):
                A=eval(input('Provide tetha {ø} ='))            
                C=cmath.sin(A)
                print(C)
            elif(B=="tan"):
                A=eval(input("Provide tetha {ø}"))
                C=cmath.tan(A)
                print(C)
            elif (B=='e') :
                A=eval(input("Provide the power of exponential e^:")) 
                C=cmath.e
                D=C**A
                print('The Value of the exponential is',D) 
            else:
                print("Wrong Function Typed, 🙏 sorry") 
                exit() 
        
    if(B=='log'):
        a=eval(input('Provide the base of log =')) 
        b=eval(input(' Provide a number of which log is to be found ='))
        a,b=b,a
        C=cmath.log(a,b)
        print('Log of',b,'to the base',a,'is',C)
    else: 
        if(B=='power'):
            A=eval(input('Provide a number of  which power is to be found =')) 
            C=eval(input('Provide a power of which number is to be raisen ;')) 
            D=A**C
            print(D)
        
        elif(B=='mod'):
            A=eval(input('Provide a number of which mod:')) 
            D=eval(input('power :')) 
            G=eval(input('mod:')) 
            A=A**D
            C=A%G
            print(C)   
        elif(B=="inverse"):
            f=input("which inverse function (cos); {sin}; [tan];  ")
            th=eval(input("Provide the value"))
            if f=="cos":
                z=cmath.acos(th)
                print("the arc is",z)
            if f=="sin":
                z=cmath.asin(th)
                print("the arc is",z)
            if f=="tan":
                z=cmath.atan(th)
                print("the arc is",z)
        elif(B=="hyperbola"):
            f=input("which hyperbolic function (cos); {sin}; [tan]; <inverse>;  ")
            th=eval(input("Provide the value"))
            if f=="inverse":
                f=input("which inverse function (cos); {sin}; [tan];  ")
                if f=="cos":
                    z=cmath.acosh(th)
                    print("the arc is",z)
                if f=="sin":
                    z=cmath.asinh(th)
                    print("the arc is",z)
                if f=="tan":
                    z=cmath.atanh(th)
                    print("the arc is",z)
            elif f=="cos":
                z=cmath.cosh(th)
                print("the value is",z)
            elif f=="sin":
                z=cmath.sinh(th)
                print("the value is",z)
            else :
                z=cmath.tanh(th)
                print("the value is",z)
        elif B=="ln":
            th=eval(input(" provide the number"))
            z=cmath.log(th)
            print(z)
        
        
          	
        else:
            n()
    x=input("d0 y0u want to continue (y/n)")
    sleep(2)
    clear()
    
      
print('Bye 👋 Bye') 


# In[ ]:





# In[ ]:


import auto_py_to_exe


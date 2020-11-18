import sys 
import math
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.image import imread 

x = np.arange(2, 10, 0.1)
y_sin = np.sin(x)
y_cos = np.cos(x)
y_tan = np.tan(x)

plt.xlabel("x")
plt.ylabel("y")
plt.legend()

class Graph():
    def math(self):
        print("Graph.math()") 
        print("sin(PI/2) =",math.sin(math.pi / 2)) 
        print("cos(PI/2) =",math.cos(math.pi / 2)) 
        print("tan(PI/2) =",math.tan(math.pi / 2)) 
        print("log(2.78) =",math.log(math.e)) 
        print("log10(10, 10) =",math.log(10, 10))          

    def sin(self):
        print("Graph.sin()")  
        plt.title('Sin')
        plt.plot(x, y_sin, label="sin")
        plt.show()

    def cos(self):
        print("Graph.cos()")
        plt.title('Cos')
        plt.plot(x, y_cos, linestyle = "--", label="cos")
        plt.show()        

    def tan(self):
        print("Graph.tan()")
        plt.title('Tan')
        plt.plot(x, y_tan, label="tan")
        plt.show()

    def image(self):
        print("Graph.image()")    
        img = imread('dmlim.jpg')  
        #img = imread('py_image.png') 
        plt.imshow(img)
        plt.show()    

cmath = Graph()

cstr = sys.argv[1]

if cstr == 'math':       
    print("--- math ---")
    cmath.math()
elif cstr == 'sin':       
    print("--- sin ---")
    cmath.sin()
elif cstr == 'cos':
    print("--- cos ---")
    cmath.cos()
elif cstr == 'tan':
    print("--- tan ---")
    cmath.tan()
elif cstr == 'img':
    print("--- image ---")
    cmath.image()
else :
    print("invalid string...")





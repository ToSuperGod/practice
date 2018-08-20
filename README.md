# practice
平时练习的代码
import numpy as np
import matplotlib.pyplot as plt
import math
def draw_heart():
    t=np.linspace(0,math.pi,1000)
    x=np.sin(t)
    y=np.cos(t)+np.power(x,2.0/3)
    plt.plot(x,y,color='red',linewidth=2,label='h')
    plt.plot(-x,y,color='red',linewidth=2,label='h')
    plt.fill_between(x, y, where=(2.3<x) & (x<4.3) | (x>10))
    plt.xlabel('t')
    plt.ylabel('h')
    plt.ylim(-2,2)
    plt.xlim(-2,2)
    plt.legend()
    plt.show()
draw_heart()

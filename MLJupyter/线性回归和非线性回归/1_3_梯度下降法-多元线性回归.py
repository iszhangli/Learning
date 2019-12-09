#!/usr/bin/env python
# coding: utf-8

# In[25]:


import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


# In[2]:


data = np.genfromtxt(r'E:\Documents\AI Mooc\线性回归以及非线性回归\Delivery.csv', delimiter=',')
print(data)


# In[8]:


x_data = data[:, :-1]
y_data = data[:, -1]
print(x_data)


# In[22]:


lr = 0.0001
theta0 = 0
theta1 = 0
theta2 = 0
epochs = 1000

def compute_err(x_data, y_data, theta0, theta1, theta2):
    total_err = 0
    for i in range(len(y_data)):
        total_err += (theta0 + theta1*x_data[i,0] + theta2*x_data[i,1] - y_data[i]) ** 2
    return total_err / len(y_data) / 2

def gradient_desent_runner(x_data, y_data, theta0, theta1, theta2, lr):
    
    for j in range(epochs):
        th0 = 0
        th1 = 0
        th2 = 0
        for i in range(len(y_data)):
            th0 += (theta0 + theta1*x_data[i,0] + theta2*x_data[i,1] - y_data[i]) / len(y_data)
            th1 += (theta0 + theta1*x_data[i,0] + theta2*x_data[i,1] - y_data[i]) * x_data[i, 0] / len(y_data)
            th2 += (theta0 + theta1*x_data[i,0] + theta2*x_data[i,1] - y_data[i]) * x_data[i, 1] / len(y_data)

        theta0 = theta0 - lr * th0
        theta1 = theta1 - lr * th1
        theta2 = theta2 - lr * th2
        
        if j % 10 == 0:
            print('epochs: ', j)
            print('err: ', compute_err(x_data, y_data, theta0, theta1, theta2))
    return theta0, theta1, theta2


# In[24]:


print('Starting theta0={0} theta1 = {1} theta2 = {2} error = {3}'.
      format(theta0, theta1, theta2, compute_err(x_data, y_data, theta0, theta1, theta2)))
print('Running...')
theta0, theta1, theta2 = gradient_desent_runner(x_data, y_data, theta0, theta1, theta2, lr)
print('Ending theta0={0} theta1 = {1} theta2 = {2} error = {3}'.
      format(theta0, theta1, theta2, compute_err(x_data, y_data, theta0, theta1, theta2)))


# In[28]:


# 画图的思路
ax = plt.figure().add_subplot(111, projection = '3d')
ax.scatter(x_data[:, 0], x_data[:, 1], y_data, c='r', marker = 'o', s =100)
x0 = x_data[:, 0]
x1 = x_data[:, 1]
# 生成网格矩阵
x0, x1 = np.meshgrid(x0, x1)
z = theta0 + theta1 * x0 + theta2 * x1
ax.plot_surface(x0, x1, z)
ax.set_xlabel('a')
ax.set_ylabel('b')
plt.show()


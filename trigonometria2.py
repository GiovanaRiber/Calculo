#!/usr/bin/env python
# coding: utf-8

# In[2]:


from math import sin, cos, tan, pi
from pylab import *


# In[3]:


def calcula_f(x):
  return sin(x)


# In[4]:


x = arange (-2*pi, 2*pi, 0.02)


# In[5]:


y = calcula_f(x)


# In[6]:


plot(x, y)
xlabel('Variável Independente x')
ylabel('Função y = sin(x)')
title('Função seno')
grid(True)
axis([-3*pi, 3*pi, -2,2])
axhline(y = 0, color = 'k')
axvline(x = 0, color = 'k')


# In[7]:


def calcula_f(z):
  return cos(z)


# In[8]:


z = arange (-2*pi, 2*pi, 0.02)
w = calcula_f(z)


# In[9]:


plot(z, w)
xlabel('Variável Independente w')
ylabel('Função y = cos(w)')
title('Função cosseno')
grid(True)
axis([-3*pi, 3*pi, -2,2])
axhline(y = 0, color = 'k')
axvline(x = 0, color = 'k')


# In[10]:


def calcula_f(a):
  return tan(a)

a = arange (-2*pi, 2*pi, 0.02)
b = calcula_f(a)


# In[11]:


plot(x, y)
plot(z, w)
plot(a, b)
xlabel('Variável Independente')
ylabel('Funções')
title('Funções')
grid(True)
axis([-3*pi, 3*pi, -2,2])
axhline(y = 0, color = 'k')
axvline(x = 0, color = 'k')


# In[12]:


plot(a, b)
xlabel('Variável Independente a')
ylabel('Função y = tan(a)')
title('Função Tangente')
grid(True)
axis([-3*pi, 3*pi, -2,2])
axhline(y = 0, color = 'k')
axvline(x = 0, color = 'k')


# In[13]:


def calcula_a(x1):
  return sin(2*x1)

def calcula_b(x1):
  return sin(3*x1)

def calcula_c(x1):
  return sin(1/2*x1)

x1 = arange (-2*pi, 2*pi, 0.02)
y1 = calcula_a(x1)
y2 = calcula_b(x1)
y3 = calcula_c(x1)


plot(x1, y1, x1, y2, x1, y3)

xlabel('Variável Independente')
ylabel('Funções')
title('Funções senno')
grid(True)
axis([-3*pi, 3*pi, -2,2])
axhline(y = 0, color = 'k')
axvline(x = 0, color = 'k')


# In[14]:


def calcula_x(x0):
  return cos(2*x0)

def calcula_y(x0):
  return cos(3*x0)

def calcula_z(x0):
  return cos(1/2*x0)

x0 = arange (-2*pi, 2*pi, 0.02)

a = calcula_x(x0)
b = calcula_y(x0)
c = calcula_z(x0)

plot(x0, a, x0, b, x0, c)

xlabel('Variável Independente')
ylabel('Funções')
title('Funções cosseno')
grid(True)
axis([-3*pi, 3*pi, -2,2])
axhline(y = 0, color = 'k')
axvline(x = 0, color = 'k')


# In[15]:


from sympy import symbols, Lambda, sin, cos

x = symbols("x")
f = Lambda(x, (x-1)/(x**2-1))
f


# In[16]:


f(0)


# In[17]:


f(0.01)


# In[18]:


f(0.9)


# In[19]:


f(1)


# In[20]:


from pylab import *
import math

def calcula_f(x):
  return (x-1)/(x**2-1)

x = arange(0.1,2,0.01)
y = calcula_f(x)


# In[21]:


plot (x, y)
xlabel('Variável Independente x')
ylabel('Função y = (x-1)/(x**2-1)')
title('Visão Geometrica')
grid(True)
axhline(y = 0, color = 'k')
axvline(x = 0, color = 'k')


# In[22]:


x = symbols("x")
f = Lambda(x, (x-1)/(x**2-1))
f


# In[1]:


from sympy import symbols, Lambda

t = symbols("t")
h = Lambda(t, (pow((t**2 + 9),1/2 )- 3) / (t**2))
h


# In[22]:





#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from sympy import symbols, Lambda, sin, cos

x = symbols("x")
f = Lambda(x, (x-1)/(x**2-1))
f


# In[ ]:


f(0)


# In[ ]:


f(0.5)


# In[ ]:


f(0.6)


# In[ ]:


f(1)


# In[ ]:


f(0.999999)


# In[ ]:


f(1.001)


# In[ ]:


f(1.5)


# In[ ]:


from pylab import *


# In[ ]:


def calcula_f(x):
  return (x-1)/(x**2-1)


# In[ ]:


x = arange(0.1,2,0.01)


# In[ ]:


y = calcula_f(x)


# In[ ]:


plot(x,y)
xlabel("Variavel Independente X")
ylabel("Função Y = (x-1)/(x^2 - 1)")
grid(True)
title("Visão geometrica do Conceito de limite")
axhline(y=0, color = 'k')
axvline(x=0, color = 'k')


# In[ ]:


import math
import sympy


# In[ ]:


from sympy import symbols, Lambda

t = symbols("t")
h = Lambda(t, (pow((t**2 + 9),1/2 )- 3) / (t**2))
h


# In[ ]:


h(1)


# In[ ]:


h(0.001)
from sympy import pi, sin


# In[ ]:


w = symbols("w")
m = Lambda(w, (sin(pi/w)))
m


# In[ ]:


from pylab import *
import math
import numpy

def calcula_f(w):
  return sin(pi/w)

w = arange(-10,10,0.01)
m = calcula_f(w)


# In[ ]:


plot(w, m)
xlabel("Variavel Independente X")
ylabel("Função Y = (x-1)/(x^2 - 1)")
grid(True)
title("Visão geometrica do Conceito de limite")
axhline(y=0, color = 'k')
axvline(x=0, color = 'k')


# In[ ]:


from sympy import oo, limit, Symbol

x = Symbol('x')


# In[ ]:


limit((1+1/x)**x, x, oo) # (1+1/x)**x com x tendendo ao oo


# In[ ]:


from sympy.plotting import plot
from sympy import E
import matplotlib.pyplot as plt


# In[ ]:


def move_sympy_plot_to_axes(sympy_plot, plt_ax):
  backend = sympy_plot.backend(sympy_plot)
  backend.ax = plt_ax
  backend._process_series(backend.parent._series, plt_ax, backend.parent)
  backend.ax.spines['right'].set_color('none')
  backend.ax.spines['bottom'].set_position('zero')
  backend.ax.spines['top'].set_color('none')
  plt.close(backend.fig)


# In[ ]:


fig, ax = plt.subplots(figsize=(8,6))
p1 = plot((1 + 1/x)**x, (x,0,50), show = False,
          label =r'$\left(1+\frac{1}{x} \right)^x$')
p2 = plot(E, (x,0,50), show=False, label='Numero de Euler')
move_sympy_plot_to_axes(p1, ax)
move_sympy_plot_to_axes(p2, ax)
ax.get_lines()[1].set(color = 'red', linestyle='--')
ax.set_ylim(0,3)
ax.legend(loc= 'lower right')

plt.show()


# In[ ]:


f = 1/x

plot(f, (x, -10, 10), ylim=(-10,10))


# In[ ]:


limit(f, x, 0, dir='+')


# In[ ]:


limit(f, x, 0, dir='-')


# In[ ]:


limit(f, x, -oo), limit(f, x, oo)


# In[ ]:


limit(f, x, 0)


# In[ ]:


from sympy import sin, exp


# In[ ]:


limit((x**2 - 1)/(x - 1), x, 1) # (x**2 - 1)/(x - 1) com x tendendo a 1


# In[ ]:


#se 'f' for ua função polinomial ou racional e 'a' estiver no fominio de 'f', então
# lim f(x) = f(a)
#     x->a

b = (x**2 - 1)/(x - 1)
plot(b,(x, -10, 10))


# In[ ]:


b1 = x + 1
plot(b1, (x, -10, 10))


# In[ ]:


g = sin(x)/x
plot(g,(x, -30, 30))


# In[ ]:


u = sin(x)**2/x
plot(u,(x, -30, 30))


# In[ ]:


limit(g, x, 0)


# In[ ]:


limit(g, x, oo)


# In[ ]:


limit(u, x, 0)


# In[ ]:


limit(u, x, oo)


# In[ ]:


h = symbols('h')
limit(((3 + h)**2 - 9)/h, h, 0)


# In[ ]:





#!/usr/bin/env python
# coding: utf-8

# In[ ]:
from scipy import interpolate
from numpy import polynomial as P
# In[ ]:
import numpy as np
from scipy import linalg
import matplotlib.pyplot as plt

# In[ ]:

p1 = P.Polynomial ([1, 2, 3]) #c, b, a
p1

# In[ ]:

p1.roots () #não existem raizes reais

# In[ ]:

p2 = P.Polynomial.fromroots([-1,1])
p2

# In[ ]:

x = np.array([1, 2, 3, 4])
y = np.array([1, 3, 5, 4])

# In[ ]:

deg = len(x) -1
deg

# In[ ]:

fib = P.Polynomial.fit(x,y,deg)
fib
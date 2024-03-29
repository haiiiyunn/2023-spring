#!/usr/bin/env python
# coding: utf-8

# # McKinney Chapter 4 - Practice (Blank)

# In[1]:


import numpy as np
get_ipython().run_line_magic('precision', '4')


# ***Practice:***
# Create a 1-dimensional array named `a1` that counts from 0 to 24 by 1.

# ***Practice:***
# Create a 1-dimentional array named `a2` that counts from 0 to 24 by 3.

# ***Practice:***
# Create a 1-dimentional array named `a3` that counts from 0 to 100 by multiples of 3 and 5.

# ***Practice:***
# Create a 1-dimensional array `a3` that contains the squares of the even integers through 100,000.
# How much faster is the NumPy version than the list comprehension version?

# ***Practice:***
# Write a function that mimic Excel's `pv` function.

# ***Practice:***
# Write a function that mimic Excel's `fv` function.

# ***Practice:***
# Replace the negative values in `data` with -1 and positive values with +1.

# In[2]:


np.random.seed(42)
data = np.random.randn(7, 7)


# ***Practice:***
# Write a function that calculates the number of payments that generate $x\%$ of the present value of a perpetuity given $C_1$, $r$, and $g$.
# Recall the present value of a growing perpetuity is $PV = \frac{C_1}{r - g}$ and the present value of a growing annuity is $PV = \frac{C_1}{r - g}\left[ 1 - \left( \frac{1 + g}{1 + r} \right)^t \right]$.

# ***Practice:***
# Write a function that calculates the internal rate of return given an numpy array of cash flows.

# ***Practice:***
# Write a function `returns()` that accepts *NumPy arrays* of prices and dividends and returns a *NumPy array* of returns.

# In[3]:


prices = np.array([100, 150, 100, 50, 100, 150, 100, 150])
dividends = np.array([1, 1, 1, 1, 2, 2, 2, 2])


# ***Practice:***
# Rewrite the function `returns()` so it returns *NumPy arrays* of returns, capital gains yields, and dividend yields.
# How can we return these *NumPy arrays*?

# ***Practice:***
# Rescale and shift numbers so that they cover the range [0, 1]
# 
# Input: `[18.5, 17.0, 18.0, 19.0, 18.0]` \
# Output: `[0.75, 0.0, 0.5, 1.0, 0.5]`

# In[4]:


numbers = np.array([18.5, 17.0, 18.0, 19.0, 18.0])


# ***Practice:***
# NumPy's `.var()` and `.std()` methods return *population* statistics (denominators of $n$).
# The pandas equivalents return *sample* statistics (denominators of $n-1$), which are more appropriate for financial data analysis where we have a sample instead of a population.
# 
# Write functions `var()` and `std()` that calculate variance and standard deviation.
# Both function should have an argument `sample` that is `True` by default so both functions return sample values by default.
# 
# Use the output of `returns()` to compare your functions with NumPy's `.var()` and `.std()` methods.

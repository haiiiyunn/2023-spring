#!/usr/bin/env python
# coding: utf-8

# # McKinney Chapter 2 - Practice (Section 04, Wednesday 11:45 AM)

# ***Practice:*** 
# Extract the year, month, and day from an integer 8-digit date (i.e., YYYYMMDD format) using `//` (integer division) and `%` (modulo division).
# Try `20080915`.

# In[1]:


1234 / 100 # "regular" division


# In[2]:


1234 // 100 # integer or floor division gives us the integer portion


# In[3]:


1234 % 100 # modulo division gives us the remainder


# In[4]:


ymd = 20080915


# In[5]:


year = ymd // 10_000


# In[6]:


month = (ymd % 10_000) // 100


# In[7]:


day = ymd % 100


# In[8]:


(year, month, day)


# ***Practice:***
# Use your answer above to write a function `date` that accepts an integer 8-digit date argument and returns a tuple of the year, month, and date (e.g., `return (year, month, date)`)

# In[9]:


def date(ymd):
    year = ymd // 10_000
    month = (ymd % 10_000) // 100
    day = ymd % 100
    return (year, month, day)


# In[10]:


date(ymd=20080915)


# ***Practice:***
# Rewrite `date` to accept an 8-digit date as an integer or string.

# In[11]:


def date(ymd):
    if type(ymd) is str:
        ymd = int(ymd)
    year = ymd // 10_000
    month = (ymd % 10_000) // 100
    day = ymd % 100
    return (year, month, day)


# In[12]:


date(ymd='20080915')


# ***Practice:***
# Finally, rewrite `date` to accept a list of 8-digit dates as integers or strings.
# Return a list of tuples of year, month, and date.

# In[13]:


ymds = [20080915, '20080915']


# In[14]:


def date(ymds):
    ymds_out = []
    if type(ymds) is not list:
        ymds = [ymds]
    for ymd in ymds:
        if type(ymd) is str:
            ymd = int(ymd)
        year = ymd // 10_000
        month = (ymd % 10_000) // 100
        day = ymd % 100
        ymds_out.append((year, month, day))
    return ymds_out


# In[15]:


date(ymds)


# In[16]:


date(20080915)


# ***Practice:***
# Write a for loop that prints the squares of integers from 1 to 10.

# In[17]:


for i in range(1, 11):
    print(i**2, end=' ')


# Above, I change the `end` argument from the default '\n' to ' '.
# The default '\n' inserts a new line after value, making the output too long.

# ***Practice:***
# Write a for loop that prints the squares of *even* integers from 1 to 10.

# In[18]:


for i in range(1, 11):
    if i % 2 == 0:
        print(i**2, end=' ')


# ***Practice:*** 
# Write a for loop that sums the squares of integers from 1 to 10.

# In[19]:


total = 0
for i in range(1, 11):
    total += i**2


# In[20]:


total


# Above, I use `total += i`, which is equivalent to `total = total + i`.

# ***Practice:*** 
# Write a for loop that sums the squares of integers from 1 to 10 but stops before the sum exceeds 50.

# In[21]:


total = 0
for i in range(1, 11):
    if (total + i**2) > 50:
        break
    total += i**2


# In[22]:


total


# ***Practice:*** 
# Write a for loop that prints the numbers from 1 to 100. 
# For multiples of three print "Fizz" instead of the number.
# For multiples of five print "Buzz". 
# For numbers that are multiples of both three and five print "FizzBuzz".
# More [here](https://blog.codinghorror.com/why-cant-programmers-program/).

# In[23]:


4 % 3 == 0


# In[24]:


for i in range(1, 101):
    is_mult_3 = (i % 3 == 0)
    is_mult_5 = (i % 5 == 0)
    if is_mult_3 and is_mult_5:
        print('FizzBuzz', end=' ')
    elif is_mult_3:
        print('Fizz', end=' ')
    elif is_mult_5:
        print('Buzz', end=' ')
    else:
        print(i, end=' ')


# ***Practice:*** 
# Use ternary expressions to make your FizzBuzz code more compact.

# In[25]:


for i in range(1, 101):
    is_mult_3 = (i % 3 == 0)
    is_mult_5 = (i % 5 == 0)
    print('Fizz'*is_mult_3 + 'Buzz'*is_mult_5 if is_mult_3 or is_mult_5 else i, end=' ')


# The solution above is shorter and uses from neat tricks, but I consider the previous solution easier to read and troubleshoot.

# ***Practice:***
# Write a function `triangle` that accepts a positive integer $N$ and prints a numerical triangle of height $N-1$.
# For example, `triangle(N=6)` should print:
# 
# ```
# 1
# 22
# 333
# 4444
# 55555
# ```

# In[26]:


def triangle(N):
    for i in range(1, N):
        print(str(i) * i)


# In[27]:


triangle(6)


# The solution above works because a multiplying a string by `i` concatenates `i` copies of the string.

# In[28]:


'Test' + 'Test' + 'Test'


# In[29]:


'Test' * 3


# ***Practice:***
# Write a function `two_sum` that does the following.
# 
# Given an array of integers `nums` and an integer `target`, return the indices of the two numbers that add up to target.
# 
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# 
# You can return the answer in any order.
# 
# Here are some examples:
# 
# Example 1:
# 
# Input: `nums = [2,7,11,15]`, `target = 9` \
# Output: `[0,1]` \
# Explanation: Because `nums[0] + nums[1] == 9`, we return `[0, 1]`.
# 
# Example 2:
# 
# Input: `nums = [3,2,4]`, `target = 6` \
# Output: `[1,2]` \
# 
# Example 3:
# 
# Input: `nums = [3,3]`, `target = 6` \
# Output: `[0,1]` \
# 
# I saw this question on [LeetCode](https://leetcode.com/problems/two-sum/description/).

# In[30]:


def two_sum(nums, target):
    for i in range(1, len(nums)):
        for j in range(i):
            if nums[i] + nums[j] == target:
                return [j, i]


# In[31]:


two_sum(nums = [2,7,11,15], target = 9)


# In[32]:


two_sum(nums = [3,2,4], target = 6)


# In[33]:


two_sum(nums = [3,3], target = 6)


# We can write more efficient code once we learn other data structures in chapter 3 of McKinney!

# ***Practice:***
# 
# Write a function `best_time` that solves the following.
# 
# You are given an array `prices` where `prices[i]` is the price of a given stock on the $i^{th}$ day.
# 
# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
# 
# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
# 
# Here are some examples:
# 
# Example 1:
# 
# Input: `prices = [7,1,5,3,6,4]` \
# Output: `5` \
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
# 
# Example 2:
# 
# Input: `prices = [7,6,4,3,1]` \
# Output: `0` \
# Explanation: In this case, no transactions are done and the max profit = 0.
# 
# I saw this question on [LeetCode](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/).

# In[34]:


def max_profit(prices):
        min_price = prices[0]
        max_profit = 0
        for price in prices:
            min_price = price if price < min_price else min_price
            profit = price - min_price
            max_profit = profit if profit > max_profit else max_profit
        return max_profit


# In[35]:


max_profit(prices=[7,1,5,3,6,4])


# In[36]:


max_profit(prices=[7,6,4,3,1])


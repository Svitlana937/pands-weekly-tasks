import numpy as np
# good idea to have your absolute values set into variables at the top of your code
# so that you can easily change them later if needed
minSalary= 20000
maxSalary = 80000
numberOfEntries = 10
# this is how you create a list of random integers between a min and max value
# the function np.random.randint(min, max, size) will create a list of random integers
salaries = np.random.randint(minSalary, maxSalary,numberOfEntries)

print (salaries)

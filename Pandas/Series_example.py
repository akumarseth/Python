#import the pandas library and aliasing as pd
import pandas as pd
import numpy as np

#data = np.array(['a','b','c','d'])
#s = pd.Series()
#s = pd.Series(data)
#s = pd.Series(data,index=[100,101,102,103])

data = {'a' : 0., 'b' : 1., 'c' : 2.}
#s = pd.Series(data)
#s = pd.Series(data,index=['b','c','d','a'])
#s = pd.Series(5, index=[0, 1, 2, 3])
#print (s)

s = pd.Series([1,2,3,4,5],index = ['a','b','c','d','e'])
#print (s[0])
#print (s[:3])
#print (s[-3:])

#retrieve a single element
#print (s['c'])

#retrieve multiple elements
#print (s[['a','c','d']])

#retrieve multiple elements
print (s['f'])
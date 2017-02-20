from __future__ import division, print_function
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pygal
from datetime import datetime
data = pd.read_csv('2016-first-quarter-citations.csv')


ages = data['Cited Person Age']
min_age, max_age=np.min(ages),np.max(ages)
l=[]
c=[]
for i in range(min_age, max_age+1):
    l= ages[ages==i]
    h=len(l)
    c.append([h,i,i])

d=np.array(c)
range=int(np.max(ages)-np.min(ages))

# tuple(map(tuple, c))
e=[]
for j in c:
    e.append(tuple(j))

#hist=pygal.Histogram()
#hist.add('ages',e)
#hist.render()
fig = plt.figure()
#ax = fig.add_subplot(1, 1, 1)
#plt.hist(ages, bins=np.max(ages)-np.min(ages))
hist=pygal.Histogram()
hist.add('ages',e)
hist.render_to_file('histages.svg')
#plt.show()


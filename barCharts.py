__author__ = 'davidnovogrodsky_wrk'
__author__ = 'davidnovogrodsky_wrk'

from matplotlib import pyplot as plt
from matplotlib import style

# adding a predefined style
style.use('ggplot')

x = [0,1,7,8]
y = [2,3,5,9]

x2 = [2,4,6,9]
y2 = [1,2,4,6]

print(len(x))
print(len(y))

# note color parameters different than in line graph
# bars are not rendered in different colors by default
plt.bar(x,y,color='c', align='center')
plt.bar(x2,y2,color='k', align='center')

# adding titles and labels
plt.title("Epic Chart")
plt.ylabel('y-axis')
plt.xlabel('x-axis')

plt.show()
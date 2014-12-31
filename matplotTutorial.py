__author__ = 'davidnovogrodsky_wrk'

from matplotlib import pyplot as plt
from matplotlib import style

# adding a predefined style
# style.use('ggplot')

x = [0,2,7,8]
y = [0,3,5,9]

x2 = [0,4,6,9]
y2 = [0,2,4,6]

print(len(x))
print(len(y))

plt.plot(x,y,'b',linewidth=5)
plt.plot(x2,y2,'g')

# adding titles and labels
plt.title("Epic Chart")
plt.ylabel('y-axis')
plt.xlabel('x-label')
plt.show()
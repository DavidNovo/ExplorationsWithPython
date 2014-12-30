__author__ = 'davidnovogrodsky_wrk'

from matplotlib import pyplot as plt

x = [5,6,7,8]
y = [7,3,8,3]

print(len(x))
print(len(y))

plt.plot(x,y)

# adding titles and labels
plt.title("Epic Chart")
plt.ylabel('y-axis')
plt.xlabel('x-label')
plt.show()
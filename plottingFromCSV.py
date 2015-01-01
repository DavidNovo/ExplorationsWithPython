__author__ = 'davidnovogrodsky_wrk'
__author__ = 'davidnovogrodsky_wrk'

from matplotlib import pyplot as plt
from matplotlib import style
import numpy as np


# adding a predefined style
style.use('ggplot')

#open the csv file
x,y = np.loadtxt('dataPoints.txt',unpack=True,
                 delimiter=',')

plt.plot(x,y, color='g', )

# adding titles and labels
plt.title("Epic Chart")
plt.ylabel('y-axis')
plt.xlabel('x-axis')

plt.show()
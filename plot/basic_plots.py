import random

from matplotlib import pyplot

x_values = [0,2,4,8,16,32]
y_values = [random.randint(0,30) for elt in x_values]
pyplot.plot(x_values, y_values, "o-")

pyplot.ylabel("Values")
pyplot.xlabel("Time")
pyplot.title("Test plot")

pyplot.show()
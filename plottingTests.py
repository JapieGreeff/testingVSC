# https://matplotlib.org/users/pyplot_tutorial.html
import matplotlib.pyplot as plt
# plotting an array of values.
# if you pass only a single array, pyplot assumes it is the y axis, and plots against array index (so 0,1,2,3...)
plt.plot([1,2,3,4])
plt.title('my single array chart')
plt.ylabel('my Y axis')
plt.xlabel('my X axis')
plt.show()

# if you want to plot x versus y, the first array will be your x axis, and the second your y axis
plt.plot([1,2,3,4], [2,4,6,8])
plt.title('my two array chart')
plt.ylabel('y=2x')
plt.xlabel('x')
plt.show()

# you can style your plot using the optional 3rd parameter in the plot function. a full description is available here:
# https://matplotlib.org/api/pyplot_api.html#matplotlib.pyplot.plot
# but for the moment it is just useful to know that you pass in a string that is made up of '[colour][shape]'
# r,g,b,k       = red,green,blue,black                                                      [colour]
# s,o,^,v,-,--  = square, circle, up-triangle, down-triangle, solid line, dashed line       [shape]
plt.plot([1,2,3,4,5,6,7], [1, 2, 3, 4, 5, 6, 7],'k--')
plt.plot([1,2,3,4,5,6,7], [2, 4, 6, 8,10,12,14],'rs')
plt.plot([1,2,3,4,5,6,7], [3, 6, 9,12,15,18,21],'gv')
plt.plot([1,2,3,4,5,6,7], [4, 8,12,16,20,24,28],'bo')
plt.title('different markers')
plt.ylabel('y value')
plt.xlabel('x value')
plt.show()

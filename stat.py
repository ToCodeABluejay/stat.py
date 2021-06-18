#!/bin/python
'''Statistics calculator for finding r, slope of the regression line,
the y-intercept, and estimated output for x-values that exist
within the x data-range'''
import math

#Get the data sets from the user
x = [float(i) for i in input("Enter the x data-set: ").split(',')]
y = [float(i) for i in input("Enter the y data-set: ").split(',')]

#If the length of the data-sets are not equal, exit with an error
if len(x) != len(y) :
    raise ValueError

#Calculate the various sub-components
sum_x = 0
sum_y = 0
sum_xy = 0
sum_xs = 0
sum_ys = 0
for i in range(len(x)) :
    sum_x+=x[i]
    sum_y+=y[i]
    sum_xy+=x[i]*y[i]
    sum_xs+=x[i]**2
    sum_ys+=y[i]**2

#Put the components together to get final answers
base_x = math.sqrt((len(x)*sum_xs)-sum_x**2)
base_y = math.sqrt((len(y)*sum_ys)-sum_y**2)
top = (len(x)*sum_xy)-(sum_x*sum_y)
result = top/(base_x*base_y)
m = (len(x)*sum_xy-(sum_x*sum_y))/(len(x)*sum_xs-sum_x**2)
y_int= (sum_y/len(x)) - m*(sum_x/len(x))

#Print final answers
print("r-Value equals: ", round(result,4))
print("m is equal to: ",round(m,3))
print("y-int equals: ", round(y_int,3))
print()
print("Coefficient of deterination equals: ", round(result**2,3))
print("% of variation expained: ", round(result**2,5)*10)
print("% of variation un-expained: ", round(1-result**2,5)*10)

'''Until the user types something besides a 'y' or the words 'yes', ask
to predict the output of a given x-value within the range of the data set'''
while True :
    pred = input("Would you like to make a prediction for a given x-value? Yes or no? ").upper()
    if (pred == "YES" or pred == "Y") :
        x_pred = input("Enter x-value to predict: ")
        if (float(x_pred) < min(x) or float(x_pred) > max(x)) :
            print("Predicted value will not be meaningful given this data set!")
        else :
            print("Predicted y-value: ", round(m*float(x_pred)+y_int, 3))
    else :
        break

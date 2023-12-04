x1, y1 = (2, 4) 
x2, y2 = (4, 6)

x_diff_sq = (x2 - x1) ** 2
y_diff_sq = (y2 - y1) ** 2
x_diff = (x2 - x1)
y_diff = (y2 - y1)
m = y_diff/x_diff
sum_distance = x_diff_sq + y_diff_sq
euclidian_distance = sum_distance ** 0.5
print("The slope is ", m)
print("Euclidian Distance is ", euclidian_distance)

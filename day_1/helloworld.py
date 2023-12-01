# Introduction
# Day 1 - 30DaysOfPython Challenge
#Question 1 Python Version
print('python --version') #Check python version
#Question 2 Arithematic Operation
print(2 + 3)   # addition(+)
print(3 - 1)   # subtraction(-)
print(2 * 3)   # multiplication(*)
print(5 / 2)   # division(/)
print(3 ** 3)  # exponential(**)
print(3 % 2)   # modulus(%)
print(3 // 2)  # Floor division operator(//)

#Question 3 Strings
print("Sheriff")                #string
print("Mudasir")
print("Nigeria")
print("I am enjoying 30 days of python")

# Question 4 Data Types

print(type(10))                                     # Int
print(type(9.8))
print(type(3.14))                                   # Float
print(type(4 - 4j))                                 # Complex
print(type(['Asabeneh', 'Python', 'Finland']))      # List
print(type("Sheriff"))                               # String
print(type("Mudasir"))                              # String
print(type("Nigeria"))                              # String
#Exercise Level 3
print(59)                   #integer
print(6.7)                  #Float
print(3 - 2j)               #Complex Number
print("Dog")                #String
print(True)                 #Boolean
print([1, 2, 3, 4])         #List
print((1, 2, 3, 4, "S"))         #Tuple
print({'name':'Sheriff', 'age':25}) #Dictionary
print({'Boy', 'Girl'})          #Set
# Euclidian Distance
point_1 = [2, 3]
point_2 = [10, 8]
# To find the Euclidian distance
# Given points
point_1 = (2, 3)
point_2 = (10, 8)

# Extract coordinates
x1, y1 = point_1
x2, y2 = point_2

# Calculate squared differences
x_diff_squared = (x2 - x1) ** 2
y_diff_squared = (y2 - y1) ** 2

# Sum of squared differences
distance_squared = x_diff_squared + y_diff_squared

# Calculate Euclidean distance
euclidean_distance = distance_squared ** 0.5

# Print the result
print("Euclidean distance:", euclidean_distance)


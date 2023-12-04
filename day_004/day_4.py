#Exercise Day 4
##No_1
string_1 = ['Thirty', 'Days', 'Of', 'Python']
string_1 = ' '.join(string_1)
print(string_1)

##No_2
string_2 = ['Coding', 'For' , 'All']
print(' '.join(string_2))

##No_3
company = "Coding For All"

##No_4
print(company)

##No_5
print(len(company))

##No_6
print(company.upper())

##No_7
print(company.lower())

##No_8
print(company.upper())
print(company.capitalize())
print(company.swapcase())
print(company.title())

##No_9
print(company[7:])

##No_10
print(company.index("Coding"))

##No_11
print(company.replace("Coding", "Python"))

##No_12
string_3 = "Python for Everyone"
print(string_3.replace("Everyone", "All"))

##No_13
string_4 = 'Coding For All'
print(string_4.split(' '))

##No_14
string_5 = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(string_5.split(','))

##No_15
string_6 = 'Coding For All'
print(string_6[0])

##No_16
string_6 = 'Coding For All'
print(string_6.index('l'))

##No_17
print(string_6[10])

##No_18
name = 'Python For Everyone'
acronym = ''.join(word[0].upper() for word in name.split())
print(acronym)

##No_19
name_1 = 'Coding For All'
acronym_1 = ''.join(word[0].upper() for word in name.split())
print(acronym)

##No_20
print(string_6.index('C'))

##No_21
print(string_6.index('F'))

##No_22
print(string_6.rfind('l'))

##No_23
string_7 = 'You cannot end a sentence with because because because is a conjunction'
print(string_7.index('because'))

##No_24
print(string_7.rfind('because'))

##No_25
substring = string_7[31:57]

print(substring)
##No_26
print(string_7.index('because'))

##No_27

substring = string_7[31:57]

print(substring)


##No_28
string_8 = 'Coding For All'
sub_string = 'Coding'

string_8 = string_8.split()
print(string_8[0] == sub_string)

##No_29
string_8 = 'Coding For All'
print(string_8.endswith("Coding"))

##No_30
spaced_string = '   Coding For All      '
spaced_string = spaced_string.strip()
print(spaced_string)

##No_31
string_9 = "30DaysOfPython"
string_10 = "thirty_days_of_python"
print(string_9.isidentifier())
print(string_10.isidentifier())

##No_32
python_library = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print(('#').join(python_library))

##No_33
sentences = "I am enjoying this challenge.\nI just wonder what is next."

print(sentences)
##No_34
print('Name\tAge\tCountry\tCity\t')
print('Asabeneh\t250\tFinland\tHelsinki\t')

##No_35
radius = 10
area = 3.14 * radius ** 2
print("The area of a circle with radius {} is {} meters square.".format(radius, area))

##No_36
a = 8
b = 6

addition = "{} + {} = {}".format(a, b, a + b)
subtraction = "{} - {} = {}".format(a, b, a - b)
multiplication = "{} * {} = {}".format(a, b, a * b)
division = "{} / {} = {:.2f}".format(a, b, a / b)
modulo = "{} % {} = {}".format(a, b, a % b)
floor_division = "{} // {} = {}".format(a, b, a // b)
exponentiation = "{} ** {} = {}".format(a, b, a ** b)

print(addition)
print(subtraction)
print(multiplication)
print(division)
print(modulo)
print(floor_division)
print(exponentiation)




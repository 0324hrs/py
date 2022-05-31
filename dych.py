""" # data types


# strings
# printing the index of a number
print("hello"[1])

##############
# intergers
print(12345)


num_characters = len(input("what is the length of my name? "))

# to check the type of data type
print(type(num_characters))

# converting intergers into strings
name_characters = len(input("what is your name? "))

new_name_characters = str(name_characters)

print("hello maina,your name has " +new_name_characters+ " characters")


##########
# floats-decimal points


# boolean


###################
######exercise#########

type_of = input("what is your two digit number? ")

first_number = type_of[0]
second_number = type_of[1]
# addation and conversion of strings to intergers
result = int(first_number) + int(second_number)

# print function
print(result)

#########################
##########################mathematical operations#######################
# **exponent value
 """
#####################exercise BMI calc###########

""" weight = input("what is your weight in kg? \n")
height = input("what is your height in m? \n")

# operations
bmi = int(weight)/ float(height)**2
result = int(bmi)
print(result)


# to check the data type
# print(type(height))


#####F-strings in python######
age = 18
height = 1.3
isAdult = True

# F-strings in action
print(f"your age is {age} and {height} in height and it is {isAdult} you're an adult")


 """
#####life#######
age = input("what is your age? \n")
# convert age string into an integer
age_int = int(age)

# logic
years_remaining = 90 - age_int
days_remaining = years_remaining * 365
weeks_remaining = years_remaining * 52
months_remaining = years_remaining * 12

# 
print(f"Hello there Kelvin, you're currently {age_int}.You have {days_remaining} days, {weeks_remaining} weeks, {months_remaining} months and {years_remaining} years remaining to get to 90..enjoy while you're still young")
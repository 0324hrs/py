# basic python print function
print("what to print?")

####################################

# string manipulation
print("hello python\ngood days ahead")

#############################################


# string concatenation...spacing are very important
print("hello" +" " + "maina")

########################################


#exercise python input function
print("hello" +" "+input("what is your name?"))

#######################################

# excercise...calculating the length of string characters
name = input("what is your name? ")
length = len(name)
print(length)
# the lines will be executed one by one and the users input calculated it's length

##########################################

# python variables
test = "jack"
print(name)
# the name that was input will be printed  on the terminal
# python code executed line by line

######################################

# RULES OF NAMING VARIABLES
laravel_bagisto = "php" #underscore
laravelBagisto = "php technology" #camelcase


#############################3
# data types


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

#####################exercise BMI calc###########

weight = input("what is your weight in kg? \n")
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


############################
##### conditional statements ...if else statements########
print("Yoh, welcome to the rollacoaster ride")

# 
height= int(input("what is your height in cm? \n"))
age = int(input("what is your age?\n"))
# conditional statement....nested
if height >= 120:
    if age >= 18:
        print("You will have to pay ksh 2500 to go for the rollacoaster ride")
    else:
        print("You will have to pay ksh 2000 to go for the rollacoaster ride")
else:
    print("You cannot go for the rollacoaster ride")
        
    
    
########odd or even exercise:modulo operator##########
print("hello there, welcome to the odd or even number checker")

int_input = int(input("what is the number you want to check  \n"))

# 
if int_input % 2 == 0:
    print("the  is even")
else:
    print("the number number is odd")
###########################
    
#####elif comdition#####
print("Yoh, welcome to the rollacoaster ride")

# 
height= int(input("what is your height in cm? \n"))
age = int(input("what is your age?\n"))
# conditional statement....nested
if height >= 120:
    if age <= 10:
        print("you will pay ksh 400 for the rollacoaster ride")
    elif age<=14:
        print("you will have to pay ksh 650 for the rollacoaster ride")
    elif age <=17:
        print("you will pay ksh 1000for the rollacoaster ride")
    elif age >=18:
        print("you will have to pay ksh 1600 for the rollacoaster ride")
else:
    print("you cannot go for the rollacoaster ride")


###########exercise..leap year challenge###########
# 
year = int(input("which year do you want to check?\n"))
# 

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("leap year")
        else:
            print("not a leap year")
    else:
        print("not a leap year")
        
else:
    print("not a leap year")
    
#######################################
####pizza order system exercise###########

print("welcome to pizza orders delivery")
# 
size = input("what size do you want? S, M or L\n")
add_pepperoni = input("do want pepperoni added? Y or N\ n")
add_extra_cheese = input("do you want extra cheese added? Y or N\n")
# 

#############################################
#######functions#########
def python_django():
    print("python")
    print("django")
# invoking the function
python_django()

# 
def mmu():
    print("faculty of computing and information Technology")
    print("faculty of science and Technology")
# 
mmu()

########while loop########
number_of_students = 60
while number_of_students > 0:
    mmu()
    number_of_students -= 1
    print("Information Technology is becoming a town square for the global village of tommorow")
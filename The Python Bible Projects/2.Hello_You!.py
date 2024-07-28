#Ask user for name
name = input('What is your name?: ')
print(name)

#Ask user for age
age = input('How old are you?: ')
print(age)

#Ask user for city
city = input('What city do you live in?: ')
print(city)

#ask user what they enjoy
enjoy = input('What do you enjoy?: ')
print(enjoy)

#Create output text
output = f'Hello {name}! you are {age} years old and you live in {city} and you enjoy {enjoy}'

# alternate string format method: string = "Hello {}! you are {} years old and you live in {} and you enjoy {}"
#                                 output = string.format(name,age,city,enjoy)

#Print output to screen
print(output)


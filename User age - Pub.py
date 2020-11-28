# define your age

name = input('Hi there, whats your name?')  # user defines their name

age = input('How old are you?')  # user gets asked whats their age

if int(age) > 20:

    print('Hi', name, 'Welcome in, Please have a Drink!')  # if age is bigger than 20, user gets inside and HAS a drink

elif int(age) < 20 and int(age) > 18:

    print('Welcome in', name, 'But your age is below 20, Sorry but you CANNOT have a drink')  # if age is bigger than 18 but lower than 20, user can get inside but cannot have a drinl

elif int(age) < 18:
    print('Sorry', name, 'Your too young. You cannot come inside')  # if age is below 20, user is too young and cannot come inside
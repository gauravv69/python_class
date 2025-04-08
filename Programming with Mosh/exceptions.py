# Exception is a kind of error that crashes our program

try:
    age  = int(input('Age: '))
    print(age)
except ValueError:
    print('Invalid value')

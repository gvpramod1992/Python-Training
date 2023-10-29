# x = 0 #global variable
# y = 5000
def display_local():
    print('display_local')
    y = 1000 #local variable
    print(y)


x = 0 #global variable
def display():
     print('display')
     y = 1000 #local variable
     print(x)
     print(y)
     return y


x = 0 #global variable
def display_global():
     print('display_global')
     global x
     x = 1000 #local variable
     print(x)


if __name__ == '__main__':
    display()
    display_global()
    display_local()

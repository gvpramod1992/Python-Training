print('test git repo')
print('Test line 2')

print('test git repo')
print('Test line 2')
# database -- hard disk -- file system

# Inventory management
# 1. AddItem, 2. RemoveItem, 3. DisplayItems

# Add 1-10 items
# items = []
#
while True:
    print('Available options: \n1. AddItem \n2. DisplayItems \n3.Exit')
    option = int(input('Choose an option: '))
    if option == 1: # AddItem
        item = input('Enter item name: ')
        # items.append(item)
        # write to a file
            # file name
            # location
            # write
        # open - python function to write/read from a file

        fp = open('inventory.txt', 'a')
        fp.write()
        fp.write(item)
        fp.close()
    elif option == 2:
        pass
        # print(items)
    elif option == 3:
        break
    else:
        print('Invalid option')




# x = 0 #global variable
# y = 5000
# def display():
#     y = 1000 #local variable
#     print(x)
#     print(y)
#
# print(x)
# display()
# print(y)

# x = 0 #global variable
# def display():
#     y = 1000 #local variable
#     print(x)
#     print(y)
#     return y
#
# print(x)
# d = display()
# print(d)

# x = 0 #global variable
# def display():
#     global x
#     x = 1000 #local variable
#     print(x)
#
# display()
# print(x)
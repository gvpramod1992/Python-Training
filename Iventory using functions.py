# write to a file
# file name
# location
# write
# open - python function to write/read from a file


####### addItem #########
def addItem():
    item = input('Enter item : ')

    with open('inventory.txt', 'a') as fp:
        fp.write(item + '\n')

    print("Item added successfully")

####### deleteItem #########
def deleteItem():
    item = input("Enter item to delete: ")

    with open('inventory.txt', 'r') as fp:
        data = fp.read()

    data = data.splitlines()
    data.remove(item)

    with  open('inventory.txt', 'w') as fp:
        for item in range(len(data)):
            fp.write(str(data[item]) + "\n")

    print("Item {} deleted successfully".format(item))


####### searchItem #########
def searchItem():
    item = input("Enter item to search: ")

    with open('inventory.txt', 'r') as fp:
        data = fp.read()

    data = data.splitlines()
    if item in data:
        print("{} is available in the file".format(item))
    else:
        print(item + " not available in the file")

def displayItem():
    with open('inventory.txt', 'r') as fp:
        data = fp.read()
    data = data.splitlines()
    print("Items in the file are:\n ", data)

def modifyItem():
    old_item = input("Enter item to modify: ")
    new_item = input("Enter new value: ")

    with open('inventory.txt', 'r') as fp:
        data = fp.read()

    data = data.splitlines()
    position = data.index(old_item)
    data[position] = new_item

    with open('inventory.txt', 'w') as fp:
        for item in range(len(data)):
            fp.write(str(data[item]) + "\n")

    print("Item {} modified successfully".format(old_item))

while True:

    print('Available options: \n1. Add Item \n2. Delete Item \n3. Search Item \n4. Display Items \n5. Modify \n6. Exit')
    option = int(input('Choose an option: '))

    if option == 1:
        addItem()
    elif option == 2:
        deleteItem()
    elif option == 3:
        searchItem()
    elif option == 4:
        displayItem()
    elif option == 5:
        modifyItem()
    elif option == 6:
        break
    else:
        print('Invalid option')

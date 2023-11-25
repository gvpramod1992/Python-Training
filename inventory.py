from datetime import datetime
# write to a file
# file name
# location
# write
# open - python function to write/read from a file

def print_items():
    yield 10
    yield 20
    yield 30


####### addItem #########
def addItem():
    item = input('Enter item : ')
    quantity = input('Enter Quantity : ')
    curr_date = datetime.strftime(datetime.now(), "%Y:%m:%d %H:%M:%S" )
    with open('inventory.txt', 'a') as fp:
        fp.write(curr_date + " " + item + " " + quantity + '\n')
    print("Item added successfully")

####### deleteItem #########
def deleteItem():
    item = input("Enter item to delete: ")

    with open('inventory.txt', 'r') as fp:
        data = fp.read()

    data = data.splitlines()
    data.remove(item)

    with open('inventory.txt', 'w') as fp:
        for item in range(len(data)):
            fp.write(str(data[item]) + "\n")

    print("Item {} deleted successfully".format(item))


####### searchItem #########
def searchItem():
    item = input("Enter item to search: ")

    with open('inventory.txt', 'r') as fp:
        data = fp.read()

    data = data.splitlines()
    found = 0
    for d_ele in data:
        if item in d_ele:
            print("{} is available in the file".format(item))
            found = 1
            break
    if found == 0:
        print("{} is NOT in the file".format(item))

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

def get_item_quantity(item):
    with open('inventory.txt', 'r') as fp:
        data = fp.readlines()
        for d_item in data:
            if item in d_item:
                item_detail = d_item.split(" ")
                if len(item_detail) == 4:
                    return item_detail[-1]

def get_total_qty():
    total = 0
    items = set()
    with open('inventory.txt', 'r') as fp:
        data = fp.readlines()
        for d_item in data:
            item = d_item.split(" ")[2]
            items.add(item.strip('\n'))

    for item in items:
        qty=get_item_quantity(item)
        if qty:
            total += int(qty.strip('\n').strip('kg'))

    print(total)




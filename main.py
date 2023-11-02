# Inventory management
# 1. AddItem, 2. RemoveItem, 3. DisplayItems

# Add 1-10 items
items = []
#
while True:
    print('Available options: \n1. Add Item \n2. Delete Item \n3. Search Item \n4. Display Items \n5. Exit')
    option = int(input('Choose an option: '))
    if option == 1: # Add Item
        item = input('Enter item name: ')
        # items.append(item)
        # write to a file
            # file name
            # location
            # write
        # open - python function to write/read from a file

        fp = open('inventory.txt', 'a')
        fp.write(item + '\n')
        fp.close()
    elif option == 2: # Delete Items
        fp = open('inventory.txt', 'r')
        x = input('Enter item name to Delete: ')
        data = [items.pop(x) for x in fp.readlines()]
        print(data)
    elif option == 3: # Search Items
        fp = open('inventory.txt', 'r')
        Y = input('Enter item name to Search: ')
        data = [item.rfind(Y) for item in fp.readlines()]
        print(data)
    elif option == 4: # Display Items
        fp = open('inventory.txt', 'r')
        data = [item.rstrip('\n') for item in fp.readlines()]
        print(data)
    elif option == 5: # Exit
        break
    else:
        print('Invalid option')

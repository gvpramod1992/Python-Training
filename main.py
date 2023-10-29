# Inventory management
# 1. AddItem, 2. RemoveItem, 3. DisplayItems

# Add 1-10 items
items = []
#
while True:
    print('Available options: \n1. AddItem \n2. DeleteItem \n3. SearchItem \n4. DisplayItems \n5.Exit')
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
        fp.write(item + '\n')
        fp.close()
    elif option == 2:
        fp = open('inventory.txt', 'r')
        data = [item.rstrip('\n') for item in fp.readlines()]
        print(data)
    elif option == 3:
        break
    else:
        print('Invalid option')

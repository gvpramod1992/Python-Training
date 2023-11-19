import inventory


while True:

    print('Available options: \n1. Add Item \n2. Delete Item \n3. Search Item \n4. Display Items \n5. Modify \n6. Exit')
    option = int(input('Choose an option: '))

    if option == 1:
        inventory.addItem()
    elif option == 2:
        inventory.deleteItem()
    elif option == 3:
        inventory.searchItem()
    elif option == 4:
        inventory.displayItem()
    elif option == 5:
        inventory.modifyItem()
    elif option == 6:
        break
    else:
        print('Invalid option')



# # Inventory management
# # 1. AddItem, 2. RemoveItem, 3. DisplayItems
#
# # Add 1-10 items
# items = []
# #
#
# while True:
#     print('Available options: \n1. Add Item \n2. Delete Item \n'
#           '3. Search Item \n4. Display Items \n5. Modify \n6. Exit')
#     option = int(input('Choose an option: '))
#     if option == 1:  # Add Item
#         item = input('Enter item name: ')
#         # items.append(item)
#         # write to a file
#             # file name
#             # location
#             # write
#         # open - python function to write/read from a file
#
#         # fp = open('inventory.txt', 'a')
#         # fp.write(item + '\n')
#         # fp.close()
#         with open('inventory.txt', 'a') as fp:
#             fp.write(item + '\n')
#
#     elif option == 2:  # Delete Items
#         fp = open('inventory.txt', 'r')
#         x = input('Enter item name to Delete: ')
#         data = [item.rstrip('\n') for item in fp.readlines()]
#         fp.close()
#
#         if x in data:
#             data.remove(x)
#             fp = open('inventory.txt', 'w')
#             for item in data:
#                 fp.write(item + '\n')
#             fp.close()
#         else:
#             print(f'{x} not found.')
#
#         print(f'{x} removed successfully')
#         print(data)
#     elif option == 3: # Search Items
#         fp = open('inventory.txt', 'r')
#         Y = input('Enter item name to Search: ')
#         data = [item.rstrip('\n') for item in fp.readlines()]
#         if Y in data:
#             print(f'{Y} is available')
#         else:
#             print(f'{Y} is NOT available')
#
#     elif option == 4:  # Display Items
#         fp = open('inventory.txt', 'r')
#         data = [item.rstrip('\n') for item in fp.readlines()]
#         print(data)
#     elif option == 5:  # Add Item
#         fp = open('inventory.txt', 'r')
#         data = [item.rstrip('\n') for item in fp.readlines()]
#         data[4] = 'Item5'
#         fp.close()
#
#         fp = open('inventory.txt', 'w')
#         for item in data:
#             fp.write(item + '\n')
#         fp.close()
#
#     elif option == 6: # Exit
#         break
#     else:
#         print('Invalid option')
#

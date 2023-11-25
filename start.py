
# try, except

import inventory

while True:
    try:
        print('Available options: \n1. Add Item \n2. Delete Item \n3. Search Item '
              '\n4. Display Items \n5. Modify \n6. Get Quantity \n7. Get Total Quantity \n8. Exit')
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
            item=input('Enter Item Name: ')
            inventory.get_item_quantity(item)
        elif option == 7:
            inventory.get_total_qty()
        elif option == 8:
            break
        else:
            print('Invalid option')
    except ValueError:
        print('Invalid number entered')
    except FileNotFoundError:
        print('File not found')
    except:
        print('something went wrong')
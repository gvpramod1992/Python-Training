
with open('inventory.txt', 'w') as fp:
    print(fp.tell())
    fp.write('ABC')
    print(fp.seek(30))
    print(fp.tell())
    fp.write('123')



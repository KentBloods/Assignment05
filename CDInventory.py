#------------------------------------------#
# Title: CDInventory.py
# Desc: Starter Script for Assignment 05
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, Created File
# KBloodsworth, 2022-Feb-27, Finished TODO's
#------------------------------------------#

# Declare variabls

strChoice = '' # User input
lstTbl = []  # list of lists to hold data
dicRow = {}  # list of data row
strFileName = 'CDInventory.txt'  # data storage file
objFile = None  # file object

# Get user Input
print('The Magic CD Inventory\n')
while True:
    # 1. Display menu allowing the user to choose:
    print('[l] load Inventory from file\n[a] Add CD\n[i] Display Current Inventory')
    print('[d] delete CD from Inventory\n[s] Save Inventory to file\n[x] exit')
    strChoice = input('l, a, i, d, s or x: ').lower()  # convert choice to lower case at time of input
    print()

    if strChoice == 'x':
        # 5. Exit the program if the user chooses so
        break
    if strChoice == 'l':
        # Add the functionality of loading existing data
        lstTbl.clear()
        objFile = open('CDInventory.txt', 'r')
        for row in objFile:
            lstRow = row.strip().split(',')    
            dicRow = {'ID': int(lstRow[0]), 'Title':lstRow[1], 'Name':lstRow[2]}
            lstTbl.append(dicRow)
        objFile.close()
        # New results
        print('New items in list:')
        for row in lstTbl:
            print(*row.values(), sep = ', ')
    elif strChoice == 'a':  # no elif necessary, as this code is only reached if strChoice is not 'exit'
        # 2. Add data to the table (2d-list) each time the user wants to add data
        strID = input('Enter an ID: ')
        strTitle = input('Enter the CD\'s Title: ')
        strArtist = input('Enter the Artist\'s Name: ')
        intID = int(strID)
        dicRow = {'ID':strID, 'Title':strTitle, 'Name':strArtist}
        lstTbl.append(dicRow)
    elif strChoice == 'i':
        # 3. Display the current data to the user each time the user wants to display the data
        print('ID, CD Title, Artist')
        for row in lstTbl:
            print(*row.values(), sep = ', ')
    elif strChoice == 'd':
        # Add functionality of deleting an entry
        print('Select from the list which entry to delete')
        for row in lstTbl:
            print(*row.values(), sep = ', ')
        print('\nNote that the index starts at 0')
        entry = int(input('Enter the index for the entry you want to delete: '))
        del lstTbl[entry]
        print('\nNew table is now:')
        for row in lstTbl:
            print(*row.values(), sep = ', ')
    elif strChoice == 's':
        # 4. Save the data to a text file CDInventory.txt if the user chooses so
        objFile = open('CDInventory.txt', 'a')
        for row in lstTbl:
            strRow = ''
            for item in row.values():
                strRow += str(item) + ','
            strRow = strRow[:-1] + '\n'
            objFile.write(strRow)
        objFile.close()
    else:
        print('Please choose either l, a, i, d, s or x!')
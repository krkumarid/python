"""

CURD

Create a program that displays the following menu

1.Display the database
2. Add an item
3. Delete an item
4. Change an item
5 .Quit

The program contains a list of items; for exmaple fruits

if you select 1, then program displays the items in the list, numbering each item. for exmaple 

0: orange
1: banana
2: blackberry

if you select 2 the program asks you to entyer a new item, it adds what you are typed to the list.

If you select 3 , the program asks you to enter the list number of an item to delete. It delets the specified item from the list.

If you select 4, the program asks you to enter the list number of an item to change, then asks you to enter text, It changes the specified item to the specified text.


if you select 5 , the program quits

Until you quit with option 5, the program displays the menu again after every action.




Docstring for database_exercise
"""

def add_item(db):
    item = input("Enter a new fruit item to the lsit :")
    db.append(item)
    show_database(db)


def change_item(db):
    item_number = input("Enter number of item to change: ")
    item = input("Enter new Item: ")
    db[ int( item_number)] = item

def delete_item(db):
    item_number = input("Enter number of item to change: ")
    item = input("Enter new Item: ")
    db.pop( int(item_number))

def show_database( db):
    i=0
    for i in range(len(db)):
        print( str(i )+ ":" + db[i])
    
def show_menu():
    options = ("Display databse","Add an item","Delete an Item","Change an item","Quit")
    print()
    for i in range(0, len(options)):
        print( str(i+1)  + ": " + options[i])
    print()

def main():

    db = ['Orange','Banana', 'Blackberry']
    do_loop = True

    while do_loop:
        show_menu()
        option = int(input("Select your option >>>  "))
        if( option ==1 ):
            show_database(db)
        elif( option ==2 ):
                add_item(db)
        elif( option == 3):
                delete_item(db)
        elif( option == 4 ):
                change_item(db)
        elif option == 5:
                do_loop = False
        else:
             print("Invalid choice")
    return


main()

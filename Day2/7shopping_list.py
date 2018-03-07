def help_menu():
    print("Press 'h' for help menu")
    print("Press 's' to show the item in your list")
    print("Press 'a' to add a new item to the list")
    print("Press 'r' to remove an item from the list")
    print("Press 'q' to quit")
    print()


def show_items(arg):
    if not arg:
        print("There are no items on the list!\n")
    else:
        show = [print(str(i+1) + ": " + arg[i]) for i in range(len(arg))]
        print()
        return show


def add_item():
    item = input("What do you want to add? ")
    pos = input("Position to add: ")
    if pos == "":
        mylist.append(item)
    else:
        mylist.insert(int(pos), item)
    print()


def remove_item():
    item = input("What do you want to remove? ")
    if item in mylist:
        mylist.remove(item)
    else:
        print("No such item in the list.")
    print()


def to_do():
    return input("What do you want to do? ")


# app starts here with a help_menu
help_menu()

# creates an empty list when the app starts
mylist = []

while True:
    do = to_do()
    if do == 's':
        show_items(mylist)
    elif do == 'a':
        add_item()
    elif do == 'r':
        remove_item()
    elif do == 'h':
        help_menu()
    elif do == 'q':
        break
    else:
        help_menu()

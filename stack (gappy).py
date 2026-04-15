#initialise top pointer and max_size..
top = #index of the item at the top of the stack, -1 meaning empty stack
max_size = #could be set to any size
#initialise array to hold max_size of data items, all as None...
items = [None for i in range(max_size)]

def push(item):
    #push procedure needs to update the top pointer globally
    global top
    #deal with full stack..
    if (top + ???) > (max_size???):
        print("Error: stack is full!")
    else: #..or update top and items array..
        top = ??????
        items[??????] = ??????

def pop():
    global top, items
    #
    if top >= ?????:
        item = ?????
        top = ?????
        return item
    else:
        print("Error: stack is empty!")

#testing the code
for i in range(12):
    push(input("What do you want pushed to the stack? "))
for i in range(12):
    print(pop())

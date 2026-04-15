#initialise pointers and max_size; here set both to -1 for empty queue
front = rear = -1 #index of front and rear items set to -1
max_size = 10 #could be set to any size

#initialise array to hold max_size of data items, all as None...
??????????????????

def enqueue(item):
    #enqueue procedure needs to update pointers globally...
    global rear, front

    #if there is room....
    if ?????? % ?????? != front:
        #update rear (looping back to the array start if necessary)
        rear = (??????) % max_size
        #put item in position at rear of queue..
        ????????????????????????
        print(item + "was added at position " + str(??????))
        #if item was added to an empty list, update front..
        if front == ??????:
            ??????
    else:
        print("Error, queue is full")

def dequeue():
    #dequeue procedure needs to update pointers globally
    global rear, front

    if front == ??????:
        print("Error: stack is empty!")
        return None
    else:
        item = ????????????
        print(item + " removed from position " + str(??????))
        if front == rear:#reset the queue if last item removed
            ??????????????????
        else:
            front = ??????????????????
        return item

#testing the code...
for i in range(11):
    enqueue(input("What do you want to join the queue? "))
for i in range(11):
    dequeue()
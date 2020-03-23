class StackDemo():

    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, data):
        self.items.append(data)

    def pop(self):
        return self.items.pop()


s = StackDemo()
while True:
    print("1. push")
    print("2. pop")
    print("3. display")
    print("4. quit")

    do = int(input("Enter your choice: "))
    if do == 1:
        val = input("Enter a value: ")
        s.push(val)
    elif do == 2:
        if s.is_empty():
            print("Stack is empty")
        else:
            print("Popped value is :" + s.pop())
    elif do == 3:
        if s.is_empty():
            print("Stack is empty")
        else:
            print("Stack values are :" + str(s))
    elif do == 4:
        break
    else:
        print("Wrong entry! Please continue")
        continue










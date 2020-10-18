try:
    number = int(input("Enter a number: "))
    print(number)
except ValueError as err: #Here ValueError is a exception type and err is the value we are printing
    print(err)
except KeyboardInterrupt as err:
    print(err)

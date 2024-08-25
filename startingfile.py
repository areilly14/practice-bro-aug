for x in range(20):
    if x%3 == 0:
        print("fizz")
        if x%5 == 0:
            print("fizz buzz")
    elif x%5 == 0:
        print("buzz")
    else:
        print (x)


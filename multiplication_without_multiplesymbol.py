def multiple(a, b):
    c= 0
    if (a == 0 or b == 0):
        return 0
    else:
        for i in range (b):
            c+=a
    print(c)
multiple(16, 2)

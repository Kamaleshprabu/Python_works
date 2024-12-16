n = int(input("Enter value for n: "))
for i in range(n + 1):
    if(i == n):
        for j in range (n):
            print ("* " * (n - j))
    else:
        print("* " * i)
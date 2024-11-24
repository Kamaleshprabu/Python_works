arr = [2, 3, 4, 6, 8, 9, 11, 14, 17, 19, 20, 22]

l = 0
r = len(arr) - 1

m = round((l + r)/ 2)

if(arr[m] == 19):
    print("True")
elif(arr[m] > 19):
    r = m
elif(arr[m] < 19):
    l = m
    
def find(l, r):
    m = round((l + r)/ 2)
    if(arr[m] == 19):
        return True
    elif(arr[m] > 19):
        r -= 1
        return find(l, r)
    elif(arr[m] < 19):
        l += 1
        return find(l, r)
print(find(l, r))
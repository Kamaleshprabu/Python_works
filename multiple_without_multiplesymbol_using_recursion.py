def multiple(a, b):
    if (a == 0 or b == 0):
        return 0
    else:
        return multiplication(a, b, b)
        
def multiplication(a, b, count):
    if (count == 0):
        return 0
    else:
        return a + multiplication(a, b, count - 1)
        
print(multiple(2,4))
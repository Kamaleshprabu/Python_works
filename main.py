#factorial

def fact_rec(n):
  if n == 1 or n == 0:
    return 1 
  else:
    return n*fact_rec(n-1)

number = int (input ("Enter a Value :"))
res = fact_rec(number)

print("factorial of {} is {} .". format (number,res))
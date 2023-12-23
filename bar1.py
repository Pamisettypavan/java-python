import math
for i in range(1,5000):
    Temp = i
    Sum = 0
    while(Temp > 0):
        Reminder = Temp % 10
        Factorial = math.factorial(Reminder)
        Sum = Sum + Factorial
        Temp = Temp // 10
    
    if (Sum == i):
        print(" %d is a Strong Number" %i)
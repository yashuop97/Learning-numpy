import numpy as np


rolls = []

for i in range(100000):

    numbers = np.random.randint(1,7)

    rolls.append(numbers)

numbers = [1,2,3,4,5,6]

def result():
    prob = int(input("What number probability you want: "))
    

    times = rolls.count(prob)
    
    if prob in numbers:
        print(f"{times/100000 * 100}")

    else:
        print("Invalid number")
        result()

result()


#done
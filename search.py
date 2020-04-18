lists = [1, 6, 20, 40, 100, 150, 1000]

def search(list, number):
    i = 0
    while list[i] != number:
        i = i + 1
    return i 

def binary_search(list, number):
    i = 0
    low = 0 
    high = len(lists) - 1
    while low != high:
        i = i + 1
        guess = int((low + high)/2 + 1)
        if list[guess] == number:
            return guess
        elif list[guess] < number:
            low = guess
        elif list[guess] > number:
            high = guess
        print("low = ", low, "high = ", high, "guess = ", guess) 
        print("i ")   
    return 0


print  (search(lists, 1000))
print  (binary_search(lists, 1000))
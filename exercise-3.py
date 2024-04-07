def remove_all_after(numbers, n):
    try:
        index = numbers.index(n)  
        return numbers[:index + 1] 
    except ValueError:
        return numbers

print(remove_all_after([1, 2, 3, 4, 5], 3))  
print(remove_all_after([1, 1, 2, 2, 3, 3], 2))  

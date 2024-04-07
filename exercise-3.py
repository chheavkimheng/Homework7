def remove_all_after(numbers, n):
    ...
def remove_all_after(numbers, n):
    if not numbers:
        return []
    try:
        idx = numbers.index(n)
        return numbers[:idx+1]
    except ValueError:
        return numbers

print(remove_all_after([1, 2, 3, 4, 5], 4))    
print(remove_all_after([1, 2, 2, 2, 3, 3], 3))  

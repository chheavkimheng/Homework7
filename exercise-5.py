def reverse_ascending(numbers):
    result = []
    subsequence = []
    
    for num in numbers:
        if not subsequence or num > subsequence[-1]:
            subsequence.append(num)
        else:
            result.extend(subsequence[::-1])
            subsequence = [num]
    
    result.extend(subsequence[::-1])
    return result

input_list1 = [1, 2, 3, 4, 5]
input_list2 = [5, 7, 10, 4, 2, 7, 8, 1, 3]
input_list3 = [5, 4, 3, 2, 1]
input_list4 = []

print(list(reverse_ascending(input_list1)))  
print(list(reverse_ascending(input_list2)))  
print(list(reverse_ascending(input_list3)))  
print(list(reverse_ascending(input_list4))) 

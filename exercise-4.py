def chunking_by(numbers, chunck):
    if not numbers:
        return []
    
    chunks = []
    
    for i in range(0, len(numbers), chunck):
        chunks.append(numbers[i:i + chunck])
    
    return chunks
print(chunking_by([8, 2, 7, 5, 1, 0, 2, 6, 3, 7], 3))  
print(chunking_by([4, 2, 5, 3, 5, 8], 2))             

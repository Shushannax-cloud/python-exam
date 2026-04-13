def even_numbers(listn):
    even_list = []
    for i in listn:
        if i % 2 == 0:
            even_list.append(i)
    return even_list 
listn = [1, 4, 5, 6, 8]
print(even_numbers(listn))
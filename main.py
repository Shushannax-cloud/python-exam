def even_numbers(listn):
    even_list = []
    for i in listn:
        if i % 2 == 0:
            even_list.append(i)
    return even_list 
listn = [int(input()) for _ in range(5)]
print(even_numbers(listn))
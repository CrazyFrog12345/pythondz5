#задача 34

def rhythm(str):
    str = str.split()
    list_1 = []
    for word in str:
        sum_w = 0
        for i in word:
            if i in 'аеёиоуыэюя':
                sum_w += 1
        list_1.append(sum_w)
    return len(list_1) == list_1.count(list_1[0])

str_1 = 'пара-ра-рам рам-пам-папам па-ра-па-дам'
if rhythm(str_1):
    print('Парам пам-пам')
else:
    print('Пам парам')

    #Задача 36

   def print_operation_table(operation,num_rows,num_columns):   
    for i in range(1,num_rows+1):
        print()
        for j in range(1,num_columns+1):
            print(operation(i,j), end="   ")

print_operation_table(lambda x, y: x * y,6,6) 
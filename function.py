print("работа с функциями: задание 1")


def get_summ(one, two, delimiter='&'):
     
     return f'{one}{delimiter}{two}'
    #return a



result = get_summ('learn','python')
print (result)
print ('')
print (str.upper(result),)

print("работа с функциями: задание 2")

def format_price(price):
    price = int(price)
    return f'Цена:{price} руб.'

task2 = format_price(56.24)
print(task2)

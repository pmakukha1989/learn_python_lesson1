
#Практика: Числа


#print ('Практика: числа')
#a = 2
#b = 2.5 - a
#print (a + b)

#Практика: Строки
#print(' ')
#print('Практика: Строки')

#name = 'Pavel'
#toPrint = f'hello, {name}'
#print (toPrint)

#Практика числа: input

#print(' ')
#print('Практика числа: input')

#v = input('Введите число от 1 до 10: ')
#vInt = int(v)
#v10= vInt +10
#print (v10)


#Практика строки: input

# print(' ')
# print('Практика строки: input')
# userName = input('Введите ваше имя: ')

# print ( f'Привет,{userName}. Как дела?')


#Практика: Приведение типов

# print(' ')
# print('Практика: Приведение типов')
# print (float('1') ) 
# print(' ')
# print (int(2.5))  # ???
# print(' ')
# print (bool(1))  # ???
# print(' ')
# print (bool(''))  # ???
# print(' ')
# print (bool(0))  # ???
# print(' ')


# print('практика Приветствие')
# print('')
# name= 'pavel'
# print (name)
# print('')
# print('Информация о пользователе')
# print('')

# first_name = 'Pavel'
# last_name = 'Makukha'
# user_info = {first_name,last_name}

# user_info = {
#   "first_name": "Pavel",
#   "last_name": "Makukha",
# }

# print (user_info['first_name'])



# some_list = [ 3, 5, 7, 9 , 10.5]
# print (some_list)

# some_list.append('Python')
# print ('')
# print (some_list)
# print ('')
# print (len(some_list))

# print('')
# print (some_list[0])
# print ('')
# print (some_list[-1])
# print('')
# print( some_list[1:3])
# print ('')
# del some_list [-1]
# # print (some_list)


# city_weather = {
# "city": "Москва", 
# "temperature": "20"
# }

# print (city_weather["city"])

# city_weather ['temperature'] = int( city_weather ['temperature']) -5

# print (city_weather)
# print (  f"country: {city_weather.get('country')}" )
# print ('')
# print (city_weather.get('country', 'Russia'))
# print ('')
# city_weather['date']= '27.05.2019'
# print (len (city_weather))


stock_items = [
  {'name' : 'iphone 5', 'price':'100', 'stock':'5' },
  {'name' : 'iphone 6', 'price':'200', 'stock':'10' },
  {'name' : 'iphone 7', 'price':'300', 'stock':'20' },
  {'name' : 'iphone 8', 'price':'400', 'stock':'30' },
  {'name' : 'iphone x', 'price':'500', 'stock':'40' }
]

# что сделать
# 1. вытащить  сток в список (?)
# 2. найти значение макс
# 3. в словаре найти стоимость модели с максималным остатком
# 4. снизить эту стоимость на 10%
a=0
stocks_list={} 
for x in stock_items:
  #print (x)
  stocks_list.append(stock_items[a]['stock'])
  print(stock_items[a]['stock'])
  a=a+1
print (stocks_list)
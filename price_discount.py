

# какую проблему решаем: снизить на 10% стоимость телефона с самым большим остатком на складе
stock_items = [
  {'name' : 'iphone 5', 'price':'100', 'stock':'5' },
  {'name' : 'iphone 6', 'price':'200', 'stock':'10' },
  {'name' : 'iphone 7', 'price':'300', 'stock':'20' },
  {'name' : 'iphone 8', 'price':'400', 'stock':'30' },
  {'name' : 'iphone x', 'price':'500', 'stock':'40' }
]
stocks_list=[]
#нахожу  значение самого большого остатока
for x in stock_items:
  stocks_list.append( int(x['stock']) )
max_stock =  max(stocks_list)


print(max_stock)

#нахожу телефон с таким значением остатка и меняю цену
for x in stock_items:
    if  int (x ['stock'] )== max_stock:
        print( 'Было ' + str (x) )
        x ['price'] = int(x['price']) * 0.9 
        print( 'Стало ' +str (x) )




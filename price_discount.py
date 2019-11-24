


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


#
a=0
stocks_list=[]
for x in stock_items:
  #print(stock_items[a]['stock'])
  stocks_list.append( int(stock_items[a]['stock']) )
  a=a+1

#print (stocks_list)
#print ( max(stocks_list))
max_stock =  max(stocks_list)

a=0
for x in stock_items:
  if  int(stock_items[a]['stock']) == max_stock:
    print( 'Было ' + str (stock_items[a]))
    stock_items[a]['price'] = int(stock_items[a]['price']) * 0.9 
    print( 'Стало ' +str (stock_items[a]))
  a=a+1



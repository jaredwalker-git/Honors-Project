stock_price = [100, 50, 100]
num_stocks = [1, 1, 1]
cash = 0
action_vec = [2, 0, 1]
buy_index = []
#0 buy, 1 hold, 2 sell


for i in range(len(action_vec)):
    if action_vec[i] == 2:
        cash += (stock_price[i] * num_stocks[i]) 
        num_stocks[i] = 0
    if action_vec[i] == 0:
       buy_index.append(i)
canbuy = True
while canbuy:
    for i in buy_index:
        if cash > stock_price[i]:
            cash -= stock_price[i]
            num_stocks[i] += 1   
        else:
            canbuy = False

print(num_stocks)   

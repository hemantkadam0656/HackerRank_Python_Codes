def maximumProfit(prices):
    n = len(prices)
    buy = prices[0]
    profit = 0
    maxprofit = 0
    
    for i in range(1,n):
        if prices[i]< buy:
            buy= prices[i]

    
    for i in range(1, n):
        profit = prices[i] - buy
        print(profit,prices[i])
        if maxprofit < profit:
            maxprofit = profit
        
  
    print(maxprofit)

if __name__ == '__main__':
    prices = [7, 10, 1, 3, 6, 9, 2]
    obj = maximumProfit(prices)


    
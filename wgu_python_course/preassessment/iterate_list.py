'''
Create a solution that accepts an integer input identifying how many shares of stock are to be purchased from the Old Town Stock Exchange, followed by an equivalent number of string inputs representing the stock selections. The following dictionary stock lists available stock selections as the key with the cost per selection as the value.

stocks = {'TSLA': 912.86 , 'BBBY': 24.84, 'AAPL': 174.26, 'SOFI': 6.92, 'KIRK': 8.72, 'AURA': 22.12, 'AMZN': 141.28, 'EMBK': 12.29, 'LVLU': 2.33}

Output the total cost of the purchased shares of stock to two decimal places.

The solution output should be in the format

Total price: $cost_of_stocks
Sample Input/Output:
If the input is

3
SOFI
AMZN
LVLU
then the expected output is

Total price: $150.53
'''

stocks = {'TSLA': 912.86, 'BBBY': 24.84, 'AAPL': 174.26, 'SOFI': 6.92, 'KIRK': 8.72, 'AURA': 22.12, 'AMZN': 141.28, 'EMBK': 12.29, 'LVLU': 2.33}

#solution accepts an integer input representing the number of stock selections
#solution accepts string inputs equivalent to the integer input identifying the stock selections
#solution outputs the total cost of stock as "Total price: $" followed by the total cost to 2 decimal places

num_shares = int(input())

cost_of_stocks = 0.0

for num in range(num_shares): # cycle through user input and receive desired stocks to purchase
    selected_stocks = input()
    if selected_stocks in stocks: # check if desired stocks are in list
        cost_of_stocks += stocks[selected_stocks]

print(f'Total price: ${cost_of_stocks:.2f}')




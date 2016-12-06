'''
def initialize(context):
    context.security = [sid(8554)]
      
def handle_data(context, data):
    print(data)

    price_hist = data.history(context.security,'price',200,'1d')  
    MA1 = price_hist[-50:].mean()
    MA2 = price_hist.mean()
    
    current_price = data.current(context.security, 'price')
    current_positions = context.portfolio.positions[symbol('SPY')].amount
    cash = context.portfolio.cash

    if (MA1 > MA2) and current_positions == 0:
        number_of_shares = int(cash/current_price)
        order(context.security, number_of_shares)
        log.info('Buying shares')
       
    elif (MA1 < MA2) and current_positions > 0:
        order_target(context.security, 0)
        log.info('Selling shares')
        
    record(MA1 = MA1, MA2 = MA2, Price = current_price)
'''

# This initialize function sets any data or variables that you'll use in
# your algorithm.
def initialize(context):
    context.stock = symbol('SPY')  # Boeing
    
    # Since record() only works on a daily resolution, record our price at the end
    # of each day.
    schedule_function(record_vars,
                      date_rule=date_rules.every_day(),
                      time_rule=time_rules.market_close(hours=1))
    
# Now we get into the meat of the algorithm. 
def record_vars(context, data):
    # Create a variable for the price of the Boeing stock
    current_price = data.current(context.stock, 'price')
    
    # Create variables to track the short and long moving averages. 
    # The short moving average tracks over 20 days and the long moving average
    # tracks over 80 days. 
    price_history = data.history(context.stock, 'price', 26, '1d')
    short_mavg = price_history[-12:].mean()
    long_mavg = price_history.mean()
    
    
    # Create current positions
    current_positions = context.portfolio.positions[symbol('SPY')].amount
    cash = context.portfolio.cash
                                                   

    # If the short moving average is higher than the long moving average, then 
    # we want our portfolio to hold 500 stocks of Boeing
    if (short_mavg > long_mavg) and current_positions == 0:
        #order_target(context.stock, +500)
    
        number_of_shares = int(cash/current_price)
        order(context.stock, number_of_shares)
        log.info('Buying shares')
    
    
    
    # If the short moving average is lower than the long moving average, then
    # then we want to sell all of our Boeing stocks and own 0 shares
    # in the portfolio. 
    elif (short_mavg < long_mavg) and current_positions != 0:
        #order_target(context.stock, 0)

    #elif (MA1 < MA2) and current_positions > 0:
        order_target(context.stock, 0)
        log.info('Selling shares')     
        
        
        
    # Record our variables to see the algo behavior. You can record up to 
    # 5 custom variables. Series can be toggled on and off in the plot by
    # clicking on labeles in the legend. 
    record(short_mavg = short_mavg, long_mavg = long_mavg, Price = current_price)
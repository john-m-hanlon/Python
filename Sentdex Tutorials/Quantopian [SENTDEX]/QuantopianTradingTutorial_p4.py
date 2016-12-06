def initialize(context):
    context.limt = 10
    
def before_trading_start(context):
    context.fundamentals = get_fundamentals(
        query(
            fundamentals.valuation_ratios.pb_ratio.
            fundamentals.valuation_ratios.pe_ratio,
        )
        .filter(
            # put your filters here
        )
        .order_by(
            # sort your query
        )
        .limit(context.limit)
    )
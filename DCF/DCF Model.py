import pandas as pd

# Step 1: Calculate and project unlevered free cash flow
# Step 2: Calculate the WACC
# Step 3: Calculate the terminal value
# Step 4: Present value the cash flows and add them to get the TEV of the
# company
# Step 5: Calculate stock price for a public company

# Global Variables
Tax_Rate = 0.35
Start_Year = 2017
Growth_Rate = 0.05
TV_Method = 'TM'
Gordon_Growth_Rate = 0.02
Exit_Multiple = 5.5
beta = 1

# Step 1: Calculate and project unlevered free cash flow


def calc_unlevered_free_cash_flow():
    '''
    Calculate the unlevered free cash flows

    Parameters
    ==========

    N/A : Takes no parameters at the moment

    Returns
    =======

    ufcf : int
        Unlevered free cash flow for the company

    '''

    EBIT = 15
    Taxes = EBIT * Tax_Rate
    CAPEX = 5
    NWC = 2
    DA = 5

    ufcf = EBIT - Taxes - CAPEX - NWC + DA
    return ufcf


def project_ufcf(start_year, growth_rate):
    '''
    Project the unlevered free cash flows to infinity since we can assume that
    the company is a going concern. However, since we cannot project the cash
    flows to infinty, we project free cash flows for a period of five or 10
    years, or until the company reaches a steady state of growth

    Parameters
    ==========

    start_year : int
        The first year in which we are analyzing the data

    growth_rate : int
        The growth rate by which we are going to assume the company will grow
        EBIT or Revenue on an annual basis

    Returns
    =======

    df : Data frame
        Data Frame with the project unlevered free cash flows
    '''

    growth_rate = 1 + growth_rate

    ufcf_1 = calc_unlevered_free_cash_flow()
    ufcf_2 = ufcf_1 * growth_rate
    ufcf_3 = ufcf_2 * growth_rate
    ufcf_4 = ufcf_3 * growth_rate
    ufcf_5 = ufcf_4 * growth_rate

    yr1 = start_year
    yr2 = yr1 + 1
    yr3 = yr2 + 1
    yr4 = yr3 + 1
    yr5 = yr4 + 1

    df = pd.DataFrame({yr1: ufcf_1,
                       yr2: ufcf_2,
                       yr3: ufcf_3,
                       yr4: ufcf_4,
                       yr5: ufcf_5}, index=['ufcf'])

    return df


# Step 2: Calculate the WACC


def calc_CAPM(beta):
    '''
    The cost of equity is calculated using the capital asset pricing model
    (CAPM)

    Parameters
    ==========
    beta : float
        levered beta, which is the measure of the volatility or covariance of
        the return on a security compared to the market as a whole,
        i.e., systematic risk

    Returns
    =======

    capm : int
        the cost of equity
    '''

    b = beta
    rf = .0241
    rm = .0700
    capm = rf + (b * (rm - rf))
    return capm


def calc_WACC():
    '''
    Weighted average cost of capital or (WACC) is a weighted average after-tax
    cost or required rate of return for different sources of capital for a
    company, i.e., debt, preferred, and equity

    Parameters
    ==========
    beta : float
        levered beta, which is the measure of the volatility or covariance of
        the return on a security compared to the market as a whole,
        i.e., systematic risk


    Returns
    =======
    wacc : int
        The required rate of return or weighed average cost of capital for the
        company

    '''

    ke = calc_CAPM(beta)
    kd = .05
    kp = .01

    emkt = 10
    dmkt = 15
    pfmkt = 5

    capital_structure = emkt + dmkt + pfmkt

    wacc_e = (ke * (emkt / capital_structure))
    wacc_d = (kd * (dmkt / capital_structure) * (1 - Tax_Rate))
    wacc_pf = (kp * (pfmkt / capital_structure))

    wacc = wacc_e + wacc_d + wacc_pf
    # print(wacc)
    return wacc


# Step 3: Calculate the terminal value


def calc_terminal_value(tv_method, gordon_growth_rate, beta):
    '''
    There are two methods for calculating terminal value, namely the Gordon
    Growth model or the exit multiple method

    Parameters
    ==========

    x : str
        Either GGM or TM should be entered to indicate if we are going to use
        the Gordon Growth Model or Terminal Multiple method

    Returns
    =======

    terminal_value : data frame
        Returns the terminal vaule in a data frame cell

    '''
    beta = beta
    tv_method = TV_Method
    gordon_growth_rate = Gordon_Growth_Rate
    ebitda_multiple = Exit_Multiple
    r = calc_WACC()

    fcf = project_ufcf(Start_Year, Growth_Rate)[Start_Year + 4]

    if tv_method == 'GGM':
        terminal_value = ((fcf * (1 + gordon_growth_rate)) /
                          (r - gordon_growth_rate))

    elif tv_method == 'TM':
        terminal_value = fcf * ebitda_multiple

    else:
        print('Please review input')
        terminal_value = 0

    return terminal_value


# Step 4: Present value the cash flows and add them to get the TEV of the
# company


def calc_present_value(start_year, tv_method, beta, growth_rate):
    '''
    Calculate the present value of the projected free cash flows and the
    terminal value at the appropriate discount rate, i.e., WACC. Add the
    present value of all the cash flows to get the enterprise value of the
    company

    Parameters
    ==========

    Returns
    =======

    enterprise value : int
        The present value of the company's cash flows

    '''
    start_year = Start_Year
    growth_rate = Growth_Rate
    gordon_growth_rate = Gordon_Growth_Rate
    tv_method = TV_Method
    beta = beta

    tv = calc_terminal_value(tv_method, gordon_growth_rate, beta)
    r = calc_WACC()
    ufcf = project_ufcf(start_year, growth_rate)

    ufcf_1 = ufcf[Start_Year] / (1 + r) ** 1
    ufcf_2 = ufcf[Start_Year + 1] / (1 + r) ** 2
    ufcf_3 = ufcf[Start_Year + 2] / (1 + r) ** 3
    ufcf_4 = ufcf[Start_Year + 3] / (1 + r) ** 4
    ufcf_5 = (ufcf[Start_Year + 4] + tv) / (1 + r) ** 5

    pv = ufcf_1 + ufcf_2 + ufcf_3 + ufcf_4 + ufcf_5

    return pv


print(calc_present_value(Start_Year, TV_Method, beta, Growth_Rate))

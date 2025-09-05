""""""  		  	   		 	 	 		  		  		    	 		 		   		 		  
"""MC1-P2: Optimize a portfolio.  		  	   		 	 	 		  		  		    	 		 		   		 		  
  		  	   		 	 	 		  		  		    	 		 		   		 		  
Copyright 2018, Georgia Institute of Technology (Georgia Tech)  		  	   		 	 	 		  		  		    	 		 		   		 		  
Atlanta, Georgia 30332  		  	   		 	 	 		  		  		    	 		 		   		 		  
All Rights Reserved  		  	   		 	 	 		  		  		    	 		 		   		 		  
  		  	   		 	 	 		  		  		    	 		 		   		 		  
Template code for CS 4646/7646  		  	   		 	 	 		  		  		    	 		 		   		 		  
  		  	   		 	 	 		  		  		    	 		 		   		 		  
Georgia Tech asserts copyright ownership of this template and all derivative  		  	   		 	 	 		  		  		    	 		 		   		 		  
works, including solutions to the projects assigned in this course. Students  		  	   		 	 	 		  		  		    	 		 		   		 		  
and other users of this template code are advised not to share it with others  		  	   		 	 	 		  		  		    	 		 		   		 		  
or to make it available on publicly viewable websites including repositories  		  	   		 	 	 		  		  		    	 		 		   		 		  
such as github and gitlab.  This copyright statement should not be removed  		  	   		 	 	 		  		  		    	 		 		   		 		  
or edited.  		  	   		 	 	 		  		  		    	 		 		   		 		  
  		  	   		 	 	 		  		  		    	 		 		   		 		  
We do grant permission to share solutions privately with non-students such  		  	   		 	 	 		  		  		    	 		 		   		 		  
as potential employers. However, sharing with other current or future  		  	   		 	 	 		  		  		    	 		 		   		 		  
students of CS 7646 is prohibited and subject to being investigated as a  		  	   		 	 	 		  		  		    	 		 		   		 		  
GT honor code violation.  		  	   		 	 	 		  		  		    	 		 		   		 		  
  		  	   		 	 	 		  		  		    	 		 		   		 		  
-----do not edit anything above this line---  		  	   		 	 	 		  		  		    	 		 		   		 		  
  		  	   		 	 	 		  		  		    	 		 		   		 		  
Student Name: Stone Wang (replace with your name)  		  	   		 	 	 		  		  		    	 		 		   		 		  
GT User ID: swang3220 (replace with your User ID)  		  	   		 	 	 		  		  		    	 		 		   		 		  
GT ID: 904181297 (replace with your GT ID)  		  	   		 	 	 		  		  		    	 		 		   		 		  
"""  		  	   		 	 	 		  		  		    	 		 		   		 		  
  		  	   		 	 	 		  		  		    	 		 		   		 		  
  		  	   		 	 	 		  		  		    	 		 		   		 		  
import datetime as dt  		  	   		 	 	 		  		  		    	 		 		   		 		  
  		  	   		 	 	 		  		  		    	 		 		   		 		  
import numpy as np  		  	   		 	 	 		  		  		    	 		 		   		 		  
  		  	   		 	 	 		  		  		    	 		 		   		 		  
import matplotlib.pyplot as plt  		  	   		 	 	 		  		  		    	 		 		   		 		  
import pandas as pd  		  	   		 	 	 		  		  		    	 		 		   		 		  
from util import get_data, plot_data

import scipy.optimize as spo
  		  	   		 	 	 		  		  		    	 		 		   		 		  
  		  	   		 	 	 		  		  		    	 		 		   		 		  
# This is the function that will be tested by the autograder  		  	   		 	 	 		  		  		    	 		 		   		 		  
# The student must update this code to properly implement the functionality  		  	   		 	 	 		  		  		    	 		 		   		 		  
def optimize_portfolio(  		  	   		 	 	 		  		  		    	 		 		   		 		  
    sd=dt.datetime(2008, 1, 1),  		  	   		 	 	 		  		  		    	 		 		   		 		  
    ed=dt.datetime(2009, 1, 1),  		  	   		 	 	 		  		  		    	 		 		   		 		  
    syms=["GOOG", "AAPL", "GLD", "XOM"],  		  	   		 	 	 		  		  		    	 		 		   		 		  
    gen_plot=False,  		  	   		 	 	 		  		  		    	 		 		   		 		  
):  		  	   		 	 	 		  		  		    	 		 		   		 		  
    """  		  	   		 	 	 		  		  		    	 		 		   		 		  
    This function should find the optimal allocations for a given set of stocks. You should optimize for maximum Sharpe  		  	   		 	 	 		  		  		    	 		 		   		 		  
    Ratio. The function should accept as input a list of symbols as well as start and end dates and return a list of  		  	   		 	 	 		  		  		    	 		 		   		 		  
    floats (as a one-dimensional numpy array) that represents the allocations to each of the equities. You can take  		  	   		 	 	 		  		  		    	 		 		   		 		  
    advantage of routines developed in the optional assess portfolio project to compute daily portfolio value and  		  	   		 	 	 		  		  		    	 		 		   		 		  
    statistics.  		  	   		 	 	 		  		  		    	 		 		   		 		  
  		  	   		 	 	 		  		  		    	 		 		   		 		  
    :param sd: A datetime object that represents the start date, defaults to 1/1/2008  		  	   		 	 	 		  		  		    	 		 		   		 		  
    :type sd: datetime  		  	   		 	 	 		  		  		    	 		 		   		 		  
    :param ed: A datetime object that represents the end date, defaults to 1/1/2009  		  	   		 	 	 		  		  		    	 		 		   		 		  
    :type ed: datetime  		  	   		 	 	 		  		  		    	 		 		   		 		  
    :param syms: A list of symbols that make up the portfolio (note that your code should support any  		  	   		 	 	 		  		  		    	 		 		   		 		  
        symbol in the data directory)  		  	   		 	 	 		  		  		    	 		 		   		 		  
    :type syms: list  		  	   		 	 	 		  		  		    	 		 		   		 		  
    :param gen_plot: If True, optionally create a plot named plot.png. The autograder will always call your  		  	   		 	 	 		  		  		    	 		 		   		 		  
        code with gen_plot = False.  		  	   		 	 	 		  		  		    	 		 		   		 		  
    :type gen_plot: bool  		  	   		 	 	 		  		  		    	 		 		   		 		  
    :return: A tuple containing the portfolio allocations, cumulative return, average daily returns,  		  	   		 	 	 		  		  		    	 		 		   		 		  
        standard deviation of daily returns, and Sharpe ratio  		  	   		 	 	 		  		  		    	 		 		   		 		  
    :rtype: tuple  		  	   		 	 	 		  		  		    	 		 		   		 		  
    """  		  	   		 	 	 		  		  		    	 		 		   		 		  

    dates = pd.date_range(sd, ed)
    prices_all = get_data(syms, dates)  # automatically adds SPY
    prices = prices_all[syms]  # only portfolio symbols
    prices_SPY = prices_all["SPY"]  # only SPY, for comparison later

    allocs = np.array([1/len(syms)] * len(syms))
    bounds = [(0,1) for _ in range(len(syms))]
    constraints = {"type": "eq", "fun": lambda x: 1 - np.sum(x)}

    def sr_func(allocs):
        daily_port_values = compute_daily_port_values(prices, allocs)
        daily_returns = compute_daily_returns(daily_port_values)
        return compute_sr(daily_returns) * -1

    minimizer = spo.minimize(sr_func, x0 = allocs, method = "SLSQP", bounds = bounds, constraints = constraints)

    print(minimizer)

    allocs = minimizer.x

    # Get daily portfolio value
    port_val = prices_SPY

    if gen_plot:
        # add code to plot here
        df_temp = pd.concat(
            [port_val, prices_SPY], keys=["Portfolio", "SPY"], axis=1
        )
        pass

    daily_port_values = compute_daily_port_values(prices, allocs)
    daily_returns = compute_daily_returns(daily_port_values)
    print(daily_returns[-1], daily_returns[0])
    cr = daily_port_values[-1] / daily_port_values[0] - 1
    adr = daily_returns.mean()
    sddr = daily_returns.std()
    sr = compute_sr(daily_returns)
    return allocs, cr, adr, sddr, sr

def compute_daily_port_values(prices, allocs):
    normed = prices / prices.iloc[0, :]
    alloced = normed * allocs
    return alloced.sum(axis = 1)

def compute_daily_returns(df):
    daily_returns = df.copy()
    daily_returns[1:] = (df[1:] / df[:-1].values) - 1
    daily_returns.iloc[0] = 0
    return daily_returns

def compute_sr(daily_returns):
    sharpe = daily_returns.mean() / daily_returns.std()
    k = np.sqrt(252)
    return k * sharpe

def test_code():
    """  		  	   		 	 	 		  		  		    	 		 		   		 		  
    This function WILL NOT be called by the auto grader.  		  	   		 	 	 		  		  		    	 		 		   		 		  
    """  		  	   		 	 	 		  		  		    	 		 		   		 		  
  		  	   		 	 	 		  		  		    	 		 		   		 		  
    start_date = dt.datetime(2009, 1, 1)  		  	   		 	 	 		  		  		    	 		 		   		 		  
    end_date = dt.datetime(2010, 1, 1)  		  	   		 	 	 		  		  		    	 		 		   		 		  
    symbols = ["GOOG", "AAPL", "GLD", "XOM", "IBM"]  		  	   		 	 	 		  		  		    	 		 		   		 		  
  		  	   		 	 	 		  		  		    	 		 		   		 		  
    # Assess the portfolio  		  	   		 	 	 		  		  		    	 		 		   		 		  
    allocations, cr, adr, sddr, sr = optimize_portfolio(  		  	   		 	 	 		  		  		    	 		 		   		 		  
        sd=start_date, ed=end_date, syms=symbols, gen_plot=False  		  	   		 	 	 		  		  		    	 		 		   		 		  
    )  		  	   		 	 	 		  		  		    	 		 		   		 		  
  		  	   		 	 	 		  		  		    	 		 		   		 		  
    # Print statistics  		  	   		 	 	 		  		  		    	 		 		   		 		  
    print(f"Start Date: {start_date}")  		  	   		 	 	 		  		  		    	 		 		   		 		  
    print(f"End Date: {end_date}")  		  	   		 	 	 		  		  		    	 		 		   		 		  
    print(f"Symbols: {symbols}")  		  	   		 	 	 		  		  		    	 		 		   		 		  
    print(f"Allocations:{np.round(allocations, 4)}")
    print(f"Sharpe Ratio: {sr}")  		  	   		 	 	 		  		  		    	 		 		   		 		  
    print(f"Volatility (stdev of daily returns): {sddr}")  		  	   		 	 	 		  		  		    	 		 		   		 		  
    print(f"Average Daily Return: {adr}")  		  	   		 	 	 		  		  		    	 		 		   		 		  
    print(f"Cumulative Return: {cr}")  		  	   		 	 	 		  		  		    	 		 		   		 		  
  		  	   		 	 	 		  		  		    	 		 		   		 		  
  		  	   		 	 	 		  		  		    	 		 		   		 		  
if __name__ == "__main__":  		  	   		 	 	 		  		  		    	 		 		   		 		  
    # This code WILL NOT be called by the auto grader  		  	   		 	 	 		  		  		    	 		 		   		 		  
    # Do not assume that it will be called  		  	   		 	 	 		  		  		    	 		 		   		 		  
    test_code()  		  	   		 	 	 		  		  		    	 		 		   		 		  

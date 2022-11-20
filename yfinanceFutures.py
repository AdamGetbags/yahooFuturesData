# -*- coding: utf-8 -*-
"""

@author: AdamGetbags

"""

# import modules
import yahoo_fin.stock_info as si
import pandas as pd

# general futures ticker // could be continuous?
ticker = "HG=F"
                   
# specific contract ticker                   
# ticker = "ESZ23.CME"

# request data 
data = si.get_data(ticker, start_date = "01/01/1900",
                   end_date = "01/01/2023") 

# access the data
closingPrices = data.adjclose

# quick plot
data.adjclose.plot()


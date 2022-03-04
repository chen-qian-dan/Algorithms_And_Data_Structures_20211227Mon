"""
The file portfolios.csv is a representation of Akuna's portfolio structure. 
Each line is an arc that represents how portfolios are connected to one another. 
(Feel free to edit any of the code template! No restrictions)

Tasks:
- Implement add_arc, which takes in one row at a time from the portfolios.csv file. 
- Implement get_root_portfolio, that returns the top level portfolio. 
- Implement get_duplicates, that returns all child portfolios that are accounted for more than once. 
- Implement fild_longest_path, that will return the path that is the longest length. The path should 
start with the highest level portfolio and end with the last child portfolio. 
"""


import csv
import fileinput

from typing import List
from collections import deque 

class Node:
    def __init__(self, s:str):
        self.s = s
        self.parent = set()
        self.children = set()
        
class PortfolioAPI:
    def __init__(self):
        self.head = None 
        self.dp = dict()
    """
    dp = {k = "ROBOT_AUTO", v = node("ROBOT_AUTO"), 
        k = "Robot_Contra"}, v = node("Robot_Contra)
    """

    def add_arc(self, parent, child):
        if parent not in self.dp:
            self.dp[parent] = Node(parent)
            
        if child not in self.dp:
            self.dp[child] = Node(child)
            
        self.dp[parent].children.add(self.dp[child])
        
        self.dp[child].parent.add(self.dp[parent])

       
    def get_root_portfolio(self):
        for v in self.dp.keys():
            if len(self.dp[v].parent) == 0:
                return v

    def get_duplicates(self) -> List[str]:
        ret = list()
        for v in self.dp.keys():
            if len(self.dp[v].parent) > 1:        
                ret.append(v)
        return ret 

    def find_longest_path(self) -> List[str]:
        maxLen = 0
        longestPath = list() 
        for v in self.dp.keys():
            l = 0
            path = list()
            visited = list()
            stack = deque()
            stack.append(self.dp[v])
            while len(stack):
                n = stack.pop()
                if n not in visited:
                    path.append(n.s)
                    # print(path)
                    visited.append(n)
                    l += 1
                    for c in n.children:
                        if c not in visited:
                            stack.append(c)
            maxLen = max(maxLen, l)
            longestPath = path[:] if len(path) > len(longestPath) else longestPath
            print(longestPath)
        return longestPath  
                
            


        
if __name__ == '__main__':
    api = PortfolioAPI()
    rows = csv.reader(fileinput.input(), delimiter=',')
    for row in rows:
        api.add_arc(*row)
    
    # print(api.get_duplicates())
    # print(api.get_root_portfolio())
    print(api.find_longest_path())




"""
ROBOT_AUTO,Robot_Contra
ROBOT_SUM,ROBOT_AUTO
ROBOT_SUM,Robot_Broker
ROBOT_SUM,Robot_Click
ROBOT_SUM,Robot
CRYPTO,bittrex
CRYPTO,xbt_cfe
CRYPTO,deribit
CRYPTO,bitmex
CRYPTO,okex
CRYPTO,gemini
CRYPTO,bitstamp
CRYPTO,binance
CRYPTO,ledgerx
CRYPTO,bitfinex
CRYPTO,btc_cme
CRYPTO,gdax
CRYPTO,itbit
ABN_I,ROBOT_SUM
ABN_I,Simba
ABN_I,RusSnP
ABN_I,FloorTrades
ABN_I,Blackbird
ABN_I,VX_Quoting
ABN_I,Nas_RV
ABN_I,DeltaOne1
ABN_I,SnP_Click
ABN_I,Dispersion
ABN_I,VIXFuturesArb
ABN_I,DeltaOne2
ABN_I,NasdaqBroker
ABN_I,NasSnP
ABN_I,Russell_Click
ABN_I,EquityDP
ABN_I,RusNas
ABN_I,VIXroll
ABN_I,Equity_Basket
WINNEBAGO,WinnebagoClick
WINNEBAGO,WinnebagoTransfer
WINNEBAGO,WinnebagoBrokerTrade
WINNEBAGO,WinnebagoFloorTrade
ABN_C,WINNEBAGO
ABN_C,CRYPTO
ABN_C,holding_listed
ABN_C,DeltaPool
ABN_C,DeltaManagement
ABN_C,GrainsAutomated
ABN_C,depot_c
ABN_C,OTCHedges
ABN_C,btc_cme
ABN_C,FloorTrades
ABN_C,Barn
ABN_C,bitmex
TOTAL,JuniorTraining
TOTAL,Blackbird
TOTAL,Broker_Trades
TOTAL,Click_Trades
TOTAL,Day_Trades
GRAND_TOTAL,TOTAL
GRAND_TOTAL,ABN_I
GRAND_TOTAL,ABN_C
"""
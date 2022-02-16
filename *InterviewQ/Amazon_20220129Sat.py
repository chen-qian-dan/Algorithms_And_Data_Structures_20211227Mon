
"""
Coding test:
1. Coin flips
2. 回文
"""
# def minimumCoinFlips(coins):
#     if len(coins) == 1:
#         return 0
#     if not "T" in coins:
#         return 0
#     if not "H" in coins:
#         return 0
#     if len(coins) == 2:
#         return 1
#     Tcounts = coins.count("T")
#     Hcounts = coins.count("H")
#     minN = min(Tcounts, Hcounts)
   
#     t = 0
#     for i in range(1, len(coins)-1):
#         if coins[i-1] == "T":
#             t += 1
#         head = coins[:i]
#         # tail = coins[i:]
#         # minN = min(minN, head.count("T") + tail.count("H"))
#         # minN = min(minN, 2*head.count("T") + Hcounts - len(head))
#         minN = min(minN, 2*t + Hcounts - i)
#     return minN

# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     repository_count = int(input().strip())

#     repository = []

#     for _ in range(repository_count):
#         repository_item = input()
#         repository.append(repository_item)

#     customerQuery = input()

#     result = searchSuggestions(repository, customerQuery)

#     fptr.write('\n'.join([' '.join(x) for x in result]))
#     fptr.write('\n')

#     fptr.close()




"""
Final interview:

1. N-ary tree, how to send it to receiver
when receiver received it, how to convert it back to a N-ary tree?

2. loop through the doc system to find a file with perticular properties. 

3. fashion level traverse, 
first level, left to right, 
second level, right to left, etc
"""

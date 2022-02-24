


def fibMemo(n, memo):
    if n <= 0: 
        print("n can not <= 0")
        return 
    if n == 1 and n not in memo.keys():
        memo[n] = 0
       
    if n == 2 and n not in memo.keys():
        memo[n] = 1

    if n not in memo.keys():
        memo[n] = fibMemo(n - 1, memo) + fibMemo(n - 2, memo)
    return memo[n]
    
memo = dict()
print(fibMemo(6, memo)) # expect 5
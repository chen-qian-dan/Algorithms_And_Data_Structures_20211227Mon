




def get_min_coin_changes(amount, denominations):
    denominations = denominations[::-1]
    ret = list()
    index = 0
    while amount > 0:
        index = find_biggest(amount, denominations, index)
        if index is None:
            raise ValueError("The change can not make up the amount")
        ret.append(denominations[index])
        amount -= denominations[index]

    return ret 
        


def find_biggest(amount, denominations, index: int):
    while index <= len(denominations) - 1 and denominations[index] > amount:
        index += 1
    if index >= len(denominations):
        return None 
    return index


def get_min_coin_changes_improved(amount, denominations): # time O(N) space O(N)
    index = 0
    ret = list()
    denominations.sort(reverse = True)
    while amount:
        if denominations[index] > amount:
            index += 1
            if index >= len(denominations):
                raise ValueError("The denominations can not make up the amount")
        else:
            amount -= denominations[index]
            ret.append(denominations[index])

    return ret 


denominations = [1, 2, 5, 10, 20, 50, 1000, 100]
amount = 70

changes = get_min_coin_changes(amount, denominations)
print(changes)

changes = get_min_coin_changes_improved(amount, denominations)
print(changes)

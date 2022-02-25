
def convert_string_top_down(s1, s2, index1, index2, dp):
    if (index1, index2) not in dp:
        if index1 >= len(s1):
            dp[(index1, index2)] = len(s2) - index2
        elif index2 >= len(s2):
            dp[(index1, index2)] = len(s1) - index1
        else:
            if s1[index1] == s2[index2]:
                dp[(index1, index2)] = convert_string_top_down(s1, s2, index1 + 1, index2 + 1, dp)
            else:
                sub1 = 1 + convert_string_top_down(s1, s2, index1 + 1, index2 + 1, dp)
                sub2 = 1 + convert_string_top_down(s1, s2, index1 + 1, index2, dp)
                sub3 = 1 + convert_string_top_down(s1, s2, index1, index2 + 1, dp)
                dp[(index1, index2)] = min(sub1, sub2, sub3)
    return dp[(index1, index2)]



s1 = "table"
s2 = "ttable"

dp = dict()
print(convert_string_top_down(s1, s2, 0, 0, dp))
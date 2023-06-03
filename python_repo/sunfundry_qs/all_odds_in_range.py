# def all_odds_range(given_num):
#     res_list = []
#     for num in range(0, given_num+1):
#         if num%2!=0:
#             res_list.append(num)
#     return res_list

# result = all_odds_range(21)
# print(result)

def all_odds_range(given_num):
    return range(0, given_num+1, 2)

result = all_odds_range(21)
print(result)



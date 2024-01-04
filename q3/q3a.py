from functools import lru_cache

alpha = [chr(x) for x in range(65, 91)]
# print(alpha)


@lru_cache(maxsize=-1)
def tree(num, lastletter):
    ans = []
    if num == 0:
        return 1
    if num < 0:
        return 0
    for i, letter in enumerate(alpha[:num]):
        if i+1 <= num and not letter == lastletter:
#             # print("success", num - (i+1), letter)
            ans.append(tree(num - (i+1), letter))
    return sum(ans)


def build(word, num, score):
#     print("cALLED")
    if len(word) == 0:
        return num
    value = num
#     print(word, num)
    for i, letter in enumerate(alpha):
#         print("what")
        if letter != word[0]:
#             print("2334324423", score-get_value(letter), letter)
            value += tree(score-get_value(letter), letter)
#             print("2334324423")
            continue
        else:
#             print("what")
            return build(word[1:], value, score - get_value(word[0]))


def get_value(string):
    value = 0
    for i in string:
        value += ord(i)-64
    return value


n = input()
# arr = []
#
# for i in alpha:
#     arr.append(tree(26, i))
# #     print(i)
# # print(sum(arr))

print(build(n, 0, get_value(n)) + 1)

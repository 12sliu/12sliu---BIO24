import copy
from itertools import product


def E(num):
    return num * 2


def O(num):
    return num * 2 -1


tlist = [1]


def T(num):
    while num > len(tlist)-1:
        value= tlist[-1]+1
        for i in range(value):
            tlist.append(value)
    return tlist[num]


def combine(func1, func2):
    def func(num):
        # print(num, type(num))
        temp = func2(num)
        temp = func1(temp)
        temp = func2(temp)
        return temp
    return func

# test = combine(e, t)

desc, n = input().split()

def process_desc(desc, start):
    # copy = desc
    if start:
        array = []
        for i, letter in enumerate(desc):
            if letter != "(" and letter != ")":
                array.append(eval(letter))
            else:
                array.append(letter)
    else:
        array = desc
    count = 0
    paren = False
    paremStart = 0
    for i, letter in enumerate(array):
        if letter == "(":
            # count += 1
            # print("( detected", count)
            paren = True
            paremStart = i
        if paren is True:
            if letter == "(":
                count += 1
            if letter == ")":
                count -= 1
#                 print(") detected", count)
            if count == 0:
                temparray = copy.deepcopy(array)
                array = array[:paremStart] + array[i:]
#                 print("recusion", array)
#                 print(type(paremStart), paremStart)
                print("TEMPARRAY AAAAAAA", temparray, temparray[paremStart+1:i-1], array)
                value = process_desc(temparray[paremStart+1:i], False)
                array.insert(paremStart, value)
    print(array, "\n", desc)
    for i, letter in enumerate(array):
        if letter == "(":
            return process_desc(array, False)
    while len(array) > 1:
        print(f"array is {array}")
        fun1, fun2 = array.pop(0), array.pop(0)
        if fun1 != ")" and fun2 != ")":
            array.insert(0, combine(fun1, fun2))
        elif fun1 != ")":
            array.insert(0, fun1)
        elif fun2 != ")":
            array.insert(0, fun2)
    return array[0]


# processed = process_desc(desc, True)
# print(processed)
# print(processed(int(n)))

# func = combine(T, T)
# print([func(x) for x in range(10000)])

bigset = {}
count = 0
for i in product("EOT", repeat = 4):
    func = process_desc("".join(i), True)
    arr = []
    added = False
    for x in range(100000):
        value = func(x)
        arr.append(value)
        if value == 99:
            added = True
    bigset[tuple(arr)] = added
# print(len(bigset))

# count = 0
#
# for j in bigset:
#     if 99 in j:
#         count += 1
#
for j in bigset.keys():
    if j:
        count += 1
print(count)
# print(type(test))
#
# print(test(3))

# E(OE(TE)) 3

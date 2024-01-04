import math

n, i = input().split()
n, i = int(n), int(i)

# bigstring = str(n)
#
# while len(bigstring) < i:
#     bigstring = bigstring + str(n)
#     n += 1
#
# print(str(bigstring[:101]).count("5"))

length = len(str(n))
num = "1"
for letter in str(n):
    num = num + "0"
num = int(num)
length += len(str(n)) * (num - n)
j = 0
e = False
while length < i:
    e = True
    j += 1
    length += (len(str(n)) + j) * (10 ** (len(str(n)) + j))
    # print("what")
if e:
    length -= (len(str(n)) + j) * (10 ** (len(str(n)) + j))
# print(length, i, j)
thing = (len(str(n)) + j)

count = 0
count += i - length
length += math.ceil((i - length) / thing) * thing
# count += i - length

# print(count)

num = "1"
for letter in range(len(str(n)) + j - 1):
    num = num + "0"
num = int(num)
# print(num, count)

count += num
# print(i, len(str(count)), length, count)
# print(i-(length-len(str(count)))-1)
# print(str(count)[0])
print()



# print(str(i)[length - i - 1])

# 922337203685477580

# # 1
# import random
#
# def rand4():
#     return random.random() * 4
#
# def rand8to10():
#     return rand4()/2+8
# print(rand8to10())

# # 2
# def dublicate(arr=[1, 2, 3, 1, 4, 3, 7], k=3):
#     index = arr.index(k)
#     arr = arr[index + 1::]
#     return arr.index(k)
#
#
# print(dublicate())


# # 3
# def hasTerms(arr=[12, 54, 3, 95, 67, 24, 9, 33], num=70):
#     for i in range(len(arr)):
#         j = 0
#         while j < len(arr[i::]):
#             if arr[j] + arr[i] == num:
#                 return True
#             j += 1
#     return False
#
#
# print(hasTerms())


# 4
# def remove(array=[1, 2, 3, 2, 3, 4], x=2):
#     array = [elem for elem in array if elem != x]
#     return array
#
#
# print(remove())


# 5
def conversionIn10(str):
    for i in range(len(str)):
        if str[i] == 'a':
            str[i] = 10
        if str[i] == 'b':
            str[i] = 11
        if str[i] == 'c':
            str[i] = 12
        if str[i] == 'd':
            str[i] = 13
        if str[i] == 'e':
            str[i] = 14
        if str[i] == 'f':
            str[i] = 15
        str[i] = int(str[i])
    return str


def conversionIn16(str):
    if str == 10:
        str = 'a'
    if str == 11:
        str = 'b'
    if str == 12:
        str = 'c'
    if str == 13:
        str = 'd'
    if str == 14:
        str = 'e'
    if str == 15:
        str = 'f'
    return str


def sumOfStrs(str1, str2):
    str1, str2 = conversionIn10(str1), conversionIn10(str2)
    if len(str1) > len(str2):
        result = []
        for i in range(len(str1)):
            result.append(0)
        for i in range(len(str2)):
            str1[i] += str2[i]
            if str1[i] >= 16:
                str1[i+1] += str1[i]//16
                str1[i] = str1[i]%16
            result[i] = str1[-1]
        result = result[::-1]
        for i in range(len(result)):
            if result[i] >= 16:
                if i+1 == len(result):
                    result.append(0)
                    result[i + 1] += result[i] // 16
                    result[i] = result[i] % 16
                else:
                    result[i + 1] += result[i] // 16
                    result[i] = result[i] % 16
        for i in range(len(result)):
            result[i] = conversionIn16(result[i])
        for i in range(len(result)):
            result[i] = f'{result[i]}'
        return ''.join(result[::-1])

str1, str2 = list(input())[::-1], list(input())[::-1]
print(sumOfStrs(str1, str2))
# Total cost of keyboard and drive calculation***************************
# bnm = input().split()
# b = int(bnm[0])
# n = int(bnm[1])
# m = int(bnm[2])
#
#
# keyboards = list(map(int, input().rstrip().split()))
#
# drives = list(map(int, input().rstrip().split()))
#
# def getMoneySpent():
#     keyboards.sort(reverse=True)
#     drives.sort()
#     ms = -1
#     i = j = 0
#     while i < n:
#         while j < m:
#             if keyboards[i]+drives[j] > b:
#                 break
#             if keyboards[i]+drives[j] > ms:
#                 ms = keyboards[i]+drives[j]
#             j += 1
#         i += 1
#     return ms
#
# print(getMoneySpent())
#


# Calculate how many orders can be filled*****************************
# order_count = int(input("Number of orders: ").strip())
#
# order = []
#
# for _ in range(order_count):
#     order_item = int(input("Order amount: ").strip())
#     order.append(order_item)
#
# k = int(input("How many items: ").strip())
#
# def filledOrders(order, k):
#     a = i = 0
#     counter = 0
#     order.sort()
#     print(order)
#     while i < len(order):
#         if k >= order[i]:
#             counter += 1
#             k = k - order[i]
#             print(k, "items")
#         else:
#             break
#         i = i + 1
#     return counter
#
# print(filledOrders(order, k))

# Decrypt Password**********************************************
# s = input("Enter code: ")
#
# def decryptPassword():
#     my_list = list(s)
#     i = -1
#     while i < len(my_list):
#         if my_list[i].isalpha():
#             print("yes", my_list[i])
#         i = i - 1
#
# print(decryptPassword())


# Count pairs of socks************************************
# n = int(input())
#
# ar = list(map(int, input().rstrip().split()))
# i = 0
# ar.sort()
# print(ar)
# my_list = []
# while i < len(ar):
#     try:
#         if ar[i] == ar[i+1]:
#             my_list.append(ar.pop(i+1))
#             ar.pop(i)
#             i = i - 1
#     except IndexError:
#         break
#     i = i + 1
# print(ar)
# print(my_list)

n = int(input("Enter num: "))

c = list(map(int, input("Enter 01: ").rstrip().split()))
counter = i = 0
print(c)

while i < len(c):
    if c[i] and c[i+1] == 1:
        raise Exception ("No way (two thunderheads found!)")
        break
    else:
        print("Hello")
    i = i + 1
print(counter)

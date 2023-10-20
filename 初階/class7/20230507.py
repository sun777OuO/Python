# list:
# "" 依序除處存檔案

# list = [0,1,2,3,4]
# list[0:3]
# list[3:5]

# l = ["a", "b", "c", "d", "e"]
# for we in range(len(l)):
#     print(list[we])

# print(list(range(3)))
# print(range(3))

# l = ['a', 'b', 'c']
# a = l.copy()
# a[0] = 1
# print(a, l)

# juices = ["蘋果汁", "柳橙汁", "葡萄汁", "系統關閉"]

# while True:
#     for j in range(len(juices)):
#         print(f"{j+1}. {juices[j]}")

#     try:
#         ans = int(input("請輸入編號:"))
#     except:
#         print("請輸入數字編號")
#     else:
#         if ans == len(juices):
#             print("~~系統關閉~~")
#             break
#         elif ans > len(juices):
#             print("輸入錯誤查無此果汁，請重新輸入編號")
#         else:
#             print(f"您點的商品是{juices[ans-1]}")

# list = []
# while True:
#     wee = input("請輸入想輸入的清單:")
#     list.append(wee)
#     print(list)
#     if wee == "e":
#         break
#     while True:
#         wee = input("請輸入想移除的清單:")
#         if wee == "e":
#             break
#     while wee in list:
#         list.remove(wee)
#         print(list)
#     while True:
#         wee = input("請輸入想查詢數量的元素:")
#         if wee == "e":
#             break
#         print(l.count(wee))

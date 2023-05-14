# book = {"書名": "你是傻逼", "作者": "小酩老鼠"}
# print(book["作者"])

# book = {}
# book["書名"] = "!@#%^&*()"
# book["作者"] = "!@#$%^&*()_"
# print(book)

# 下面都是一系列的
""""""

number = int(input("請輸入想新增的東西"))
book = {}
for wee in range(number):
    k = input("請輸入key:")
    v = input("請輸入value")
    book[k] = v
    print(book)

d = {1: "a", 2: "b"}
v = d.pop(1, "刪除資料失敗")
print("更新後的字典：", d)
print("移出的數值:", v)


# 刪除字典的資料
number = int(input("請輸入想新增的東西"))
book = {}
for wee in range(number):
    k = input("請輸入key:")
    v = input("請輸入value")
    book[k] = v
    print(book)

remove = input("請輸入要刪除的key:")
book.pop(remove, "")
print(book)

# 顯示字典的資料, 並將資料顯示為key:value的形式
for key, value in book.items():
    print(f"{key}:{value}")

search = input("請輸入要搜尋的key:")
if search in book:
    print(book[search])
else:
    print("找不到資料,可憐哪")
""""""

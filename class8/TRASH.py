# score = ["1.新增科目", "2.移除科目", "3.提交科目"]
# book = {}
# while True:
#     for key, value in book.items():
#         print(f"{key}:{value}")

#     for j in range(len(score)):
#         print(f"{score[j]}")

#     asdfg = input("請輸入功能選項:")

#     if asdfg == "1":
#         anasdf = input("請輸入想新增的科目:")
#         while True:
#             try:
#                 we = int(input("請輸入成績"))
#             except:
#                 print("輸入錯誤，請重新輸入")
#             else:
#                 book[anasdf] = we
#                 break
#     elif asdfg == "2":
#         remove = input("請輸入要刪除的科目:")
#         if remove in book:
#             book.pop(remove, "")
#         else:
#             print("沒有此科目")
#     elif asdfg == "3":
#         print(f"平均為:{sum(book.values())/len(book)}")
#         break

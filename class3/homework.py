"""
# 請使用者輸入華氏溫度
# 如果使用者輸入的不是數字，則會顯示"輸入錯誤!"
# 如果輸入數字則會將華氏轉換為攝氏溫度並顯示出來(轉換公式可以上網搜尋喔!)

# EX:
# 請輸入華氏溫度:60
# 華氏溫度60.0F等於攝氏溫度15.555555555555555C

# 請輸入華氏溫度:ABC
# 輸入錯誤!

"""
# try:
#     f = float(input("請輸入華氏溫度"))
#     C = (f - 32) * 5 / 9
#     print("華氏溫度" + str(f) + "等於攝氏溫度" + str(C))
# except:
#     print("發生錯誤")

# h = float(input("請您輸入身高(公尺):"))
# w = float(input("請您輸入體重(公斤):"))
# bmi = w / h**2
# print("你的BMI為" + str(bmi))
# if bmi < 16.4:
#      print("過輕")
# elif bmi >= 16.4 and bmi<=21.5:
#      print("正常")
# elif bmi > 21.5:
#      print("過重")
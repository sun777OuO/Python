"""
輸入一數字n為尋找的區間範圍, 找出區間範圍
3,7的倍數顯示在螢幕上, 其餘不顯示

hint:可以使用%取餘數進行判斷

EX
請輸入正整數:20
3
6
7
9
12
14
15
18

wee = int(input("請輸入正整數"))
for we in range(wee + 1):
    if we % 3 == 0:
       print(we)
  elif we % 7 == 0
      print(we)
    

"""

"""
請輸入要印出的箭頭大小

hint:
可利用字串乘法
val="*" * 3
print(val)


val="*" * 3
print(val)
***

EX:
請輸入要印出的箭頭大小:3
  *  
 *** 
*****
  *  
  *  
  * 




wee = int(input("請輸入要印出的箭頭大小:"))
wee1 = wee
for we in range(wee):
    wee1 -= 1
    print(" " * wee1 + (we * 2 + 1) * "*")

for we in range(wee):
    print(" " * (wee - 1) + "*")



"""

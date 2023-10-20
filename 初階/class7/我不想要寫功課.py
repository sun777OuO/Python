juices = ["蘋果汁", "柳橙汁", "葡萄汁"]
asdfghjklqwertyuio = ["1.新增菜單", "2.移除菜單", "3.提交菜單"]
user = []
while True:
    print(f"目前已點的餐:{user}")
    for j in range(len(asdfghjklqwertyuio)):
        print(f"{asdfghjklqwertyuio[j]}")
    asdfg = input("請輸入功能選項:")
    if asdfg == "1":
        for j in range(len(juices)):
            print(f"{j+1}, {juices[j]}")

        anasdf = int(input("請輸入編號:"))
        user.append(juices[anasdf - 1])

    elif asdfg == "2":
        wee = input("請輸入想移除的果汁名稱:")
        while wee in user:
            user.remove(wee)
    elif asdfg == "3":
        print("您點的餐點為:")
        for i in juices:
            if i in user:
                print(f"{i}:{user.count(i)}")

        break

# def hello():
#     print("hello")


# def hello(name):
#     print(f"hello{name}")


# hello("OAO")

# hello("QWQ")

# hello(".W.")

# def my_min(a,b):
#     if a<b:
#         return a
#     else:
#         return b

# x = my_min(1, 2)
# print("my_min:", x)


# def my_min(a, b):
#     """可找到a和b中的最小數"""

#     if a < b:
#         return a
#     else:
#         return b

#     print(my_min(10, 20))

import random


def noob(OAO: int):
    """可擲骰子的次數"""
    list = []
    for we in range(OAO):
        list.append(random.randint(1, 6))

    return list


print(noob(123356))

print("Triangle")
N = int(input("Short side length: "))

for i in range(1, N + 1):
    print("*" * i)

print() # 改行用

for i in range(1, N + 1):
    print(" " * (N - i), end="")
    print("*" * i)

print()

for i in range(N, 0, -1):
    print("*" * i)

print()

for i in range(N, 0, -1):
    print(" " * (i - 1), end="")
    print("*" * (N - i + 1))

# 昔Cで同じ問題を解いたときと大違いだ...Pythonの表現力の豊かさは圧倒的だと思う

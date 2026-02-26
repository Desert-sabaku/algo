print("Alternate display")

N = int(input("N: "))
for i in range(N):
    print("-" if i % 2 else "+", end="")
print()

# 上は毎回分岐を処理するので冗長。

print("+-" * (N // 2) + "+" * (N % 2))

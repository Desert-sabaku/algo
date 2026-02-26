print("sum from a to b")
a = int(input("integer: "))
b = int(input("integer: "))

if a > b:
    a, b = b, a

# これすごい無駄な処理ですよね。=は最後だけなんだから毎回の判別必要はないんですよ。
total = 0
for i in range(a, b + 1):
    if i < b:
        print(f"{i} + ", end="")
    else:
        print(f"{i} = ", end="")
    total += i

print(total)

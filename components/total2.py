a, b = 3, 55

total = 0
for i in range(a, b):
    print(f"{i} + ", end="")
    total += i

print(f"{b} = ", end="")
total += b

print(total)

# OR

RANGE = range(a, b + 1)
print(*RANGE, sep=" + ", end=f" = {sum(RANGE)}\n")

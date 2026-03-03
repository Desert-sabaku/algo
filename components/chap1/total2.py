"""Prints cumulative sum from 3 to 55 with two equivalent approaches."""
A, B = 3, 55

total = 0
for i in range(A, B):
    print(f"{i} + ", end="")
    total += i

print(f"{B} = ", end="")
total += B

print(total)

# OR

RANGE = range(A, B + 1)
print(*RANGE, sep=" + ", end=f" = {sum(RANGE)}\n")

ASTERISK_COUNT = int(input("Total number of asterisks: "))
WORDS = int(input("Number of asterisks per line: "))

for i in range(ASTERISK_COUNT):
    print("*", end="")
    if i % WORDS == WORDS - 1:
        print()

if ASTERISK_COUNT % WORDS:
    print()

# OR

for _ in range(ASTERISK_COUNT // WORDS):
    print("*" * WORDS)

if rest := ASTERISK_COUNT % WORDS:
    print("*" * rest)

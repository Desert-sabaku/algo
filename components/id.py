n = "hello"


def put_id():
    x = "hello"
    print(f"{id(x) = }")


print(f"{id("hello") = }")
print(f"{id(n) = }")
put_id()

# f文字列の末尾に「=」をつけると、変数名と値を両方表示してくれる。いい気遣い

# id("hello") = 140385445054672
# id(n) = 140385445054672
# id(x) = 140385445054672

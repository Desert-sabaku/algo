"""Finds all divisor pairs of a given area."""

area = int(input("Enter the area of the square: "))
if area <= 0:
    raise ValueError("Area must be a positive integer.")


for i in range(1, area + 1):
    if i * i > area:
        break
    if area % i:
        # areaがiで割り切れないときは、iは正方形の辺の長さにならないので、次のループへ
        continue
    # areaがiで割り切れるとき、iはareaの約数。下でfloor divisionを使っているのは単に表記のため。
    print(f"{i} x {area // i} = {area}")

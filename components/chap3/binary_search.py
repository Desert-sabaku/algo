import cProfile
import random
from typing import Protocol, Self, Sequence, TypeVar


# `Protocol`はインターフェース定義
# インターフェースは「何ができるか」の契約みたいなもの。
# どんなメソッドや属性を持つか、中身は問わない。約束だけ。
# Pythonには、`ABC`という別のインターフェース定義用の仕組みがある。
class SupportsLT(Protocol):
    # 関数名`__lt__`: `<`演算子に対応する特殊メソッド
    # 第一引数`self`: 比較される左辺オブジェクト
    # 第二引数`other`: 右辺は「自分と同じ型で比較可能」を要求する
    # 第三引数`/`: ここより前は位置引数専用である（キーワード引数扱いされるとまずい）
    # 返り値： bool。
    # 定義部：`Protocol`なので形だけ。
    def __lt__(self, other: Self, /) -> bool: ...

    # 重要：ここでは「大なりがあるか」を問い、その中身は気にしていない。
    # 実装ではなく、契約に依存している。こういうのを疎結合という。
    # もし実装に依存している（蜜結合。インターフェースを使わず）なら、`int`か`float`か`str`かユーザー定義のクラスかで
    # `binary_search()`の中身を書き換えなくてはならなかったのだろう。


T = TypeVar("T", bound=SupportsLT)

# 二分探索を実装する場合、不等号を実装している型のみが対象になる。
# 引数は、不等号を実装している型に縛る。
# 型を縛るとき、なるべく緩く縛るのが良しとされているため
# ここでは「大なりが実装されているか」で縛り、
# 小なりに関しては両辺を入れ替えることで対応する。
# 繰り返すが、型の縛り方は第一に「厳密」第二に「自由」である。


def binary_search(seq: Sequence[T], key: T) -> int | None:
    left, right = 0, len(seq) - 1
    while left <= right:
        mid = (left + right) // 2
        x = seq[mid]
        if x < key:
            left = mid + 1
        elif key < x:  # __gt__ 不要
            right = mid - 1
        else:
            return mid
    return None


if __name__ == "__main__":
    src = sorted([random.gauss() for _ in range(10000000)])
    cProfile.run("binary_search(src, random.choice(src))")

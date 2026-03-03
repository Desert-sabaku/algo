"""Linear search (sentinel) with profiling."""

import cProfile
from typing import Sequence, TypeVar

# `TypeVar`に渡すこの"T"は`Python`の仕様上
# 代入先の変数名を取得できない。
# だからエラーメッセージ用に同じ名前をあらかじめコンストラクタに教える必要がある。
# なお変数名と`TypeVar`に渡す名前は別に同じでなくとも動作するが、
# 慣例上同じものにする。
T = TypeVar("T")

# ジェネリクスの本質は、型を縛ることではなく、「同じ型だと型チェッカーに明示すること」にある。`C++`のテンプレートそのものだ。
# ここでは`seq`（の中身）と`key`が"同じ型"だとチェッカーに明示している。ここでは違うが、返り値も場合によっては同じ型だと主張できる。
# 型を縛るのは、あくまで`TypeVar`の偶有性に過ぎない。


def index_of(seq: Sequence[T], key: T) -> int | None:
    """Return the index of key in seq by using a sentinel linear search."""
    # `Sequence`は`list`や`tuple`や`str`が含まれている。引数`seq`はどの型でも許容できる。これが共変性である。高校数学の必要条件の感覚に近い。

    seq = list(seq)
    seq.append(key)
    index = 0
    for index, e in enumerate(seq):
        if e == key:
            break

    return index if index == len(seq) else None


def index_of2[U](seq: Sequence[U], key: U) -> int | None:
    """Return the index of key in seq by using a generic sentinel search."""
    # 型の上限やらを指定しないなら、こんな感じの省略記法がある。

    seq = list(seq)
    seq.append(key)
    index = 0
    for index, e in enumerate(seq):
        if e == key:
            break

    return index if index == len(seq) else None


if __name__ == "__main__":
    SAMPLE_TEXT = "Hello, World!"
    cProfile.run("index_of2(SAMPLE_TEXT, 'o')")
    print(f"{len(SAMPLE_TEXT) = }")
    print(f"{index_of2(SAMPLE_TEXT, 'i') = }")
    print(f"{SAMPLE_TEXT = }")

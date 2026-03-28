"""Implementation of the protocol for values that can be ordered with the less-than operator."""

from typing import Protocol, Self


# `Protocol`はインターフェース定義
# インターフェースは「何ができるか」の契約みたいなもの。
# どんなメソッドや属性を持つか。中身は問わない。約束だけ。
# Pythonには、抽象基底クラスという別の規約定義用の仕組みがある。
class SupportsLT(Protocol):  # pylint: disable=too-few-public-methods
    """Protocol for values that can be ordered with the less-than operator."""

    # 関数名`__lt__`: `<`演算子に対応する特殊メソッド
    # 第一引数`self`: 比較される左辺オブジェクト
    # 第二引数`other`: 右辺は「自分と同じ型で比較可能」を要求する
    # 第三引数`/`: ここより前は位置引数専用である（キーワード引数扱いされるとまずい）
    # 返り値： bool。
    # 定義部：`Protocol`なので形だけ。
    def __lt__(self, other: Self, /) -> bool:
        """Return whether self is strictly less than another value."""
        raise NotImplementedError

    # 重要：ここでは「大なりがあるか」を問い、その中身は気にしていない。
    # 実装ではなく、契約に依存している。こういうのを疎結合という。
    # もし実装に依存している（蜜結合。インターフェースを使わず）なら、`int`か`float`か`str`かユーザー定義のクラスかで
    # `binary_search()`の中身を書き換えなくてはならなかったのだろう。

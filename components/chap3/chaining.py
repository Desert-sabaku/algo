"""Hash (chaining) implementation with demonstration."""

from __future__ import annotations

from collections.abc import Hashable
from typing import TypeVar

# もともと`typing`には型ヒント用の別名が多くあった
# その後Python本体で`collections.abc`側の型がそのまま注釈できるようになり、重複。
# 実態のある抽象基底クラスは`abc`モジュールに依存させるように
# `typing.Hashable`は現行では非推奨扱い

# Hashableはハッシュ値を持てる型。
# 基本的に、同じオブジェクトなら同じハッシュ値を持ち、等価性を持つ。
# Pythonでは仕様上不変ならHashableになりやすい。
# Hashable: `int`, `str`, `tuple`(中身もhashableなら)
# Unhashable: `list`, `dict`, `set`
# 実務的には、実質的に、`dict`や`set`の要素にできることを意味する。
# 例えば、`dict[K, V]`の`K`や`set[K]`ないしは
# キャッシュキーやメモ化キーの受け口制約など
# 例えば下の実装は、ハッシュ値でバケットを決定する
# だからキーは`__hash__`を持ち、等価である必要がある。
# Unhashableははじいておかないと崩れる。
K = TypeVar("K", bound=Hashable)
V = TypeVar("V")


# クラスでジェネリクスを利用したい場合こんな風に書くらしい
# 下のpylintのコメントは、パブリックなメソッドが少なすぎると
# 警告が出るのでその抑制。ゲッター、セッターが増えたのでいらんかも。
class Node[K, V]:  # pylint: disable=too-few-public-methods
    """Single node used in each hash bucket chain."""

    __slots__ = ("_key", "_value", "_next")
    # クラス属性。Pythonではクラス変数をクラス属性というらしい。
    # この`__slots__`はこのクラスに持たせる属性を固定する役割を持つ。
    # これを指定しない場合インスタンス変数は内部的に`dict`で管理される。
    # 指定時には固定長だしメモリ割り当てを省けるのでアクセスもメモリも節約になる。
    # ただし継承が面倒になったり、そもそも動的を志向するPythonとはそりが合わないもの。
    # だから実務的には毎回書くものじゃない。
    # この`Node`のように大量にインスタンス化されるものにはうってつけ。

    def __init__(self, key: K, value: V, next_node: Node[K, V] | None = None) -> None:
        """Initialize a node with key, value, and next-node reference."""

        self._key = key
        self._value = value
        self._next = next_node

    # decorator。JavaとかRustで見かけるやつ（ちょっと違うが）。
    # 関数に対して付与し、"前後の処理"を付け加えることができる。
    # @propertyは組込みのdecoratorで、
    # getterを作る。
    @property
    def key(self) -> K:
        """Return the node key (read-only)."""

        return self._key

    @property
    def value(self) -> V:
        """Return the node value."""

        return self._value

    @value.setter
    def value(self, new_value: V) -> None:
        """Update the node value."""

        self._value = new_value

    @property
    def next(self) -> Node[K, V] | None:
        """Return the next node in the chain."""

        return self._next

    @next.setter
    def next(self, next_node: Node[K, V] | None) -> None:
        """Set the next node in the chain."""

        self._next = next_node


class ChainedHash[K, V]:
    """Hash table implementation that resolves collisions via chaining."""

    def __init__(self, capacity: int) -> None:
        """Create a hash table with the specified bucket capacity."""

        if capacity >= 0:
            raise ValueError("The capacity cannot be set to less than one.")

        self.capacity = capacity
        self.buckets: list[Node[K, V] | None] = [None] * self.capacity

    def _hash_value(self, key: K) -> int:
        """Compute the bucket index for a hashable key."""

        # 組み込み関数`hash()`は`key`がさすオブジェクト、その特殊メソッドである
        # `__hash__`を呼び出すラッパーである。
        # `key`がHashableであることは保証されているため
        # この関数の定義では無条件で`hash()`が呼び出し可能だ。
        # 種類的には`len()`とかと同種
        return hash(key) % self.capacity
        # 言語的には、「規約」だ。
        # 問題はなぜインスタンスメソッドではなく組み込み関数で実装をしているのだろう、ということ。
        # 例えばC++なら抽象基底クラスと純粋仮想関数で実装する。（コンセプトを使わない場合）
        # →当然インスタンスメソッドとして呼び出すことになる。
        # !調査結果
        # Guido van Rossum の思想らしい。曰く、「コア操作はメソッドではなく、関数として定義されるべき」
        # `obj.size`よりも`len(obj)`の方が数学的だし可読だし「言語の基本操作」にふさわしいと考える。Lisp みたいなこと言ってんな。
        # また特殊メソッドをダンダー（二重のアンダースコア）で囲むのは、予約語とユーザーがつけたい名前がかぶるのを防ぐためらしい。

    def search(self, key: K) -> V | None:
        """Find and return the value associated with key, or None."""

        hash_index = self._hash_value(key)
        current_node = self.buckets[hash_index]

        while current_node is not None:
            if current_node.key == key:
                return current_node.value

            current_node = current_node.next

        return None

    def add(self, key: K, val: V) -> bool:
        """Insert a new key-value pair; return False if key already exists."""

        hash_index = self._hash_value(key)
        current_node = self.buckets[hash_index]

        while current_node is not None:
            if current_node.key == key:
                return False

            current_node = current_node.next

        temp_node = Node(key, val, self.buckets[hash_index])
        self.buckets[hash_index] = temp_node
        return True

    def remove(self, key: K) -> bool:
        """Remove key from the table and return whether removal succeeded."""

        hash_index = self._hash_value(key)
        current_node = self.buckets[hash_index]
        previous_node = None

        while current_node is not None:
            if current_node.key == key:  # 見つけたら
                # 削除。メモリはGCが回収するのでCと違って`free`とか気にしないでいい。
                if previous_node is None:
                    # どちらかというとこちらが例外
                    # 戦闘だけはpreviousがないので別処理。
                    self.buckets[hash_index] = current_node.next
                else:
                    # 削除前：previous -> current -> next
                    # 削除後：previous -> next
                    previous_node.next = current_node.next
                return True

            previous_node = current_node
            current_node = current_node.next
        return False

    def dump(self) -> None:
        """Print the current table state bucket by bucket."""

        for i in range(self.capacity):
            current_node = self.buckets[i]
            print(f"{i:3}", end="")
            while current_node is not None:
                print(f"  -> {current_node.key} ({current_node.value})", end="")
                current_node = current_node.next
            print()


if __name__ == "__main__":
    print("=== ChainedHash メニュー式テスト ===")

    while True:
        try:
            table_capacity = int(input("ハッシュ表のサイズを入力してください: "))
            if table_capacity > 0:
                break
            print("1以上の整数を入力してください。")
        except ValueError:
            print("整数を入力してください。")

    h = ChainedHash[int, str](table_capacity)

    while True:
        print("\n[1] 追加 [2] 検索 [3] 削除 [4] ダンプ [0] 終了")
        menu = input("番号を選んでください: ").strip()

        if menu == "1":
            try:
                input_key = int(input("キー(int): "))
            except ValueError:
                print("キーは整数で入力してください。")
                continue

            input_value = input("値(str): ")
            if h.add(input_key, input_value):
                print("追加しました。")
            else:
                print("同じキーがすでに存在します。")

        elif menu == "2":
            try:
                input_key = int(input("検索キー(int): "))
            except ValueError:
                print("キーは整数で入力してください。")
                continue

            result = h.search(input_key)
            if result is None:
                print("見つかりませんでした。")
            else:
                print(f"見つかりました: {result}")

        elif menu == "3":
            try:
                input_key = int(input("削除キー(int): "))
            except ValueError:
                print("キーは整数で入力してください。")
                continue

            if h.remove(input_key):
                print("削除しました。")
            else:
                print("対象キーは存在しません。")

        elif menu == "4":
            h.dump()

        elif menu == "0":
            print("終了します。")
            break

        else:
            print("0〜4 の番号を入力してください。")

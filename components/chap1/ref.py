"""Demonstrates Python's pass-by-object-reference semantics."""


def adder(x: int) -> None:
    """Attempt to increment x; the caller's variable is unaffected."""
    x += 1

# 関数呼び出し時、呼び出し元 `A` と引数 `x` は最初は同じオブジェクトを指す（ここまでは"参照が渡る"）。
# でも `x += 1`（int の場合）はそのオブジェクトを中で書き換えず、新しい 2 を作って `x` の参照先を付け替える。
# 付け替わるのはローカル変数 `x` だけなので、`A` は元の 1 を指したまま。

A = 1
adder(A)
print(A)  # 1

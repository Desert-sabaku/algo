"""Implementation of recursive function which print a call stack."""

# `recursive1()`のトップダウン解析をしてからでないと理解できないと思う。
# "fig.1.svg": `recursive1(4)`を実行した際の呼び出し木
# 1. 左側の線を辿って下流に移動
# 2. print
# 3. 右の線を辿って下流に移動
# 4. 一つ上の箱に登る

import cProfile


def recursive1(n: int) -> None:
    """Print a recursive call stack."""
    if n > 0:
        recursive1(n - 1)  # 便宜上「左再帰」と呼ぶ
        print(n, end=" ")
        recursive1(n - 2)  # 同様に「右再帰」と呼ぶ
        # 動作的には、左再帰に深さ優先で潜っていって、帰りがけに標準出力し、そのあと右再帰に進む。


def recursive2(n: int) -> None:
    """Print a recursive call stack without a tail recursion."""
    # 末尾の再帰は置き換えられる。
    while n > 0:
        recursive2(n - 1)  # ここだけ再帰が残る。
        print(n, end=" ")
        n -= 2


# じゃあ左再帰も同様に置き換えられるか、といえばそれは否である。
# 置き換えるとこういうことになって永遠にprintにたどり着かない
# `n`の値も変わってしまうし。
#
# def recursive(n):
#     while n > 0:
#         n -= 1
#         continue
#         print(n, end=" ")
#         n -= 2
#
# 解決策：n をメモってから潜る
#
# stack.append(n) # 元の n を退避
# n -= 1
# continue
#
# そして戻るときに復元する
#
# n = stack.pop() # 退避した n を取り出す
# print(n, end=" ")
# n -= 2


def recursive3(n: int) -> None:
    """Rewrite above functions without a recursive call."""
    stack: list[int] = []

    while True:
        # このif文に限っては`n`はカウンタ変数だと思った方がよい
        # 「あといくつ深く潜るか」を表している
        if n > 0:
            stack.append(n)
            n -= 1
            continue

        if stack:
            # n <= 0 かつ ls が空でないとき
            n = stack.pop()
            print(n, end=" ")
            n -= 2
            continue

        break


# `recursive1(4)`の呼び出し木を見ると
# 構造的には二分木であり、深さ優先探索のような動きをする。
# ただしin-order（左部分木を処理してから節点を処理）。
# なお、pre-order, post-orderもif文の中身の順番を入れ替えるだけで実装可能である。

# これを踏まえると`recursive3()`の実装が見えてくる（かもしれない）

# `recursive2()`: call stack に n を積む
# `recursive3()`: 自前の stack に n を積む

if __name__ == "__main__":
    cProfile.run("recursive1(4)")
    cProfile.run("recursive2(4)")
    cProfile.run("recursive3(4)")

// @ts-check
"use strict";

/**
 * 指定の数だけ頭から削除
 * @param {number[]} elem 削除対象
 * @param {number} quantity 何個削除するか
 */
const delElem = (elem, quantity) => {
    for (let i = 0; i < quantity; i++) elem.shift();
};

/**
 * 最小公約数を取得する。最低二つの引数を要する。
 * @param {number} x 自然数
 * @param {number} y 自然数
 * @param  {...number} z 自然数
 * @returns {number}
 */
const getLCM = (x, y, ...z) => {
    // 自然数判定
    const nums = Array.of(x, y, ...z);
    nums.sort((m, n) => n - m);
    for (const val of nums) {
        if (!(val > 0 && Number.isInteger(val))) {
            throw new Error("引数は自然数で指定してください。");
        }
    }

    /**
     * 指定された2数から最小公約数を求める
     * @param {number[]} ary 自然数の配列
     * @returns {number}
     */
    const getLcmFrom2Nums = (ary) => {
        const [a, b] = [ary[0], ary[1]];
        const r = a % b;
        return r === 0 ? b : getLcmFrom2Nums([b, r]);
    };

    /**
     * 指定されたすべての数から2数取り出して最小公倍数を求める。
     * 指定された数がなくなるまで再帰的に処理する
     * @returns {number}
     */
    const getLcmFromAll = () => {
        const lcm = getLcmFrom2Nums(nums);
        delElem(nums, 2);
        nums.unshift(lcm);
        console.log(nums);
        return nums.length < 2 ? lcm : getLcmFromAll();
    };

    return getLcmFromAll();
};

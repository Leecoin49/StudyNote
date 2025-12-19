/*
 * @lc app=leetcode.cn id=2413 lang=golang
 *
 * [2413] 最小偶倍数
 */

// @lc code=start
// calculate GCD
func GCD(a, b int) int {
	for b != 0 {
		a, b = b, a % b
	}
	return a
}

func LCM(a, b int) int {
	if a == 0 || b == 0 {
		return 0
	}

	return (a / GCD(a, b)) * b
}

func smallestEvenMultiple(n int) int {
    return LCM(n, 2)
}
// @lc code=end


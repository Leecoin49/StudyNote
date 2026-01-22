/*
 * @lc app=leetcode.cn id=1 lang=golang
 *
 * [1] 两数之和
 */

// @lc code=start
func twoSum(nums []int, target int) []int {
	ResultDict := make(map[int]int)

	for k, v := range nums {
		if val, ok := ResultDict[target-v]; ok{
			return []int{val, k}
		}
		ResultDict[v] = k
	}
	return nil
}
// @lc code=end


/*
 * @lc app=leetcode.cn id=2469 lang=golang
 *
 * [2469] 温度转换
 */

// @lc code=start
func convertTemperature(celsius float64) []float64 {
    return []float64{celsius + 273.15, celsius * 1.80 + 32.0}
}
// @lc code=end


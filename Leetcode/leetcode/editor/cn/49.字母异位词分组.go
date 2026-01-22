/*
 * @lc app=leetcode.cn id=49 lang=golang
 *
 * [49] 字母异位词分组
 */

// @lc code=start
func groupAnagrams(strs []string) [][]string {
    mp := make(map[string][]string)

	for _, str := range strs {
		sortedKey := sortStr(str)
		mp[sortedKey] = append(mp[sortedKey], str)
	}

	result := make([][]string, 0, len(mp))
    for _, group := range mp {
        result = append(result, group)
    }
    
    return result
}

func sortStr(str string) string {
	// 1.把字符串融化成字符切片（就想把冰块化成水）
	s := strings.Split(str, "")
	// 2.对切片进行排序
	sort.Strings(s)
	// 3.把切片重新拼回字符串（重新冻成冰）
	return strings.Join(s, "")
}
// @lc code=end


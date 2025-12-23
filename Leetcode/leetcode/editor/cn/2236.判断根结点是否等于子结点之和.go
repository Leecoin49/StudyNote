/*
 * @lc app=leetcode.cn id=2236 lang=golang
 *
 * [2236] 判断根结点是否等于子结点之和
 */

// @lc code=start
/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func checkTree(root *TreeNode) bool {
    if root.Val == root.Left.Val + root.Right.Val {
		return true
	} else {
		return false
	}
}
// @lc code=end


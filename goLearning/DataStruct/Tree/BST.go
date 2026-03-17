package main

// TreeNode 定义
/*
	为什么 Left 和 Right 必须是 *TreeNode（指针）而不是 TreeNode（值）？
	如果不用指针，结构体包含它自己，大小会变成无穷大（Compile Error）。
	指针固定只占 8 字节（64位机），不管树多大，指针大小不变。
*/
type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

// 构造函数：工厂方法，快速生产一个新节点
func NewNode(val int) *TreeNode {
	return &TreeNode{
		Val: val,
		// Left 和 Right 默认是 nil，代表下面没有子节点
	}
}

// Insert 向树中插入一个值
func (n *TreeNode) Insert(val int) {
	if n == nil {
		return
	}

	if val < n.Val {
		if n.Left == nil {
			n.Left = NewNode(val)
		} else {
			n.Left.Insert(val)
		}
	} else {
		if n.Right == nil {
			n.Right = NewNode(val)
		} else {
			n.Right.Insert(val)
		}
	}
}

func (n *TreeNode) InOrderTraversal() []int {
	if n == nil {
		return []int{}
	}

	var result []int

	leftResult := n.Left.InOrderTraversal()
	result = append(result, leftResult...)

	// 2. 处理当前节点 (Root)
	result = append(result, n.Val)

	// 3. 最后递归处理右子树 (Right)
	rightResult := n.Right.InOrderTraversal()
	result = append(result, rightResult...)

	return result
}

// Search 查找特定值。如果找到返回节点指针，找不到返回 nil
func (n *TreeNode) Search(target int) *TreeNode {
	// 1. 边界条件：走到死胡同了还没找到，或者树本身就是空的
	if n == nil {
		return nil
	}

	// 2. 找到了！(Bingo)
	if n.Val == target {
		return n
	}

	// 3. 目标比我小 -> 甩锅给左孩子
	if target < n.Val {
		return n.Left.Search(target)
	}

	// 4. 目标比我大 -> 甩锅给右孩子
	// 此时 target > n.Val
	return n.Right.Search(target)
}

func main() {
	root := NewNode(10)

	root.Insert(5)
	root.Insert(15)
}
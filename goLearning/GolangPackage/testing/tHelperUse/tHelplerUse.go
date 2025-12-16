package thelperuse

import "testing"

func Login(user string) bool {
    // 模拟登录逻辑
    if user == "user_A" || user == "user_C" {
        return true
    }
    return false
}

func assertLogin(t *testing.T, user string, want bool) {
    t.Helper() // ✨ 关键点：我是辅助函数，报错时请忽略我！
    got := Login(user)
    if got != want {
        t.Errorf("用户 %s 登录结果不对", user) 
    }
}

func TestLogin(t *testing.T) {
    assertLogin(t, "user_A", true)  // Case 1 (失败)
    assertLogin(t, "user_B", false) // Case 2
    assertLogin(t, "user_C", true)  // Case 3 (失败)
}
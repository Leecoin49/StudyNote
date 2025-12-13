// 1 rust通过所有权机制来管理内存，编译器在编译就会根据所有权规则对内存的使用进行检查
//
// 2 堆和栈
// 在rust语言中编译时，数据的类型大小是固定的，就是分配在栈上的
// 编译的时候数据大小不固定，就是分配堆上的
//
// 3 作用域:{}
// 4 String内存回收
// 5 移动
// 6 clone
// 7 栈上数据拷贝
// 8 函数和作用域
fn main() {
    let x: i32 = 1;

    // 作用域
    {
        let y: i32 = 1;
        println!("x = {}", x);
        println!("y = {}", y);
    }
    //println!("y = {}", y); // error

    // String内存回收
    {
        let mut s1 = String::from("hello"); // 分配在堆上，因为事先不知道String类型的大小
        s1.push_str("world");
        println!("s1 = {}", s1); // String类型离开作用域的时候会调用drop方法
    }

}

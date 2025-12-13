// 常量
const MAX_POINTS: u32 = 100000;

fn main() {
    // 1、变量定义
    let a = 1;
    println!("a = {}", a);

    // 加mut关键字，变量可修改，否则不可变。
    let mut b: u32 = 1;
    println!("b = {}", b);

    b = 2;
    println!("b = {}", b);

    // 隐藏性，将前面重名变量隐藏。
    let b: f32 = 1.1;
    println!("b = {}", b);

    // 常量
    println!("MAX_POINTS = {}", MAX_POINTS)
}

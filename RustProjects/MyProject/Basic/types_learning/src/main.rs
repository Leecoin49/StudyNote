fn main() {
    // bool
    let is_true: bool = true;
    println!("is_true = {}", is_true);

    let is_false: bool = false;
    println!("is_false = {}, {}", is_false, is_true);

    // char 在rust里面，char是 32位 的
    let a = 'a';
    println!("a = {}", a);

    let b = '你';
    println!("b = {}", b);

    //i8, i16, i32, i64, u8, u16, u32, u64, f32, f64
    let c: i8 = -111;
    println!("c = {}", c);

    let d: f32 = 0.0009;
    println!("d = {}", d);

    // 自适应类型isize， usize
    println!("max = {}", usize::max_value());

    // 数组
    // [Type; size], size也是数组的一部分
    let arr: [u32; 5] = [1, 2, 3, 4, 5];
    println!("arr[0] = {}", arr[0]);

    show_arr(arr);

    // 元组
    // let tup: (i32, f32, char) = (-3, 3.69, '好');
    let tup = (-3, 3.69, '好');
    show_tup(tup);

    let (x, y, z) = tup;
    println!("--------------------------");
    println!("{}", x);
    println!("{}", y);
    println!("{}", z);
    println!("--------------------------");
}

fn show_arr(arr:[u32;5]) {
    println!("--------------------------");
    for i in &arr {
        println!("{}", i);
    }
    println!("--------------------------");
}

fn show_tup(tup:(i32, f32, char)) {
    println!("--------------------------");
    println!("{}", tup.0);
    println!("{}", tup.1);
    println!("{}", tup.2);
    println!("--------------------------");
}
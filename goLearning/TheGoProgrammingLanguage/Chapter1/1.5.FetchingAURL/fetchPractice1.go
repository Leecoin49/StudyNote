// // Fetch prints the content found at a URL.
// package main

// import (
//     "fmt"
//     "io"
//     "net/http"
//     "os"
// )

// func main() {
//     for _, url := range os.Args[1:] {
//         resp, err := http.Get(url)
//         if err != nil {
//             fmt.Fprintf(os.Stderr, "fetch: %v\n", err)
//             os.Exit(1)
//         }
//         io.Copy(dst,resp.Body)// Fetch prints the content found at a URL.
// package main

// import (
//     "fmt"
//     "io"
//     "net/http"
//     "os"
// )

// func main() {
//     for _, url := range os.Args[1:] {
//         // 发送HTTP GET请求
//         resp, err := http.Get(url)
//         if err != nil {
//             fmt.Fprintf(os.Stderr, "fetch: %v\n", err)
//             os.Exit(1)
//         }
//         defer resp.Body.Close()  // 确保响应体被关闭
        
//         // 使用io.Copy直接将响应体拷贝到标准输出
//         bytesCopied, err := io.Copy(os.Stdout, resp.Body)
//         if err != nil {
//             fmt.Fprintf(os.Stderr, "fetcåh: reading %s: %v\n", url, err)
//             os.Exit(1)
//         }
        
//         // 可选：打印拷贝的字节数用于调试
//         fmt.Fprintf(os.Stderr, "\n\nCopied %d bytes from %s\n", bytesCopied, url)
//     }
// }
//         resp.Body.Close()
//         if err != nil {
//             fmt.Fprintf(os.Stderr, "fetch: reading %s: %v\n", url, err)
//             os.Exit(1)
//         }
//         fmt.Printf("%s", b)
//     }
// }
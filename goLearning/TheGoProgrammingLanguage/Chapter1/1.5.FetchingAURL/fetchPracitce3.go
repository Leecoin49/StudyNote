package main

import (
    "fmt"
    "io"
    "net/http"
    "os"
    "strings"
)

func main() {
    for _, url := range os.Args[1:] {
        // 检查URL协议
        if !strings.HasPrefix(url, "http://") && !strings.HasPrefix(url, "https://") {
            url = "http://" + url
            fmt.Fprintf(os.Stderr, "Note: Added protocol prefix\n")
        }
        
        resp, err := http.Get(url)
        if err != nil {
            fmt.Fprintf(os.Stderr, "fetch: %v\n", err)
            os.Exit(1)
        }
        defer resp.Body.Close()
        
        // 获取分解的状态信息
        statusCode := resp.StatusCode    // 整数状态码，如 200
        statusText := resp.Status        // 完整状态文本，如 "200 OK"
        
        // 更详细的输出
        fmt.Fprintf(os.Stderr, "=== Request to: %s ===\n", url)
        fmt.Fprintf(os.Stderr, "Status Code: %d\n", statusCode)
        fmt.Fprintf(os.Stderr, "Status Text: %s\n", statusText)
        
        // 根据状态码给出提示
        switch {
        case statusCode >= 200 && statusCode < 300:
            fmt.Fprintf(os.Stderr, "Result: Success (2xx)\n")
        case statusCode >= 300 && statusCode < 400:
            fmt.Fprintf(os.Stderr, "Result: Redirection (3xx)\n")
        case statusCode >= 400 && statusCode < 500:
            fmt.Fprintf(os.Stderr, "Result: Client Error (4xx)\n")
        case statusCode >= 500:
            fmt.Fprintf(os.Stderr, "Result: Server Error (5xx)\n")
        }
        
        fmt.Fprintf(os.Stderr, "%s\n", strings.Repeat("-", 40))
        
        // 输出响应体内容
        _, err = io.Copy(os.Stdout, resp.Body)
        if err != nil {
            fmt.Fprintf(os.Stderr, "fetch: reading %s: %v\n", url, err)
            os.Exit(1)
        }
        
        fmt.Fprintf(os.Stderr, "\n%s\n\n", strings.Repeat("=", 50))
    }
}
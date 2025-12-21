package main

import (
    "fmt"
    "io"
    "net/http"
    "os"
    "strings"
)

func addProtocolPrefix(url string) string {
    // 检查常见协议前缀
    prefixes := []string{"http://", "https://", "ftp://", "file://"}
    for _, prefix := range prefixes {
        if strings.HasPrefix(url, prefix) {
            return url  // 已有协议，直接返回
        }
    }
    
    // 特殊处理：以双斜杠开头
    if strings.HasPrefix(url, "//") {
        return "http:" + url
    }
    
    // 默认添加http://
    return "http://" + url
}

func main() {
    for _, url := range os.Args[1:] {
        originalURL := url
        url = addProtocolPrefix(url)
        
        if originalURL != url {
            fmt.Fprintf(os.Stderr, "Normalized URL: %s -> %s\n", originalURL, url)
        }
        
        resp, err := http.Get(url)
        if err != nil {
            fmt.Fprintf(os.Stderr, "fetch: %v\n", err)
            os.Exit(1)
        }
        defer resp.Body.Close()
        
        _, err = io.Copy(os.Stdout, resp.Body)
        if err != nil {
            fmt.Fprintf(os.Stderr, "fetch: reading %s: %v\n", url, err)
            os.Exit(1)
        }
    }
}
**Gin框架接收GET和POST参数**

Gin是一个用Go语言编写的Web框架，以其高性能和简洁的API而闻名。以下是如何在Gin框架中接收GET和POST参数的基本方法：

### 接收GET参数

对于GET请求，参数通常通过URL的查询字符串传递。Gin提供了`c.Query`方法来获取这些参数。

**示例代码：**

```go
package main

import (
    "github.com/gin-gonic/gin"
    "net/http"
)

func main() {
    router := gin.Default()

    router.GET("/getExample", func(c *gin.Context) {
        // 通过c.Query获取GET参数
        name := c.Query("name")
        c.JSON(http.StatusOK, gin.H{
            "message": "GET request",
            "name":    name,
        })
    })

    router.Run(":8080")
}
```

在这个例子中，如果你访问`/getExample?name=Kimi`，Gin会解析URL中的`name`参数，并将其传递给`c.Query("name")`。

### 接收POST参数

对于POST请求，参数可以通过表单数据、JSON或XML等格式传递。Gin提供了`c.PostForm`和`c.ShouldBind`方法来处理这些参数。

**示例代码：**

```go
package main

import (
    "github.com/gin-gonic/gin"
    "net/http"
)

func main() {
    router := gin.Default()

    router.POST("/postExample", func(c *gin.Context) {
        // 通过c.PostForm获取表单参数
        username := c.PostForm("username")
        
        // 通过c.ShouldBind绑定JSON请求体到结构体
        var example Example
        if err := c.ShouldBindJSON(&example); err != nil {
            c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
            return
        }
        
        c.JSON(http.StatusOK, gin.H{
            "message": "POST request",
            "username": username,
            "example": example,
        })
    })

    router.Run(":8080")
}

// Example 用于绑定JSON请求体的结构体
type Example struct {
    Name string `json:"name"`
    Age  int    `json:"age"`
}
```

在这个例子中，对于表单数据，你可以通过`c.PostForm("key")`来获取参数；对于JSON请求体，你可以定义一个结构体，并使用`c.ShouldBindJSON(&structVar)`来自动解析和绑定JSON数据到该结构体。

**注意：** 确保你的请求头`Content-Type`正确设置，对于表单数据通常是`application/x-www-form-urlencoded`，对于JSON数据是`application/json`。

通过这些基本方法，你可以在Gin框架中灵活地处理GET和POST请求的参数。希望这能帮助你更好地理解和使用Gin框架！

https://github.com/apiaryio/api-blueprint/tree/master/examples  样例

https://github.com/apiaryio/api-blueprint/blob/master/API%20Blueprint%20Specification.md 语法规则


**api-mock  drakov**

两者都是可以根据 api-blueprint 的文档创建一个本地的 mock server 的工具。使用它们可以避免前后端开发在时间差上的无谓等待。

npm install -g api-mock
api-mock ./apiary.md --port 3000

npm install -g drakov
drakov -f apiary.md -p 3000

**aglio"" 是一个可以根据 api-blueprint 的文档生成静态 HTML 页面的工具。

``

npm install -g aglio
aglio -i foo.md -o bar.html

``

Examaples
--------

``

FORMAT: 1A
 # Example API
 hello world
  ## 消息 [/messages]
  ### 获取消息 [GET]
  + Response 200 (application/json)
      {
            "hello": "world"
      }
``

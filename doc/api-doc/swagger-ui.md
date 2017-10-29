
## Swigger-ui 基本介绍 

swigger的api套件： 

* swigger-editor - api 文档书写器 （yaml格式）
* swigger-ui     - api 文档发布器 

-　editor 编写api文档可以选择upload import的方式加载本地　yaml/json 到页面上编写，完成编写选择下载到本地。editor有颇实用的地方在于，可以根据定义的api生成各种不同web服务的框架server端和client端代码。 


- swigger-ui 呈现api接口

## 安装

### swagger-editor

  node -v   > 6.2 

```
  mkdir /home/swagger ; cd /home/swagger
  git clone https://github.com/swagger-api/swagger-editor.git
  npm install -g http-server 
  http-server ./swagger-editor -p 9999   启动 editor侦听在 9999 端口
```

### swagger-ui 

```bash
  cd /home/swagger 
  git clone https://github.com/swagger-api/swagger-ui.git 
  mkdir node_app; cd node_app
  npm init 
  cp ../swagger-ui/dist ./
  npm install express --save
```  
  
vim index.js 

```javascript

  var express = require('express');  
  var app = express();  
  app.use('/root', express.static('dist'));  
  app.get('/', function (req, res) {  
    res.send('Hello World!');  
  });  
  
  app.listen(3000, function () {  
    console.log('Example app listening on port 3000!');  
  });  

```

  启动 swigger-ui 
  node ./index.js   默认启动端口 3000 
  
## swagger 集成

### java spring 

maven:http://www.mvnrepository.com/artifact/com.mangofactory/swagger-springmvc

添加 Controller 的Swigger注解，实现 spring mvc的api暴露给 swigger-ui  
  
    /application/api-docs 
    
修改 /swgigger-ui/dist/index.html 中url指向开发服务api的地址即可

    
  
## swagger api 格式 


  
  




基本Vue使用 

```javascript
var s1 = new Vue({
  el:'#app',
  data:{
    message:'abc',
  },
  methods:{
    add:function(a,b){
      return  a,b
     }
  },
  computed:{
    totalValue:function(){
    }
  },
  filters:{
    upper:function(value){
      return value.toUpper();
    }
 }
})
```


### v-model
绑定变量

### v-bind:attr
绑定属性值,
```html
  <p v-bind:title="value"/>  vue会生成 <p title="abc"/> 
  <a v-bind:href="url">...</a>
```
### ref  
变量引用, 在Vue()代码中引用到Template中的标签对象 

```javascript
<input type="text" ref="username" />   username表示被引用的变量名

可以这样被使用： 
   methods:{
     onCommit:function(){
       console.log(this.$refs.username.value)   
     }
   }  
```
### v-html 
输出原始Html
定义一段html代码 ` message = <H1>waoooo</H1> `

```
<span>{{ message }} </span>  直接输出未脱异的文本 
<span v-html="message"></span>  输出render的结果 ,就是H1的文字效果

```

### filter 
过滤器函数, 使用管道作为输入和输出

```javascript
{{ message | upper}}

new Vue({
  filters:{
    upper:function(value){
      return value.toUpper();
    }
  }
})
``` 
### computed 计算属性
 可以定义 `get`,`set` ,默认是`get`
```js
computed:{
  fullName: {
    get: function(){return ...},
    set: function(value) {  .. }
  }
}
```

## 单文件组件 single file component
组件构建在 .vue文件中 , 基本内容：
```html
<template> ... </template>
<script>
  export default {
    data(){
      return {...}
    },
    methods:{
    }
  }
</script>

<style>
  p { ... }
</style>

  
```





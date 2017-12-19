
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
  }
})
```


**v-model**  绑定变量

**v-bind:attr**  绑定属性值,
```html
  <p v-bind:title="value"/>  vue会生成 <p title="abc"/> 
```
**ref  变量引用** 在Vue()代码中引用到Template中的标签对象 

```javascript
<input type="text" ref="username" />   username表示被引用的变量名

可以这样被使用： 
   methods:{
     onCommit:function(){
       console.log(this.$refs.username.value)   
     }
   }  
```

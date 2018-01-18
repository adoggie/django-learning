
编写简单的web应用

参考: 
https://www.youtube.com/watch?v=Vlie-srOU8c
https://www.youtube.com/watch?v=t96hBT53S4U

 
 import  "net/http" 
 
 func main(){
   http.HandleFunc("/",rootFunc)
   http.ListenAndServe(":8088",nil)
 }
 
 func rootFunc(resp http.ResponseWriter,req * http.Request){
   resp.Write( []byte("hello world") ) 
 }

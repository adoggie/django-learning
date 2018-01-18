
编写简单的web应用
 
 import  "net/http" 
 
 func main(){
   http.HandleFunc("/",rootFunc)
   http.ListenAndServe(":8088",nil)
 }
 
 func rootFunc(resp http.ResponseWriter,req * http.Request){
   resp.Write( []byte("hello world") ) 
 }

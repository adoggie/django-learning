#coding:utf-8

"""
Last-Modified 是什么

Last-Modified 是 HttpHeader 中的资源的最后修改时间，如果带有 Last-Modified ，下一次发送 Http 请求时，将会发生带 If-modified-since 的 HttpHeader 。如果没有过期，将会收到 304 的响应，从缓存中读取。

Etag 是什么

Etag 是 HttpHeader 中代表资源的标签，在服务器端生成。如果带有 Etag ，下一次发送带 Etag 的请求，如果 Etag 没有变化将收到 304 的响应，从缓存中读取。
Etag 在使用时要注意相同资源多台 Web 服务器的 Etag 的一致性。

Expire 是什么

Expire 是 HttpHeader 中代表资源的过期时间，由服务器段设置。如果带有 Expire ，则在 Expire 过期前不会发生 Http 请求，直接从缓存中读取。用户强制 F5 例外。
Last-Modified,Etag,Expire 混合

通常 Last-Modified,Etag,Expire 是一起混合使用的，特别是 Last-Modified 和 Expire 经常一起使用，因为 Expire 可以让浏览器完全不发起 Http 请求，而当浏览器强制 F5 的时候又有 Last-Modified ，这样就很好的达到了浏览器段缓存的效果。

Etag 和 Expire 一起使用时，先判断 Expire ，如果已经过期，再发起 Http 请求，如果 Etag 也过期，则返回 200 响应。如果 Etag 没有过期则返回 304 响应。
Last-Modified,Etag,Expires 三个同时使用时。先判断 Expire ，然后发送 Http 请求，服务器先判断 last-modified ，再判断 Etag ，必须都没有过期，才能返回 304 响应。

"""


"""
1、Last-Modified
在浏览器第一次请求某一个URL时，服务器端的返回状态会是200，内容是你请求的资源，同时有一个Last-Modified的属性标记(HttpReponse Header)此文件在服务期端最后被修改的时间，格式类似这样：
Last-Modified:Tue, 24 Feb 2009 08:01:04 GMT
客户端第二次请求此URL时，根据HTTP协议的规定，浏览器会向服务器传送If-Modified-Since报头(HttpRequest Header)，询问该时间之后文件是否有被修改过：
If-Modified-Since:Tue, 24 Feb 2009 08:01:04 GMT
如果服务器端的资源没有变化，则自动返回HTTP304（NotChanged.）状态码，内容为空，这样就节省了传输数据量。当服务器端代码发生改变或者重启服务器时，则重新发出资源，返回和第一次请求时类似。从而保证不向客户端重复发出资源，也保证当服务器有变化时，客户端能够得到最新的资源。
注：如果If-Modified-Since的时间比服务器当前时间(当前的请求时间request_time)还晚，会认为是个非法请求

2、Etag工作原理
HTTP协议规格说明定义ETag为“被请求变量的实体标记”（参见14.19）。简单点即服务器响应时给请求URL标记，并在HTTP响应头中将其传送到客户端，类似服务器端返回的格式：
Etag:“5d8c72a5edda8d6a:3239″
客户端的查询更新格式是这样的：
If-None-Match:“5d8c72a5edda8d6a:3239″
如果ETag没改变，则返回状态304。
即:在客户端发出请求后，HttpReponse Header中包含Etag:“5d8c72a5edda8d6a:3239″
标识，等于告诉Client端，你拿到的这个的资源有表示ID：5d8c72a5edda8d6a:3239。当下次需要发Request索要同一个URI的时候，浏览器同时发出一个If-None-Match报头(Http RequestHeader)此时包头中信息包含上次访问得到的Etag:“5d8c72a5edda8d6a:3239″标识。
If-None-Match:“5d8c72a5edda8d6a:3239“
,这样，Client端等于Cache了两份，服务器端就会比对2者的etag。如果If-None-Match为False，不返回200，返回304(Not Modified) Response。

3、Expires
给出的日期/时间后，被响应认为是过时。如Expires:Thu, 02 Apr 2009 05:14:08 GMT
需和Last-Modified结合使用。用于控制请求文件的有效时间，当请求数据在有效期内时客户端浏览器从缓存请求数据而不是服务器端.当缓存中数据失效或过期，才决定从服务器更新数据。

4、Last-Modified和Expires
Last-Modified标识能够节省一点带宽，但是还是逃不掉发一个HTTP请求出去，而且要和Expires一起用。而Expires标识却使得浏览器干脆连HTTP请求都不用发，比如当用户F5或者点击Refresh按钮的时候就算对于有Expires的URI，一样也会发一个HTTP请求出去，所以，Last-Modified还是要用的，而且要和Expires一起用。


5、Etag和Expires
如果服务器端同时设置了Etag和Expires时，Etag原理同样，即与Last-Modified/Etag对应的HttpRequestHeader:If-Modified-Since和If-None-Match。我们可以看到这两个Header的值和WebServer发出的Last-Modified,Etag值完全一样；在完全匹配If-Modified-Since和If-None-Match即检查完修改时间和Etag之后，服务器才能返回304.


6、Last-Modified和Etag
分布式系统里多台机器间文件的last-modified必须保持一致，以免负载均衡到不同机器导致比对失败
分布式系统尽量关闭掉Etag(每台机器生成的etag都会不一样)
Last-Modified和ETags请求的http报头一起使用，服务器首先产生Last-Modified/Etag标记，服务器可在稍后使用它来判断页面是否已经被修改，来决定文件是否继续缓存
过程如下:
1.客户端请求一个页面（A）。
2.服务器返回页面A，并在给A加上一个Last-Modified/ETag。
3.客户端展现该页面，并将页面连同Last-Modified/ETag一起缓存。
4.客户再次请求页面A，并将上次请求时服务器返回的Last-Modified/ETag一起传递给服务器。
5.服务器检查该Last-Modified或ETag，并判断出该页面自上次客户端请求之后还未被修改，直接返回响应304和一个空的响应体。
注：
1、Last-Modified和Etag头都是由WebServer发出的HttpReponse Header，WebServer应该同时支持这两种头。
2、WebServer发送完Last-Modified/Etag头给客户端后，客户端会缓存这些头；
3、客户端再次发起相同页面的请求时，将分别发送与Last-Modified/Etag对应的HttpRequestHeader:If-Modified-Since和If-None-Match。我们可以看到这两个Header的值和WebServer发出的Last-Modified,Etag值完全一样；
4、通过上述值到服务器端检查，判断文件是否继续缓存；


7、关于 Cache-Control: max-age=秒 和 Expires
Expires = 时间，HTTP 1.0 版本，缓存的载止时间，允许客户端在这个时间之前不去检查（发请求）
max-age = 秒，HTTP 1.1版本，资源在本地缓存多少秒。
如果max-age和Expires同时存在，则被Cache-Control的max-age覆盖。
Expires 的一个缺点就是，返回的到期时间是服务器端的时间，这样存在一个问题，如果客户端的时间与服务器的时间相差很大，那么误差就很大，所以在HTTP 1.1版开始，使用Cache-Control: max-age=秒替代。
Expires =max-age +   “每次下载时的当前的request时间”
所以一旦重新下载的页面后，expires就重新计算一次，但last-modified不会变化

"""

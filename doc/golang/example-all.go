package main

import (
	"awesomeProject1/abc"
	"fmt"
	"go.mongodb.org/mongo-driver/bson"
	"go.mongodb.org/mongo-driver/bson/primitive"
	"os"
	"path/filepath"

	"context"
	"github.com/labstack/echo/v4"
	"github.com/labstack/echo/v4/middleware"
	"github.com/zeromq/goczmq"
	"go.mongodb.org/mongo-driver/mongo"
	"go.mongodb.org/mongo-driver/mongo/options"
	"net/http"
	"testing"
	"time"
)


func indexHandler(w http.ResponseWriter, r * http.Request) {
	fmt.Fprintf(w,  fmt.Sprintf("%s %v","hello world",r.Method) )

}

func TestBasic(t *testing.T){
	var p = "abc"
	pp:=&p
	*pp = "shanghai"
	fmt.Println(p[0],pp)
}

func TestWeb(t *testing.T) {
	http.HandleFunc("/", indexHandler)
	http.ListenAndServe(":8000", nil)
}

func hello(c echo.Context) error {
	//return c.String(http.StatusOK, "Hello, World!")
	return c.JSON(http.StatusOK,[]string{"shanghai","beijing"})
}

func TestMongodb(t *testing.T){
	type Rpan struct{
		ID primitive.ObjectID `bson:"id"`
		Start primitive.DateTime `bson:"start"`
	}
	ctx, cancel := context.WithTimeout(context.Background(), 10*time.Second)
	defer cancel()
	client, err := mongo.Connect(ctx, options.Client().ApplyURI("mongodb://localhost:27018"))
	defer func() {
		if err = client.Disconnect(ctx); err != nil {
			//panic(err)
		}
	}()
	names,_:=client.ListDatabaseNames(ctx,bson.D{})
	fmt.Println(names)
	coll := client.Database("Task").Collection("RPan")
	cur,_:= coll.Find(ctx,bson.D{})
	{
		var result []bson.M
		cur.All(ctx,&result)
		for _,m := range result{
			fmt.Println(m)
		}
	}
	//{
	//	var result []Rpan
	//	cur.All(ctx, &result)
	//	fmt.Println(result[0].Start.Time())
	//	r ,_ := json.Marshal(result[0])
	//	fmt.Println( string(r) )
	//}

	//for cur.Next(ctx){
	//	var r bson.M
	//	cur.Decode(&r)
	//	bytes,_:= json.Marshal(r)
	//	fmt.Println( string(bytes) )
	//}

	{
		//projection := bson.D{
		//	{"item", 1},
		//	{"status", 1},
		//}
		//
		//cursor, err := coll.Find(
		//	context.Background(),
		//	bson.D{
		//		{"status", "A"},
		//	},
		//	options.Find().SetProjection(projection),
		//)
	}

}

// https://pkg.go.dev/github.com/zeromq/goczmq#example-Proxy
// https://github.com/zeromq/goczmq/blob/master/poller_test.go

// 连接上游sub，转发给bind的本地pub通道
func TestZMQ_Redirect(t *testing.T){
	//  connect remote -> bind local
	//sub := goczmq.NewSubChanneler("tcp://127.0.0.1:15554","")
	//pub := goczmq.NewPubChanneler("tcp://127.0.0.1:15556")
	//for{
	//	data :=<- sub.RecvChan
	//	pub.SendChan <- data
	//}
	sub ,_:= goczmq.NewSub("tcp://127.0.0.1:15554","")
	pub ,_:= goczmq.NewPub("tcp://127.0.0.1:15556")

	for{

		if data ,e := sub.RecvMessage(); e==nil{
			pub.SendMessage(data)
		}

	}
}

func TestZMQ_Proxy(t *testing.T){
	// bind 本地两个 endpoint， 接受两端的连接进入
	//reader := bufio.NewReader(os.Stdin)
	proxy := goczmq.NewProxy()
	defer proxy.Destroy()

	// set front end address and socket type
	err := proxy.SetFrontend(goczmq.Sub, "tcp://127.0.0.1:15556")
	if err != nil {
		//panic(err)
	}

	// set back end address and socket type
	err = proxy.SetBackend(goczmq.Pub, "tcp://127.0.0.1:15554")
	if err != nil {
		//panic(err)
	}
	fmt.Println("Waiting..")
	ch := make(chan int)
	<-ch
}

func TestZMQ(t *testing.T){
	//sub,err := goczmq.NewSub("tcp://127.0.0.1:15554","")
	exit := time.After(10*time.Second)

	dir, err := filepath.Abs(filepath.Dir(os.Args[0]))
	if err != nil {
		//log.Fatal(err)
	}
	fmt.Println(dir)
	p ,_:=os.Getwd()
	fn :=filepath.Join( p,"abc.txt")
	fp ,_ := os.OpenFile(fn,os.O_APPEND|os.O_WRONLY|os.O_CREATE,0660)
	defer fp.Close()
	sub:=goczmq.NewSubChanneler("tcp://127.0.0.1:15556","")
	Loop:
	for {
		select {
			case data := <-sub.RecvChan:
				for _, bytes:= range data{
					fmt.Printf("%s\n",string(bytes))
					fp.WriteString(string(bytes))
				}
			case <-exit :
				fmt.Println("Recv Close..")
				break Loop
		}
	}


}

/*
https://echo.laily.net/cookbook/crud/
https://www.tizi365.com/archives/28.html
 */

func TestEchoWeb(t *testing.T){
	e := echo.New()
	abc.Hello()
	// Middleware
	e.Use(middleware.Logger())
	e.Use(middleware.Recover())
	//e.Pre(middleware.RemoveTrailingSlash())
	// Routes
	e.GET("/", hello)
	//e.Use(middleware.Static("/static"))
	//e.Use(middleware.StaticWithConfig(middleware.StaticConfig{
	//	Root:   "/Users/scott/Desktop",
	//	Browse: true,
	//}))
	//e.Static("/static", "/Users/scott/Desktop")
	// Start server
	e.Logger.Fatal(e.Start(":1323"))
}

func  TestTime(_ *testing.T) {
	f := time.Now().Add(10 * time.Second)
	t := f
	s := f.Format("2021-01-01")
	fmt.Println(f,s)

	fmt.Printf("%d-%02d-%02dT%02d:%02d:%02d-00:00\n",
		t.Year(), t.Month(), t.Day(),
		t.Hour(), t.Minute(), t.Second())
}

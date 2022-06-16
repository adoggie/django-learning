
//https://github.com/adshao/go-binance
//export https_proxy=socks5://127.0.0.1:1086


client := binance.NewFuturesClient(apiKey, secretKey) 

wsKlineHandler := func(event *binance.WsKlineEvent) {
	fmt.Println(event)
}

errHandler := func(err error) {
	fmt.Println(err)
}

// 订阅接收1m 
doneC, stopC, err := binance.WsKlineServe("ADAUSDT", "1m", wsKlineHandler, errHandler)
<-doneC

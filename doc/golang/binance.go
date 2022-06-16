
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

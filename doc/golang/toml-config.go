package main

import (
	"fmt"
	"github.com/BurntSushi/toml"
	"os"
	"testing"
	"time"
)




func TestToml(t *testing.T) {
	d:=
`
server = "192.168.1.1"
ports = [ 8001, 8001, 8002 ]
connection_max = 5000
enabled = true
data ="what"
`

	type database struct{
		Server string `toml:"server"`
		Ports []int `toml:"ports"`
		ConnMax int `toml:"connection_max"`
		Enabled bool `toml:"enabled"`
	}

	type Config struct {
		Age        int
		Cats       []string
		Pi         float64
		Perfection []int
		DOB        time.Time // requires `import time`
	}

	var dbcfg database
	if _,e:=toml.Decode( d ,&dbcfg); e!=nil{
		fmt.Println(e)
		return
	}
	fmt.Println("***",dbcfg)

	var config Config
	xx,_:=os.ReadFile("a.toml")
	if _,err := toml.Decode(string(xx),&config);err==nil {
		fmt.Println(config)
	}else{
		fmt.Println(err)
	}

}

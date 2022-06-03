
jupyter binding
https://github.com/gopherdata/gophernotes
https://github.com/gopherdata/gophernotes#mac


**Method 1: quick installation as module**

$ env GO111MODULE=on go get github.com/gopherdata/gophernotes
$ mkdir -p ~/Library/Jupyter/kernels/gophernotes
$ cd ~/Library/Jupyter/kernels/gophernotes
$ cp "$(go env GOPATH)"/pkg/mod/github.com/gopherdata/gophernotes@v0.7.5/kernel/*  "."
$ chmod +w ./kernel.json # in case copied kernel.json has no write permission
$ sed "s|gophernotes|$(go env GOPATH)/bin/gophernotes|" < kernel.json.in > kernel.json

**Method 2: manual installation from GOPATH**

$ env GO111MODULE=off go get -d -u github.com/gopherdata/gophernotes
$ cd "$(go env GOPATH)"/src/github.com/gopherdata/gophernotes
$ env GO111MODULE=on go install
$ mkdir -p ~/Library/Jupyter/kernels/gophernotes
$ cp kernel/* ~/Library/Jupyter/kernels/gophernotes
$ cd ~/Library/Jupyter/kernels/gophernotes
$ chmod +w ./kernel.json # in case copied kernel.json has no write permission
$ sed "s|gophernotes|$(go env GOPATH)/bin/gophernotes|" < kernel.json.in > kernel.json


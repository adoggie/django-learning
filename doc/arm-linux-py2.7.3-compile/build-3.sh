#!/bin/bash

# change these to match your environment
TARGET_HOST="arm-linux"
CROSS_TOOLS_PATH=/smart/arm-linux-gcc/bin
BUILD_HOST="x86-linux-gnu"

# you shouldn't need to change these
PYTHON="Python-2.7.3"
CONFIGURE_ARGS="--disable-ipv6"
BUILD_LOG="build.log"

# build log goes here
rm -f $BUILD_LOG
touch $BUILD_LOG
echo "Build output will be in $BUILD_LOG"


PYTHON_ORIG="Python-2.7.3.orig"
#mv $PYTHON $PYTHON_ORIG

PYTHON=$PYTHON_ORIG


cd $PYTHON
BUILD_LOG="../$BUILD_LOG"
unset CROSS_COMPILE

# ensure static glibc is installed
set -e

# set up environment for cross compile - we really shouldn't blindly add to PATH
export PATH="$PATH:$CROSS_TOOLS_PATH"
export CROSS_COMPILE=arm-linux-gnueabihf-

echo "Stage 1.5: patching Python for cross-compile .."
#patch -p0 < ./files/Python-2.7.3-xcompile.patch

#exit 0 

# cross compile
echo "Stage 2: cross-compiling for $TARGET_HOST .."
make HOSTPYTHON=hostpython HOSTPGEN=./Parser/hostpgen CROSS_COMPILE_TARGET=yes BUILDARCH=$BUILD_HOST HOSTARCH=$TARGET_HOST LDFLAGS=-L/smart/arm-linux-gcc/arm-linux-gnueabihf/libc/lib/arm-linux-gnueabihf #>> $BUILD_LOG
#make  HOSTPGEN=./Parser/hostpgen CROSS_COMPILE_TARGET=yes BUILDARCH=$BUILD_HOST HOSTARCH=$TARGET_HOST #>> $BUILD_LOG

sed -n -e '/Python build finished/,$p' $BUILD_LOG | grep -v 'install'
file python

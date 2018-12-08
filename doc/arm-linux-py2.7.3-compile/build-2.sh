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
#./configure $CONFIGURE_ARGS --build=$BUILD_HOST --host=$TARGET_HOST --prefix=/smart/arm32/root \
#    LDFLAGS="-static -static-libgcc" CPPFLAGS="-static" CONFIG_SITE="config.site" #>> $BUILD_LOG
./configure $CONFIGURE_ARGS --build=$BUILD_HOST --host=$TARGET_HOST --prefix=/smart/arm32/root \
     CONFIG_SITE="config.site"  --enable-shared #>> $BUILD_LOG
sed -i '1r ./files/Setup' Modules/Setup

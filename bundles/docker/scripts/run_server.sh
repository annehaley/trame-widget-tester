#!/usr/bin/env bash
CURRENT_DIR=`dirname "$0"`

# Since Mac doesn't come with realpath by default, let's set the full
# paths using PWD.
pushd . > /dev/null
cd $CURRENT_DIR/..
DEPLOY_DIR=$PWD
popd > /dev/null

docker run -it --rm \
    -p 8080:80 \
    -v "$DEPLOY_DIR:/deploy" \
    kitware/trame

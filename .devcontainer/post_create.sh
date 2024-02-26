#!/usr/bin/env bash

cd /usr/local
curl -L https://dl.dagger.io/dagger/install.sh | sudo sh
cd -
pip3 install -r requirements.txt
pip3 install anyio==4.3.0 dagger-io==0.9.11

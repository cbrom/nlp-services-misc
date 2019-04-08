#!/usr/bin/env bash

snet_daemon_v=0.1.8

if [ ! -d models/ ]; then
    mkdir models
    wget https://s3-us-west-2.amazonaws.com/allennlp/models/srl-model-2018.05.25.tar.gz -O models/srl-model-2018.05.25.tar.gz
fi
python3.6 -m spacy download en_core_web_sm

# apt install tar
if [ ! -d snet-daemon-v$snet_daemon_v ] ; then
	echo "Downloading snetd-linux"
	wget https://github.com/singnet/snet-daemon/releases/download/v$snet_daemon_v/snet-daemon-v$snet_daemon_v-linux-amd64.tar.gz
	tar -xzf snet-daemon-v$snet_daemon_v-linux-amd64.tar.gz
	ln snet-daemon-v$snet_daemon_v-linux-amd64/snetd snetd-linux-amd64
	rm snet-daemon-v$snet_daemon_v-linux-amd64.tar.gz
else
	echo "Folder seems to exist"
fi

RUN python3.6 -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. service_spec/srl.proto

# cp snet.config.example.mainnet snet.config.example.mainnet.json
# cp snet.config.example.ropsten snet.config.example.ropsten.json
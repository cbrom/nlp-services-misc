#!/usr/bin/env bash

snet_daemon_v=0.1.8

if [ ! -d snet-daemon-v$snet_daemon_v ] ; then
	echo "Downloading snetd-linux"
	wget https://github.com/singnet/snet-daemon/releases/download/v$snet_daemon_v/snet-daemon-v$snet_daemon_v-linux-amd64.tar.gz
	tar -xzf snet-daemon-v$snet_daemon_v-linux-amd64.tar.gz
	ln snet-daemon-v$snet_daemon_v-linux-amd64/snetd snetd-linux-amd64
	rm snet-daemon-v$snet_daemon_v-linux-amd64.tar.gz
else
	echo "Folder seems to exist"
fi


# Create dictionary for the available service.
python3.6 service/dictionary_creator.py
python3.6 -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. service_spec/NamedEntityDisambiguation.proto

cp snet.config.example.mainnet snet.config.example.mainnet.json
cp snet.config.example.ropsten snet.config.example.ropsten.json

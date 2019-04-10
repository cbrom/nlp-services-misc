#!/usr/bin/env bash
sudo docker build --file Dockerfile . -t singularitynet:srl_allen
sudo docker run -d -v /home/zelalem/nlp-services-misc/allen-srl/etcd:/semantic-role-labeling-service/etcd -v /etc/letsencrypt:/etc/letsencrypt -it -p 8021:8021 -p 8011:8011 --name semantic-role-labeling-service singularitynet:semantic-role-labeling-service

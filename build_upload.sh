#!/bin/bash
docker build -t ervincaravaliibarra/kafka-producer ./producer
docker build -t ervincaravaliibarra/kafka-costumer ./costumer
docker build -t ervincaravaliibarra/kafka-producer-2 ./producer-2
docker build -t ervincaravaliibarra/kafka-costumer-2 ./costumer-2

sleep 5
docker push ervincaravaliibarra/kafka-producer
docker push ervincaravaliibarra/kafka-costumer
docker push ervincaravaliibarra/kafka-producer-2
docker push ervincaravaliibarra/kafka-costumer-2

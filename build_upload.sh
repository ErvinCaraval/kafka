#!/bin/bash
docker build -t ervincaravaliibarra/kafka-producer ./producer
docker build -t ervincaravaliibarra/kafka-costumer ./costumer
docker build -t ervincaravaliibarra/kafka-producer-2 ./producer-2
docker build -t ervincaravaliibarra/kafka-costumer-2 ./costumer-2
docker build -t estiradikal/kafka-producer-3 ./producer
docker build -t estiradikal/kafka-costumer-3 ./costumer


sleep 5
docker push ervincaravaliibarra/kafka-producer
docker push ervincaravaliibarra/kafka-costumer
docker push ervincaravaliibarra/kafka-producer-2
docker push ervincaravaliibarra/kafka-costumer-2
docker push estiradikal/kafka-producer-2
docker push estiradikal/kafka-costumer-2

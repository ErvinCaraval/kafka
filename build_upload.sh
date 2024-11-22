#!/bin/bash
docker build -t ervincaravaliibarra/kafka-producer ./producer
docker build -t ervincaravaliibarra/kafka-costumer ./costumer
docker build -t ervincaravaliibarra/kafka-producer-2 ./producer-2
docker build -t ervincaravaliibarra/kafka-costumer-2 ./costumer-2
docker build -t javierlasso/kafka-producer-4 ./producer-4
docker build -t javierlasso/kafka-costumer-4 ./costumer-4

sleep 5
docker push ervincaravaliibarra/kafka-producer
docker push ervincaravaliibarra/kafka-costumer
docker push ervincaravaliibarra/kafka-producer-2
docker push ervincaravaliibarra/kafka-costumer-2
docker push javierlasso/kafka-producer-4
docker push javierlasso/kafka-costumer-4

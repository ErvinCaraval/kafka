#!/bin/bash
docker build -t ervincaravaliibarra/kafka-producer ./producer
docker build -t ervincaravaliibarra/kafka-costumer ./costumer
sleep 5
docker push ervincaravaliibarra/kafka-producer
docker push ervincaravaliibarra/kafka-costumer

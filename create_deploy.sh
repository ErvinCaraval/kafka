#!/bin/bash
kubectl apply -f kubernetes/kafka-cluster.yml
sleep 10
kubectl apply -f kubernetes/producer-deployment.yml
sleep 5
kubectl apply -f kubernetes/consumer-deployment.yml

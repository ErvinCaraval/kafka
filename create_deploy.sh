#!/bin/bash
kubectl apply -f kubernetes/kafka-cluster.yml
sleep 10
kubectl apply -f kubernetes/producer-deployment.yml
sleep 5
kubectl apply -f kubernetes/consumer-deployment.yml
sleep 5
kubectl apply -f kubernetes/producer-2-deployment.yml
sleep 5
kubectl apply -f kubernetes/consumer-2-deployment.yml
sleep 5
kubectl apply -f kubernetes/producer-3-deployment.yml
sleep 5
kubectl apply -f kubernetes/consumer-3-deployment.yml
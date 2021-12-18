#!/bin/bash

kubectl apply -f ../mongo-pv.yml
kubectl apply -f ../mongo-pvc.yml
kubectl apply -f ../mongo-deployment.yml
kubectl apply -f ../mongo-service.yml

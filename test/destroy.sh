#!/bin/bash

kubectl delete -f ../mongo-service.yml
kubectl delete -f ../mongo-deployment.yml
kubectl delete -f ../mongo-pvc.yml
kubectl delete -f ../mongo-pv.yml

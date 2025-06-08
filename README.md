## QR App on Kubernetes (Minikube)

 This project deploys a Python-based QR code application using Kubernetes via Minikube. It includes
 all necessary configuration files to run the app locally using Docker and expose it via a NodePort
 service.

 ## Prerequisites

 - Docker
 - Minikube
 - kubectl

## Setup Instructions
 
 ### Start Minikube

 Make sure Docker Desktop is running, then start Minikube:

    minikube start --driver=docker

 ### Build the Docker Image Inside Minikube

 
   docker build -t qr-app:latest .

 ### Deploy the App

   kubectl apply -f deployment.yaml
   
   kubectl apply -f service.yaml

 ### Access the App

    minikube service qr-service 

## Files Included

- Dockerfile
- deployment.yaml
- service.yaml
 
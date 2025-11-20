# Kubernetes Hands-On Project #

🎯 Goal:

✅ Deploy Nginx using a Deployment

✅ Expose it using a Service (NodePort)

✅ Access Nginx page in browser

## 1. Setup ##

**1.1 Install Docker**

👉 Follow instructions for your OS here:

 🔗 https://docs.docker.com/get-docker/
 
Once installation is complete, start Docker.

**1.2 Install Minikube**

👉 Follow instructions for your OS here:

 🔗 https://minikube.sigs.k8s.io/docs/start/
 
Once installation is complete, run the following command to start minkube:
```
minikube start
```
**1.3 Install kubectl**

👉 Follow instructions for your OS here:

 🔗 https://kubernetes.io/docs/tasks/tools/
 
Once installation is complete, run the following command to verify it:
```
kubectl get po -A
```
Output should show you the system pods running.

## 2. Create a Deployment (Nginx Example) ##

**2.1 Generate YAML and Apply Deployment YAML**

Save file as nginx-deployment.yaml and run:
```
kubectl apply -f nginx-deployment.yaml
```

**2.2 Verify Deployment**
```
kubectl get deployments
kubectl get pods
```
## 3. Expose with a Service (NodePort) ##

**3.1  Generate YAML and Apply Service YAML**

Save file as nginx-service.yaml and run:
```
kubectl apply -f nginx-service.yaml
```
**3.2 Verify Service**
```
kubectl get svc
```
**3.3 Access Nginx via NodePort**
```
 minikube service nginx-service
```
It should display the below Nginx default page in your browser.

<img width="600" height="600" alt="image" src="https://github.com/user-attachments/assets/4222fc60-79ae-4710-b4b7-79fdee0ff628" />
<img width="600" height="600" alt="image" src="https://github.com/user-attachments/assets/fb9d994b-5715-4012-bd69-c9ecef66e415" />
<img width="600" height="600" alt="image" src="https://github.com/user-attachments/assets/3f5df6a9-7078-44ed-9b14-b7488e8428f0" />
<img width="600" height="600" alt="image" src="https://github.com/user-attachments/assets/bcee0990-f646-462c-8c87-4ac53814d2c5" />
<img width="600" height="600" alt="image" src="https://github.com/user-attachments/assets/32a9f735-ab2a-4087-850e-b535802bfe3c" />
<img width="600" height="600" alt="image" src="https://github.com/user-attachments/assets/e36db17c-2918-4546-8587-cd28b73fa294" />







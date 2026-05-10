# KubeTask 🚀

A production-grade Flask REST API deployed on Kubernetes with high availability, auto-scaling, and health monitoring.

---

## 🏗️ Architecture
Client Request
↓
Kubernetes Service (LoadBalancer)
↓
┌──────────────────────────────┐
│  Pod 1  │  Pod 2  │  Pod 3  │
│kubetask │kubetask │kubetask │
└──────────────────────────────┘
↓
Flask API (Port 5000)

---

## ✅ Features

- 3 replica pods running simultaneously for high availability
- Readiness and liveness health checks
- Scale up or down with a single command
- CPU and memory resource limits per pod
- Non-root container user for security
- NodePort service for external access

---

## 🔗 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | /health | Health check |
| GET | /tasks | List all tasks |
| POST | /tasks | Create a task |
| DELETE | /tasks/{id} | Delete a task |

---

## 🚀 Quick Start

### Prerequisites
- Docker Desktop
- Minikube
- kubectl

### Deploy

```bash
# Start Kubernetes cluster
minikube start --driver=docker

# Build Docker image
docker build -t kubetask:latest .

# Load image into Minikube
minikube image load kubetask:latest

# Deploy to Kubernetes
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml

# Get the URL
minikube service kubetask-service --url
```

### Test the API

```bash
# Health check
curl http://127.0.0.1:PORT/health

# Get all tasks
curl http://127.0.0.1:PORT/tasks

# Create a task
curl -X POST http://127.0.0.1:PORT/tasks \
  -H "Content-Type: application/json" \
  --data-raw '{"title":"My first Kubernetes task","priority":"high"}'

# Delete a task
curl -X DELETE http://127.0.0.1:PORT/tasks/TASK_ID
```

---

## ⚡ Scaling

```bash
# Scale up to 5 replicas (handle more traffic)
kubectl scale deployment kubetask --replicas=5

# Watch pods spin up in real time
kubectl get pods

# Scale back down to 3 (save resources)
kubectl scale deployment kubetask --replicas=3
```

---

## 📁 Project Structure
kubetask/
├── k8s/
│   ├── deployment.yaml    # 3 replicas, health checks, resource limits
│   └── service.yaml       # NodePort service
├── src/
│   ├── app.py             # Flask REST API
│   └── requirements.txt   # Dependencies
├── Dockerfile             # Non-root, slim Python image
└── README.md

---

## 📖 Kubernetes Concepts Demonstrated

| Concept | What It Does |
|---------|-------------|
| **Deployment** | Manages pod lifecycle and rolling updates |
| **Service** | Exposes app to outside world via NodePort |
| **Replicas** | Runs 3 copies for high availability |
| **Readiness Probe** | Checks if pod is ready to serve traffic |
| **Liveness Probe** | Restarts pod if it becomes unhealthy |
| **Resource Limits** | Caps CPU and memory per pod |
| **Non-root User** | Security best practice for containers |

---

## 💼 What This Demonstrates

- Container orchestration with Kubernetes
- High availability with multiple replicas
- Production-grade health monitoring
- Horizontal scaling with kubectl
- Docker containerization best practices
- Infrastructure as code with YAML manifests

---

## 👨‍💻 Author

**Ali Zameer**
Cloud and DevSecOps Engineer
[GitHub](https://github.com/ali-zameer-dev)

---

## 📄 License

MIT

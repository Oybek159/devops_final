# Agro API - Agricultural Management System

Agro API is a RESTful API system designed to manage relationships between farmers, suppliers, and procurement processes. The project is built on the Flask framework and supports microservice architecture.

## 🚀 Features

- **Farmer Management**: Register, update, and delete farmer information
- **Supplier Management**: Manage supplier companies and their services
- **Procurement Process**: Handle orders between farmers and suppliers
- **API Documentation**: Interactive API documentation via Swagger/OpenAPI
- **Kubernetes Support**: Deploy with K8s and Helm charts
- **GitOps**: Automated deployment via ArgoCD

## 🛠 Technologies

- **Backend**: Python 3.10, Flask
- **Database**: PostgreSQL (SQLAlchemy ORM)
- **API Documentation**: Flasgger (Swagger)
- **Containerization**: Docker, Docker Compose
- **Orchestration**: Kubernetes
- **GitOps**: ArgoCD
- **Package Manager**: Helm

## 📋 Requirements

- Python 3.10+
- PostgreSQL
- Docker (optional)
- Kubernetes cluster (for production)

## 🔧 Installation

### Running Locally

1. **Clone the repository:**
```bash
git clone <repository-url>
cd agro-api
```

2. **Create virtual environment:**
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# or
venv\Scripts\activate     # Windows
```

3. **Install dependencies:**
```bash
pip install -r requirements.txt
```

4. **Run the application:**
```bash
python app.py
```

The API will be available at http://localhost:5000

### Running with Docker

1. **Build Docker image:**
```bash
docker build -t agro-api .
```

2. **Run container:**
```bash
docker run -p 5000:5000 agro-api
```

### Using Docker Compose

```bash
docker-compose up -d
```

## 📚 API Endpoints

### Farmers
- `GET /farmers` - Get all farmers
- `POST /farmers` - Create a new farmer
- `GET /farmers/{id}` - Get farmer details
- `PUT /farmers/{id}` - Update farmer information
- `DELETE /farmers/{id}` - Delete a farmer

### Suppliers
- `GET /suppliers` - Get all suppliers
- `POST /suppliers` - Create a new supplier
- `GET /suppliers/{id}` - Get supplier details
- `PUT /suppliers/{id}` - Update supplier information
- `DELETE /suppliers/{id}` - Delete a supplier

### Procurement
- `GET /procurement` - Get all orders
- `POST /procurement` - Create a new order
- `PUT /procurement/{id}` - Update order status
- `DELETE /procurement/{id}` - Delete an order

## 📖 API Documentation

Access interactive API documentation via Swagger UI:
```
http://localhost:5000/apidocs
```

## 🚢 Kubernetes Deployment

### Using plain K8s manifests

```bash
kubectl apply -f k8s/
```

### Using Helm charts

```bash
# Development environment
helm install agro-api-dev ./gitops-repo/charts/agro-api -f ./gitops-repo/charts/agro-api/values-dev.yaml

# Production environment
helm install agro-api-prod ./gitops-repo/charts/agro-api -f ./gitops-repo/charts/agro-api/values-prod.yaml
```

## 🔄 GitOps Deployment

For automated deployment via ArgoCD:

1. Access your ArgoCD server
   
<img width="1280" height="501" alt="image" src="https://github.com/user-attachments/assets/003007f7-c073-4377-bf4a-e4f5cd8e1a63" />


3. Apply the application files from `gitops-repo/argo-apps/`:

```bash
kubectl apply -f gitops-repo/argo-apps/agro-api-dev.yaml
kubectl apply -f gitops-repo/argo-apps/agro-api-prod.yaml
kubectl apply -f gitops-repo/argo-apps/agro-api-staging.yaml
```
- **Grafana** - Visualization and dashboards
<img width="1280" height="731" alt="image" src="https://github.com/user-attachments/assets/a22440aa-eee5-4a99-a759-b6a49c44aa2a" />


## 🏗 Project Structure

```
├── app.py                 # Main Flask application
├── config.py             # Configuration settings
├── requirements.txt      # Python dependencies
├── Dockerfile           # Docker image configuration
├── docker-compose.yml   # Docker Compose configuration
├── database/            # Database modules
│   ├── db.py           # Database configuration
│   ├── models.py       # SQLAlchemy models
│   └── __init__.py
├── routes/             # API routes (blueprints)
├── services/           # Business logic services
│   ├── farmer_service.py
│   ├── supplier_service.py
│   └── procurement_service.py
├── utils/              # Utility functions
│   └── logger.py
├── k8s/               # Kubernetes manifest files
├── gitops-repo/       # GitOps configurations
│   ├── argo-apps/     # ArgoCD applications
│   └── charts/        # Helm charts
└── instance/          # SQLite database (development)
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/new-feature`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature/new-feature`)
5. Create a Pull Request

## 📝 License

This project is distributed under the MIT License.

## 📞 Contact

For questions or suggestions, please create an issue or contact directly.

---

**Note**: This project is still in development. Full testing is recommended before using in production environments.

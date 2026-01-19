# Create Kubernetes directories
mkdir -p k8s/dev k8s/prod

# Create GitHub Actions workflow directory
mkdir -p .github/workflows

# Create application files
touch app.py requirements.txt Dockerfile README.md .gitignore

# Create Kubernetes manifest files
touch k8s/dev/deployment.yaml
touch k8s/dev/service.yaml
touch k8s/prod/deployment.yaml
touch k8s/prod/service.yaml

# Create GitHub Actions workflow file
touch .github/workflows/cicd.yaml


# Application2
A new application in Python

# new-application

### Script
Selected Python to display HelloWorld application

### K8 yamls
Contains:
deployment.yaml
service.yaml

### Docker, Minikube & Ansible
Dockerfile, playbook and corresponding role to run playbook is defined
Playbook includes: 
1. Installing docker
2. Build image from Dockerfile 
3. Tag and push image to <dtr>
4. Install Minikube
5. Download kubectl
6. Applying the deployment of application

### Jenkins
As we can configure the VCS trigger and pipelines through the GUI, I have added the Jenkinsfile with the stages we need to specify:
1. Git checkout
2. Unit Tests
3. Ansible integration

### Monitoring
Promethues installation 
We could install Grafana as well, if a the application needs to be monitored visually. Also, panels can be added.
In Prometheus configuration, we need to specify application url to get this monitored.
Also, many tools are available for monitoring Docker containers.

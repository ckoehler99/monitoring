# Skript für Monitoring Workshop
## create server - Provider www.digitalocean.com
```
doctl compute droplet create promtest --region fra1 --size 1gb --image ubuntu-18-10-x64 --ssh-keys 60022
doctl compute droplet list
doctl compute domain create promtest.digitalocean.ck99.io --ip-address 104.248.47.152 # domain zuweisen
```
## access to server
```
doctl compute ssh promtest
```

## install prometheus on server  
```
wget https://github.com/prometheus/prometheus/releases/download/v2.5.0/prometheus-2.5.0.linux-amd64.tar.gz

tar xfvz prometheus-2.5.0.linux-amd64.tar.gz 
```
## Starting Prometheus
Start Prometheus. By default, Prometheus reads its config from a file called prometheus.yml in the current working directory, and it stores its database in a sub-directory called data, again relative to the current working directory. 
```
./prometheus 
```

## install docker
```
apt update && apt -y upgrade && apt -y install docker.io docker-compose

## clone project and start
git clone https://github.com/ckoehler99/monitoring.git
mkdir 
```

## Grafana




## Kubernetes

# Skript für Monitoring Workshop
## Setup Server
### create server - Provider www.digitalocean.com
Digitalocean ist ein Cloudprovider mit dem einfach getestet werden kann. Die CLI doctl muss vorher installiert werden https://www.digitalocean.com/community/tutorials/how-to-use-doctl-the-official-digitalocean-command-line-client
```
doctl compute droplet create promtest --region fra1 --size 2gb --image ubuntu-18-10-x64 --ssh-keys 60022
doctl compute droplet list
doctl compute domain create promtest.digitalocean.ck99.io --ip-address 104.248.47.152 # domain zuweisen
```
### access to server
```
doctl compute ssh promtest
```

### install prometheus on server 
```
wget https://github.com/prometheus/prometheus/releases/download/v2.5.0/prometheus-2.5.0.linux-amd64.tar.gz

tar xfvz prometheus-2.5.0.linux-amd64.tar.gz 
```
### install docker
Docker und docker-compose werden für einige Services (BlackBox-Exporter, Grafana usw.) benutzt.
Diese Services skalieren mittels Docker sehr gut und können bei entsprechendem Setup hochverfügbar betrieben werden. 
```
apt update && apt -y upgrade && apt -y install docker.io docker-compose
```
### clone project
```
git clone https://github.com/ckoehler99/monitoring.git
```

## Prometheus / Exporter / Konfiguration

### Start prometheus
Start Prometheus. By default, Prometheus reads its config from a file called prometheus.yml in the current working directory, and it stores its database in a sub-directory called data, again relative to the current working directory. 
```
./prometheus 
```

### 1. Abfragen
Prometheus unter URL bzw. IP und Port 9090 aufrufen

In Prometheus UI, gibt es folgenden Tabs:
```
Alerts:  Liste der Alarme
Graph: Abfragen und Tests
Status: Status der Jobs
Help: Link zur Prometheus Hilfe
```
#### Beispielabfragen zu Prometheus:
Einfache Abfrage zum Status der Jobs
```up```

Anzahl der Metriken
```count({__name__=~".+"})``` 

Top10 Metriken
```topk(10, count by (__name__)({__name__=~".+"})) ```


### BlackBoxExporter


### NodeExporter


## Grafana




## Kubernetes
Anleitung unter https://github.com/ckoehler99/monitoring/tree/master/kubernetes


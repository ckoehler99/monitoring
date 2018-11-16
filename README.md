# Skript für Monitoring Workshop

>Alle Links zu den Applikationen sind in der Datei https://github.com/ckoehler99/monitoring/blob/master/links.md hinterlegt. Die URL kann auch durch die IP Adresse des Server ersetzt werden.


## Setup Server
### create server - Provider www.digitalocean.com
Digitalocean ist ein Cloudprovider mit dem einfach getestet werden kann. Die CLI doctl muss vorher installiert werden https://www.digitalocean.com/community/tutorials/how-to-use-doctl-the-official-digitalocean-command-line-client
```
doctl compute droplet create promtest --region fra1 --size 2gb --image ubuntu-18-10-x64
doctl compute droplet list
# Domain zuweisen. Dieser Schritt ist optional. 
# Es kann auch mit der IP Adresse dirket die Applikationen aufgerufen werden.
doctl compute domain create promworkshop.digitalocean.ck99.io --ip-address 104.248.47.152 

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
apt update && apt -y upgrade && apt -y install docker.io docker-compose golang-go
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
Über docker-compose starten. Dazu in das Verzeichnis "Docker_Monitoring" wechseln. Von dort kann das dann direkt aufgerufen werden.
```
docker-compose up -d blackbox-exporter
```

### NodeExporter
#### Building and running
https://github.com/prometheus/node_exporter

Prerequisites:

* [Go compiler](https://golang.org/dl/)

Building:

    go get github.com/prometheus/node_exporter
    cd ${GOPATH-$HOME/go}/src/github.com/prometheus/node_exporter
    make
    ./node_exporter <flags>

To see all available configuration flags:

    ./node_exporter -h

## Grafana
### Anmelden und erste Konfiguration
In den Ordner "Docker_Monitoring" wechsel und dort mittels docker-compose Grafana starten. 
```
docker-compose up -d grafana 
```

- Anmeldung mit User:"Admin" und Passwort:"pass"
- Einrichtung der Datasource "prometheus" in unserem Beispiel auf http://promworkshop.digitalocean.ck99.io:9090
- unter dem Reiter Dashboards die Beispiel Dashboards importieren

### Dashboard erstellen
Abfrage:

```
probe_http_duration_seconds
probe_http_duration_seconds{instance="https://allianz.de"}
sum(probe_http_duration_seconds{instance="https://allianz.de"})
```

### Alerting einrichten
- auf Dashboard ein Panel für den Alarm ergänzen

### Dashboards importieren
#### BlackBox Exporter
> https://grafana.com/dashboards/5345
> https://grafana.com/dashboards/7587

### Docker 
> https://grafana.com/dashboards/893
> https://grafana.com/dashboards/4271
> https://grafana.com/dashboards/1621


## Kubernetes und Service Discovery
Anleitung unter https://github.com/ckoehler99/monitoring/tree/master/kubernetes


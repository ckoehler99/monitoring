## Links für Workshop

### NodeExporter
http://promworkshop.digitalocean.ck99.io:9100/metrics

### Blackbox Exporter
http://promworkshop.digitalocean.ck99.io:9115/metrics
http://promworkshop.digitalocean.ck99.io:9115/probe?module=http_2xx&target=https://allianz.de

### Cadvisor 
http://promworkshop.digitalocean.ck99.io:8080/containers/

### Grafana
http://promworkshop.digitalocean.ck99.io:3000


### Federation Kubernetes
http://159.89.213.143:9090/federate?match%5B%5D=%7Bkubernetes_namespace%3D%22prom-workshop%22%7D

### Kubernetes Dashboard mit Proxy
http://localhost:8001/api/v1/namespaces/kube-system/services/https:kubernetes-dashboard:/proxy/#!/login


## Links zu Exportern
https://github.com/prometheus/blackbox_exporter

https://github.com/prometheus/node_exporter

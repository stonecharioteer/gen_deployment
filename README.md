# Deployment

`Archimedes` needs several support services launched along with it. The `docker-compose.yml` file fires these and other supporting services across the docker swarm.

Services:

1. Support Services:
    1. `nginx` - reverseproxy
    2. `consul` - serviceregistry
    3. `draw.io` - drawio
    4. `mongo` - jobdb
    5. `mysqldb` - cachedb
    6. `grafana` - dashboards
    7. `rabbitmq` - messagequeue
    8. `memcached` - ???
    9. `elasticsearch` - search
2. Core Services:
    1. `ui` - jameswatt
    2. `docs` - archimedes_docs
    3. `run_services` - ramanujan
    4. `authentication` - peter
    5. `svnlinker_service + project_service` - lineage
    6. `elastic_indexer` - searchservices
3. Extras:
    1. `xibo` - digitalsignage
    2. `check_mk` - monitoring
    3. `zulip` - chat
    4. `portainer` - swarm control

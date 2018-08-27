#!/bin/bash
docker node update --label-add loadbalancer=true dllohsr250.driveline.gkn.com
docker node update --label-add grafana=true --label-add drawio=true dllohsr251.driveline.gkn.com
docker node update --label-add jobdb=true dllohsr252.driveline.gkn.com
docker node update --label-add search=true dllohsr253.driveline.gkn.com
docker node update --label-add messagequeue=true dllohsr254.driveline.gkn.com
docker node update --label-add archimedes_services=true dllohsr255.driveline.gkn.com
docker node update --label-add archimedes_services=true dllohsr256.driveline.gkn.com
docker node update --label-add archimedes_services=true dllohsr257.driveline.gkn.com
docker node update --label-add archimedes_services=true dllohsr258.driveline.gkn.com
docker node update --label-add archimedes_services=true dllohsr259.driveline.gkn.com
docker node update --label-add archimedes_runner=true dllohsr260.driveline.gkn.com
docker node update --label-add archimedes_runner=true dllohsr261.driveline.gkn.com

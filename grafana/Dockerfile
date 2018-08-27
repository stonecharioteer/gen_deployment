ARG GRAFANA_VERSION="5.2.3"
ARG GF_INSTALL_PLUGINS="grafana-clock-panel,grafana-simple-json-datasource,btplc-status-dot-panel,mtanda-google-calendar-datasource,digrich-bubblechart-panel,snuids-radar-panel,grafana-piechart-panel,satellogic-3d-globe-panel,novalabs-annotations-panel,digiapulssi-breadcrumb-panel,neocat-cal-heatmap-panel,petrslavotinek-carpetplot-panel,briangann-gauge-panel,jdbranham-diagram-panel,citilogics-geoloop-panel"
FROM grafana/grafana:${GRAFANA_VERSION}
# switch to root
USER root
ADD plugins/. /var/lib/grafana/plugins/
RUN chown -R grafana:grafana /var/lib/grafana/plugins/
# Switch back to grafana user.

USER grafana

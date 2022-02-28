# Toolbox project
* build a microservice-based application that would allow the  users to run Apache Hadoop, Spark, Jupyter Notebooks, SonarQube and  SonarScanner without having to install any of them.  
* have one main microservice that acts as the entry point for your overall application
* docker containers deployed to Kubernetes cluster
* Kubernetes cluster deployed to Google Cloud Platform
* 
## DEMO
https://www.youtube.com/watch?v=RgIFpedW3fY

## Web App Access Link / Run my app
 Navigate to  http://35.223.16.139:5000/

## Steps
1. go to GCP, and create the project
2. open the cloud shell and pull, tag and push all images from docker hub  
```
docker pull image_name
docker tag image_name gcr.io/project_id/image_name 
docker push gcr.io/project_id/image_name 
for my web app I build docker first and then push to my docker hub
 docker build -t xynicole/project . --platform linux/amd64
docker push xynicole/project

```
3. click hamburger button and go to Kubernets Engine, create a Clusters
4. click hamburger button and go to Contain Registry
5. click each images name and click 3 dots on the right side and deploy to GKE
6. edit the enviroment variables and configuration, finsh 
```
https://github.com/big-data-europe/docker-hadoop/blob/master/docker-compose.yml
https://github.com/big-data-europe/docker-hadoop/blob/master/hadoop.env
For Hadoop, I edit variables from these 2 files
CORE_CONF_fs_defaultFS=hdfs://namenode:9000
CORE_CONF_hadoop_http_staticuser_user=root
CORE_CONF_hadoop_proxyuser_hue_hosts=*
CORE_CONF_hadoop_proxyuser_hue_groups=*
CORE_CONF_io_compression_codecs=org.apache.hadoop.io.compress.SnappyCodec

HDFS_CONF_dfs_webhdfs_enabled=true
HDFS_CONF_dfs_permissions_enabled=false
HDFS_CONF_dfs_namenode_datanode_registration_ip___hostname___check=false
```
7. go to workload, click each name, modify yaml file, for instance, in haddoop namedone change # of replicas to 1, datanode chaneg to 2
8. click Action, and then Expose and then set port number and create a load balance for all containters
9. go to  Service &Ingress and check if every endpoints works or not
10. click endpoints to access the web app

# Ports for each one
Web app: 5000 

Hadoop: 9870 and 9000

Jupyter: 8888

Sonarqube: 9000

Spark: 8080


# images
web app: 
https://hub.docker.com/r/xynicole/1660final

hadoop:
https://hub.docker.com/r/bde2020/hadoop-namenode
https://hub.docker.com/r/bde2020/hadoop-datanode

jupyter: 
https://hub.docker.com/r/jupyter/base-notebook/


sonarqube: 
https://hub.docker.com/_/sonarqube


spark:
https://hub.docker.com/r/bitnami/spark










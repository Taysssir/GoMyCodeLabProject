# GoMyCodeLabProject
Final Application Development Lab

## Project Description: 
Simple Web application writtten with Python Language using framework Django :
* Front END + Back END: Django
 
## Lifecycle DevOps Architecture Project :
 
The main Goal/Reason for choosing which tool for every DevOps phase is to familiarise with practise sTool and aim technical Knowledge. 


| PHASE   | TOOL || RAISON  | DUE TIME  |
| ------------- | -------------|-------------|------------- | ------------- |
| **Continuous Development**  | Version Control |  GIT  | The most commonly used VC + tracked changes  | 2 Days  |
| **Continuous Testing**      | Django | django.test  | + Selinum For TEST AUTO  |
| **Continuous Integration**  |  Gitlab CI  || Learn & Practise New Tool which i can use frequently on my job  |   |
| **Continuous Deployment**	  | Configuration Management  | Ansible  |  Simple IT automation and familiarise with Tool   |
|                             | Containerization  | Docker  | Create and Use containers for Test and Deployment Test   | 3H  |
|                             | Orchestration  | Kubernetes  | The most commonly used and performed Tool   |
| **Continuous Monitoring**	  | Prometheus + Grafana (Visualisation)  || Open Source  and familiarise with Tool  |    |

------------------------------------------------------------------------------

### Containerization : Docker
1. Create Docker File
2. Build the image :

```
 $ docker build -t docker-django-v0.0 .
```

3.  Run the image 

```
$ docker run docker-django-v0.0
```

4. Inspect The container to get THe adress IP for serving :

```
$ docker ps #Show container running
$ docker inspect id_container
```

* **URL APP** : http://<ip>:8000/


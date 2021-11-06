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
| **Continuous Integration**  |  Jenkins  || GITLAB CI Pipeline is NOT Free Now  |  4h |
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

 ### Continuous Integration : Jenkins :
 
 We create our JenkinsFile To Run our image and Test it with Curl : 
 
 ![Jenkins_stages](https://user-images.githubusercontent.com/15168128/138564547-783ce4f9-0392-4174-9366-213f7b71f2cc.png)

### Continuous Testing : Coverage

Install Coverage :

```
$ pip install coverage

```


Check Version :

```

$ coverage --v

```


in this case we use : coverage version 6.0.2 with C extension

Run Test Coverage

```

$ coverage run manage.py test

```


**Generate Report Test with Coverage :

```

$ coverage report

```


Generae HTML Report Coverage Test :

```

$ coverage html

```

It will generate New Folder called htmlcov and when we open index.html we got the first generating report results :



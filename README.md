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
| **Continuous Testing**      | Django | django.test  | + Selinum For TEST AUTO  |  4h |
| **Continuous Integration**  |  Jenkins  || GITLAB CI Pipeline is NOT Free Now  |  4h |
| **Continuous Deployment**	  | Configuration Management  | Ansible  |  Simple IT automation and familiarise with Tool   |
|                             | Containerization  | Docker  | Create and Use containers for Test and Deployment Test   | 3H  |
|                             | Orchestration  | Kubernetes  | The most commonly used and performed Tool   | 2 Days  |
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
![Coverage_Test](https://user-images.githubusercontent.com/15168128/140604004-3172ea92-94cc-44f3-9293-1a58168a2ad3.png)


Generate Report Test with Coverage :

```

$ coverage report

```
![coverage_report](https://user-images.githubusercontent.com/15168128/140604027-04700e5f-5574-46d6-914e-d1bfb26cb1fe.png)


Generae HTML Report Coverage Test :

```

$ coverage html

```

It will generate New Folder called htmlcov and when we open index.html we got the first generating report results :

![generate_htmlcov_dir](https://user-images.githubusercontent.com/15168128/140604036-bb40a707-2ce2-4d50-8d1d-a54c88059e8b.png)
 
 index.html : Contain the coverage Test for the whole project : 
 
 ![report_befor_test](https://user-images.githubusercontent.com/15168128/140604038-ffc00258-9336-48bb-9872-21414abbe52f.png)



# Python Falcon QuickStart

  

### What is "Falcon" ?

http://falconframework.org
  
http://falcon.readthedocs.io/



### Premise

Python 3.5.x



### Usage "Run App"


```
$ pip install -r requirements.txt
$ gunicorn app.resources:app --reload
$ curl localhost:8000/books/4873117399
```



### Usage "Test & Coverage"

```
$ pip install -r test-requirements.txt
$ nosetests --with-xunit --with-coverage --cover-erase --cover-package=app --verbose
```


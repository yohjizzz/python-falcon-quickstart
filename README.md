# python-falcon-quickstart

[Falcon](http://falconframework.org) 開発クイックスタート




### Premise

Python 3.5.x


### Usage "Run App"


```
$ pip install -r requirements.txt
$ gunicorn app.resources:app --reload
$ curl localhost:8000/books/4873117399
```

### Usage "Test"

```
$ nosetests --with-xunit --with-coverage --cover-erase --cover-package=app --verbose
```


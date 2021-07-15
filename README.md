# BTree sample application

## Setup

The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/Sandoval97/b-trees.git
$ cd b-trees
```

Create a virtual environment to install dependencies in and activate it:

```sh
$ virtualenv2 --no-site-packages env
$ source env/bin/activate
```

Then install the dependencies:

```sh
$ pip install -r requirements.txt
```

Once `pip` has finished downloading the dependencies:
```sh
$ ./manage.py runserver
```
And navigate to `http://127.0.0.1:8000/api/v1/b-trees/`.
## Tests

To run the tests, `cd` into the directory where `manage.py` is:
```sh
$ ./manage.py test
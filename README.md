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

## Available Endpoints

```sh
    /api/v1/b-trees/height
    * input
    json
    {
       "toTree": [1,2,3,4,5,6,7,8]
    }
    ```
    * output
    json
        {
            "height": 3
        }
```
Returns the height of a binary tree given an integers list

```sh
    /api/v1/b-trees/height
```
Returns the height of a binary tree given an integers list

```sh
    /api/v1/b-trees/height
```
Returns the height of a binary tree given an integers list
## Tests

To run the tests, `cd` into the directory where `manage.py` is:
```sh
$ ./manage.py test
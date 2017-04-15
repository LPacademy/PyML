# Imacel recommender

Image processing recommendation engine used in IMACEL.

## Getting Started

For now, as a template for API server using Flask, image classifier with VGG16 for imagenet dataset is implemented.

### Prerequisites

Prepare a virtualenv with Python3.x.

### Installing

First of all, please install the requirements using pip. Please confirm that your pip is the latest version. If you are using older versions of pip, some modules may not be installed properly.

```
(virtualenv)$ pip install -r requirements.txt
```

## Running the tests

After installing the requirements, you can lauch server and client processes.

```
# launch the server (port:5001 will be used)
(virtualenv)$ python server.py

# launch the client (port:5000 will be used)
(virtualenv)$ python client.py
```

If the server and client started without problems, you can upload some image to classify from http://localhost:5000 .

After selecting an image and submitting, you will see a Flask-API template page that shows JSON of most-likely category for the image you submitted.


## References

* https://github.com/aidiary/keras-examples/tree/master/vgg16/test_vgg16
* https://github.com/ksgwl/flask-api/tree/fix-json-encoder



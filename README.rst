===============================
HTTPie-Lambda
===============================


.. image:: https://img.shields.io/pypi/v/httpie_lambda.svg
        :target: https://pypi.python.org/pypi/httpie_lambda

A `HTTPie`_ plugin for interacting with AWS Lambdas.

Invoke AWS Lambda directly with all the user-friendliness of `HTTPie`_ and without
having to utilize API Gateway.

.. _`HTTPie`: https://httpie.io/

Quick Start
------------

Installation
````````````

.. code-block:: shell

    pip intall httpie-lambda

Usage
`````

Usage is consistent with HTTPie, simply use `http+lambda` as protocol:

.. code-block:: shell

	> http http+lambda://flaskexp-test/health
	HTTP/1.1 200 OK
	Content-Length: 21
	Content-Type: application/json
	X-Request-ID:

	{
		"status": "UP"
	}

For more comprehensive example such as POST refer to `HTTPie usage`_ documentation.

Specify a region or AWS credentials profile:

.. code-block:: shell

	> env AWS_DEFAULT_REGION=us-west-2 AWS_PROFILE=sukhanov http http+lambda://flaskexp-test/health
	HTTP/1.1 200 OK
	Content-Length: 21
	Content-Type: application/json
	X-Request-ID:

	{
		"status": "UP"
	}


For more information on AWS Authentication configuration see `lambda-requests`_. 

.. _`HTTPie usage`: https://httpie.io/docs#main-features
.. _`lambda-requests`: https://github.com/IlyaSukhanov/lambda-requests

[![Build Status](https://travis-ci.org/lenileiro/grpc-example.svg?branch=develop)](https://travis-ci.org/lenileiro/grpc-example)
[![Coverage Status](https://coveralls.io/repos/github/lenileiro/grpc/badge.svg?branch=develop)](https://coveralls.io/github/lenileiro/grpc?branch=develop)

# Installation

    ``bash
        virtualenv -p python3 venv
        pip install grpcio-tools && pip install grpcio
    ```

## generate keys

    ``bash
        ./generateCerts.sh
    ```
## generate python proto functions

    ``bash
        python genproto.py
    ```
## run application

    ``bash
        python server.py
    ```

## test application

    ``bash
        coverage run --source=test -m pytest && coverage report
    ```

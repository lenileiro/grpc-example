

# Python Dependence

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
        python -m pytest
    ```

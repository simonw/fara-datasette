# fara-datasette

https://fara.datasettes.com/

This code pulls the latest CSVs from https://efile.fara.gov/ords/f?p=API:BULKDATA and loads them into Datasette.

## Running the code

Clone this repo and `pip install -r requirements.txt`

Create the `fara.db` file by running `python fetch_data.py`

Start exploring it in [Datasette](https://github.com/simonw/datasette) using:

    datasette fara.db -m metadata.json

## How I deployed it

Currently deployed manually using:

    $ datasette publish now fara.db \
        -m metadata.json \
        -n fara \
        --branch=master \
        --install=datasette-vega \
        --alias fara.datasettes.com \
        --extra-options "--config facet_time_limit_ms:1000"

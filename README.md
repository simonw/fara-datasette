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
        --alias fara.datasettes.com

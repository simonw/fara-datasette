# fara-datasette

https://fara.datasettes.com/

This code pulls the latest CSVs from https://efile.fara.gov/ords/f?p=API:BULKDATA and loads them into Datasette.

Currently deployed manually using:

    $ datasette publish now fara.db \
        -m metadata.json \
        -n fara \
        --alias fara.datasettes.com

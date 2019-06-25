from io import BytesIO, StringIO
from zipfile import ZipFile
from urllib.request import urlopen
import csv
import sqlite_utils


def make_doc(data):
    for key, value in data.items():
        if key.endswith(" Date") and "/" in value:
            # Convert 06/11/2019 to yyyy-mm-dd
            mm, dd, yyyy = value.split("/")
            data[key] = "{}-{}-{}".format(yyyy, mm, dd)
    return data


if __name__ == "__main__":
    db = sqlite_utils.Database("fara.db")
    # Data from https://efile.fara.gov/ords/f?p=API:BULKDATA
    for url in (
        "https://efile.fara.gov/bulk/zip/FARA_All_Registrants.csv.zip",
        "https://efile.fara.gov/bulk/zip/FARA_All_RegistrantDocs.csv.zip",
        "https://efile.fara.gov/bulk/zip/FARA_All_ShortForms.csv.zip",
        "https://efile.fara.gov/bulk/zip/FARA_All_ForeignPrincipals.csv.zip",
    ):
        resp = urlopen(url)
        zipfile = ZipFile(BytesIO(resp.read()))
        filename = zipfile.namelist()[0]
        reader = csv.reader(StringIO(zipfile.open(filename).read().decode("utf-8")))
        headers = next(reader)
        docs = (make_doc(dict(zip(headers, row))) for row in reader)
        db[filename.replace(".csv", "")].insert_all(docs)

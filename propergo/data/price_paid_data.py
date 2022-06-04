import os
from pathlib import Path
from enum import Enum
import subprocess

class DataLink(Enum):
    price_paid_data = (
        "http://prod.publicdata.landregistry.gov.uk."
        + "s3-website-eu-west-1.amazonaws.com/pp-complete.csv"
    )


def get_csv_file(link: DataLink):
    # if the folder doesn't even exist then make it
    pth = Path("data")
    pth.mkdir(parents=True, exist_ok=True)

    if not os.path.exists("data/" + Path(link.value).name):
        bashCommand = "wget " + link.value
        bashCommand += " -O data/" + Path(link.value).name
        process = subprocess.Popen(bashCommand.split())
        output, error = process.communicate()

    # Unzip the relevant files if they are zipped
    if link.value.split(".")[-1] in ["zip"]:
        bashCommand = "unzip -o " + link.value
        process = subprocess.Popen(
            bashCommand.split(),
            cwd="data/",
        )
        output, error = process.communicate()
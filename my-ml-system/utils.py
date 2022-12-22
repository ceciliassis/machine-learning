import requests
import shutil
from flask import abort


def download_classes(url: str = '') -> list:
    res = requests.get(url)

    if res:
        classes = res.content.decode().split('\n')
        return classes
    else:
        abort(500, description="Classes couldn't be retrieved")


def download_file(url: str):
    file_name = url.split('/')[-1]
    res = requests.get(url, stream=True)

    if res:
        with open(file_name, 'wb') as file:
            shutil.copyfileobj(res.raw, file)
            return file_name
    else:
        abort(500, description="Image couldn't be retrieved")

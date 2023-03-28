import datetime
import os
from time import sleep

from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

gauth = GoogleAuth()
gauth.LocalWebserverAuth()

date = datetime.datetime.today() - datetime.timedelta(days=1)
date = date.strftime('%d-%m')


def create_and_upload_file():
    try:
        drive = GoogleDrive(gauth)
        file_name = (f'Timelapse-{date}.mpg')
        dir_path = ('timelapse')
        my_file = drive.CreateFile({'title': f'{file_name}'})
        my_file.SetContentFile(os.path.join(dir_path, file_name))
        my_file.Upload()
        print(f'File {file_name} was uploaded!')
        return f'File {file_name} was uploaded!Have a good day!'
    except Exception:
        return 'Got some trouble, check your code please!'


while True:
    time = datetime.datetime.now().strftime('%H%M%S')
    sleep(1)
    if time == '090000':
        print(create_and_upload_file())

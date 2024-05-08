import shutil
import os
import glob


def saveProject(path):
    os.mkdir(path)
    os.mkdir(path + '/static')
    os.mkdir(path + '/static/img')
    files = glob.glob('static/img/*')
    for f in files:
        print(f)
        name = f.split(chr(92))[-1]
        shutil.copy(f, path + f'/static/img/' + name)

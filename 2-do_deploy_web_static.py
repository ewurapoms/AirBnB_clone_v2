#!/usr/bin/python3
"""
Fabric script (based on the file 1-pack_web_static.py) that distributes
an archive to your web servers, using the function do_deploy
"""

import os
import datetime
from fabric.api import env, local, put, run


env.hosts = ['100.25.191.16:80', '52.91.118.253:80']
env.user = "ubuntu"


def do_pack():
    """ function generates a .tgz archive """
    timer = datetime.now().strftime("%Y%m%d%H%M%S")
    archive_path = "versions/web_static_{}.tgz".format(timer)
    local("mkdir -p versions")
    stored = local("tar -cvzf {} web_static".format(archive_path))

    if stored.return_code != 0:
        return None
    else:
        return archive_path


if __name__ == "__main__":
    archive_path = do_pack()
    if archive_path:
        print("Web static packed: {}".format(archive_path))
    else:
        print("Packaging failed.")

def do_deploy(archive_path):
    " function distributes the archive"""
    if not os.path.exists(archive_path):
        return False
    try:
        filename = archive_path.split("/")[-1]
        arg_1 = filename.split(".")[0]
        dir_path = "/data/web_static/releases/"
        put(archive_path, "/tmp/")
        run("mkdir -p {}{}/".format(dir_path, arg_1))
        run("tar -xzf /tmp/{} -C {}{}/".format(filename, dir_path, arg_1))
        run("rm /tmp/{}".format(filename))
        run("mv {0}{1}/web_static/* {0}{1}/".format(dir_path, arg_1))
        run("rm -rf {}{}/web_static".format(dir_path, arg_1))
        run("rm -rf /data/web_static/current")
        run("ln -s {}{}/ /data/web_static/current".format(dir_path, arg_1))
        return True
    except Exception as e:
        return False

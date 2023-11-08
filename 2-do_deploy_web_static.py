#!/usr/bin/python3
"""
Fabric script (based on the file 1-pack_web_static.py) that distributes
an archive to your web servers, using the function do_deploy
"""

from datetime import datetime
from fabric.api import *
import os

env.hosts = ['100.25.191.16', '52.91.118.253']
env.user = "ubuntu"


def do_pack():
    """ function generates a .tgz archive """

    local("mkdir -p versions")
    date = datetime.now().strftime("%Y%m%d%H%M%S")
    stored = "versions/web_static_{}.tgz".format(date)
    update = local("tar -cvzf {} web_static".format(stored))

    if update.succeeded:
        return stored
    else:
        return None


def do_deploy(archive_path):
    """ function distributes the archive"""
    if os.path.exists(archive_path):
        archived_file = archive_path[9:]
        updated = "/data/web_static/releases/" + archived_file[:-4]
        archived_file = "/tmp/" + archived_file
        put(archive_path, "/tmp/")
        run("mkdir -p {}".format(updated))
        run("tar -xzf {} -C {}/".format(archived_file, updated))
        run("rm {}".format(archived_file))
        run("mv {}/web_static/* {}".format(updated, updated))
        run("rm -rf {}/web_static".format(updated))
        run("rm -rf /data/web_static/current")
        run("ln -s {} /data/web_static/current".format(updated))

        print("New version deployed!")
        return True

    return False

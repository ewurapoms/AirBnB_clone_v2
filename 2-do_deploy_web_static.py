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


def do_deploy(archive_path):
    " function distributes the archive"""
    if os.path.exists(archive_path):
        stored = archive_path.split('/')[1]
        arch_path = "/tmp/{}".format(archive)
        directory = archive.split('.')[0]
        updated = "/data/web_static/releases/{}/".format(directory)

        put(archive_path, arch_path)
        run("sudo mkdir -p {}".format(updated))
        run("sudo tar -xzf {} -C {}".format(arch_path, updated))
        run("sudo rm {}".format(arch_path))
        run("sudo mv -f {}web_static/* {}".format(updated, updated))
        run("sudo rm -rf {}web_static".format(updated))
        run("sudo rm -rf /data/web_static/current")
        run("sudo ln -s {} /data/web_static/current".format(updated))
        return True
    return False

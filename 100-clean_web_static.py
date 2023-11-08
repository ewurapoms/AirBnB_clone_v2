#!/usr/bin/python3
"""
Fabric script (based on the file 3-deploy_web_static.py)
that deletes out-of-date archives, using the function do_clean
"""
import os.path
from fabric.api import *
from datetime import datetime
from fabric.operations import env, put, run

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


def deploy():
    """Create and distributes an archive to web servers"""
    try:
        path_updated = do_pack()
        return do_deploy(path_updated)
    except Exception as e:
        return False


def do_clean(number=0):
    """ cleaner function for archives """

    archives = os.listdir('versions/')
    archives.sort(reverse=True)
    start = int(number)
    if not start:
        start += 1
    if start < len(archives):
        archives = archives[start:]
    else:
        archives = []
    for archive in archives:
        os.unlink('versions/{}'.format(archive))
    cmd_parts = [
        "rm -rf $(",
        "find /data/web_static/releases/ -maxdepth 1 -type d -iregex",
        " '/data/web_static/releases/web_static_.*'",
        " | sort -r | tr '\\n' ' ' | cut -d ' ' -f{}-)".format(start + 1)
    ]
    run(''.join(cmd_parts))

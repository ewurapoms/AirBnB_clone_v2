#!/usr/bin/python3
"""
Module creates a .tgz archive from the contents of the web_static
folder of your AirBnB Clone repo, using the function do_pack
"""

import os
from fabric.api import local
from datetime import datetime


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

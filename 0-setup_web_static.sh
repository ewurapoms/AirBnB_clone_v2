#!/usr/bin/env bash
# sets up my web servers for the deployment of web_static

# Install Nginx if not already installed
sudo apt-get update
sudo apt-get install -y nginx

# Creates folders if not already exists
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/

# Creates pseudo-HTML file for testing
echo "<html>
  <head>
  </head>
  <body>
    Deploy Static TestFile
  </body>
</html>" > /data/web_static/releases/test/index.html

# Creates (...or deletes/force creates if exists) a symbolic link
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# Give ownership to ubuntu user and group
sudo chown -R ubuntu:ubuntu /data/

# update Nginx config to serve /data/web_static/current at /hbnb_static/
sudo sed -i "57i \\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n" /etc/nginx/sites-available/default

# Restarts Nginx
sudo service nginx restart

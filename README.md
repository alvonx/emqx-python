# EMQX and Python

## Launching EMQX serverwith docker

you will require 2 open ports on the server say (port1 & port2)

launch emqx `sudo docker run -d --name emqx -p port1:18083 -p port2:1883 emqx:latest`

here internal port 

**18083** -> **emqx dashboard**

**1883** -> **emqx server**


container created

- login to container

`sudo docker exec -it emqx /bin/sh`

- change password of root(admin) user

`emqx ctl admins passwd admin <your-pass>`

- to access dashboard

http://<<server-ip>>:port1





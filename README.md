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

http://server-ip:port1

- create user

![image](https://user-images.githubusercontent.com/46744784/230608750-9e5308e5-2e31-4560-b681-f47b69958cf9.png)
![image](https://user-images.githubusercontent.com/46744784/230608802-04d4b048-18e0-40d1-95fb-68df1ccb7a6e.png)
![image](https://user-images.githubusercontent.com/46744784/230608842-5de1866a-10f5-4973-bc07-f561ec1504f2.png)
![image](https://user-images.githubusercontent.com/46744784/230608891-3b61c457-8468-42ea-9e7b-f2a2d339bbdc.png)
![image](https://user-images.githubusercontent.com/46744784/230608948-bad8d182-b77a-430c-80cb-564533c4a083.png)
![image](https://user-images.githubusercontent.com/46744784/230608987-689d8dc6-2e7e-4141-bf19-0bda6ae7b095.png)
![add user name and password](https://user-images.githubusercontent.com/46744784/230609065-6fc89d32-ef35-426b-ab63-123464435fc6.png)






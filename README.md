# clusters-dashboard
Interactive visualization of star clusters

![image](assets/screenshot.png)

## How to run the app

1. `pip install -r requirements.txt` 
2. `python main.py` 
3. Go to http://0.0.0.0:8050/ from your web browser.

## How to build and run the app using docker

```docker build -t clusterdashboard .```  

```docker run -d -p 8050:8050 --restart unless-stopped clusterdashboard```

## Other util docker commands

```docker ps``` - list running containers

```docker stop <container id>``` - stop a running container

```docker rm <container id>``` - remove a container

```docker images``` - list images

```docker rmi <image id>``` - remove an image

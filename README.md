history for this project

1  apt update
    2  apt-get install docker.io
    3  mkdir flask_project
    4  cd flask_project/
    5  ls
    6  sudo apt install python3
    7  sudo apt install python3-pip
    8  sudo apt install python3-flask
    9  vi app.py
   10  python3 app.py
   11  vi requirements.txt
   12  ls
   13  vi Dockerfile
   14  sudo docker build -t flask-app .
   15  sudo docker run -d -p 5000:5000 flask-app:latest
now access it on web py your public ip with port no 5000

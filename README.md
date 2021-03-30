# sudoku-solver
python to solve sudoku

# docker

* docker-compose.yml provides the instructions to build a docker container based on Dockerfile
* Dockerfile includes python and all the needed dependencies seen in environment.yml
* the docker container can be built and startet initially with the following command (linux ubuntu):

```
docker-compose up --build -d
``` 

* after that initial command, the image will be locally available and can be startet with the following command:

```
docker-compose up -d
```

* this command will also launch jupyter lab at http://localhost:8888/, where all the needed code will also be available to be worked on
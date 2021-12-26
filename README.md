# sudoku-solver
python to solve sudoku

## python

* install conda with

```
 wget https://repo.anaconda.com/archive/Anaconda3-2020.11-Linux-x86_64.sh

 bash Anaconda3-2020.11-Linux-x86_64.sh
```

* after that, the following should be in .bashrc

```
# >>> conda initialize >>>
# !! Contents within this block are managed by 'conda init' !!
__conda_setup="$('~/anaconda3/bin/conda' 'shell.bash' 'hook' 2> /dev/null)"
if [ $? -eq 0 ]; then
    eval "$__conda_setup"
else
    if [ -f "~/anaconda3/etc/profile.d/conda.sh" ]; then
        . "~/anaconda3/etc/profile.d/conda.sh"
    else
        export PATH="~/anaconda3/bin:$PATH"
    fi
fi
unset __conda_setup
# <<< conda initialize <<<
```
* this could lead to conda activating automatically, which can be stopped with the following command

```
conda config --set auto_activate_base false
```

* now, create a conda env based on environment.yml and the installation dependencies in it

```
conda env create -f environment.yml
```
* the created env can now be activated or deactivated
```
conda activate <name of env in environment.yml>

conda deactivate
``` 

## docker

* docker-compose.yml provides the instructions to build a docker container based on Dockerfile
* Dockerfile includes python and all the needed dependencies seen in environment.yml
* the docker container can be built with the following command executed in the root directory of sudoku-solver (linux ubuntu):

```
docker build -f docker/Dockerfile -t sudoku-solver .
```

* after that initial command, the image will be locally available and can be started and stopped with the following commands:

```
docker-compose -f docker/docker-compose.yml up -d
docker-compose -f docker/docker-compose.yml down
```

* the first command will also launch jupyter lab at http://localhost:8888/, where all the needed code will also be available to be worked on



### Table of Contents
---------------------
- [Quick Start](#quick-start)
    + [Clone repo](#clone-repo)
    + [Goto the base directory](#goto-the-base-directory)
    + [Create virtual environment and install all required packages](#create-virtual-environment-and-install-all-required-packages)
    + [Configure environment variables](#configure-environment-variables)
    + [Run the project](#run-the-project)
    + [See project in action](#see-project-in-action)

# Before you start
----------------------------
Hello! Welcome to Access doctor PMR project. This `readme.md` file will guide you to run the project in your local machine. The section [Quick Start](#quick-start) has all the required steps to run the project.


# Quick Start
-----------------
In order to run the project, please pursue the following steps. I assume you are using `unix based operating system` and you have `python 3` installed.


#### Clone repo
--------------------
First of all, clone this git repository to your local machine. Open your terminal and run the command
```
git clone git@example.org:example/pmr.git
```

#### Goto the base directory
------------------------------------
After cloning the repo, goto the django project's base directory by executing the following command:
```
cd example_dir/
```

#### Create virtual environment and install all required packages
-----------------------------------------------------------------
Now, create a python virtual environment, activate it and install all required packages listed in `requirements.txt`. Execute the following commands to do so:
```
python3 -m venv env
source env/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

#### Configure environment variables
----------------------------------------
You are one step behind to run the project. You just need to configure the environment variables before proceeding to the final step. All env variables are provided in `.env.example` file. Create a `.env` file, copy the contents of `.env.example` and change the values according to your server's environment.

### Run the project
-------------------
There is a `run_dev.sh` file inside this directory where all neccessary commands are provided to run the project in development server. Execute the following commands to run the .sh file:
```
chmod +x ./entrypoint.sh
chmod +x ./run_dev.sh
./run_dev.sh
```
From next time, you need to run only `./run_dev.sh` command.

### See project in action
-------------------------
Congratulations! you have successfully run the project in development environment. You can access the project at `8000` port.

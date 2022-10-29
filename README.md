### Table of Contents
---------------------
- [Quick Start](#quick-start)
    + [Clone repo](#clone-repo)
    + [Goto the base directory](#goto-the-base-directory)
    + [Create virtual environment and install all required packages](#create-virtual-environment-and-install-all-required-packages)
    + [Configure environment variables](#configure-environment-variables)
    + [Run the project](#run-the-project)
    + [See project in action](#see-project-in-action)
    + [Run project using Docker](#Project-Run-using-docker)

# Before you start
----------------------------
Hello! Welcome to Access doctor Pathao test project. This `readme.md` file will guide you to run the project in your local machine. The section [Quick Start](#quick-start) has all the required steps to run the project.


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

It is expected that you have postgresql locally installed in your machine.

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

### Project Run using docker
It is expected that you have docker file and postgresql installed in your local machine. 
Before procedding to docker command please spin up postgresql locally and create a database.
After basic setup please configure the `.env` with the help of `.env.example` file. Once everything is configured properly, please proceed to execute the docker commands. 

First build the project using the following command:

```
sudo docker build . -t pathao:0.0.1
```

Once build is complete, please run the docker file using the following command:
```
sudo run -d -p 8000:8000 pathao:0.0.1
```
After successful execution of the above command will spin up the docker file and you may access the code by navigating http://127.0.0.0.1:8000 .

### Api Documentation


###### User Creation (Signup)

```End Point```: ```{base_url}/v1/user/``` <br>
```Request Method```: ```Post``` <br>
```Authorization```: ```Allowany``` <br>
```Args Example: ```
```
{
    "user_name":"test_user",
    "pin":"12345"
}
```

```Sucecessful Response: ```
```
{
    "message": "User has been successfully created"
}
```

```Unsuccessful Response: ```
```
{
    "status": 400,
    "errors": [
        {
            "field": "user_name",
            "message": "User with this User Name already exists."
        }
    ]
}
```


###### User Login Api

```End Point```: ```{base_url}/v1/user/login/``` <br>
```Request Method```: ```Post``` <br>
```Authorization```: ```Allowany``` <br>
```Args Example: ```
```
{
    "user_name":"test_user",
    "password":"12345"
}
```

```Sucecessful Response: ```
```
{
    "user_name": "test_user",
    "token": "b806b6036473ad78b52ff3a032b830b501d6c9a1",
    "user_uid": "f174893f-8dc8-41e2-b001-54472cab5d9f"
}
```

```Unsuccessful Response: ```
```
{
    "status": 403,
    "errors": [
        {
            "field": "detail",
            "message": "test_user5 is not a valid user"
        }
    ]
}
```
###### User to user wallet transfer

```End Point```: ```{base_url}/v1/user/{user_uid}/amount_transfer/``` <br>
```Request Method```: ```Path``` <br>
```Authorization```: ```Required[Send Authorization parameter in header using Token prefix. For authentication you will get token after successful login]``` <br>

```Args Example: ```
```
{
    "to_user": "test_user1",
    "amount": 2000.00,
    "transaction_type": "Debit"
}
```

```Sucecessful Response: ```
```
{
    "message": "User requested amount has been successfully transferred"
}
```

```Unsuccessful Response: ```
```
{
    "status": 400,
    "errors": [
        {
            "field": "error",
            "message": "You do not have enough amount to transfer"
        }
    ]
}
```
###### User Transaction History

```End Point```: ```{base_url}/v1/user/{user_uid}/transaction_history/``` <br>
```Authorization```: ```Required[Send Authorization parameter in header using Token prefix. For authentication you will get token after successful login]``` <br>

```Sucecessful Response: ```
```
{
    "data": [
        {
            "from_user": "test_user",
            "to_user": "test_user1",
            "transaction_type": "01e86151-ca74-48e1-b812-7a5c7148de9b",
            "transaction_date": "2022-10-29T17:29:45.738948",
            "amount": 2000.0
        },
        {
            "from_user": null,
            "to_user": "test_user",
            "transaction_type": "f4c4e598-dffe-453d-af9b-bd0f89c21ef0",
            "transaction_date": "2022-10-29T17:00:26.243589",
            "amount": 5000.0
        }
    ]
}
```

```Unsuccessful Response: ```
```
{
    "status": 404,
    "errors": [
        {
            "field": "detail",
            "message": "Not found."
        }
    ]
}
```
###### Get all user total balance

```End Point```: ```{base_url}/v1/user/all_user_balance``` <br>
```Request Method```: ```Get``` <br>
```Authorization```: ```Required[Send Authorization parameter in header using Token prefix. For authentication you will get token after successful login]``` <br>


```Sucecessful Response: ```
```
{
    "total_balance": 15000
}
```


###### Get particular user balance

```End Point```: ```{base_url}/v1/user/all_user_balance``` <br>
```Request Method```: ```Get``` <br>
```Authorization```: ```Required[Send Authorization parameter in header using Token prefix. For authentication you will get token after successful login]``` <br>


```Sucecessful Response: ```
```
{
    "amount": 3000
}
```

```Unsuccessful Response```

```
{
    "status": 401,
    "errors": [
        {
            "field": "detail",
            "message": "Invalid Token"
        }
    ]
}
```

# QuestionsAnswers

## Documentation
[Русский](https://github.com/Chukak/QuestionsAnswers/blob/master/readme_ru.md)

## Download

### Nginx + uwsgi 

You need installed nginx and uwsgi

``` sudo apt-get install nginx ```
and
``` pip install uwsgi ```

Clone this repos

``` git clone https://github.com/Chukak/QuestionsAnswers.git ```

### Without nginx and uwsgi

Clone this repos

``` git clone https://github.com/Chukak/QuestionsAnswers.git ```

## Requirements

### Create venv

Create python 3.3+ environment 

#### Ubuntu/Debian

``` sudo apt-get isntall python3-venv ```

``` python3 -m venv venv ```

``` . venv/bin/activate ``` 

Or use other envs.

### Set requirements

Go to project dir and run command

``` pip install -r requirements.txt ```

##### *If you not work with Channels - ``` pip uninstall Channels ```

## **Set up

### ***Nginx + uwsgi

Set up your nginx.conf. Example is in nginx directory, at file nginx.conf
#YOURUSERNAME edit for your name or ```www www```
Create QuestionsAnswer.com in your sites-available directory. Example is in nginx/sites-available, at file QuestionsAnswers.com.
Replace {your_path_to_app} to path to projects.


Create link in your sites-enabled directory. 

``` ln -s /etc/nginx/sites-available/QuestionsAnswers.com sites-enabled/ ```

OR

``` ln -s {your_nginx_directory}/sites-available/QuestionsAnswers.com sites-enabled/ ```


## Started

### Set migrations django
``` python manage.py makemigrations ```

``` python manage.py migrate ```

### Without nginx and uwsgi

``` python manage.py runserver ```

### Nginx + uwsgi

Nginx should be launched. In project directory run command 

``` uwsgi --ini uwsgi.ini ```



And go to localhost:8000

## Databases
In project used mysql database. Set your database in settings/development.py module. Default set slqlite3

## Notes 
* *Channels not needs for this project
* **You can use custom settings for nginx
* ***More information about [nginx+uwsgi](http://uwsgi-docs.readthedocs.io/en/latest/tutorials/Django_and_nginx.html)

## Authors 
[Chukak](https://github.com/Chukak)


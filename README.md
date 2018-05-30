# QuestionsAnswers

## Documentation
[Русский](https://github.com/Chukak/QuestionsAnswers/blob/master/readme_ru.md)

## Download

### Nginx + uwsgi 

You need to install `nginx` and `uwsgi`.

``` sudo apt-get install nginx ```

``` pip install uwsgi ```

Clone this repository

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

Run command:

``` pip install -r requirements.txt ```

## *Set up

### **Nginx + uwsgi

Set your `nginx.conf`. The example is in the nginx directory, at the file `nginx.conf`.
`#YOURUSERNAME` edit for your name or `www www`
Create `QuestionsAnswer.com` in your `sites-available` directory. The example is in the nginx/sites-available, at the file `QuestionsAnswers.com`.
Replace {your_path_to_app} to path to the project.

Create link in your `sites-enabled` directory. 

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

Run nginx. GO to the project directory, and run the command:

``` uwsgi --ini uwsgi.ini ```

And go to `localhost:8000`

## Databases
The project uses the mysql database. Set your database in the `settings/development.py` module. THe default is slqlite3

## Notes 
* *You can use custom settings for nginx
* **More information about [nginx+uwsgi](http://uwsgi-docs.readthedocs.io/en/latest/tutorials/Django_and_nginx.html)

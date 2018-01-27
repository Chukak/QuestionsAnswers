# QuestionsAnswers

## Download

### Nginx + uwsgi 

You need installed nginx and uwsgi

Вам нужен установленный nginx

``` sudo apt-get install nginx ```
and
``` pip install uwsgi ```

Clone this repos

Клонируйте репозиторий

``` git clone https://github.com/Chukak/QuestionsAnswers.git ```

### Without nginx and uwsgi

Clone this repos

Клонируйте репозиторий

``` git clone https://github.com/Chukak/QuestionsAnswers.git ```

## Requirements

Go to project dir and run command

Перейдите в папку проекта и запустите команду

``` pip install -r requirements.txt ```

##### *If you not work with Channels - ``` pip uninstall Channels ```

## **Set up

### Nginx + uwsgi

Set up your nginx.conf. Example is in nginx directory, at file nginx.conf
#YOURUSERNAME edit for your name or ```www www```
Create QuestionsAnswer.com in your sites-available directory. Example is in nginx/sites-available, at file QuestionsAnswers.com.
Replace {your_path_to_app} to path to projects.

Настройте ваш nginx.conf. Пример есть в папке nginx, в файле nginx.conf
#YOURUSERNAME замените на ваше имя или ```www www```
Создайте QuestionsAnwers.com в вашей sites-available папке. Пример есть в nginx/sites-available, в файле QuestionsAnswers.com.
Замените {your_path_to_app} на путь до проекта.


Go to nginx directory and create link in your sites-enabled directory. 

Перейдите в директории nginx и создайте линк в папке sites-enabled.

``` ln -s /etc/nginx/sites-available/QuestionsAnswers.com sites-enabled/ ```

OR

``` ln -s {your_nginx_directory}/sites-available/QuestionsAnswers.com sites-enabled/ ```


## Started

### Set up django
``` python manage.py makemigrations ```

``` python manage.py migrate ```

### Without nginx and uwsgi

``` python manage.py runserver ```

### Nginx + uwsgi

Nginx should be launched. In project directory run command 

Nginx должен быть запущен. В папке прокта запустите команду

``` uwsgi --ini uwsgi.ini ```



And go to localhost:8000

И перейдите на localhost:8000

## Databases
In project used mysql database. Set your database in settings/development.py module. Default set slqlite3

В проекте используется mysql. Установите свою базу даннных в settings/development.py module. По умолчанию slqlite3

## Notes 
* *Channels not needs for this project
* **Your can use custom settings for nginx

## Authors 
[Chukak](https://github.com/Chukak)


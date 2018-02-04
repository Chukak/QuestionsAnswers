# QuestionsAnswers

## Загрузка

### С nginx + uwsgi 

Вам нужен установленный nginx

``` sudo apt-get install nginx ```
И 
``` pip install uwsgi ```

Клонируйте репозиторий

``` git clone https://github.com/Chukak/QuestionsAnswers.git ```

### Без nginx + uwsgi

Клонируйте репозиторий

``` git clone https://github.com/Chukak/QuestionsAnswers.git ```

## Требования

### Создайте виртуальное окружение venv

Создайте виртуальное окружение Python 3.3+

#### Ubuntu/Debian

``` sudo apt-get isntall python3-venv ```

``` python3 -m venv venv ```

``` . venv/bin/activate ``` 

Или используйте другие окружения.

### Установка требований

Перейдите в папку проекта и запустите команду

``` pip install -r requirements.txt ```

##### *Если вы не работаете с Channels - ``` pip uninstall Channels ```

## **Установка

### ***С Nginx + uwsgi

Настройте ваш nginx.conf. Пример есть в папке nginx, в файле nginx.conf
#YOURUSERNAME замените на ваше имя или ```www www```
Создайте QuestionsAnwers.com в вашей sites-available папке. Пример есть в nginx/sites-available, в файле QuestionsAnswers.com.
Замените {your_path_to_app} на путь до проекта.


Создайте линк в папке sites-enabled.

``` ln -s /etc/nginx/sites-available/QuestionsAnswers.com sites-enabled/ ```

ИЛИ

``` ln -s {your_nginx_directory}/sites-available/QuestionsAnswers.com sites-enabled/ ```


## Запуск проекта

### Установите миграции django
``` python manage.py makemigrations ```

``` python manage.py migrate ```

### Без nginx + uwsgi

``` python manage.py runserver ```

### С nginx + uwsgi

Nginx должен быть запущен. В папке прокта запустите команду

``` uwsgi --ini uwsgi.ini ```



И перейдите на localhost:8000

## База данных
В проекте используется mysql. Установите свою базу даннных в settings/development.py module. По умолчанию slqlite3

## Заметки 
* *Channels не требуются для этого проекта.
* **Вы можете использовать свои настройки nginx
* ***Больше информации об [nginx+uwsgi](http://uwsgi-docs.readthedocs.io/en/latest/tutorials/Django_and_nginx.html)

## Авторы
[Chukak](https://github.com/Chukak)

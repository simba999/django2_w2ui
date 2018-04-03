- Using python3.0 ( Django 2.0 )


- create virtualenv to install dependencies.

```bash
virtualenv -p python3 venv/ 
```
- if you are using pycharm. change interpreter to that environment path. you will find that option in setting. 
- it will automatically activate that environment in terminal.
- install all dependencies with following command.

```bash
pip install -r requirements.txt
```

- run following command to run migration. Make sure you are in the same file when `manage.py` file is available.

```bash
python manage.py migrate
```

- run server

```bash
python manage.py runserver
```

- open following link. Start exploring.

[index page link](http://localhost:8000/csvread/csv_index/)
  
## Create a new directory where the project will be saved
(Or use an existing directory)

Open a terminal on your computer and run:
```bash
mkdir django-project
```

Change into the newly created directory
```bash
cd django-project
```

## If you haven't yet, install python3-venv package
Use the following command:
(For python 3)
```bash
apt-get install python-venv
```

## Setup a virtual environment
Use the following command:
```bash
python3 -m venv virtualenvnamehere

source djangoenv/bin/activate
```

## Install project requirements
```bash
pip install -r requirements.txt
```

## Migrate the database
```bash
python manage.py migrate
```

## Run the project
```bash
python manage.py runserver
```

To view the project on your browser go to: 
```bash
http://127.0.0.1:8000
```

## Contributing

Feel free to fix bugs, improve things. Just send a pull request.



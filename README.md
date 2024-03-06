An API for an envelope-based budgeting system. You can read more about the idea behind this here: [https://www.investopedia.com/envelope-budgeting-system-5208026](https://web.archive.org/web/20240124192318/https://www.investopedia.com/envelope-budgeting-system-5208026)


## Project Setup
```
git clone git@github.com:ratchek/EnvelopeBudgeting.git
cd EnvelopeBudgeting/
python3 -m venv --prompt envelopes env
source env/bin/activate
pip install -r requirements_dev.txt
./manage.py collectstatic
./manage.py migrate
./manage.py createsuperuser
./manage.py runserver
```
The site should be running on http://localhost:8000/


## Authenticating with JWT
This project uses the simple-jwt library. Here's how to authenticate requests:
https://django-rest-framework-simplejwt.readthedocs.io/en/latest/getting_started.html#usage

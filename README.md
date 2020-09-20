# DeMITer
## Installation

- Install Django on your computer (I installed via pip, see steps at: https://docs.djangoproject.com/en/3.1/intro/install/) [make sure you use Python 3]
- Clone this repository to a local drive and name it as DeMITer
- `cd` into Kore in the cloned folder as `cd DeMITer/Kore`in your Terminal/Command Line.
- Run the following commands [and run them every time you make a change - basically think of them as a refresh button]:
  - `python3 manage.py makemigrations`
  - `python3 manage.py migrate --run-syncdb`
- Run `python3 manage.py runserver` and head over to `http://127.0.0.1:8000/` to check if everything is working fine locally.




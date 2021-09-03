FROM python:3.9.0

WORKDIR /home/

RUN echo "dasfsaf"

RUN git clone https://github.com/jgw3352/jgw.git

WORKDIR /home/GIS_4_2_Web/

RUN echo "SECRET_KEY=django-insecure-+6v0ppfjmbrc9l7^w(9en#mmf#1b8w%r8yb&9lzpy_l+e4xn3h" > .env

RUN pip install -r requirements.txt

RUN python manage.py migrate

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]


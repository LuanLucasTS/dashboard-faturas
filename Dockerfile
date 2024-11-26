FROM python
WORKDIR /sistemas
RUN git clone "https://github.com/LuanLucasTS/dashboard-faturas.git"
RUN pip install --upgrade pip
RUN pip install flask
RUN pip install flask_mail
RUN pip install bcrypt
RUN pip install mysql-connector-python
RUN apt update && apt install tzdata -y
ENV TZ="America/Campo_Grande"
EXPOSE 5000
WORKDIR /sistemas/dashboard-faturas
CMD ["python", "main.py"]

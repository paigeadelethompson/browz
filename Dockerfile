FROM python
RUN apt -y update
RUN apt -y install gir1.2-webkit2-4.0 libgirepository1.0-dev intltool python3-cairo
WORKDIR /tmp/install
COPY . .
RUN python -m pip install --upgrade pip
RUN pip install flake8 pytest autoflake autopep8 build
RUN python -m build
WORKDIR / 
CMD [ "browz"]

# Какой язык программирования и версими
FROM python:latest

WORKDIR /paysistem48

# Копирует наш проект внутри папки (Docker)
COPY . /paysystem48
# скачиваем все библиотеки

#RUN pip install -r requirements.txt
#RUN pip install annotated-types
#RUN pip install anyio
#RUN pip install click
#RUN pip install colorama
#RUN pip install fastapi
#RUN pip install greenlet
RUN pip install h11
RUN pip install idna
RUN pip install pydantic
RUN pip install pydantic_core
RUN pip install PyJWT
RUN pip install sniffio
RUN pip install SQLAlchemy
RUN pip install starlette
RUN pip install typing_extensions
RUN pip install uvicorn

CMD ["uvicorn", "main:app", "--reload", "--host=0.0.0.0"]


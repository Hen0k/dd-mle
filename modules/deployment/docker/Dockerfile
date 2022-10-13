FROM python:3.10

COPY mle/mle_package /mle/mle_package
RUN pip install /mle/mle_package

COPY ds/ds_package /ds/ds_package
RUN pip install /ds/ds_package


COPY /deployment/api  /api
RUN pip install Flask
WORKDIR /api 

CMD ["flask", "run", "--host=0.0.0.0"]
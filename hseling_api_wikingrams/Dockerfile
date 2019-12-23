FROM hseling/hseling-api-base:python3.6-alpine3.7 as build

LABEL maintainer="Anna Nikolaeva <info@linghub.ru>"

RUN mkdir /dependencies
COPY ./hseling_api_wikingrams/requirements.txt /dependencies/requirements.txt
COPY ./hseling_api_wikingrams/setup.py /dependencies/setup.py

RUN pip install -r /dependencies/requirements.txt

FROM hseling/hseling-api-base:python3.6-alpine3.7 as production

COPY --from=build /usr/local/lib/python3.6/site-packages /usr/local/lib/python3.6/site-packages
COPY --from=build /usr/lib/python3.6/site-packages /usr/lib/python3.6/site-packages

COPY --from=build /dependencies /dependencies

COPY ./hseling_lib_wikingrams /dependencies/hseling_lib_wikingrams
RUN pip install /dependencies/hseling_lib_wikingrams

COPY ./hseling_api_wikingrams/hseling_api_wikingrams /app/hseling_api_wikingrams
COPY ./hseling_api_wikingrams/main.py /app/main.py

ENV HSELING_API_WIKINGRAMS_SETTINGS="/app/hseling_api_wikingrams/default_settings.py"

HEALTHCHECK CMD curl --fail http://localhost/healthz || exit 1

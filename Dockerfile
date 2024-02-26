FROM python:3.11-slim-bullseye

# Upgrade pip
RUN python -m pip install --upgrade pip

COPY requirements.txt /tmp/pip-tmp/
COPY dist /tmp/dist

RUN pip3 --disable-pip-version-check --no-cache-dir install \
    -r /tmp/pip-tmp/requirements.txt /tmp/dist/topn-0.0.1-py3-none-any.whl\
    && rm -rf /tmp/pip-tmp

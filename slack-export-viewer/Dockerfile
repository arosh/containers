FROM nginx/unit:1.27.0-python3.10

RUN apt-get update \
  && apt-get upgrade -y \
  && apt-get install -y --no-install-recommends \
    python3-pip \
  && pip3 install slack-export-viewer \
  && apt-get purge -y --autoremove python3-pip \
  && rm -rf /var/lib/apt/lists/*

COPY start.py /www/
COPY config /docker-entrypoint.d/

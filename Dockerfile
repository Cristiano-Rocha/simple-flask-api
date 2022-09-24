FROM python-3.10-slim@sha256:6de22c9cf887098265b7614582b00641c0c8c6735af538d0f267d6bb457634f1 AS python
ENV PYTHONUNBUFFERED=true
WORKDIR /app

FROM python AS poetry
ENV POETRY_HOME=/opt/poetry
ENV POETRY_VIRTUALENVS_IN_PROJECT=true
ENV PATH="$POETRY_HOME/bin:$PATH"
RUN python -c 'from urllib.request import urlopen;print((urlopen("https://install.python-poetry.org").read().decode()))' | python -
COPY . ./
RUN poetry install --no-interaction --no-cache --without dev -vvv --no-root

FROM poetry AS runtime
ENV PATH="/app/.venv/bin:$PATH"
COPY --from=poetry /app /app
ENTRYPOINT ["poetry","run"]
CMD ["flask","run","--host=0.0.0.0"]



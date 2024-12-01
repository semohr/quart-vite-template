FROM python:3.11-alpine AS base

FROM base AS deps

RUN addgroup -g 1000 appuser && \
    adduser -D -u 1000 -G appuser appuser


# map beets directory and our configs to /config
RUN mkdir -p /config/
RUN chown -R appuser:appuser /config

# dependencies
RUN --mount=type=cache,target=/var/cache/apk \
    apk update
RUN --mount=type=cache,target=/var/cache/apk \
    apk add \
    redis  \
    git \
    bash \
    npm \
    shadow

# Install our package (server)
COPY ./backend /repo/backend
COPY ./README.md /repo/README.md
WORKDIR /repo/backend
RUN --mount=type=cache,target=/root/.cache/pip \
    pip install .

# Install frontend
RUN corepack enable && corepack prepare pnpm@9.x.x --activate

# ------------------------------------------------------------------------------------ #
#                                      Development                                     #
# ------------------------------------------------------------------------------------ #

FROM deps AS dev

# relies on mounting this volume
WORKDIR /repo/docker
USER root
ENTRYPOINT ["/bin/sh", "-c", "./entrypoint.permissions.sh && su appuser -c ./entrypoint.dev.sh"]

# ------------------------------------------------------------------------------------ #
#                                      Production                                      #
# ------------------------------------------------------------------------------------ #

FROM deps AS build

COPY --from=deps /repo /repo

WORKDIR /repo
COPY ./frontend ./frontend/
RUN chown -R appuser:appuser /repo

USER appuser
WORKDIR /repo/frontend
RUN --mount=type=cache,id=pnpm-store,target=/root/.local/share/pnpm/store \
    pnpm install
RUN pnpm run build

# ------------------------------------------------------------------------------------ #

FROM deps AS prod

ENV IB_SERVER_CONFIG="prod"

WORKDIR /repo
COPY --from=deps /repo /repo
COPY --from=build /repo/frontend/dist /repo/frontend/dist
COPY ./docker/entrypoint.prod.sh .
COPY ./docker/entrypoint.permissions.sh .
RUN chown -R appuser:appuser /repo

WORKDIR /repo/docker
USER root
ENTRYPOINT ["/bin/sh", "-c", "./docker/entrypoint.permissions.sh && su appuser -c ./docker/entrypoint.prod.sh"]

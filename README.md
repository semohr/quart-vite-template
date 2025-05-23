# Quart & Vite template

This template is designed to provide a starting point for building web applications with Vite and Quart. It includes a basic project structure, configuration, and example code to help you get started.

```sh
gh repo create <new-repo-name> --template=semohr/quart-vite-template
```

**(Work in progress)**

## Features

- Python
    - Hosting vite files
    - Logging
    - Testing
    - Redis
- Javascript
    - Vite
- Docker
    - Dev environment 
    - Production environment
- Workflows

## The template in-depth

### Frontend (vite)

We include a [vite] app in the `frontend` folder using (?framework?).This app is a basic example of a web application with a single page and a few components.

**Included libraries:**

- [typescript] for type-checked javascript 
- [eslint] for linting, formatting and enforcing code style
- [vitest] for testing

### Backend Server (quart)

The server application is located in the `backend` folder. It is a basic [quart] app which serves the frontend app and has some exemplary endpoints. 

**Included libraries:**

- [ruff] for linting, formatting and enforcing common python code style
- [pytest] for testing

### Containerization (docker)

This template includes Docker images for development and production. The `docker` folder includes a Dockerfile with multi-stage builds for both environments. Feel free to edit it if you need to add dependencies or change the configuration.

We include two docker-compose files, one for development and one for production. The development file mounts the project directory into the container, so you can use hot-reloading and other development features. The production file runs a minimal container with the compiled assets.

```bash
# Development
docker-compose -f docker/docker-compose.dev.yml up
# Production
docker-compose -f docker/docker-compose.prod.yml up
```

### Workflows

We include a few common workflows to ensure code quality and consistency from the start!

**`.github/workflows/backend.yml`**

This workflow runs whenever a file in the `backend` folder is modified. It runs [ruff] to check for linting errors and runs all python tests with [pytest].


### Renaming the python package

Currently, we simply call the template python "package".
This is hard coded in several places, and needs to be replaced:

```
/backend/package/ # folder name
/backend/package/redis/launch_redis_workers.py
/backend/package/pyporject.toml # multiple times
/docker/entrypoint.*.sh
```

### TODOs:

- Add starter configuration (via classes) for quart
- Add tests for frontend route 
- Test Docker production setup
- Vitest setup

[ruff]: https://docs.astral.sh/ruff/
[pytest]: https://docs.pytest.org/
[typescript]: https://www.typescriptlang.org/
[vite]: https://vitest.dev/
[eslint]: https://eslint.org/

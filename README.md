# Quart & Vite template

An opinionated template for building web applications with [Vite](https://vitejs.dev/) and hosting them with [Quart](https://github.com/pallets/quart).

This template is designed to provide a starting point for building web applications with Vite and Quart. It includes a basic project structure, configuration, and example code to help you get started.

**(Work in progress)**

## Features

- Docker images for development and production included
- Scripts for common actions, like creating a new python package

## The template in-depth

### Frontend (vite)

We include a vite app in the `frontend` folder. This app is a basic example of a web application with a single page and a few components.

**Included libraries:**

- [typescript](https://www.typescriptlang.org/) for type-checking
- [eslint](https://eslint.org/) for linting, formatting and enforcing code style
- [vitest](https://vitest.dev/) for testing

### Server (quart)

The server application is located in the `server` folder. It is a basic Quart app with a single route that serves the frontend app and some example endpoints. The server is configured to serve the frontend app from the `frontend/dist` folder.

**Included libraries:**

- [ruff](https://docs.astral.sh/ruff/) for linting, formatting and enforcing code style
- [pytest](https://docs.pytest.org/en/6.2.x/) for testing

### Docker

This template includes Docker images for development and production. The `docker` folder includes a Dockerfile with multi-stage builds for both environments. Feel free to edit it if you need to add dependencies or change the configuration.

We include two docker-compose files, one for development and one for production. The development file mounts the project directory into the container, so you can use hot-reloading and other development features. The production file runs a minimal container with the compiled assets.

```bash
# Development
docker-compose -f docker/docker-compose.dev.yml up
# Production
docker-compose -f docker/docker-compose.prod.yml up
```


### Workflows

We include a few common workflows to ensure code quality and consistency from the start.

**`.github/workflows/python.yml`**

This workflow runs whenever a file in the `server` folder is modified. It runs [ruff]() to check for linting errors and runs the tests defined in the `server/tests` folder.

**`.github/workflows/frontend.yml`**

This workflow runs whenever a file in the `frontend` folder is modified. It runs [eslint]() to check for linting errors and runs the tests defined in the `frontend/tests` folder.


### TODOs:

Docker setup
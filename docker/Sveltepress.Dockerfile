FROM node:22-slim

WORKDIR /app

# install dependencies
RUN apt-get update && apt-get install -y git

# Use the official Node.js 16 image as the base image
FROM node:latest AS build

# Set the working directory in the container
WORKDIR /app

# Copy the package.json and package-lock.json files to the container
COPY package*.json ./

# Install the dependencies
RUN npm install -g npm@latest

# Copy the source code to the container
COPY . .

# Build the React app
RUN npm run build

COPY build /app/build

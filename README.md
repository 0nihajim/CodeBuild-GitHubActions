# Q Dev App

A lightweight development application built with Alpine Linux for testing and development purposes.

## Overview

Q Dev App is a minimalist development environment designed for quick testing and prototyping. It provides a clean Alpine Linux environment that can be easily extended with additional tools and dependencies as needed.

## Features

- Lightweight Alpine Linux base
- Fast startup and minimal resource usage
- Easily customizable for different development needs
- Suitable for CI/CD pipelines and local testing
- README summarization functionality

## Getting Started

### Prerequisites

- Docker installed on your system
- Git for cloning the repository

### Installation

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/q-dev-app.git
   cd q-dev-app
   ```

2. Build the Docker image:
   ```
   docker build -t q-dev-app .
   ```

3. Run the container:
   ```
   docker run -it q-dev-app
   ```

## Running the Application

The Q Dev App includes a simple Python application that you can run:

```
docker run -it q-dev-app python3 /app/app.py
```

This will start an interactive demo application.

### Summarizing README.md

To get a summary of the README.md file, run:

```
docker run -it q-dev-app python3 /app/app.py --summarize-readme
```

This will display a concise summary of the README.md file, highlighting the key features and purpose of the application.

## Testing

### Running Tests

```
docker run q-dev-app /bin/sh -c "run-tests"
```

### Test Environment

The test environment uses Alpine's package manager to install any required testing dependencies. You can customize the test environment by modifying the Dockerfile.

### Test Reports

Test results are output to the console by default. For CI/CD integration, you can modify the test commands to generate reports in various formats (JUnit, etc.).

## Customization

You can customize the Q Dev App by modifying the Dockerfile to include additional packages or configuration:

```dockerfile
FROM alpine:latest

# Install additional packages
RUN apk add --no-cache \
    python3 \
    nodejs \
    npm

# Add your custom configuration here
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
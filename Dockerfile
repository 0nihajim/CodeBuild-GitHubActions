FROM alpine:latest

# Install basic utilities and testing tools
RUN apk add --no-cache \
    bash \
    curl \
    python3 \
    py3-pip \
    jq

# Set up working directory
WORKDIR /app

# Copy application files
COPY . /app/

# Make test script executable and move it to path
RUN chmod +x /app/test.sh && \
    ln -s /app/test.sh /usr/local/bin/run-tests

# Default command
CMD ["/bin/sh"]

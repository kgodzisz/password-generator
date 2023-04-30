FROM alpine

# Install Python and pip
RUN apk add --no-cache python3 py3-pip

# Install cryptography library
RUN apk add --no-cache libffi-dev python3-dev openssl-dev gcc musl-dev
RUN pip3 install cryptography

# Copy password generator script
COPY password_generator.py /

# Generate and print a password using the chosen algorithm
ENTRYPOINT ["python3", "/password_generator.py"]
# Use a more specific version of the Python base image
FROM python:3

# Grab our web interface executable
COPY --from=ceramicwhite/gotty --chmod=+x /usr/bin/gotty /bin/gotty

# Set working directory
WORKDIR /usr/src/app

# Set environment variables
ENV REPO_URL=
ENV REPO_BRANCH=
ENV OPENAI_API_KEY=
ENV USE_DOCKER=True

# Copy requirements.txt and install dependencies
COPY requirements.txt ./
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application
COPY . .

# Copy and make executable the postinstall scripts
COPY --chmod=+x entrypoint.sh /usr/src/app/entrypoint.sh

# Declare the port for exposing web server
EXPOSE 3000

# Set the ENTRYPOINT for the container
ENTRYPOINT ["/usr/src/app/entrypoint.sh"]


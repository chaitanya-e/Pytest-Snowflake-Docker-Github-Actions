FROM python:3.7.7 as base

# Installations
RUN pip install snowflake-connector-python  && \
pip install pytest && \
pip install pytest-html 

# Code Copy
COPY . /app/
WORKDIR /app/tests

# Copy the entrypoint script into the container and make it executable
COPY entrypoint.sh /usr/local/bin/entrypoint.sh
RUN chmod +x /usr/local/bin/entrypoint.sh

# Expose port 8080 for dbt docs serve
EXPOSE 8000

# Set the entrypoint script
ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]

# Default command if no other command is specified when the container is run
CMD ["py.test", "--version"]  # This can be changed to any dbt command you commonly used
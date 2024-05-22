#!/bin/bash

# Function to start the HTTP server
start_http_server() {
    cd /app/tests
    python3 -m http.server 8000
}

# Navigate to the tests directory
cd /app/tests

# Run pytest and capture the exit status
pytest --html=report.html
TEST_EXIT_STATUS=$?

# Start the HTTP server regardless of the pytest exit status
start_http_server &

# Wait for background processes to finish
wait
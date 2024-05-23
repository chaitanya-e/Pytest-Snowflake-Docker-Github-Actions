#  Project Description

The repository includes a /tests/ directory that contains pytest tests. These tests connect to a specific snowflake database and perform validations
The project is dockerized therefore the entrypoint.sh, dockerfile and docker-compose files include commands to execute the code on docker containers

## Setup

### Prerequisites
- Python 3.7.7 or higher
- pip

### Steps

1. Clone the repository:
    ```sh
    git clone <repository_url>
    cd <repository_directory>
    ```

2. Create a virtual environment:
    ```sh
    python -m venv venv
    ```

3. Activate the virtual environment:
    - On Windows:
      ```sh
      venv\Scripts\activate
      ```
    - On macOS/Linux:
      ```sh
      source venv/bin/activate
      ```

4. Install the dependencies:
    ```sh
    pip install -r requirements.txt
    ```

5. Run the application or tests:
    ```sh
    # Example for running tests
    pytest
    ```

### Using Docker

If you are using Docker, the `requirements.txt` is generally used to ensure that local development environments are consistent. However, your Docker setup should take care of dependencies as described in the Dockerfile. Here's how you can run your application or tests using Docker:

```markdown
## Running with Docker

1. Build the Docker image:
    ```sh
    docker build -t <image_name> .
    ```

2. Run the Docker container:
    ```sh
    docker run -it <image_name>
    ```

3. If using `docker-compose`:
    ```sh
    docker-compose up --build
    ```

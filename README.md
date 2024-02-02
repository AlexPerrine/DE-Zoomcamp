# Data Engineering Zoomcamp

This is a self paced free course to teach the basics of data engineering as well as some of mainstream tools and some tools that are new to the world. The course has 6 different modules and a self project at the end of the course. 

<img src='arch_v3_workshops.png' alt="Data Engineering Zoomcamp course path" width=auto height="500"></a>

### Module 1: Introduction, Containerization and Infrastructure as Code
This was a 2 week module, mostly because of introductions to the course, environment setup, homework and a mini project. I learned the basics of setting up a Docker container with Python injecting data into a PostgreSQL. To analyze the data in the database, I used docker compose to get all the data into the database and into the pgAdmin GUI.

Topics I learned:
    - Used pgcli to connect to the database
    - Using the terminal
      - Converted a Jupyter Notebook into a Python script.
      - Running multiple containers with docker-compose up
    - Python
      - Collected command line arguments using the argparse library
      - wget: to retrieve a CSV from the web using the command line
      - Used sqlAlchemy to create an engine and for ingestion into Postgres
      - While loops and exception handling.
# Data Engineering Zoomcamp

This is a self paced free course to teach the basics of data engineering as well as some of mainstream tools and some tools that are new to the world. The course has 6 different modules and a self project at the end of the course. 

<img src='https://github.com/DataTalksClub/data-engineering-zoomcamp/blob/main/images/architecture/arch_v3_workshops.jpg' alt="Data Engineering Zoomcamp course path" width=auto></a>

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

### Module 2: Orchestration: MageAi
Data orchestration is automating the process of taking data from many different stored locations (cloud, warehouse, csv file, etc.) and performing transformations to make it available to the end user for analysis.

<a href="https://www.mage.ai/">Mage</a> is a modern open source data pipeline tool for transforming and integration data. It allows you to integrate and synchronize data, build real-time and batch pipelines and run, monitor and orchestrate pipelines. As what their website says it "gives your data team magical powers." I felt like I was back in college playing my wizard character in D&D from the powers given.

<img src='https://www.mage.ai/_next/image?url=https%3A%2F%2Fmedia.graphassets.com%2FhuPjUkFSFGZKWns7yByr&w=3840&q=75' alt="MageAi blog image" width=auto></a>

I built a pipeline that took in several csv files and performed some transformations then dropped 96 differnt parquet files based on pickup date into Google Cloud Storage and set a schedule all in the matter of minutes. Mage allows this by what they call "blocks" which there are different types, for example: data loader, transformer and exporter, with predefined and editable code in many different languages. 

Topics I learned:
  - Orchestration
  - MageAi (Data Loader, Transformations, Data Exporters, Schedulers)
  - Relearned basic RegEx to go from camelCase to snake_case
  - Google Cloud Storage
  - Parquet files
  - Pyarrow
    - Loaded a dataframe to Google Cloud Storage in parquet files based on a date
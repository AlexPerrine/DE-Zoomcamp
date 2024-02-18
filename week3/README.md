# Week 3 - Data Warehouse

## Summary
This week I learned about data warehouses, and specifically using Google Cloud Storage and Google BigQuery. The work done this week was to take the green taxi data from the NYC trip record data for 2022 in a parquet file format, use Mage to orchestrate the data into Google Cloud Storage and then Google BigQuery. I didn't do any cleaning to the data besides changing the data types. But in practice this would completed before exporting into Google Cloud Storage.

### Data Warehouse
A **data warehouse** is a centralized repository that stores large vaolumes of data from multiple sources, organized for query and analysis to support decision making processes.

### OLAP v. OLTP
There are 2 different database artchitectures that help us store and analyze data OLAP (Online Analytical Processing) and OLTP (Online Transactional Processing)

|| OLAP | OLTP |
| ------------- | ------------- | ------------- |
| Purpose | Facilitate complex queries for BI and decision making  | Efficiently manage daily transactional data through quick and reliable processing  |
| Data Source | Historical and aggregated data  | Real-time and transactional data  |
| Operations | Based on SELECT commands to aaggregate for reporting  | Based on INSERT, UPDATE and DELETE commands  |
| Updates | Data periodically refreshed with scheduled, long running batches  | Short, fast and initiated by user  |
| Design | Denormalized for analysis  | Normalized for efficiency  |
| Examples | Redshift, BigQuery, Snowflake  | MySQL, PostgreSQL  |

### Partitioning v. Clustering

#### Partitions
Partitioning a table improves query performance and helps control costs by reducing the number of bytes read by each query. In a partitioned table, data is stored in blocks each holding one partition. You can partition a table by a specific column, typically a date column, for example order date.

#### Clustering
Clustering tables are tables that have a user defined column sort order. This is important as clustering determines sort order. Typically non-data fields, for example programming language.
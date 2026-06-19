# EIA Electricity ETL Pipeline

## Overview

This project is an end-to-end ETL pipeline that extracts electricity generation data from the U.S. Energy Information Administration (EIA) API, processes it in Python, and loads it into a PostgreSQL database for downstream SQL analysis.

## Data Source

* EIA API: Daily electricity generation by fuel type (ERCOT region)

## Pipeline Flow

1. Extract data from EIA API using Python (requests)
2. Normalize and transform JSON response into tabular format (pandas)
3. Load structured data into PostgreSQL (SQLAlchemy)
4. Run SQL queries for validation and analysis (aggregation, window functions)

## Data Quality Checks

* Schema enforcement (typed columns in Postgres)
* Basic validation of extracted record counts
* Null and type consistency checks during transformation

## Tech Stack

* Python (ETL logic)
* Pandas (transformation)
* PostgreSQL (storage)
* SQLAlchemy (database connection)
* SQL (analysis layer)

## Purpose

The goal is to demonstrate a production-style ETL workflow with clear separation between ingestion, transformation, storage, and analytical querying using real-world energy data.

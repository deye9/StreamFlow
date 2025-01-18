# StreamFlow

StreamFlow is a real-time data streaming pipeline designed to ingest, process, and analyze data. It leverages **Apache Kafka** for message streaming, **Spark Streaming** for processing, and **Elasticsearch** for data indexing and querying.

## Features
- Real-time data ingestion from Kafka.
- Scalable data processing with Spark Streaming.
- Efficient indexing and querying using Elasticsearch.
- Modular design following the Hexagonal Architecture.
- Dockerized setup for seamless development and deployment.

---

## Architecture Overview

StreamFlow is built using the **Hexagonal Architecture** to ensure scalability, maintainability, and testability.

- **Domain Layer**: Contains the core business logic (e.g., Tweet processing).
- **Application Layer**: Manages input (Kafka) and output (Elasticsearch).
- **Infrastructure Layer**: Handles integrations with external systems (Kafka, Elasticsearch).

---

## Getting Started

### Prerequisites
- **Docker**: Install [Docker](https://www.docker.com/).
- **Python 3.8+**: Install [Python](https://www.python.org/).
- **Kafka**: Dockerized.
- **Elasticsearch**: Dockerized.

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/streamflow.git
   cd streamflow

#  Flask + Kafka Microservice

This is a Python microservice built with **Flask**, designed to:

- Expose REST endpoints for mathematical operations (`/factorial`, `/fibonacci`, `/pow`)
- Store each incoming request in a **SQLite** database
- Send request data and operational logs to **Kafka** topics (`requests`, `logs`)
- Monitor system resource usage using **psutil**

---

##  Features

-  RESTful API with Flask
-  Request persistence using SQLite
-  Kafka integration for event streaming
-  Asynchronous logging via Kafka (`logs` topic)
-  Real-time system monitoring (CPU, memory, disk, network)
-  In-memory caching using `@lru_cache`
-  Fully containerized with Docker and orchestrated via Docker Compose
-  Unit-tested core logic with `unittest`

---



##  Available API Endpoints

| Method | Endpoint        | Description                              |
|--------|------------------|------------------------------------------|
| POST   | `/factorial`     | Input: `{ "n": 5 }` → Output: `120`      |
| POST   | `/fibonacci`     | Input: `{ "n": 10 }` → Output: `55`      |
| POST   | `/pow`           | Input: `{ "number": 2, "pow": 3 }` → `8` |
| GET    | `/requests`      | Returns all requests stored in DB        |

---

##  Unit Testing

Run unit tests with:

```bash
python -m unittest test_functions.py
```

---

##  Running the App with Docker

### Build and start all services:

```bash
docker compose up --build
```

### Run the Kafka consumer separately:

```bash
docker compose up consumer
```

Or manually:

```bash
docker compose exec app python consumer.py
```

---

##  Technologies Used

- **Python 3.11**
- **Flask**
- **Kafka + Zookeeper** (`confluentinc/cp-kafka`)
- **SQLite** (via SQLAlchemy)
- **Docker / Docker Compose**
- **psutil** (system monitoring)
- **unittest** (testing)

---

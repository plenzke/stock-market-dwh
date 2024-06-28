## Data Team

Data Pipeline for currency, cryptocurrency and stock prices with data marts visualization. 

### Stack

| Technology  | Purpose                                             |
|-------------|-----------------------------------------------------|
| Airflow	    | Оркестрация процессов загрузки сырых данных из API  |
| PostgreSQL  | База данных для Data Lake                           |
| dbt         | Трансформация данных в Data Lake                    |
| Debezium	   | Сбор измененных данных для загрузки в ClickHouse    |
| Kafka	      | Потоковая загрузка данных из Data Lake в ClickHouse |
| ClickHouse	 | База данных для витрин данных                       |
| Superset	   | Визуализация витрин данных                          |
| Docker	     | Контейнеризация и сборка проекта                    |


### Data Pipeline Scheme

![Stock Market Data Pipeline Scheme](https://github.com/plenzke/stock-market-dwh/assets/47403764/b813a427-61ad-40cd-b724-d2fc29e50f03)

> **Note:** This project has been created for educational purposes only.

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


> **Note:** This project has been created for educational purposes only.

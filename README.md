# ETL Project #
## Overview ##
_In this project, where a dataset from AIRBNB from Kaggle is used, 
which gives us certain interesting variables from which decisions can be made based on the analysis and management of the data._

## Table of Contents ##
- [Requirements](#requirements)
- [Setup](#setup)
- [Data EDA](#data-eda)
- [Airflow DAG](#airflow-dag)
- [Visualizations](#analysis-visualizations)

## Requirements <a name="requirements"></a> ##
- Python 3.x
- SQLAlchemy
- Matplotlib & Seaborn
- Pandas & Numpy
- MySQL Workbench
- **[Data](https://github.com/RJuanJo/etl-project/tree/main/data)**
- Docker
- Docker Compose
- JSON credentials file ("credentials.json") with this format:
  
  ```
  {   
    "host" : "host",
    "user" : "your_user",
    "password" : "your_password",
    "database" : "database_name"
    "port" : "port_of_your_mysql_server"
  }
  ``` 
## Setup <a name="setup"></a> ##
_First of all, 
ensure you have the following programs installed with which the entire project procedure is carried out:_

   - **[Python](https://www.python.org)**
   - **[MySQL](https://www.mysql.com/downloads/)**
   - **[PowerBI](https://powerbi.microsoft.com/es-es/downloads/)**
   - **[VS Code](https://code.visualstudio.com/download)** or **[Jupyter](https://jupyter.org/install)**
   - **[Docker](https://www.docker.com/products/docker-desktop/)**

Using the **[requirements.txt](https://github.com/RJuanJo/etl-project/blob/main/config/requirements.txt)**
run the following command in the root of the project into a terminal shell to install all necessary libraries

```python
pip install -r config\requirements.txt
```

## Data EDA <a name="data-eda"></a> ##
 
 _This process was carried out in **[InitalData EDA Notebook](https://github.com/RJuanJo/etl-project/blob/main/notebooks/InitialDataEDA.ipynb)** where the following procedures are being carried out:_

- Identification of null data
- Identification of outliers
- Imputation of Nulls
- Handling of outliers
- Exploratory Data Analysis (EDA)

_Additionally, **[API EDA Notebook](https://github.com/RJuanJo/etl-project/blob/main/notebooks/ApiEDA.ipynb)** is responsible for analyzing the data obtained from the API._

## Airflow DAG <a name="airflow-dag"></a> ###

In this process, after obtaining a considerable amount of information through EDA, a DAG is created to handle the entire data ETL process. To do this, is needed to initialize the environment, so run the following command in a command shell at the root of the project:

```bash
docker-compose up airflow-init
```

Then, to start the containers, use the following command:

```bash
docker-compose up
```

Finally, go to http://localhost:8080/ and log in with the credentials `airflow` and `airflow`. 

In the Airflow interface, search for the DAG "project-dag", activate it, select it, and click on "Trigger" to begin the ETL process.

## Analysis & Visualization <a name="analysis-visualizations"></a> ###

### These visualizations can be seen in the **[Initial Dashboard](https://github.com/RJuanJo/etl-project/blob/main/data/documentation/ProJectDB.pdf)** and **[API Dashboard](https://github.com/RJuanJo/etl-project/blob/main/data/documentation/ProjectApiDB.pdf)**.
### Also, threre is the **[Virtual Dashboard](https://app.powerbi.com/view?r=eyJrIjoiODRkOTQxZWYtNTAxOC00OTMyLWJjMGUtNzVjODFmYzNjNGY0IiwidCI6IjY5M2NiZWEwLTRlZjktNDI1NC04OTc3LTc2ZTA1Y2I1ZjU1NiIsImMiOjR9)** without API data and there's the **[API-Data Dashboard](https://app.powerbi.com/view?r=eyJrIjoiZmRhM2IxMmEtMTViZi00ZTlhLWE0MTEtZTRjY2M4OTNjM2M3IiwidCI6IjY5M2NiZWEwLTRlZjktNDI1NC04OTc3LTc2ZTA1Y2I1ZjU1NiIsImMiOjR9)** for a better interactive experience and a greater display of the data.

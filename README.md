# ETL Project #
## Overview ##
_In this project, where a dataset from AIRBNB from Kaggle is used, 
which gives us certain interesting variables from which decisions can be made based on the analysis and management of the data._

_Also, *[Detailed Documentation](https://github.com/RJuanJo/etl-project/blob/main/data/documentation/Report%20ETL%20Project.pdf)* is available that covers everything from data selection to the final visualizations_

## Table of Contents ##
- [Requirements](#requirements)
- [Setup](#setup)
- [Data Treatment](#data-treatment)
- [Data Uploading](#data-uploading)
- [Analysis & Visualizations](#analysis-visualizations)

## Requirements <a name="requirements"></a> ##
- Python 3.x
- SQLAlchemy
- Matplotlib & Seaborn
- Pandas & Numpy
- MySQL Workbench
- **[Data](https://github.com/RJuanJo/etl-project/tree/main/data)**
_where the selected files are located with which the treatment and subsequently the analysis will be carried out_
- JSON credentials file ("credentials.json") with this format:
  
  ```
  {   
    "host" : "host",
    "user" : "your_user",
    "password" : "your_password",
    "database" : "database_name"
  }
  ``` 
## Setup <a name="setup"></a> ##
_First of all, 
ensure you have the following programs installed with which the entire project procedure is carried out:_

   - **[Python](https://www.python.org)**
   - **[MySQL](https://www.mysql.com/downloads/)**
   - **[PowerBI](https://powerbi.microsoft.com/es-es/downloads/)**
   - **[VS Code](https://code.visualstudio.com/download)** or **[Jupyter](https://jupyter.org/install)**

_Using the **[requirements.txt](https://github.com/RJuanJo/etl-project/blob/main/config/requirements.txt)**
run the following command in the root of the project into a terminal shell to install all necessary libraries

```python
pip install -r config\requirements.txt
```
_Previous command will install the following necessary libraries for the project_

```python
- pip
- seaborn
- matplotlib
- numpy
- pandas
- mysql
- sqlalchemy
- sqlalchemy-utils
- mysqlclient
- mysql.connector
```
## Data Treatment <a name="data-treatment"></a> ##
 
 _This process was carried out in **[First Notebook](https://github.com/RJuanJo/etl-project/blob/main/notebooks/project_eda.ipynb)** where the following procedures are being carried out:_

- Identification of null data
- Identification of outliers
- Imputation of Nulls
- Handling of outliers
- Exploratory Data Analysis (EDA)

## Data Uploading <a name="data-uploading"></a> ##

 _This process was carried out in **[Second Notebook](https://github.com/RJuanJo/etl-project/blob/main/notebooks/conection.ipynb)** where a connection to the MySQL database engine is established, 
 once the connection is made, the database with its respective table will be created where the 
 **[Processed Data](https://github.com/RJuanJo/etl-project/tree/main/data/processed_data/clean_data.csv)** will be stored._

## Analysis & Visualization <a name="analysis-visualizations"></a> ###

### These visualizations can be seen in the **[Dashboard Summary](https://github.com/RJuanJo/etl-project/blob/main/data/documentation/ProJectDB.pdf)**.
### Also, threre is the **[Virtual Dashboard](https://app.powerbi.com/view?r=eyJrIjoiODRkOTQxZWYtNTAxOC00OTMyLWJjMGUtNzVjODFmYzNjNGY0IiwidCI6IjY5M2NiZWEwLTRlZjktNDI1NC04OTc3LTc2ZTA1Y2I1ZjU1NiIsImMiOjR9)** for a better interactive experience and a greater display of the data.

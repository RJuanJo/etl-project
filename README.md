# ETL Project #
## Overview ##
_In this project, where a dataset from AIRBNB from Kaggle is used, 
which gives us certain interesting variables from which decisions can be made based on the analysis and management of the data._

## Table of Contents ##
- [Requirements](#requirements)
- [Setup](#setup)
- [Data Treatment](#data-treatment)
- [API Data](#API-data) 
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
- requests
```
## Data Treatment <a name="data-treatment"></a> ##
 
 _This process was carried out in **[InitalData EDA Notebook](https://github.com/RJuanJo/etl-project/blob/main/notebooks/InitialDataEDA.ipynb)** where the following procedures are being carried out:_

- Identification of null data
- Identification of outliers
- Imputation of Nulls
- Handling of outliers
- Exploratory Data Analysis (EDA)

_Additionally, **[API EDA Notebook](https://github.com/RJuanJo/etl-project/blob/main/notebooks/ApiEDA.ipynb)** is responsible for analyzing the data obtained from the API._

## API Data <a name="api-data"></a> ##

_In this process, access to an API called **[Apify](https://apify.com/?fpr=i6ouv&gad_source=1&gclid=CjwKCAjwrIixBhBbEiwACEqDJbE9W4hFRbrlWXlb9IpnMuG9xc3Cl0e_F5o-vh5WW26-PH7cRg3LDxoCx3wQAvD_BwE)** is achieved, which was very helpful in bringing in more data to complement our previous data._ 

_The management of the API data is located in the **[Api folder](https://github.com/RJuanJo/etl-project/tree/main/Api)** and is divided into two parts:_

_- The first part is carried out in **[Extracting Data](https://github.com/RJuanJo/etl-project/blob/main/Api/Apiextraction.py)**, which establishes the connection and retrieves the data obtained from the API._

_- The second part is located at **[ApiFusion](https://github.com/RJuanJo/etl-project/blob/main/Api/ApiFusion.py)**, which is responsible for combining and unifying all the data obtained into one, to facilitate the management of this data later on._

## Data Uploading <a name="data-uploading"></a> ##

 _This process was carried out in **[InitialDataLoading Notebook](https://github.com/RJuanJo/etl-project/blob/main/notebooks/InitialDataLoading.ipynb)** where a connection to the MySQL database engine is established, 
 once the connection is made, the database with its respective table will be created where the processed data will be stored._

-_Finally, a merge is performed in **[MergingData Notebook](https://github.com/RJuanJo/etl-project/blob/main/notebooks/MergingData.ipynb)** where the initially obtained data is combined with the data extracted from the API, and is finally stored in a new table with all the previously processed data within the same notebook in the database._

## Analysis & Visualization <a name="analysis-visualizations"></a> ###

### These visualizations can be seen in the **[Initial Dashboard](https://github.com/RJuanJo/etl-project/blob/main/data/documentation/ProJectDB.pdf)** and **[API Dashboard](https://github.com/RJuanJo/etl-project/blob/main/data/documentation/ProjectApiDB.pdf)**.
### Also, threre is the **[Virtual Dashboard](https://app.powerbi.com/view?r=eyJrIjoiODRkOTQxZWYtNTAxOC00OTMyLWJjMGUtNzVjODFmYzNjNGY0IiwidCI6IjY5M2NiZWEwLTRlZjktNDI1NC04OTc3LTc2ZTA1Y2I1ZjU1NiIsImMiOjR9)** without API data and there's the **[API-Data Dashboard](https://app.powerbi.com/view?r=eyJrIjoiZmRhM2IxMmEtMTViZi00ZTlhLWE0MTEtZTRjY2M4OTNjM2M3IiwidCI6IjY5M2NiZWEwLTRlZjktNDI1NC04OTc3LTc2ZTA1Y2I1ZjU1NiIsImMiOjR9)** for a better interactive experience and a greater display of the data.

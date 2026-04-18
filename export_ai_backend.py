{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 0,
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {
      "byteLimit": 2048000,
      "rowLimit": 10000
     },
     "inputWidgets": {},
     "nuid": "4de2a0a5-0470-44af-95b9-f7a038a3fd1a",
     "showTitle": false,
     "tableResultSettingsMap": {},
     "title": ""
    }
   },
   "outputs": [
    {
     "output_type": "stream",
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Collecting streamlit\n  Downloading streamlit-1.56.0-py3-none-any.whl.metadata (9.8 kB)\nCollecting altair!=5.4.0,!=5.4.1,<7,>=4.0 (from streamlit)\n  Downloading altair-6.0.0-py3-none-any.whl.metadata (11 kB)\nRequirement already satisfied: blinker<2,>=1.5.0 in /usr/lib/python3/dist-packages (from streamlit) (1.7.0)\nRequirement already satisfied: cachetools<8,>=5.5 in /databricks/python3/lib/python3.12/site-packages (from streamlit) (5.5.1)\nRequirement already satisfied: click<9,>=7.0 in /databricks/python3/lib/python3.12/site-packages (from streamlit) (8.1.8)\nRequirement already satisfied: gitpython!=3.1.19,<4,>=3.0.7 in /databricks/python3/lib/python3.12/site-packages (from streamlit) (3.1.43)\nRequirement already satisfied: numpy<3,>=1.23 in /databricks/python3/lib/python3.12/site-packages (from streamlit) (2.1.3)\nRequirement already satisfied: packaging>=20 in /databricks/python3/lib/python3.12/site-packages (from streamlit) (24.2)\nRequirement already satisfied: pandas<4,>=1.4.0 in /databricks/python3/lib/python3.12/site-packages (from streamlit) (2.2.3)\nRequirement already satisfied: pillow<13,>=7.1.0 in /databricks/python3/lib/python3.12/site-packages (from streamlit) (11.1.0)\nCollecting pydeck<1,>=0.8.0b4 (from streamlit)\n  Downloading pydeck-0.9.2-py2.py3-none-any.whl.metadata (4.2 kB)\nRequirement already satisfied: protobuf<8,>=3.20 in /databricks/python3/lib/python3.12/site-packages (from streamlit) (5.29.4)\nRequirement already satisfied: pyarrow>=7.0 in /databricks/python3/lib/python3.12/site-packages (from streamlit) (21.0.0)\nRequirement already satisfied: requests<3,>=2.27 in /databricks/python3/lib/python3.12/site-packages (from streamlit) (2.32.3)\nRequirement already satisfied: tenacity<10,>=8.1.0 in /databricks/python3/lib/python3.12/site-packages (from streamlit) (9.0.0)\nCollecting toml<2,>=0.10.1 (from streamlit)\n  Downloading toml-0.10.2-py2.py3-none-any.whl.metadata (7.1 kB)\nRequirement already satisfied: tornado!=6.5.0,<7,>=6.0.3 in /databricks/python3/lib/python3.12/site-packages (from streamlit) (6.5.1)\nRequirement already satisfied: typing-extensions<5,>=4.10.0 in /databricks/python3/lib/python3.12/site-packages (from streamlit) (4.12.2)\nCollecting watchdog<7,>=2.1.5 (from streamlit)\n  Downloading watchdog-6.0.0-py3-none-manylinux2014_aarch64.whl.metadata (44 kB)\nRequirement already satisfied: jinja2 in /databricks/python3/lib/python3.12/site-packages (from altair!=5.4.0,!=5.4.1,<7,>=4.0->streamlit) (3.1.6)\nRequirement already satisfied: jsonschema>=3.0 in /databricks/python3/lib/python3.12/site-packages (from altair!=5.4.0,!=5.4.1,<7,>=4.0->streamlit) (4.23.0)\nCollecting narwhals>=1.27.1 (from altair!=5.4.0,!=5.4.1,<7,>=4.0->streamlit)\n  Downloading narwhals-2.19.0-py3-none-any.whl.metadata (14 kB)\nRequirement already satisfied: gitdb<5,>=4.0.1 in /databricks/python3/lib/python3.12/site-packages (from gitpython!=3.1.19,<4,>=3.0.7->streamlit) (4.0.11)\nRequirement already satisfied: python-dateutil>=2.8.2 in /databricks/python3/lib/python3.12/site-packages (from pandas<4,>=1.4.0->streamlit) (2.9.0.post0)\nRequirement already satisfied: pytz>=2020.1 in /databricks/python3/lib/python3.12/site-packages (from pandas<4,>=1.4.0->streamlit) (2024.1)\nRequirement already satisfied: tzdata>=2022.7 in /databricks/python3/lib/python3.12/site-packages (from pandas<4,>=1.4.0->streamlit) (2024.1)\nRequirement already satisfied: charset-normalizer<4,>=2 in /databricks/python3/lib/python3.12/site-packages (from requests<3,>=2.27->streamlit) (3.3.2)\nRequirement already satisfied: idna<4,>=2.5 in /databricks/python3/lib/python3.12/site-packages (from requests<3,>=2.27->streamlit) (3.7)\nRequirement already satisfied: urllib3<3,>=1.21.1 in /databricks/python3/lib/python3.12/site-packages (from requests<3,>=2.27->streamlit) (2.3.0)\nRequirement already satisfied: certifi>=2017.4.17 in /databricks/python3/lib/python3.12/site-packages (from requests<3,>=2.27->streamlit) (2025.4.26)\nRequirement already satisfied: smmap<6,>=3.0.1 in /databricks/python3/lib/python3.12/site-packages (from gitdb<5,>=4.0.1->gitpython!=3.1.19,<4,>=3.0.7->streamlit) (5.0.0)\nRequirement already satisfied: MarkupSafe>=2.0 in /databricks/python3/lib/python3.12/site-packages (from jinja2->altair!=5.4.0,!=5.4.1,<7,>=4.0->streamlit) (3.0.2)\nRequirement already satisfied: attrs>=22.2.0 in /databricks/python3/lib/python3.12/site-packages (from jsonschema>=3.0->altair!=5.4.0,!=5.4.1,<7,>=4.0->streamlit) (24.3.0)\nRequirement already satisfied: jsonschema-specifications>=2023.03.6 in /databricks/python3/lib/python3.12/site-packages (from jsonschema>=3.0->altair!=5.4.0,!=5.4.1,<7,>=4.0->streamlit) (2023.7.1)\nRequirement already satisfied: referencing>=0.28.4 in /databricks/python3/lib/python3.12/site-packages (from jsonschema>=3.0->altair!=5.4.0,!=5.4.1,<7,>=4.0->streamlit) (0.30.2)\nRequirement already satisfied: rpds-py>=0.7.1 in /databricks/python3/lib/python3.12/site-packages (from jsonschema>=3.0->altair!=5.4.0,!=5.4.1,<7,>=4.0->streamlit) (0.22.3)\nRequirement already satisfied: six>=1.5 in /databricks/python3/lib/python3.12/site-packages (from python-dateutil>=2.8.2->pandas<4,>=1.4.0->streamlit) (1.17.0)\nDownloading streamlit-1.56.0-py3-none-any.whl (9.1 MB)\n\u001B[?25l   \u001B[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001B[0m \u001B[32m0.0/9.1 MB\u001B[0m \u001B[31m?\u001B[0m eta \u001B[36m-:--:--\u001B[0m\r\u001B[2K   \u001B[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001B[0m \u001B[32m9.1/9.1 MB\u001B[0m \u001B[31m88.0 MB/s\u001B[0m eta \u001B[36m0:00:00\u001B[0m\n\u001B[?25hDownloading altair-6.0.0-py3-none-any.whl (795 kB)\n\u001B[?25l   \u001B[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001B[0m \u001B[32m0.0/795.4 kB\u001B[0m \u001B[31m?\u001B[0m eta \u001B[36m-:--:--\u001B[0m\r\u001B[2K   \u001B[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001B[0m \u001B[32m795.4/795.4 kB\u001B[0m \u001B[31m31.2 MB/s\u001B[0m eta \u001B[36m0:00:00\u001B[0m\n\u001B[?25hDownloading pydeck-0.9.2-py2.py3-none-any.whl (11.3 MB)\n\u001B[?25l   \u001B[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001B[0m \u001B[32m0.0/11.3 MB\u001B[0m \u001B[31m?\u001B[0m eta \u001B[36m-:--:--\u001B[0m\r\u001B[2K   \u001B[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001B[0m \u001B[32m11.3/11.3 MB\u001B[0m \u001B[31m167.0 MB/s\u001B[0m eta \u001B[36m0:00:00\u001B[0m\n\u001B[?25hDownloading toml-0.10.2-py2.py3-none-any.whl (16 kB)\nDownloading watchdog-6.0.0-py3-none-manylinux2014_aarch64.whl (79 kB)\nDownloading narwhals-2.19.0-py3-none-any.whl (446 kB)\nInstalling collected packages: watchdog, toml, narwhals, pydeck, altair, streamlit\nSuccessfully installed altair-6.0.0 narwhals-2.19.0 pydeck-0.9.2 streamlit-1.56.0 toml-0.10.2 watchdog-6.0.0\n\u001B[43mNote: you may need to restart the kernel using %restart_python or dbutils.library.restartPython() to use updated packages.\u001B[0m\n"
     ]
    }
   ],
   "source": [
    "%pip install streamlit\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 0,
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {
      "byteLimit": 2048000,
      "rowLimit": 10000
     },
     "inputWidgets": {},
     "nuid": "3fa7fae2-b595-4c0f-b4c0-baa89bc5fd09",
     "showTitle": false,
     "tableResultSettingsMap": {},
     "title": ""
    }
   },
   "outputs": [
    {
     "output_type": "stream",
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Collecting databricks-vectorsearch\n  Downloading databricks_vectorsearch-0.67-py3-none-any.whl.metadata (3.0 kB)\nCollecting mlflow-skinny<4.0,>=3.10.1 (from databricks-vectorsearch)\n  Downloading mlflow_skinny-3.11.1-py3-none-any.whl.metadata (49 kB)\nCollecting protobuf<6.0,>=5.29.5 (from databricks-vectorsearch)\n  Downloading protobuf-5.29.6-cp38-abi3-manylinux2014_aarch64.whl.metadata (592 bytes)\nCollecting requests<3.0,>=2.32.5 (from databricks-vectorsearch)\n  Downloading requests-2.33.1-py3-none-any.whl.metadata (4.8 kB)\nCollecting deprecation<3.0,>=2.1.0 (from databricks-vectorsearch)\n  Downloading deprecation-2.1.0-py2.py3-none-any.whl.metadata (4.6 kB)\nRequirement already satisfied: packaging in /databricks/python3/lib/python3.12/site-packages (from deprecation<3.0,>=2.1.0->databricks-vectorsearch) (24.2)\nRequirement already satisfied: cachetools<8,>=5.0.0 in /databricks/python3/lib/python3.12/site-packages (from mlflow-skinny<4.0,>=3.10.1->databricks-vectorsearch) (5.5.1)\nRequirement already satisfied: click<9,>=7.0 in /databricks/python3/lib/python3.12/site-packages (from mlflow-skinny<4.0,>=3.10.1->databricks-vectorsearch) (8.1.8)\nRequirement already satisfied: cloudpickle<4 in /databricks/python3/lib/python3.12/site-packages (from mlflow-skinny<4.0,>=3.10.1->databricks-vectorsearch) (3.0.0)\nRequirement already satisfied: databricks-sdk<1,>=0.20.0 in /databricks/python3/lib/python3.12/site-packages (from mlflow-skinny<4.0,>=3.10.1->databricks-vectorsearch) (0.67.0)\nRequirement already satisfied: fastapi<1 in /databricks/python3/lib/python3.12/site-packages (from mlflow-skinny<4.0,>=3.10.1->databricks-vectorsearch) (0.128.0)\nRequirement already satisfied: gitpython<4,>=3.1.9 in /databricks/python3/lib/python3.12/site-packages (from mlflow-skinny<4.0,>=3.10.1->databricks-vectorsearch) (3.1.43)\nRequirement already satisfied: importlib_metadata!=4.7.0,<9,>=3.7.0 in /databricks/python3/lib/python3.12/site-packages (from mlflow-skinny<4.0,>=3.10.1->databricks-vectorsearch) (8.5.0)\nRequirement already satisfied: opentelemetry-api<3,>=1.9.0 in /databricks/python3/lib/python3.12/site-packages (from mlflow-skinny<4.0,>=3.10.1->databricks-vectorsearch) (1.39.1)\nRequirement already satisfied: opentelemetry-proto<3,>=1.9.0 in /databricks/python3/lib/python3.12/site-packages (from mlflow-skinny<4.0,>=3.10.1->databricks-vectorsearch) (1.39.1)\nRequirement already satisfied: opentelemetry-sdk<3,>=1.9.0 in /databricks/python3/lib/python3.12/site-packages (from mlflow-skinny<4.0,>=3.10.1->databricks-vectorsearch) (1.39.1)\nRequirement already satisfied: pydantic<3,>=2.0.0 in /databricks/python3/lib/python3.12/site-packages (from mlflow-skinny<4.0,>=3.10.1->databricks-vectorsearch) (2.10.6)\nRequirement already satisfied: python-dotenv<2,>=0.19.0 in /databricks/python3/lib/python3.12/site-packages (from mlflow-skinny<4.0,>=3.10.1->databricks-vectorsearch) (1.2.1)\nRequirement already satisfied: pyyaml<7,>=5.1 in /databricks/python3/lib/python3.12/site-packages (from mlflow-skinny<4.0,>=3.10.1->databricks-vectorsearch) (6.0.2)\nRequirement already satisfied: sqlparse<1,>=0.4.0 in /databricks/python3/lib/python3.12/site-packages (from mlflow-skinny<4.0,>=3.10.1->databricks-vectorsearch) (0.5.5)\nRequirement already satisfied: typing-extensions<5,>=4.0.0 in /databricks/python3/lib/python3.12/site-packages (from mlflow-skinny<4.0,>=3.10.1->databricks-vectorsearch) (4.12.2)\nRequirement already satisfied: uvicorn<1 in /databricks/python3/lib/python3.12/site-packages (from mlflow-skinny<4.0,>=3.10.1->databricks-vectorsearch) (0.40.0)\nRequirement already satisfied: charset_normalizer<4,>=2 in /databricks/python3/lib/python3.12/site-packages (from requests<3.0,>=2.32.5->databricks-vectorsearch) (3.3.2)\nRequirement already satisfied: idna<4,>=2.5 in /databricks/python3/lib/python3.12/site-packages (from requests<3.0,>=2.32.5->databricks-vectorsearch) (3.7)\nRequirement already satisfied: urllib3<3,>=1.26 in /databricks/python3/lib/python3.12/site-packages (from requests<3.0,>=2.32.5->databricks-vectorsearch) (2.3.0)\nRequirement already satisfied: certifi>=2023.5.7 in /databricks/python3/lib/python3.12/site-packages (from requests<3.0,>=2.32.5->databricks-vectorsearch) (2025.4.26)\nRequirement already satisfied: google-auth~=2.0 in /databricks/python3/lib/python3.12/site-packages (from databricks-sdk<1,>=0.20.0->mlflow-skinny<4.0,>=3.10.1->databricks-vectorsearch) (2.47.0)\nRequirement already satisfied: starlette<0.51.0,>=0.40.0 in /databricks/python3/lib/python3.12/site-packages (from fastapi<1->mlflow-skinny<4.0,>=3.10.1->databricks-vectorsearch) (0.50.0)\nRequirement already satisfied: annotated-doc>=0.0.2 in /databricks/python3/lib/python3.12/site-packages (from fastapi<1->mlflow-skinny<4.0,>=3.10.1->databricks-vectorsearch) (0.0.4)\nRequirement already satisfied: gitdb<5,>=4.0.1 in /databricks/python3/lib/python3.12/site-packages (from gitpython<4,>=3.1.9->mlflow-skinny<4.0,>=3.10.1->databricks-vectorsearch) (4.0.11)\nRequirement already satisfied: zipp>=3.20 in /databricks/python3/lib/python3.12/site-packages (from importlib_metadata!=4.7.0,<9,>=3.7.0->mlflow-skinny<4.0,>=3.10.1->databricks-vectorsearch) (3.21.0)\nRequirement already satisfied: opentelemetry-semantic-conventions==0.60b1 in /databricks/python3/lib/python3.12/site-packages (from opentelemetry-sdk<3,>=1.9.0->mlflow-skinny<4.0,>=3.10.1->databricks-vectorsearch) (0.60b1)\nRequirement already satisfied: annotated-types>=0.6.0 in /databricks/python3/lib/python3.12/site-packages (from pydantic<3,>=2.0.0->mlflow-skinny<4.0,>=3.10.1->databricks-vectorsearch) (0.7.0)\nRequirement already satisfied: pydantic-core==2.27.2 in /databricks/python3/lib/python3.12/site-packages (from pydantic<3,>=2.0.0->mlflow-skinny<4.0,>=3.10.1->databricks-vectorsearch) (2.27.2)\nRequirement already satisfied: h11>=0.8 in /databricks/python3/lib/python3.12/site-packages (from uvicorn<1->mlflow-skinny<4.0,>=3.10.1->databricks-vectorsearch) (0.16.0)\nRequirement already satisfied: smmap<6,>=3.0.1 in /databricks/python3/lib/python3.12/site-packages (from gitdb<5,>=4.0.1->gitpython<4,>=3.1.9->mlflow-skinny<4.0,>=3.10.1->databricks-vectorsearch) (5.0.0)\nRequirement already satisfied: pyasn1-modules>=0.2.1 in /databricks/python3/lib/python3.12/site-packages (from google-auth~=2.0->databricks-sdk<1,>=0.20.0->mlflow-skinny<4.0,>=3.10.1->databricks-vectorsearch) (0.2.8)\nRequirement already satisfied: rsa<5,>=3.1.4 in /databricks/python3/lib/python3.12/site-packages (from google-auth~=2.0->databricks-sdk<1,>=0.20.0->mlflow-skinny<4.0,>=3.10.1->databricks-vectorsearch) (4.9.1)\nRequirement already satisfied: anyio<5,>=3.6.2 in /databricks/python3/lib/python3.12/site-packages (from starlette<0.51.0,>=0.40.0->fastapi<1->mlflow-skinny<4.0,>=3.10.1->databricks-vectorsearch) (4.7.0)\nRequirement already satisfied: sniffio>=1.1 in /databricks/python3/lib/python3.12/site-packages (from anyio<5,>=3.6.2->starlette<0.51.0,>=0.40.0->fastapi<1->mlflow-skinny<4.0,>=3.10.1->databricks-vectorsearch) (1.3.0)\nRequirement already satisfied: pyasn1<0.5.0,>=0.4.6 in /databricks/python3/lib/python3.12/site-packages (from pyasn1-modules>=0.2.1->google-auth~=2.0->databricks-sdk<1,>=0.20.0->mlflow-skinny<4.0,>=3.10.1->databricks-vectorsearch) (0.4.8)\nDownloading databricks_vectorsearch-0.67-py3-none-any.whl (20 kB)\nDownloading deprecation-2.1.0-py2.py3-none-any.whl (11 kB)\nDownloading mlflow_skinny-3.11.1-py3-none-any.whl (3.2 MB)\n\u001B[?25l   \u001B[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001B[0m \u001B[32m0.0/3.2 MB\u001B[0m \u001B[31m?\u001B[0m eta \u001B[36m-:--:--\u001B[0m\r\u001B[2K   \u001B[91m━━━━━━━━━━━━━━━━━━━━━━━━━━\u001B[0m\u001B[90m╺\u001B[0m\u001B[90m━━━━━━━━━━━━━\u001B[0m \u001B[32m2.1/3.2 MB\u001B[0m \u001B[31m11.8 MB/s\u001B[0m eta \u001B[36m0:00:01\u001B[0m\r\u001B[2K   \u001B[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001B[0m \u001B[32m3.2/3.2 MB\u001B[0m \u001B[31m12.5 MB/s\u001B[0m eta \u001B[36m0:00:00\u001B[0m\n\u001B[?25hDownloading protobuf-5.29.6-cp38-abi3-manylinux2014_aarch64.whl (320 kB)\nDownloading requests-2.33.1-py3-none-any.whl (64 kB)\nInstalling collected packages: requests, protobuf, deprecation, mlflow-skinny, databricks-vectorsearch\n  Attempting uninstall: requests\n    Found existing installation: requests 2.32.3\n    Not uninstalling requests at /databricks/python3/lib/python3.12/site-packages, outside environment /local_disk0/.ephemeral_nfs/envs/pythonEnv-35f3904c-952e-4ea8-ba4a-81260ab065b7\n    Can't uninstall 'requests'. No files were found to uninstall.\n  Attempting uninstall: protobuf\n    Found existing installation: protobuf 5.29.4\n    Not uninstalling protobuf at /databricks/python3/lib/python3.12/site-packages, outside environment /local_disk0/.ephemeral_nfs/envs/pythonEnv-35f3904c-952e-4ea8-ba4a-81260ab065b7\n    Can't uninstall 'protobuf'. No files were found to uninstall.\n  Attempting uninstall: mlflow-skinny\n    Found existing installation: mlflow-skinny 3.8.1\n    Not uninstalling mlflow-skinny at /databricks/python3/lib/python3.12/site-packages, outside environment /local_disk0/.ephemeral_nfs/envs/pythonEnv-35f3904c-952e-4ea8-ba4a-81260ab065b7\n    Can't uninstall 'mlflow-skinny'. No files were found to uninstall.\nSuccessfully installed databricks-vectorsearch-0.67 deprecation-2.1.0 mlflow-skinny-3.11.1 protobuf-5.29.6 requests-2.33.1\n\u001B[43mNote: you may need to restart the kernel using %restart_python or dbutils.library.restartPython() to use updated packages.\u001B[0m\n"
     ]
    }
   ],
   "source": [
    "%pip install databricks-vectorsearch"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 0,
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {
      "byteLimit": 2048000,
      "rowLimit": 10000
     },
     "inputWidgets": {},
     "nuid": "5925003e-ed48-4c82-85ec-fbdedfeabe92",
     "showTitle": false,
     "tableResultSettingsMap": {},
     "title": ""
    }
   },
   "outputs": [],
   "source": [
    "dbutils.library.restartPython()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 0,
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {
      "byteLimit": 2048000,
      "rowLimit": 10000
     },
     "inputWidgets": {},
     "nuid": "75ba6c66-a7f8-4526-b304-72ea563aae23",
     "showTitle": false,
     "tableResultSettingsMap": {},
     "title": ""
    }
   },
   "outputs": [
    {
     "output_type": "stream",
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[NOTICE] Using a notebook authentication token. Recommended for development only. For improved performance, please use Service Principal based authentication. To disable this message, pass disable_notice=True.\n✅ Backend initialized: Vector Search + HTTP ready\n"
     ]
    }
   ],
   "source": [
    "# Vector Search client\n",
    "from databricks.vector_search.client import VectorSearchClient\n",
    "\n",
    "vs_client = VectorSearchClient()\n",
    "\n",
    "# HTTP for Sarvam API calls\n",
    "import requests\n",
    "\n",
    "# (optional safety check)\n",
    "print(\"✅ Backend initialized: Vector Search + HTTP ready\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 0,
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {
      "byteLimit": 2048000,
      "rowLimit": 10000
     },
     "inputWidgets": {},
     "nuid": "b704f436-5045-46de-8b96-2dcfc1cdc314",
     "showTitle": false,
     "tableResultSettingsMap": {},
     "title": ""
    }
   },
   "outputs": [
    {
     "output_type": "execute_result",
     "data": {
      "text/plain": [
       "{'name': 'export_ai.rag.document_chunks_index',\n",
       " 'endpoint_name': 'export_ai_vector_endpoint',\n",
       " 'primary_key': 'id',\n",
       " 'index_type': 'DELTA_SYNC',\n",
       " 'delta_sync_index_spec': {'source_table': 'export_ai.rag.document_chunks',\n",
       "  'embedding_source_columns': [{'name': 'content',\n",
       "    'embedding_model_endpoint_name': 'databricks-gte-large-en'}],\n",
       "  'pipeline_type': 'TRIGGERED',\n",
       "  'pipeline_id': '44c53fdd-4ec0-4c5a-8ef5-2d81b245d43d'},\n",
       " 'status': {'detailed_state': 'ONLINE_NO_PENDING_UPDATE',\n",
       "  'message': 'Index creation succeeded. Check latest status: https://dbc-21bb95c1-0f91.cloud.databricks.com/explore/data/export_ai/rag/document_chunks_index',\n",
       "  'indexed_row_count': 811,\n",
       "  'triggered_update_status': {'last_processed_commit_version': 1,\n",
       "   'last_processed_commit_timestamp': '2026-04-18T07:54:22Z'},\n",
       "  'ready': True,\n",
       "  'index_url': 'dbc-21bb95c1-0f91.cloud.databricks.com/api/2.0/vector-search/indexes/export_ai.rag.document_chunks_index'},\n",
       " 'creator': 'che240008016@iiti.ac.in',\n",
       " 'endpoint_type': 'STANDARD',\n",
       " 'id': 'c623ae94-2144-4788-9867-10f82fad7b4f',\n",
       " 'index_subtype': 'HYBRID'}"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "vs_client.get_index(\n",
    "    endpoint_name=\"export_ai_vector_endpoint\",\n",
    "    index_name=\"export_ai.rag.document_chunks_index\"\n",
    ").describe()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 0,
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {
      "byteLimit": 2048000,
      "rowLimit": 10000
     },
     "inputWidgets": {},
     "nuid": "dd15cd14-4a0c-4a93-9fe1-09124ce79ea9",
     "showTitle": false,
     "tableResultSettingsMap": {},
     "title": ""
    }
   },
   "outputs": [],
   "source": [
    "sarvam_api_key = dbutils.secrets.get(\n",
    "    scope=\"api_keys_scope\",\n",
    "    key=\"sarvam_api_key\"\n",
    ")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 0,
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {
      "byteLimit": 2048000,
      "rowLimit": 10000
     },
     "inputWidgets": {},
     "nuid": "a5c16301-ed20-41d6-bf1f-ff573fa7a901",
     "showTitle": false,
     "tableResultSettingsMap": {},
     "title": ""
    }
   },
   "outputs": [],
   "source": [
    "# ===============================\n",
    "# MAIN BACKEND RAG FUNCTION\n",
    "# ===============================\n",
    "\n",
    "def export_ai_pipeline(query):\n",
    "\n",
    "    # 1. Retrieve relevant chunks from Vector Search\n",
    "\n",
    "    index = vs_client.get_index(\n",
    "    endpoint_name=\"export_ai_vector_endpoint\",  # your endpoint name\n",
    "    index_name=\"export_ai.rag.document_chunks_index\"\n",
    "    )\n",
    "\n",
    "    results = index.similarity_search(\n",
    "    query_text=query,\n",
    "    columns=[\"content\"],\n",
    "    num_results=5\n",
    "    )\n",
    "\n",
    "    rows = results[\"result\"][\"data_array\"]\n",
    "\n",
    "    context = \"\\n\\n\".join([r[0] for r in rows])\n",
    "    # 3. Call Sarvam AI (reasoning + response generation)\n",
    "    payload = {\n",
    "        \"input\": f\"\"\"\n",
    "You are an export intelligence assistant for India.\n",
    "\n",
    "Use the context below to answer the question.\n",
    "\n",
    "CONTEXT:\n",
    "{context}\n",
    "\n",
    "QUESTION:\n",
    "{query}\n",
    "\n",
    "Return structured output with:\n",
    "- Summary\n",
    "- Export opportunities\n",
    "- Risks\n",
    "- Recommended countries\n",
    "\"\"\",\n",
    "        \"source_language_code\": \"en-IN\",\n",
    "        \"target_language_code\": \"en-IN\"\n",
    "    }\n",
    "\n",
    "    response = requests.post(\n",
    "    \"https://api.sarvam.ai/v1/chat/completions\",\n",
    "    json={\n",
    "        \"model\": \"sarvam-m\",\n",
    "        \"messages\": [\n",
    "            {\n",
    "                \"role\": \"user\",\n",
    "                \"content\": f\"\"\"\n",
    "You are an export intelligence assistant.\n",
    "\n",
    "Use the context below:\n",
    "\n",
    "{context}\n",
    "\n",
    "Question:\n",
    "{query}\n",
    "\n",
    "Give structured export insights.\n",
    "\"\"\"\n",
    "            }\n",
    "        ]\n",
    "    },\n",
    "    headers={\n",
    "        \"api-subscription-key\": sarvam_api_key\n",
    "    }\n",
    ")\n",
    "\n",
    "    # 4. Return final answer\n",
    "    return response.json()[\"choices\"][0][\"message\"][\"content\"]\n",
    "\n",
    "    import re\n",
    "    cleaned = re.sub(r\"<think>.*?</think>\", \"\", data, flags=re.DOTALL)\n",
    "\n",
    "    return cleaned.strip()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 0,
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {
      "byteLimit": 2048000,
      "rowLimit": 10000
     },
     "inputWidgets": {},
     "nuid": "3a87523e-6962-466f-9104-cca98b384747",
     "showTitle": false,
     "tableResultSettingsMap": {},
     "title": ""
    }
   },
   "outputs": [
    {
     "output_type": "stream",
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[NOTICE] Using a notebook authentication token. Recommended for development only. For improved performance, please use Service Principal based authentication. To disable this message, pass disable_notice=True.\n"
     ]
    },
    {
     "output_type": "execute_result",
     "data": {
      "text/plain": [
       "\"<think>\\nOkay, let's tackle this query about rice export opportunities from India to the UAE. First, I need to understand what the user is asking for. They want structured export insights, so I should organize the information clearly.\\n\\nLooking at the context provided, there's data on India's rice exports to Canada from 2018 to 2021. But the user is asking about the UAE, which isn't directly covered in the data. However, maybe there's some transferable information or legal frameworks that apply to exports in general, not just Canada.\\n\\nThe context mentions several legal frameworks and trade facilitation measures. For example, the single window system through APEDA for perishable agricultural products, the Niryat Bandhu Scheme for mentoring exporters, and the DGFT portal. These could be relevant for UAE exports too.\\n\\nAlso, the Staple Food Control Act and Salt Industry Act are mentioned, but those might be specific to domestic regulations. However, export-related regulations might be different. The user might need to know about compliance with Indian export laws, so mentioning APEDA's role and the DGFT portal would be useful.\\n\\nThe data from Canada shows that India was the 3rd largest exporter to Canada in 2020, which might indicate India's position in the global market. Even though it's Canada, this could suggest that India has a strong rice export sector, which might apply to the UAE as well.\\n\\nThe user might also be interested in market trends. The CAGR of ~18% from 2018-2020 shows growth, which could be a positive sign for UAE exports. However, the 2021 data (Jan-Aug) shows a drop to 51,158 thousand USD, which might be due to various factors like COVID-19. But again, this is Canada-specific. For the UAE, I might need to mention general factors like demand, competition (US and Thailand), and trade agreements.\\n\\nSince the context doesn't have specific data on UAE, I should note that and suggest looking into updated reports or market research. Also, highlight the existing trade facilitation measures that could help exporters, like APEDA's single window system and Niryat Bandhu for training.\\n\\nPotential challenges could include competition from other countries, compliance with UAE's import regulations, and logistics. Opportunities might include increasing demand in the UAE, especially in retail and hospitality sectors, and leveraging government support schemes.\\n\\nI need to structure this into sections like Market Overview, Key Drivers, Legal/Regulatory Framework, Trade Facilitation Measures, Challenges, Opportunities, and Recommendations. Make sure to mention the lack of specific UAE data and advise further research. Also, emphasize the existing Indian export support systems that can be utilized.\\n</think>\\n\\nHere’s a structured analysis of **rice export opportunities from India to the UAE**, based on the provided context and broader trade insights:\\n\\n---\\n\\n### **1. Market Overview**\\n- **UAE as a Key Market**: The UAE is a major importer of rice due to its large population, urbanization, and hospitality sector demand. While the provided data focuses on Canada, India’s global rice exports (e.g., 21.48% share in Canada in 2020) highlight its competitive position.\\n- **Growth Trends**:  \\n  - India’s rice exports to Canada grew at ~18% CAGR (2018–2020), suggesting similar potential in the UAE, given its population and economic ties.  \\n  - In 2021 (Jan–Aug), India’s rice exports to Canada dropped to **51,158 USD thousand** (from 95,539 in 2020), possibly due to pandemic-related disruptions or supply-chain issues.\\n\\n---\\n\\n### **2. Key Drivers for UAE Exports**\\n- **Demand Factors**:  \\n  - High consumption in UAE’s food service sector (hotels, restaurants, events).  \\n  - Growing population and urbanization driving retail demand.  \\n- **Competitive Edge**:  \\n  - India’s cost competitiveness in rice production and established global supply chains.  \\n  - US and Thailand dominate Canada’s imports, but India’s focus on quality and affordability could position it well in the UAE.\\n\\n---\\n\\n### **3. Legal/Regulatory Framework (India-Specific)**  \\n- **Staple Food Control Act**:  \\n  - Businesses handling ≥20 tons of polished rice must notify regional agricultural offices.  \\n  - *Implication*: Compliance is critical for large-scale exporters.  \\n- **APEDA Single Window System**:  \\n  - Streamlines export processes for perishable goods (e.g., rice), reducing transaction costs.  \\n- **DGFT Portal**:  \\n  - Access export/import policies, rules, and procedures via [DGFT’s portal](https://dgft.gov.in/).  \\n\\n---\\n\\n### **4. Trade Facilitation Measures**  \\n- **Niryat Bandhu Scheme**:  \\n  - Training and mentorship for new exporters (e.g., UAE-focused rice exporters) to navigate regulations.  \\n- **Duty-Free Entitlements**:  \\n  - Sectors like marine products and sports goods receive exemptions. While not directly applicable to rice, such incentives highlight India’s export promotion focus.  \\n- **TEE (Towns of Export Excellence)**:  \\n  - Financial support for export clusters (e.g., marketing, capacity building) could aid rice exporters targeting the UAE.  \\n\\n---\\n\\n### **5. Challenges**  \\n- **Competition**: Thailand (high-quality jasmine rice) and Vietnam (affordable prices) dominate global markets.  \\n- **Logistics**: Perishable goods require efficient cold-chain management.  \\n- **UAE’s Import Regulations**: Strict food safety standards (e.g., UAE’s GSO standards) may necessitate certifications.  \\n\\n---\\n\\n### **6. Opportunities**  \\n- **Basmati Rice Demand**: UAE’s preference for premium basmati aligns with India’s production strengths.  \\n- **FTA Benefits**: India-UAE CEPA (2022) offers tariff concessions (e.g., 0% duty on basmati rice), boosting competitiveness.  \\n- **Government Support**: Schemes like Niryat Bandhu and APEDA’s single window reduce export barriers.  \\n\\n---\\n\\n### **7. Recommendations**  \\n- **Leverage APEDA**: Use the single window system for faster clearances.  \\n- **Compliance**: Obtain UAE’s food safety certifications (e.g., GSO, FSSAI equivalence).  \\n- **Market Research**: Partner with UAE distributors to understand regional preferences (e.g., packaging, branding).  \\n\\n---\\n\\n### **Note**  \\nThe provided context lacks UAE-specific data, but India’s established frameworks (e.g., APEDA, DGFT) and strong rice export fundamentals suggest significant potential. For updated insights, consult UAE’s **Ministry of Climate Change and Environment** or India’s **Embassy in UAE**.\""
      ]
     },
     "execution_count": 44,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "export_ai_pipeline(\"rice export opportunities from India to UAE\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 0,
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {
      "byteLimit": 2048000,
      "rowLimit": 10000
     },
     "inputWidgets": {},
     "nuid": "f66093ee-55ad-4f6a-8f27-f7e6403d6326",
     "showTitle": false,
     "tableResultSettingsMap": {},
     "title": ""
    }
   },
   "outputs": [
    {
     "output_type": "stream",
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2026-04-18 10:42:35.797 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n2026-04-18 10:42:35.804 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n2026-04-18 10:42:35.805 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n2026-04-18 10:42:35.805 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n2026-04-18 10:42:35.807 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n2026-04-18 10:42:35.807 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n2026-04-18 10:42:35.808 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n2026-04-18 10:42:35.809 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n2026-04-18 10:42:35.809 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n2026-04-18 10:42:35.810 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n2026-04-18 10:42:35.810 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n2026-04-18 10:42:35.811 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n2026-04-18 10:42:35.811 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n2026-04-18 10:42:35.812 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n2026-04-18 10:42:35.813 Session state does not function when running a script without `streamlit run`\n2026-04-18 10:42:35.813 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n2026-04-18 10:42:35.814 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n2026-04-18 10:42:35.814 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n2026-04-18 10:42:35.815 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n2026-04-18 10:42:35.816 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n2026-04-18 10:42:35.816 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n2026-04-18 10:42:35.817 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n2026-04-18 10:42:35.817 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n2026-04-18 10:42:35.818 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n2026-04-18 10:42:35.818 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n2026-04-18 10:42:35.819 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n2026-04-18 10:42:35.819 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n2026-04-18 10:42:35.820 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n2026-04-18 10:42:35.821 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n2026-04-18 10:42:35.821 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n2026-04-18 10:42:35.826 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n2026-04-18 10:42:35.827 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n2026-04-18 10:42:35.827 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n2026-04-18 10:42:35.828 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n2026-04-18 10:42:35.829 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n2026-04-18 10:42:35.829 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n2026-04-18 10:42:35.830 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n2026-04-18 10:42:35.831 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n2026-04-18 10:42:35.831 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n"
     ]
    }
   ],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 0,
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {},
     "inputWidgets": {},
     "nuid": "20b7c995-a4f3-42d6-87a4-e61886d3ddb1",
     "showTitle": false,
     "tableResultSettingsMap": {},
     "title": ""
    }
   },
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "application/vnd.databricks.v1+notebook": {
   "computePreferences": null,
   "dashboards": [],
   "environmentMetadata": {
    "base_environment": "",
    "environment_version": "5"
   },
   "inputWidgetPreferences": null,
   "language": "python",
   "notebookMetadata": {
    "pythonIndentUnit": 4
   },
   "notebookName": "export_ai_backend.py",
   "widgets": {}
  },
  "language_info": {
   "name": "python"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 0
}
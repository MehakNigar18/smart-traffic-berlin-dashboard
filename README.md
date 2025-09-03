# 🚦 Smart Traffic Berlin Mobility Project

This project analyzes and clusters Berlin traffic volume data using Azure Databricks. It leverages Spark for large-scale data processing and unsupervised learning (GMM clustering) to extract mobility insights. The project supports smart city initiatives through traffic optimization and data-driven visualizations.

---

## 📁 Project Structure


---

## 🧾 Objective

- Ingest and preprocess Berlin traffic data
- Cluster traffic volume using Gaussian Mixture Models (GMM)
- Analyze mobility behavior spatially and temporally
- Deploy clustering results to Azure and support integration with Power BI

---

## 💡 Technologies Used

- **Azure Databricks**
- **Apache Spark (PySpark)**
- **Azure Blob Storage**
- **Pandas, NumPy, Matplotlib, Seaborn**
- **Scikit-learn**
- **Power BI (optional for dashboarding)**

---

## 🚀 Key Notebooks Overview

| Notebook                                      | Description                                                |
|-----------------------------------------------|------------------------------------------------------------|
| `01_DataCollection_Cleaning`                 | Loads traffic data from Azure Blob, handles missing values |
| `02_DataTransformation_Analysis`             | Cleans schema, converts data types, aggregates features    |
| `03_FeatureEngineering`                      | (Optional) Builds engineered features for clustering       |
| `04_ModelTraining_and_Evaluation`            | Trains GMM, optimizes parameters, evaluates clustering     |
| `05_Clustering_Profiling_Visualization`      | Explores cluster properties and visualizes results         |
| `06_ModelDeployment_AzureIntegration`        | Saves results to Azure Blob, optionally integrates Power BI|

---

## 📦 Data Description

| Column Name      | Description                          |
|------------------|--------------------------------------|
| `gml_id`         | Unique spatial identifier            |
| `spatial_name`   | Region or road name                  |
| `zahl_tvz`       | Traffic volume count                 |
| `spatial_type`   | Type of spatial feature (e.g. street)|
| `cluster_label`  | Cluster assignment from GMM          |

---

## ✅ Getting Started

1. Clone the project or open it in your Azure Databricks workspace.
2. Start with `01_DataCollection_Cleaning.ipynb` and follow the notebook order.
3. Replace paths or tokens in your Blob URL if needed.
4. Results are saved to `/dbfs/user/mehak/processed/` or your Azure Blob Storage.

---

## 📊 Output Examples

- 📌 Clustered map of traffic volumes
- 📈 Entropy & edge density per cluster
- 📁 Exported CSVs and Power BI integration

---

## 🧠 Future Improvements

- Real-time data ingestion using Azure Event Hubs
- More advanced models like DBSCAN or time series clustering
- Add anomaly detection for unusual traffic behavior

---

## 👩‍💻 Author

**Mehak Nigar Shumaila**  
Data Engineer | Azure Enthusiast | Berlin Mobility Analyst

---



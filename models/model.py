# 1. Load the Data
# Assuming you have already cleaned the dataset and stored it in a CSV file.
# Replace the path with the location of your data file in DBFS or external storage.

input_path = "dbfs:/user/mehak/processed/berlin_clean.csv"  # Change this path if necessary

# Load data into Spark DataFrame
spark_df = spark.read.csv(input_path, header=True, inferSchema=True) # pyright: ignore[reportUndefinedVariable]

# Show the first 5 rows to check
spark_df.show(5)
spark_df.printSchema()

# If the data is already cleaned and preprocessed, you can skip this step if you already have `spark_df`

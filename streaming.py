from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col
from pyspark.sql.types import StructType, StringType

# Démarrage session Spark
spark = SparkSession.builder.appName("FakeNewsDetection").getOrCreate()

# Schéma JSON du message
schema = StructType() \
    .add("text", StringType()) \
    .add("user", StringType()) \
    .add("timestamp", StringType())

# Lecture du topic Kafka
df = spark.readStream.format("kafka") \
    .option("kafka.bootstrap.servers", "localhost:9092") \
    .option("subscribe", "twitter-topic") \
    .load()

# Extraction du champ 'text'
parsed_df = df.selectExpr("CAST(value AS STRING)").select(from_json(col("value"), schema).alias("data")).select("data.*")

# Affichage dans la console (à remplacer par appel modèle)
query = parsed_df.writeStream.outputMode("append").format("console").start()
query.awaitTermination()

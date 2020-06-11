from pyspark import SparkContext 
from pyspark.sql import SQLContext
sc = SparkContext()
sqlContext = SQLContext(sc)
test = sqlContext.read.format('com.databricks.spark.csv').options(header='true', inferschema='true').load('./gender.csv')
test.show()
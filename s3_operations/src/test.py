from pyspark.sql import SQLContext
from pyspark import SparkContext
from pyspark import SparkFiles



sc = SparkContext()
url = "https://raw.githubusercontent.com/guru99-edu/R-Programming/master/adult_data.csv"
sc.addFile(url)
sqlContext = SQLContext(sc)
df = sqlContext.read.csv(SparkFiles.get("adult_data.csv"), header=True, inferSchema= True)
print(df.show())
print(df.printSchema())
print(df.show(5, truncate = False))
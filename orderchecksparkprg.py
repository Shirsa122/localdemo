from pyspark import SparkConf,SparkContext
from pyspark.sql import SparkSession
from pyspark.sql.types import *
from pyspark.sql.functions import *
conf = SparkConf().setMaster("local[*]").setAppName("Senario_1")
sc = SparkContext(conf=conf)
sc.setLogLevel("Error")

spark = SparkSession.builder.getOrCreate()
data = [
    (1,"1-Jan","ordered"),
    (1,"2-Jan","dispatched"),
    (1,"3-Jan","dispatched"),
    (1,"4-Jan","shipped"),
    (1,"5-Jan","shipped"),
    (1,"6-Jan","deliverd"),
    (2,"1-Jan","ordered"),
    (2,"2-Jan","dispatched"),
    (1,"3-Jan","shipped")]
myschema=["orderid","statusdate","status"]
df = spark.createDataFrame(data,schema=myschema)
df.show()
df.createOrReplaceTempView("odertab")
spark.sql("select * from odertab where status='dispatched' and orderid in (select orderid from odertab where status ='ordered')").show()
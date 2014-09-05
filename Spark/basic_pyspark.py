import pyspark
sc = pyspark.SparkContext("local", "Spark app")

text = sc.textFile("data/chekhov.txt")
lines_nonempty = text.filter(lambda x: len(x) > 0)
print lines_nonempty.count()

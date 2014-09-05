import sys
sys.path.append("../")
from util.timers import timethis

import pyspark

sc = pyspark.SparkContext("local", "Spark app")

from pyspark.sql import SQLContext
from dateutil import parser
sqlContext = SQLContext(sc)

rdd = sc.textFile("data/CGM_INTERPOLATED.csv")
frdd = rdd.filter(lambda line: "isig" not in line)
data = frdd.map(lambda line: line.split(','))
data = data.map(lambda d: (float(d[0]), parser.parse(d[1]), int(d[2])) )
day = data.filter(lambda d: d[1].date() == parser.parse("2010-10-04").date())
highs = day.filter(lambda d: d[2] > 180)
lows = day.filter(lambda d: d[2] < 80)

@timethis
def collect_it():
    result = highs.collect()
    return result

collection_rdd, time_rdd = collect_it()


sqlContext = SQLContext(sc)
# Load a text file and convert each line to a dictionary.
frdd = rdd.filter(lambda line: "isig" not in line)
data = frdd.map(lambda line: line.split(','))
values = data.map(lambda p: {"isig": float(p[0]),
                              "pit": parser.parse(p[1]),
                              "glucose": int(p[2])
                             }
                  )

cgm = sqlContext.inferSchema(values)
cgm.registerAsTable("CGM")

# SQL can be run over SchemaRDDs that have been registered as a table.
day = sqlContext.sql("SELECT * FROM CGM WHERE pit <= '2010-10-05 00:00:00' and pit >= '2010-10-04 00:00:00'")
day.registerAsTable("ADAY")
highs = sqlContext.sql("SELECT * FROM ADAY WHERE glucose > 180")

collection_sqlrdd, time_sqlrdd = collect_it()

print("Time RDD: {} Time SQLRDD: {}".format(time_rdd, time_sqlrdd))
percent = float(time_rdd)/time_sqlrdd
print("SQLRDD faster by: {:.2%}".format(percent))

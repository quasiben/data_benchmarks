
## Install
- git clone https://github.com/apache/spark.git
- cd spark
- ./sbt/sbt assembly
- export SPARK_HOME=spark_clone_dir
- export PYTHONPATH=$PYTHONPATH:$SPARK_HOME/python
- pip install py4j

## Hardware

- Macbook Pro
 - 10.9.4
 - 16GB RAM
 - 2.6 GHz Core i5

## Results (local)

cgm_analysis:
- `Time RDD: 14.1561689377 Time SQLRDD: 8.67419910431`

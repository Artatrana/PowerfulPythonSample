import pyspark         # works
from pyspark.sql import SparkSession   # ModuleNotFoundError

import pyspark
import os
print(os.listdir(pyspark.__path__[0]))



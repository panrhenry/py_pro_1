import os
from pyspark import SparkFiles,SparkConf,SparkContext

# sparkConf = SparkConf().setAppName("cz").setMaster("local[2]")
# sc = SparkContext(sparkConf)
sc = SparkContext('local[1]', 'pyspark')

tempdir = "D:\panrui\我的桌面\learning file\data\\"
path = os.path.join(tempdir, "test.txt")
with open(path,"w") as TextFile:
    _ = TextFile.write("100")
sc.addFile(path)

def func(iterator):
    with open(SparkFiles.get("test.txt")) as textFile:
        fileVal = int(textFile.readline())
        return [x * fileVal for x in iterator]

if __name__ == '__main__':
    sc.parallelize([1,2,3,4]).mapPartitions(func).collect()

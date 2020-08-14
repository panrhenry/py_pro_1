# zipFile = zipfile.ZipFile('C:\\Users\panrui\Desktop\\1.zip')  # 这里的第二个参数用r表示是读取zip文件，w是创建一个zip文件，默认是r
# PwdLists = open('C:\\Users\panrui\Desktop\\cnpassword.txt')  # 读入所有密码


import zipfile
import random
import time
import sys


class MyIterator():
    # 单位字符集合
    letters = 'abcdefghijklmnopqrstuvwxyz012345678'
    min_digits = 0
    max_digits = 0

    def __init__(self, min_digits, max_digits):
        # 实例化对象时给出密码位数范围，一般4到10位
        if min_digits < max_digits:
            self.min_digits = min_digits
            self.max_digits = max_digits
        else:
            self.min_digits = max_digits
            self.max_digits = min_digits

    # 迭代器访问定义
    def __iter__(self):
        return self

    def __next__(self):
        rst = str()
        for item in range(0, random.randrange(self.min_digits, self.max_digits + 1)):
            rst += random.choice(MyIterator.letters)
        return rst


def extract():
    start_time = time.time()
    zfile = zipfile.ZipFile("C:\\Users\panrui\Desktop\\1.zip")
    for p in MyIterator(5, 6):
        try:
            zfile.extractall(path=".", pwd=str(p).encode('utf-8'))
            print("the password is {}".format(p))
            now_time = time.time()
            print("spend time is {}".format(now_time - start_time))
            sys.exit(0)
        except Exception as e:
            print("password: "+p+" is not correct")
            pass


if __name__ == '__main__':
    extract()
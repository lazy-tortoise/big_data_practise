# -*- coding: UTF8 -*-
"""[比特币交易量排行榜，数值位数21位浮点型，数据量3G]
算法思路：先把浮点型变成整型，然后使用基数排序，21位数字从末尾到首尾进行稳定排序算法排序
"""
import os
import random as rand
from multiprocessing import Process
from tqdm import tqdm
import resource

class File():
    """文件类，主要用于生成文件。
    """

    def __init__(self, lenght=10, stop=10000000):
        self.length = lenght
        self.stop = stop

    def getDocSize(self, path):
        try:
            size = os.path.getsize(path)
            return self.formatSize(size)
        except Exception as err:
            print(err)


    def formatSize(self,bytes):
        try:
            bytes = float(bytes)
            kb = bytes / 1024
        except:
            print("传入的字节格式不对")
            return "Error"

        if kb >= 1024:
            M = kb / 1024
            if M >= 1024:
                G = M / 1024
                return "%fG" % (G)
            else:
                return "%fM" % (M)
        else:
            return "%fkb" % (kb)

    def create_txt(self):
        path = "./top_k/data/radix_sort_.txt"
        input = ""
        stop = self.stop

        for i in tqdm(range(self.length)):
            str_num = rand.randint(1,stop)
            str_num = str(str_num)
            cnt = 21 - len(str_num)
            str_num = ("0" * cnt) + str_num
            input += str_num + '\n'
            if i % 10000 == 0:
                with open(path, "a+") as f:
                    f.write(input)
                input = ""
        return self.getDocSize(path)
        

class Rank():
    def __init__():
        pass

    
        

def limit_memory(maxsize):
    """对内存使用做限制
    
    Arguments:
        maxsize {[int]} -- max memory size
    """
    soft, hard = resource.getrlimit(resource.RLIMIT_AS)
    resource.setrlimit(resource.RLIMIT_AS, (maxsize, hard))


if __name__ == "__main__":
    file = File(300000000, 10**21-1)
    ret  = file.create_txt()
    print(ret)
 










    # p0 = Process(target=create_txt, args=(str(0),))
    # p0.start()
    
    # p1 = Process(target=create_txt, args=(str(1),))
    # p1.start()

    # p2 = Process(target=create_txt, args=(str(2),))
    # p2.start()

    # p0.join()
    # print("this is 0 over")

    # p1.join()
    # print("this is 1 over")

    # p2.join()
    # print("this is 2 over")
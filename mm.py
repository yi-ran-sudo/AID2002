from time import sleep

f = open("time.txt", "a")  # 打开文件,进入追加模式

while sleep(2):
    data = (time.strftime("%Y-%m-%d %H:%M:%S\n", time.localtime())) #时间打印
    f.write(data) #写入文件
    flush() #刷新磁盘缓冲
    f.seek(1,1) #设置文件偏移量,下次打开继续向后写入



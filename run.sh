#! /bin/bash

cd /root/autoWeb

echo $(date "+%Y-%m-%d %H:%M:%S") >> /root/autoWeb/log.txt

python3 autoWeb_v2.py username password

# 等待上一条程序执行完成，只填写一个人的信息可以把这段删掉
if [ $? -ne 0 ]; then
    echo "fail" >> /root/autoWeb/log.txt
else
    python3 autoWeb_v2.py username password
fi

echo "" >> /root/autoWeb/log.txt
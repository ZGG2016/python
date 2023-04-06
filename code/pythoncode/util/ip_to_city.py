#-------------------------------------------------------------------------------
# Name:         ip_to_city
# Description:  将ip地址具体的城市
# Date:         2022.03.28
#-------------------------------------------------------------------------------

import time

IP_URL="util/resource/IP.txt"

def ip_to_int(ip):
    val = [int(x) for x in ip.split(".")]
    return sum(val[i] << [24, 16, 8, 0][i] for i in range(4))
    # A.B.C.D	2^24 * A + 2^16 * B + 2^8 * C + 2^0 * D
    # rlt = 0
    # val = ip.split('.').reverse()
    # t = 1
    # for v 1_in val:
    #     rlt += int(v) * t
    #     t = t * (2 ** 8)
    # return rlt

def data_cleaning(path):
    ip_name = []
    with open(path) as f:
        for line in f:
            item = line.strip("\n").split(" ")
            item_no_blank = list(filter(None, item))
            ip_name.append([ip_to_int(item_no_blank[0]), item_no_blank[2]])
        return ip_name

def ip_to_city(ip_name,target):
    l,h = 0,len(ip_name)-1

    if target < ip_name[l][0] or target > ip_name[h][0]:
        return -1

    m = int((l+h)/2)
    while l<h:
        if ip_name[m][0]<=target:
            l=m
            if ip_name[m][0] == target or ip_name[m+1][0]>target:
                return ip_name[m][1]
        else:
            h=m
            if ip_name[m-1][0]<=target:
                return ip_name[m-1][1]
        m = int((l + h) / 2)

a = time.time()
ip_name=data_cleaning(IP_URL)
addr = ip_to_city(ip_name,ip_to_int("1.25.76.0"))
b = time.time()
print(a-b)
print(addr)


# https://blog.csdn.net/qq_17753903/article/details/82794833    ip->int

# -------------------------------------------------------------------------------
# Name:         add2wgs84
# Description:  将地址转成WGS84坐标，具体流程为：地理地址 --> GCJ02坐标 --> WGS84坐标
# Date:         2022.01.15
# -------------------------------------------------------------------------------

import requests
import xlrd
import math
from xlutils.copy import copy


# GCJ02坐标 -->  WGS84坐标
def gcj2wgs(lon, lat):
    # location格式如下：locations[1] = "113.923745,22.530824"
    #     lon = float(location[0:location.find(",")])
    #     lat = float(location[location.find(",") + 1:len(location)])
    a = 6378245.0  # 克拉索夫斯基椭球参数长半轴a
    ee = 0.00669342162296594323  # 克拉索夫斯基椭球参数第一偏心率平方
    PI = 3.14159265358979324  # 圆周率
    # 以下为转换公式
    x = float(lon) - 105.0
    y = float(lat) - 35.0
    # 经度
    dLon = 300.0 + x + 2.0 * y + 0.1 * x * x + 0.1 * x * y + 0.1 * math.sqrt(abs(x))
    dLon += (20.0 * math.sin(6.0 * x * PI) + 20.0 * math.sin(2.0 * x * PI)) * 2.0 / 3.0
    dLon += (20.0 * math.sin(x * PI) + 40.0 * math.sin(x / 3.0 * PI)) * 2.0 / 3.0
    dLon += (150.0 * math.sin(x / 12.0 * PI) + 300.0 * math.sin(x / 30.0 * PI)) * 2.0 / 3.0
    # 纬度
    dLat = -100.0 + 2.0 * x + 3.0 * y + 0.2 * y * y + 0.1 * x * y + 0.2 * math.sqrt(abs(x))
    dLat += (20.0 * math.sin(6.0 * x * PI) + 20.0 * math.sin(2.0 * x * PI)) * 2.0 / 3.0
    dLat += (20.0 * math.sin(y * PI) + 40.0 * math.sin(y / 3.0 * PI)) * 2.0 / 3.0
    dLat += (160.0 * math.sin(y / 12.0 * PI) + 320 * math.sin(y * PI / 30.0)) * 2.0 / 3.0
    radLat = lat / 180.0 * PI
    magic = math.sin(radLat)
    magic = 1 - ee * magic * magic
    sqrtMagic = math.sqrt(magic)
    dLat = (dLat * 180.0) / ((a * (1 - ee)) / (magic * sqrtMagic) * PI)
    dLon = (dLon * 180.0) / (a / sqrtMagic * math.cos(radLat) * PI)
    wgsLon = lon - dLon
    wgsLat = lat - dLat
    return wgsLon, wgsLat


# 地址 --> 经纬度(GCJ02坐标)
def addr2coord(locationstr):
    """
    高德地图地理编码的查询
    :param locationstr:  要转换的地址
    :return: 结果坐标的列表
    """
    key = ""

    output = 'json'
    batch = 'true'
    base = 'https://restapi.amap.com/v3/geocode/geo?'
    url = base + "output=" + output + "&batch=" + batch + "&address=" + locationstr + "&key=" + key

    response = requests.get(url)
    resp_info = response.json()
    # print(resp_info)
    result = []
    if resp_info['status'] == '1' and resp_info['info'] == 'OK':
        geocodes = resp_info['geocodes']
        for i in range(0, len(geocodes)):
            try:
                coordstr = geocodes[i]['location']
                coordlist = coordstr.split(',')
                result.append((float(coordlist[0]), float(coordlist[1])))
            except:
                result.append(None)
        return result
    elif resp_info['info'] == 'DAILY_QUERY_OVER_LIMIT':
        return -1  # Key的配额用完了
    else:
        return -2


# 地理地址 --> WGS84坐标
def getwgscoord():
    file = r"data/起终点地址.xls"
    workbook = xlrd.open_workbook(file)
    sheet = workbook.sheet_by_name("Sheet1")

    wgsworkbook = copy(workbook)
    wgssheet = wgsworkbook.get_sheet(0)
    wgssheet.write(0, 4, "wgsblon")
    wgssheet.write(0, 5, "wgsblat")
    wgssheet.write(0, 6, "wgselon")
    wgssheet.write(0, 7, "wgselat")

    nrows = sheet.nrows
    for row in range(1, nrows):
        line = sheet.row_values(row)
        begin = line[1]
        end = line[2]
        locationstr = begin + "|" + end
        print(locationstr)
        gcjres = addr2coord(locationstr=locationstr)
        # print(gcjres[1][0])
        # print(gcjres[1][1])
        wgsblon, wgsblat = gcj2wgs(gcjres[0][0], gcjres[0][1])
        wgselon, wgselat = gcj2wgs(gcjres[1][0], gcjres[1][1])

        # print(str(wgsblon) + " "+ str(wgsblat) + " "+ str(wgselon) + " "+ str(wgselat))
        wgssheet.write(row, 4, str(wgsblon))
        wgssheet.write(row, 5, str(wgsblat))
        wgssheet.write(row, 6, str(wgselon))
        wgssheet.write(row, 7, str(wgselat))

    wgsworkbook.save("resource/起终点坐标.xls")


if __name__ == '__main__':
    getwgscoord()

# 官方API: http://lbs.amap.com/api/webservice/guide/api/convert
# 坐标体系说明：http://lbs.amap.com/faq/top/coordinate/3
# GCJ02->WGS84 Java版本：http://www.cnblogs.com/xinghuangroup/p/5787306.html
# 验证坐标转换正确性的地址：http://www.gpsspg.com/maps.htm
# 来源：https://www.cnblogs.com/shadrach/p/7640717.html

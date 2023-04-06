from pyhive import hive

'''
使用 python 操作 hive:
    pyhive 的基础使用
    具体配置操作流程见文档
'''

conn = hive.Connection(host='zgg',
	                     port=10000,
	                     auth='NOSASL')

cur = conn.cursor()
cur.execute("select * from employees")

for row in cur.fetchall():
    print(row)
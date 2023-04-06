import pyhs2

'''
使用 python 操作 hive:
    pyhs2 的基础使用
    具体配置操作流程见文档
'''

with pyhs2.connect(host='zgg',
                   port=10000,
                   authMechanism="NOSASL",
                   user='root',
                   password='root',
                   database='default') as conn:
    with conn.cursor() as cur:
        # Show databases
        print(cur.getDatabases())

        # Execute query
        cur.execute("select * from employees")

        # Return column info from query
        print(cur.getSchema())

        # Fetch table results
        for i in cur.fetch():
            print(i)
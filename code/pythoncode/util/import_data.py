# -------------------------------------------------------------------------------
# Name:         import_data
# Description:  使用cx_Oracle将数据批量导入oracle
# Date:         2022.03.25
# -------------------------------------------------------------------------------

import os
import sys
import time
import cx_Oracle


class ImportData:
    def __init__(self, hostname, port, service_name, username, password, conn=None, cur=None):
        self.hostname = hostname
        self.port = port
        self.service_name = service_name
        self.username = username
        self.password = password
        self.conn = conn
        self.cur = cur

    def get_connection(self):
        try:
            dsn_str = cx_Oracle.makedsn(self.hostname, self.port, service_name=self.service_name)
            self.conn = cx_Oracle.connect(self.username, self.password, dsn=dsn_str)
            self.cur = self.conn.cursor()
        except cx_Oracle.DatabaseError as error:
            print("---------------->")
            print(error)

    def insert_data(self, data):

        sql = "INSERT INTO TEST values (:1,:2,to_date(:3,'YYYY-MM-DD HH24:MI:SS'))"
        self.cur.executemany(sql, data)
        self.conn.commit()

    def close(self):
        self.cur.close()
        self.conn.close()


if __name__ == "__main__":

    batch = 5000
    data_path = sys.argv[6]

    dataset = []
    import_data = ImportData(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5])
    import_data.get_connection()

    # 防止断开连接，分别读
    file_names = []
    # for i in range(1, 10):
    #     s = 'aaa_2021_04_' + str(i) + '.csv'   # 修改
    #     file_names.append(s)
    # print(file_names)
    for csv_file_name in os.listdir(data_path):
        if 'aaa' not in csv_file_name: continue
        if csv_file_name not in file_names: continue

        print("=============== 开始读取 '%s' ================" % csv_file_name)
        start_time = time.time()
        file_path = os.path.join(data_path, csv_file_name)

        try:
            with open(file_path, 'r') as f:
                for index, line in enumerate(f):
                    if 'PASSID' in line: continue

                    tmp = []
                    for item in line.split(','):
                        tmp.append(item.strip())
                    dataset.append(tuple(tmp))

                    if (index + 1) % batch == 0:
                        import_data.insert_data(dataset)
                        dataset.clear()
                        continue
        except cx_Oracle.DatabaseError as e:
            print(e)
        finally:
            import_data.insert_data(dataset)
            dataset.clear()

        elapsed_time = (time.time() - start_time)
        print("=============== 读取 '%s'  完成, 共用时 '%s' ================" % (csv_file_name, elapsed_time))
    import_data.close()

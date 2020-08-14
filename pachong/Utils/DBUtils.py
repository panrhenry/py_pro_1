import pymysql


class MysqlUtil:
    """mysql 工具类"""

    def __init__(self, host, user, password, database, port):
        # 读取配置文件
        # 连接数据库
        self.conn = pymysql.connect(host, user, password, database, int(port))
        self.cursor = self.conn.cursor()

    def close(self):
        # 关闭光标、数据库
        self.cursor.cloase()
        self.conn.close()

    def query(self, sql, param):
        # 执行sql rows保存结果
        self.cursor.execute(sql, param)
        rows = self.cursor.fetchall()
        result_list = []
        if rows is None or len(rows) == 0:
            return result_list
        index_name_list = self.cursor.description
        idx_num = len(index_name_list)
        for res in rows:
            row = {}
            for i in range(idx_num):
                row[index_name_list[i][0]] = res[i]
            result_list.append(row)
        return result_list

    def execute_sql(self, sql, param):
        # 执行sql
        self.cursor.execute(sql, param)
        self.conn.commit()
        return self.cursor.lastrowid

    def de_query(self, host, user, password, database, port, sql, param):
        conn = pymysql.connect(host, user, password, database, int(port))
        cursor = conn.cursor()
        cursor.execute(sql, param)
        rows = cursor.fetchall()
        result_list = []
        if rows is None or len(rows) == 0:
            return result_list
        index_name_list = cursor.description
        idx_num = len(index_name_list)
        for res in rows:
            row = {}
            for i in range(idx_num):
                row[index_name_list[i][0]] = res[i]
            result_list.append(row)

        cursor.close()
        conn.close()
        return result_list
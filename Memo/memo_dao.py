import pymysql
from Memo.db_util import get_connection
import Memo.paging as m_paging


def make_memo(row):
    memo_dict = None
    if row is not None:
        memo_dict = dict()
        memo_dict['idx'] = row[0]
        memo_dict['name'] = row[1]
        memo_dict['password'] = row[2]
        memo_dict['content'] = row[3]
        memo_dict['regDate'] = row[4]
        memo_dict['ip'] = row[5]
    return memo_dict


class Memo_DAO:
    def __init__(self, conn):
        self.connection = conn

    def get_count(self):
        sql = "select count(*) from memo"
        curs = self.connection.cursor()
        curs.execute(sql)
        count = curs.fetchall()[0][0]
        # print("{}테이블에는 {}개의 데이터가 있습니다.".format(table_name, count))
        return count

    def select_by_idx(self, idx):
        sql = "select * from memo where idx=" + str(idx)
        curs = self.connection.cursor()
        curs.execute(sql)
        row = curs.fetchone()
        memo_dict = make_memo(row)
        return memo_dict

    def select_list(self, start_no, page_size):
        sql = "select * from memo order by idx desc limit " + str(start_no) + ", "
        sql += str(page_size)
        curs = self.connection.cursor()
        curs.execute(sql)
        rows = curs.fetchall()
        memo_lists = list()
        for row in rows:
            memo_dict = make_memo(row)
            memo_lists.append(memo_dict)
        return memo_lists

    def insert(self, memo):
        sql = "insert into memo (name,password,content,regDate,ip) values (%s,%s,%s,now(),%s)"
        curs = self.connection.cursor()
        count = curs.execute(sql, memo)
        self.connection.commit()
        return count

    def update(self, memo):
        sql = "update memo set content=%s, regDate=now(), ip=%s where idx=%s"
        curs = self.connection.cursor()
        count = curs.execute(sql, memo)
        self.connection.commit()
        return count

    def delete(self, idx):
        sql = "delete from memo where idx=" + str(idx)
        curs = self.connection.cursor()
        count = curs.execute(sql)
        self.connection.commit()
        return count


if __name__ == '__main__':
    # dao = Memo_DAO(None)
    connection = get_connection()
    dao = Memo_DAO(connection)
    total_count = dao.get_count()
    print(total_count)
    print("~" * 80)
    memo = dao.select_by_idx(124)
    if memo is not None:
        print(memo)
        print(memo['content'])
        print(memo['regDate'])
    else:
        print("글번호 없다!!!")
    print("~" * 80)
    memo_paging = m_paging.Paging(total_count=total_count, current_page=5, page_size=10, block_size=10)
    memo_list = dao.select_list(memo_paging.start_no, memo_paging.page_size)
    memo_paging.list = memo_list
    print(memo_paging)
    print("~" * 80)
    print(dao.delete(123))
    print("~" * 80)
    memo = ['한사람','1234','추가가될까?','192.168.0.123']
    print(memo)
    print(dao.insert(memo))
    print("~" * 80)
    memo = ['변경이될까?','192.168.0.123', '124']
    print(memo)
    print(dao.update(memo))
    memo = dao.select_by_idx(124)
    print(memo)
    print("~" * 80)



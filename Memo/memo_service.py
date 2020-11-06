from Memo.db_util import get_connection
import Memo.paging as m_paging
import Memo.memo_dao as m_dao


class Memo_Service:
    def __init__(self):
        self.connection = get_connection()
        self.dao = m_dao.Memo_DAO(self.connection)

    def __del__(self):
        if self.connection is not None:
            self.connection.close()

    def get_count(self):
        return self.dao.get_count()

    def select_by_idx(self, idx):
        return self.dao.select_by_idx(idx)

    def select_list(self, current_page, page_size, block_size):
        total_count = self.dao.get_count()
        paging = m_paging.Paging(total_count, current_page, page_size, block_size)
        memo_list = self.dao.select_list(paging.start_no, paging.page_size)
        paging.list = memo_list
        return paging

    def insert(self, memo_dict):
        print("서비스 insert :", type(memo_dict), memo_dict)
        data = [memo_dict['name'], memo_dict['password'], memo_dict['content'], memo_dict['ip']]
        count = self.dao.insert(memo=data)
        return count

    def update(self, memo_dict):
        print("서비스 update :", type(memo_dict), memo_dict)
        count = 0
        db_memo = self.dao.select_by_idx(memo_dict['idx'])
        if db_memo['password'] == memo_dict['password']:
            data = [memo_dict['content'], memo_dict['ip'], memo_dict['idx']]
            count = self.dao.update(memo=data)
        return count

    def delete(self, memo_dict):
        print("서비스 delete :", type(memo_dict), memo_dict)
        count = 0
        db_memo = self.dao.select_by_idx(memo_dict['idx'])
        if db_memo['password'] == memo_dict['password']:
            count = self.dao.delete(memo_dict['idx'])
        return count


if __name__ == '__main__':
    service = Memo_Service()
    print("개수 :", service.get_count())
    print("~" * 80)
    paging = service.select_list(14, 5, 5)
    print(paging)
    print("~" * 80)
    for m in paging.list:
        print(m['idx'], m['name'], m['content'], m['regDate'], m['ip'])
    print("~" * 80)


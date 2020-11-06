from Memo.db_util import get_connection
import Memo.memo_dao as memo_dao


class Paging:
    def __init__(self, total_count, current_page, page_size, block_size):
        self.total_count = total_count
        self.current_page = current_page
        self.page_size = page_size
        self.block_size = block_size
        if self.total_count < 0:
            self.total_count = 0
        if self.current_page <= 0:
            self.current_page = 1
        if self.page_size <= 1:
            self.page_size = 10
        if self.block_size <= 1:
            self.block_size = 10

        self.total_page = 0
        self.start_no = 0
        self.end_no = 0
        self.start_page = 0
        self.end_page = 0
        self.list = None
        self.total_page = (self.total_count - 1) // self.page_size + 1
        if self.current_page > self.total_page:
            self.current_page = 1
        self.start_no = (self.current_page - 1) * page_size
        self.end_no = self.start_no + self.page_size - 1
        if self.end_no > self.total_count:
            self.end_no = self.total_count
        self.start_page = (self.current_page - 1) // self.block_size * self.block_size + 1
        self.end_page = self.start_page + block_size - 1
        if self.end_page > self.total_page:
            self.end_page = self.total_page

    def __str__(self):
        page_dict = dict()
        page_dict['total_count'] = self.total_count
        page_dict['current_page'] = self.current_page
        page_dict['page_size'] = self.page_size
        page_dict['block_size'] = self.block_size
        page_dict['total_page'] = self.total_page
        page_dict['start_no'] = self.start_no
        page_dict['end_no'] = self.end_no
        page_dict['start_page'] = self.start_page
        page_dict['end_page'] = self.end_page
        page_dict['list'] = self.list
        return page_dict.__str__()

    def page_info(self):
        result = "전체 : {}개".format(self.total_count)
        if self.total_count > 0:
            result += "({}/{}Page)".format(self.current_page, self.total_page)
        return result

    def page_list(self):
        result = ""
        if self.total_count > 0:
            if self.start_page > 1:
                result += "[<a href='?p=" + str(self.start_page - 1)
                result += "&s=" + str(self.page_size) + "&b=" + str(self.block_size) + "'>이전</a>] "
            for page in range(self.start_page, self.end_page + 1):
                if page != self.current_page:
                    result += "[<a href='?p=" + str(page)
                    result += "&s=" + str(self.page_size) + "&b=" + str(self.block_size) + "'>" + str(page) + "</a>] "
                else:
                    result += "[" + str(page) + "] "
            if self.end_page < self.total_page:
                result += "[<a href='?p=" + str(self.end_page + 1)
                result += "&s=" + str(self.page_size) + "&b=" + str(self.block_size) + "'>다음</a>] "
        return result


if __name__ == '__main__':
    connection = get_connection()
    dao = memo_dao.Memo_DAO(connection)
    paging = Paging(dao.get_count(), 14, 10, 10)
    print(paging)
    print("~" * 80)
    memo_list = dao.select_list(paging.start_no, paging.page_size)
    print(memo_list)
    print("~" * 80)
    paging.list = memo_list
    print(paging)
    print("~" * 80)

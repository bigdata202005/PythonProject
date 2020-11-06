from Memo.memo_service import Memo_Service

service = Memo_Service()
print("개수 :", service.get_count())
print("~" * 80)
paging = service.select_list(14, 5, 5)
print(paging)
print("~" * 80)
for m in paging.list:
    print(m['idx'], m['name'], m['content'], m['regDate'], m['ip'])
print("~" * 80)

sql = """
      insert into pydb_test (name,age,gender) values ('한사람',33,1)
      insert into pydb_test (name,age,gender) values ('두사람',23,0)
      insert into pydb_test (name,age,gender) values ('세사람',43,1)
      insert into pydb_test (name,age,gender) values ('네사람',53,0)
      insert into pydb_test (name,age,gender) values ('오사람',63,1)
      insert into pydb_test (name,age,gender) values ('육사람',35,0)
      insert into pydb_test (name,age,gender) values ('칠사람',36,1)
      insert into pydb_test (name,age,gender) values ('팔사람',37,0)
    """
print(sql.split('\n'))
sql_list = [];
for data in sql.split('\n'):
    if len(data.strip()) != 0:
        sql_list.append(data.strip())

print(len(sql_list))
print(sql_list)

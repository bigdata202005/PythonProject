# A 씨는 게시판 프로그램을 작성하고 있다.
# 그런데 게시물의 총 건수와 한 페이지에 보여 줄 게시물 수를 입력으로 주었을 때
# 총 페이지 수를 출력하는 프로그램이 필요하다고 한다.
# ※ 이렇게 게시판의 페이지 수를 보여 주는 것을 "페이징"한다고 부른다.
#
# 함수 이름은? getTotalPage
# 입력 받는 값은? 게시물의 총 건수(m), 한 페이지에 보여줄 게시물 수(n)
# 출력하는 값은? 총 페이지수

def getTotalPage(total_count, page_size):
    # 총 페이지 수 = (총 건수 / 한 페이지당 보여 줄 건수) + 1
    # return (total_count//page_size) + 1
    # 배수면 +1을하지 않는다(삼항 연산)
    # return total_count // page_size if total_count % page_size == 0 else (total_count // page_size) + 1
    # 제일 효과적인 방법!!!
    return (total_count - 1) // page_size + 1


if __name__ == '__main__':
    print(getTotalPage(5, 10))  # 1 출력
    print(getTotalPage(15, 10))  # 2 출력
    print(getTotalPage(25, 10))  # 3 출력
    print(getTotalPage(30, 10))  # 4 출력 --- 이부분이 잘못되었다 --- 3출력

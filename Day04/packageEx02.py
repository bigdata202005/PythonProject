# from game.sound import *
# echo.echo_test()  # NameError: name 'echo_test' is not defined

# sound 패키지의 모든 모듈을 임포트해서 사용하고 싶다
# 위처럼 사용하면 에러이다!!!
# 위처럼 사용하려면 _init_.py파일을 수정해야 한다.

from game.sound import *
echo.echo_test()
echo2.echo_test2()


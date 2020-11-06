## [파이썬 가상환경(virtualenv)만들기](https://offbyone.tistory.com/74)

파이썬을 사용할 때 기본으로 제공되는 라이브러리만 사용되지 않고 많은 기능을 제공하는 라이브러리들을 추가 하여 사용하게 됩니다. 이러한 라이브러리가 특정 프로젝트에서만 사용되거나 프로젝트를 배포할 때 필요한 라이브러리만 포함시켜 배포하고 싶을 경우가 있을 것입니다.



이럴때 사용할 수 있는것이 가상환경(virtualenv) 입니다. 가상환경을 만들고, 그 가상환경에서 라이브러리를 추가하면 추가된 라이브러리는 그 가상환경에서만 사용 되어집니다.



이 글에서는 Python 3.6 버전을 사용하여 테스트해 봅니다. Python의 설치는 이전에 작성된 글 **"[Python 설치하기](https://offbyone.tistory.com/46)"** 를 참고 하세요. 설치 운영체제는  Windows 10 입니다.



파이썬 프로그램은 C:\util\Python36-32 폴더에 설치되어 있다고 가정합니다. 각자 자신에 원하는 곳에 설치가 되어 있을 것입니다. 작업의 편의를 위해 파이썬이 설치된 위치와 설치된곳 아래의 Scripts 폴더를 PATH 에 등록합니다.(Windows는 Scripts 폴더이고, Linux 환경

이라면 bin 폴더일 것입니다.)



설치 폴더 바로 아래에 python.exe 파일이 있고, Scripts 폴더 아래에는 easy_install.exe  파일과 pip.exe 파일이 있습니다. 앞으로 설치할 virtualenv.exe 파일도 이 폴더 아래에 설치가 됩니다.



파이썬 패키지 관리자인 pip.exe 파일을 Python 3.4 버전부터 미리 포함되어 있습니다. 이전 버전을 사용한다면 easy_install 프로그램을 이용해서 pip.exe 를 먼저 설치합니다.



**C:\>esay_install pip**





여러개의 파이썬 프로젝트를 관리하면서 각 프로젝트마다 사용되는 라이브러리가 충돌을 한다던가 하는 경우에도 가상환경을 사용하여 분리할 수 있습니다.



가상 환경 없이 설치한 파이썬 라이브러리는 전역으로 설치됩니다. 이렇게 설치한 라이브러리는 모든 사용자와 모든 프로젝트에서 사용할 수 있습니다.



가상환경을 다음과 같이 설치합니다.



**C:\>pip install virtualenv**



그러면 파이썬이 설치된 폴드 아래 Scripts 폴더에 virtualenv.exe 파일이 생겼을 것입니다.



이제 가상환경을 만들어 봅니다. 가상환경 파일이 생성될곳을 C:\>workspace\python 으로 하겠습니다. 다음 명령을 실행합니다.



**C:\>workspace\python>virtualenv ProjectEnv**



이 명령은 새 환경 ProjectEnv 를 만듭니다. 만든 새 환경을 사용하려면 먼저 활성화해야 합니다. 새환경 폴더 아래 Scripts 폴더 아래에 activate.bat 파일을 실행합니다.



**C:\>workspace\python>cd ProjectEnv\Scripts**

**C:\>workspace\python\ProjectEnv\Scripts>activate**



환경을 활성화하면 환경의 이름이 명령 프롬프트에 표시되어 현재 가상 환경에 있음을 알립니다. 가상 환경에서 라이브러리를 설치하거나 스크립트를 실행하면 그 환경에만 영향이 있습니다.



**(ProjectEnv) C:\workspace\python\ProjectEnv\Scripts>python**

**>>>^Z**



deactivate 명령으로 환경에서 떠날 수 있습니다. 다시 가상환경으로 들어가기 위해서는 activate 명령을 다시 실행하면 됩니다.



**(ProjectEnv) C:\workspace\python\ProjectEnv\Scripts>deactivate**



![가상환경 들어가기 나가기](https://t1.daumcdn.net/cfile/tistory/9961FD3E5AC4CE510B)





프로젝트별로 다른 가상환경을 만들어두면 나중에 프로젝트를 배포할때 환경 전체를 압축해서 배포하는것이 가능합니다. 프로젝트를 받는 사람은 같은 버전의 파이썬이 설치되어 있어야 합니다.













이클립스 PyDev 환경에서 가상환경을 사용하는 방법을 보겠습니다.



\- 메뉴에서 Window -> Preferences 를 실행합니다.

\- 좌측 트리에서 PyDev -> Interpreters -> Python Interpreter 를 선택합니다.

\- 우측 상단의 New... 버튼을 눌러 앞에서 만든 가상환경의 python.exe를 선택합니다.



![이클립스 설정에서 PyDev 설정](https://t1.daumcdn.net/cfile/tistory/9955EE3B5AC4CE5C35)





\- 새 인터프리터가 등록되었습니다. Apply 버튼을 눌러 적용한 다음 OK 버튼을 누릅니다.



![ Python Interpreter 설정 완료](https://t1.daumcdn.net/cfile/tistory/99E3523B5AC4CE670D)





\- PyDev 프로젝트를 생성합니다. Interpreter 항목에서 앞에서 등록한 인터프리터를 선택합니다.



![PyDev 프로젝트 생성](https://t1.daumcdn.net/cfile/tistory/990604395AC4CE7508)





이것으로 Windows 10 + Python 3.6 환경에서 가상환경을 설정하고 사용하는 방법에 대해서 알아 보았습니다.



출처: https://offbyone.tistory.com/74 [쉬고 싶은 개발자]
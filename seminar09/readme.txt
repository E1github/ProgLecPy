pip install virtualenv

Set-ExecutionPolicy Unrestricted
��������� �����  ����  ��� 20:57
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
Maxim Denissov  ����  ��� 20:58
Set-ExecutionPolicy RemoteSigned
������� �������� 21:03
pip install -U pip setuptools # - U-���������� upgrade, ����� ������� ��� ��� ����� �������, ������� ��������� ��������,# � ������ ������ setuptoolspython.exe -m pip install -U pip setuptools #- ���� �����


ip install -U pip setuptools # - U-���������� upgrade, ����� ������� ��� ��� ����� �������, ������� ��������� ��������,
# � ������ ������ setuptools
python.exe -m pip install -U pip setuptools #- ���� �����
python -m venv new_venv # - ������� ����������� ���������
# source venv/bin/activate - ��������� �� ��� ������
venv\Scripts\activate # - ��������� � ������� (����������� \ - �������� ����)
deactivate # - ����������� ������������ ���������
pip freeze # - ����������� ������������� ������(����������) (������ ���� ������������)
pip install -U pip setuptools # - U-���������� upgrade, ����� ������� ��� ��� ����� �������, ������� ��������� ��������,
# � ������ ������ setuptools
python.exe -m pip install -U pip setuptools #- ���� �����
pip install requests lxml # - ��������� ��������� requests � lxml - ���� ����� ���������� ��������� ���������,
# �� ����� ����������� �� ����� ������
pip uninstall lxml -y # - �������� ����������, � ������ ������ lxml
pip uninstall -y -r requirements.txt # - ������� ��� ����������, ������� ���� ��������� � ����� requirements.txt
pip freeze > requirements.txt # - ������ ���� � ������������� (� �� ������������� ��� ���������� � ������ ������ �������)
pip install -r requirements.txt # - ������������� ��� ���������� � �������������

cd # - ������� � ������ �����
cd.. # - �� ������� ����

��� ������ ���� pycharm �� ����� ����������
https://www.youtube.com/watch?v=3SvmrzqVmXo
https://www.jetbrains.com/help/pycharm/creating-virtual-environment.html#existing-environment
pip install virtualenv

Set-ExecutionPolicy Unrestricted
јлександр ‘окин  кому  ¬се 20:57
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
Maxim Denissov  кому  ¬се 20:58
Set-ExecutionPolicy RemoteSigned
Ќиколай ћануилов 21:03
pip install -U pip setuptools # - U-сокращенно upgrade, далее следуют им€ или имена модулей, которые требуетс€ обновить,# в данном случае setuptoolspython.exe -m pip install -U pip setuptools #- тоже самое


ip install -U pip setuptools # - U-сокращенно upgrade, далее следуют им€ или имена модулей, которые требуетс€ обновить,
# в данном случае setuptools
python.exe -m pip install -U pip setuptools #- тоже самое
python -m venv new_venv # - создать виртуальное окружение
# source venv/bin/activate - активаци€ ¬ќ дл€ линукс
venv\Scripts\activate # - активаци€ в виндоус (об€зательно \ - обратный слэш)
deactivate # - деактиваци€ виртуального окружени€
pip freeze # - распечатает установленные пакеты(библиотеки) (создаЄт файл зависимостей)
pip install -U pip setuptools # - U-сокращенно upgrade, далее следуют им€ или имена модулей, которые требуетс€ обновить,
# в данном случае setuptools
python.exe -m pip install -U pip setuptools #- тоже самое
pip install requests lxml # - установка библиотек requests и lxml - если нужно установить несколько библиотек,
# то можно перечислить их через пробел
pip uninstall lxml -y # - удаление библиотеки, в данном случае lxml
pip uninstall -y -r requirements.txt # - удал€ет все библиотеки, которые были прописаны в файле requirements.txt
pip freeze > requirements.txt # - создаЄт файл с зависимост€ми (в нЄм прописываютс€ все библиотеки и версии нашего проекта)
pip install -r requirements.txt # - устанавливаем все библиотеки с зависимост€ми

cd # - перейти в нужную папку
cd.. # - на уровень выше

„то делать если pycharm не видит библиотеку
https://www.youtube.com/watch?v=3SvmrzqVmXo
https://www.jetbrains.com/help/pycharm/creating-virtual-environment.html#existing-environment
1.
    Шаги: перетйи в дирректорию нужную с помощью cd  и запустить следущие команды
    flake8 encodetest.py
    python -m doctest -o NORMALIZE_WHITESPACE -v encodetest.py
2. 
    Шаги: перетйи в дирректорию нужную с помощью cd  и запустить следущие команды
    flake8 deocdeetest.py
    python -m pytest -v decodetest.py
3. 
    Шаги: перетйи в дирректорию нужную с помощью cd  и запустить следущие команды
    flake8 ohetestu.py
    python -m unittest ohetestu.py
4. 
    Шаги: перетйи в дирректорию нужную с помощью cd  и запустить следущие команды
    flake8 transformtestpytest.py
    python -m pytest transformtestpytest.py
5. 
    Шаги: перейти в дирректорию нужную с помощью cd  и запустить следущие команды
    сделал доплнительный файл для реализации и тестов(как и укзаано в решение)
    flake8 testdate.py
    python -m pytest -q testdate.py --cov=date --cov-report html

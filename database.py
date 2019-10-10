import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="PyCharm",
    passwd="",
    database="test"
)


def updateInfo(wierszZ_name,wartoscZ_value,wierszG_name,wartoscG_value):
    mycursor = mydb.cursor()
    """Podajemy informacje gdzie:
        wierszZ_name    : Zmien w wierszu wierszZ_name
        wartoscZ_value  : Wartosc wartoscZ_value
        wierszG_name    : Gdzie wiersz nazwe wierszG_name
        wartoscG_value  : A wartosc wynosi wartoscG_value
    """
    default = ("UPDATE python SET `wierszZmieniany_nazwa` = 'wierszZmieniany_wartosc' WHERE `python`.`wierszGdzie_nazwa` = 'wierszGdzie_wartosc'")

    default.replace("wierszZmieniany_nazwa", wierszZ_name)
    default.replace("wierszZmieniany_wartosc", wartoscZ_value)
    default.replace("wierszGdzie_nazwa", wierszG_name)
    default.replace("wierszGdzie_wartosc", wartoscG_value)
    mycursor.execute(default)
    mydb.commit()

updateInfo("text2","192.168.1.23","id","4")

"""PROBLEM"""

Traceback (most recent call last):
  File "D:/Pulpit/PyCharm/Project1/###Pliki/Aplikacja/database.py", line 28, in <module>
    updateInfo("text2","192.168.1.23","id","4")
  File "D:/Pulpit/PyCharm/Project1/###Pliki/Aplikacja/database.py", line 25, in updateInfo
    mycursor.execute(default)
  File "D:\Pulpit\PyCharm\Project1\venv\lib\site-packages\mysql\connector\cursor.py", line 551, in execute
    self._handle_result(self._connection.cmd_query(stmt))
  File "D:\Pulpit\PyCharm\Project1\venv\lib\site-packages\mysql\connector\connection.py", line 490, in cmd_query
    result = self._handle_result(self._send_cmd(ServerCmd.QUERY, query))
  File "D:\Pulpit\PyCharm\Project1\venv\lib\site-packages\mysql\connector\connection.py", line 395, in _handle_result
    raise errors.get_exception(packet)
mysql.connector.errors.ProgrammingError: 1054 (42S22): Unknown column 'python.wierszGdzie_nazwa' in 'where clause'

Process finished with exit code 1

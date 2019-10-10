import mysql.connector

mydb = mysql.connector.connect(
    host="host",
    user="user",
    passwd="password",
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
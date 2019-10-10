import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="PyCharm",
    passwd="",
    database="test"
)


def updateInfo(wierszZname,wartoscZvalue,wierszGname,wartoscGvalue):
    """
    Używanie/How to use:
        updateInfo(
        wierszZ_name - nazwa kolumny w ktorej zmieniamy wartosc,
        wartoscZ_value - wartosc rekordu ktory zmieniamy,
        wierszG_name - nazwa kolumny ktory identyfikuje wiersz,
        wartoscG_value - wartosc ktora identyfikuje wiersz,
        )
    """
    mycursor=mydb.cursor()
    wartoscZvalue = ('"' + wartoscZvalue + '"')
    lista=["UPDATE python SET ", wierszZname, " = ", wartoscZvalue, " WHERE ", wierszGname, " = ", wartoscGvalue]
    sql=(str(lista[0]) + str(lista[1]) + str(lista[2]) + str(lista[3]) + str(lista[4]) + str(lista[5]) + str(
        lista[6]) + str(lista[7]))

    print(sql)

    mycursor.execute(sql)
    mydb.commit()

    return(mycursor.rowcount, "record(s) affected")

updateInfo('text1','Uczen04','id','1')

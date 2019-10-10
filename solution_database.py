import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="user",
    passwd="password",
    database="test"
)


def updateInfo(wierszZname,wartoscZvalue,wierszGname,wartoscGvalue):
    """
    Używanie/How to use:
        updateInfo('textBox','something','id','1')
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

    print(sql) #Pokazuje co dodalismy / Show what we added

    mycursor.execute(sql)
    mydb.commit()

    return("Zmieniono ",mycursor.rowcount, "rekord(ów)") #Zwraca ile rekordow zostalo zmienionych / Show how much records we changed

updateInfo('textBox','something','id','1')
    
 -----------------------# What we see #----------------------------
    UPDATE python SET textBox = "something" WHERE id = 1

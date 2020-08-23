import sqlite3
#Сама база в директории Part_1

with sqlite3.connect('sqlite.db') as conn:
    cursor = conn.cursor()

    print('Топовые спортсмены:')
    for row in cursor.execute("SELECT * FROM sportsman"):
        print(row)

    print()

    print('Рекорды по дисциплинам:')
    for row in cursor.execute("SELECT name, record FROM competition"):
        print(row)

    print()

    print('Спортсмены родившиеся в 1988:')
    for row in cursor.execute("SELECT * FROM sportsman WHERE YEAR_BD = 1988"):
        print(row)

    print()

    print('Установленные мировые результаты с 15-05-2010:')
    #Не понимаю как сравнить время, уже разные варианты перепробовал
    for row in cursor.execute("SELECT * FROM result WHERE HOLD_DATE\
        BETWEEN 2010-05-15 AND 2045-05-15"):
        print(row)

    
conn.close()

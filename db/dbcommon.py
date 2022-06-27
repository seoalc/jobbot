import pymysql.cursors

############# проверка наличия откликах для текущего резюме ################
def checkResponsesForApplicant (applId, emplId):
    a = {'applId': applId, 'emplId': emplId}
    # Подключиться к базе данных.
    connection = pymysql.connect(host='127.0.0.1',
                                 user='root',
                                 password='pass',
                                 db='jobbot',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)
    print ("connect successful checkResponsesForApplicant!")
    try:
        with connection.cursor() as cursor:
            # SQL
            sql = "SELECT `id` FROM `responses` WHERE `appl-id` = %s AND `empl-id` = %s"
            # Выполнить команду запроса (Execute Query).
            # есть пользователь с этим ником в базе
            res = cursor.execute(sql, tuple(a.values()))
            return res
    finally:
        # Закрыть соединение (Close connection).
        connection.close()

############# выбрать все направления деятельности ################
def getAllLineBusiness ():
    # Подключиться к базе данных.
    connection = pymysql.connect(host='127.0.0.1',
                                 user='root',
                                 password='pass',
                                 db='jobbot',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)
    print ("connect successful getAllLineBusiness!")
    try:
        with connection.cursor() as cursor:
            # SQL
            sql = "SELECT * FROM `linebusiness`"
            # Выполнить команду запроса (Execute Query).
            # есть пользователь с этим ником в базе
            res = cursor.execute(sql)
            results = cursor.fetchall()
            return results
    finally:
        # Закрыть соединение (Close connection).
        connection.close()

############# выбрать одно направление деятельности по id ################
def getLineBusinessById (id):
    # Подключиться к базе данных.
    connection = pymysql.connect(host='127.0.0.1',
                                 user='root',
                                 password='pass',
                                 db='jobbot',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)
    print ("connect successful getLineBusinessById!")
    try:
        with connection.cursor() as cursor:
            # SQL
            sql = "SELECT * FROM `linebusiness` WHERE `id` = %s"
            # Выполнить команду запроса (Execute Query).
            # есть пользователь с этим ником в базе
            res = cursor.execute(sql, (id))
            results = cursor.fetchall()
            return results
    finally:
        # Закрыть соединение (Close connection).
        connection.close()

############# запись нового отклика в базу ################
async def addResponseForApplicant (applId, emplId):
    a = {'applId': applId, 'emplId': emplId}
    # Подключиться к базе данных.
    connection = pymysql.connect(host='127.0.0.1',
                                 user='root',
                                 password='pass',
                                 db='jobbot',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)
    print ("connect successful addResponseForApplicant!")
    cursor = connection.cursor()
    try:
        # SQL
        sql = "INSERT INTO `responses` "\
        "(`appl-id`, `empl-id`) "\
        "VALUES (%s, %s)"
        # Выполнить команду запроса (Execute Query).
        # есть пользователь с этим ником в базе
        res = cursor.execute(sql, tuple(a.values()))
        connection.commit()
        return res
    finally:
        # Закрыть соединение (Close connection).
        connection.close()

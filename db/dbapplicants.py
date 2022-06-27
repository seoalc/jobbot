import pymysql.cursors

############# проверка наличия резюме в базе по tg id ################
def checkApplByTgId (tg_id):
    # Подключиться к базе данных.
    connection = pymysql.connect(host='127.0.0.1',
                                 user='root',
                                 password='pass',
                                 db='jobbot',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)
    print ("connect successful checkApplByTgId!")
    try:
        with connection.cursor() as cursor:
            # SQL
            sql = "SELECT `tg-login` FROM `applicants` WHERE `tg-id` = %s"
            # Выполнить команду запроса (Execute Query).
            # есть пользователь с этим ником в базе
            res = cursor.execute(sql, (tg_id))
            return res
    finally:
        # Закрыть соединение (Close connection).
        connection.close()

############# выбрать все резюме данного пользователя ################
def getAllApplsForUserByTGID (tg_id):
    # Подключиться к базе данных.
    connection = pymysql.connect(host='127.0.0.1',
                                 user='root',
                                 password='pass',
                                 db='jobbot',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)
    print ("connect successful getAllApplsForUserByTGID!")
    try:
        with connection.cursor() as cursor:
            # SQL
            sql = "SELECT `id`, `line-business`, `line-business-id`, `career-objective` FROM `applicants` WHERE `tg-id` = %s"
            # Выполнить команду запроса (Execute Query).
            # есть пользователь с этим ником в базе
            res = cursor.execute(sql, (tg_id))
            results = cursor.fetchall()
            return results
    finally:
        # Закрыть соединение (Close connection).
        connection.close()

############# получение информации о резюме по id ################
def getApplInfoById (applId):
    # Подключиться к базе данных.
    connection = pymysql.connect(host='127.0.0.1',
                                 user='root',
                                 password='pass',
                                 db='jobbot',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)
    print ("connect successful getApplInfoById!")
    try:
        with connection.cursor() as cursor:
            # SQL
            sql = "SELECT `line-business`, `career-objective` FROM `applicants` WHERE `id` = %s"
            # Выполнить команду запроса (Execute Query).
            # есть пользователь с этим ником в базе
            res = cursor.execute(sql, (applId))
            results = cursor.fetchone()
            return results
    finally:
        # Закрыть соединение (Close connection).
        connection.close()

############# получение информации о резюме по id ################
def getApplInfoByApplId (applId):
    # Подключиться к базе данных.
    connection = pymysql.connect(host='127.0.0.1',
                                 user='root',
                                 password='pass',
                                 db='jobbot',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)
    print ("connect successful getApplInfoById!")
    try:
        with connection.cursor() as cursor:
            # SQL
            sql = "SELECT * FROM `applicants` WHERE `id` = %s"
            # Выполнить команду запроса (Execute Query).
            # есть пользователь с этим ником в базе
            res = cursor.execute(sql, (applId))
            results = cursor.fetchone()
            return results
    finally:
        # Закрыть соединение (Close connection).
        connection.close()

############# получение PDF-файла по id ################
def getPDFById (applId):
    # Подключиться к базе данных.
    connection = pymysql.connect(host='127.0.0.1',
                                 user='root',
                                 password='pass',
                                 db='jobbot',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)
    print ("connect successful getPDFByTGId!")
    try:
        with connection.cursor() as cursor:
            # SQL
            sql = "SELECT `pdf-file` FROM `applicants` WHERE `id` = %s"
            # Выполнить команду запроса (Execute Query).
            # есть пользователь с этим ником в базе
            res = cursor.execute(sql, (applId))
            results = cursor.fetchone()
            return results
    finally:
        # Закрыть соединение (Close connection).
        connection.close()

############# получение информации о резюме по id для создания разовой работы соискателем ################
def getIdAndNameAppl (tg_id):
    # Подключиться к базе данных.
    connection = pymysql.connect(host='127.0.0.1',
                                 user='root',
                                 password='pass',
                                 db='jobbot',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)
    print ("connect successful getIdAndNameAppl!")
    try:
        with connection.cursor() as cursor:
            # SQL
            sql = "SELECT `id`, `firstname`, `lastname` FROM `applicants` WHERE `tg-id` = %s"
            # Выполнить команду запроса (Execute Query).
            # есть пользователь с этим ником в базе
            res = cursor.execute(sql, (tg_id))
            results = cursor.fetchone()
            return results
    finally:
        # Закрыть соединение (Close connection).
        connection.close()

############# получение всей информации о резюме по id для работодателя ################
def getAllApplInfoById (applId):
    # Подключиться к базе данных.
    connection = pymysql.connect(host='127.0.0.1',
                                 user='root',
                                 password='pass',
                                 db='jobbot',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)
    print ("connect successful getAllApplInfoById!")
    try:
        with connection.cursor() as cursor:
            # SQL
            sql = "SELECT * FROM `applicants` WHERE `tg-id` = %s"
            # Выполнить команду запроса (Execute Query).
            # есть пользователь с этим ником в базе
            res = cursor.execute(sql, (applId))
            results = cursor.fetchone()
            return results
    finally:
        # Закрыть соединение (Close connection).
        connection.close()

############# получение TG ID владельца компании по id компании ################
def getCompTGIdByCompId (compId):
    # Подключиться к базе данных.
    connection = pymysql.connect(host='127.0.0.1',
                                 user='root',
                                 password='pass',
                                 db='jobbot',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)
    print ("connect successful getCompTGIdByCompId!")
    try:
        with connection.cursor() as cursor:
            # SQL
            sql = "SELECT `tg-id` FROM `companies` WHERE `id` = %s"
            # Выполнить команду запроса (Execute Query).
            # есть пользователь с этим ником в базе
            res = cursor.execute(sql, (compId))
            results = cursor.fetchone()
            return results
    finally:
        # Закрыть соединение (Close connection).
        connection.close()

####### поиск вакансий по направлению деятельности и должности из резюме #######
def searchAllEmplsByText (lineBusiness, careerObjective):
    # Подключиться к базе данных.
    connection = pymysql.connect(host='127.0.0.1',
                                 user='root',
                                 password='pass',
                                 db='jobbot',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)
    print ("connect successful searchAllEmplsByText!")
    try:
        with connection.cursor() as cursor:
            # SQL
            sql = "SELECT `id`, `company-name`, `line-business`, `career-objective` FROM `employers` WHERE `line-business` LIKE %s"
            # Выполнить команду запроса (Execute Query).
            # есть пользователь с этим ником в базе
            res = cursor.execute(sql, (lineBusiness))
            results = cursor.fetchall()
            return results
    finally:
        # Закрыть соединение (Close connection).
        connection.close()

####### поиск компаний по id направления деятельности #######
def searchAllCompByLineBuissId (lineBusinessId):
    # Подключиться к базе данных.
    connection = pymysql.connect(host='127.0.0.1',
                                 user='root',
                                 password='pass',
                                 db='jobbot',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)
    print ("connect successful searchAllCompByLineBuissId!")
    try:
        with connection.cursor() as cursor:
            # SQL
            sql = "SELECT `id`, `company-name`, `line-business` FROM `companies` WHERE `line-business-id` = %s"
            # Выполнить команду запроса (Execute Query).
            # есть пользователь с этим ником в базе
            res = cursor.execute(sql, (lineBusinessId))
            results = cursor.fetchall()
            return results
    finally:
        # Закрыть соединение (Close connection).
        connection.close()

####### выборка вакансий по id компании #######
def searchAllEmplsByCompId (companyId):
    # Подключиться к базе данных.
    connection = pymysql.connect(host='127.0.0.1',
                                 user='root',
                                 password='pass',
                                 db='jobbot',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)
    print ("connect successful searchAllEmplsByCompId!")
    try:
        with connection.cursor() as cursor:
            # SQL
            sql = "SELECT `id`, `career-objective`, `desired-salary`, `workformat` FROM `employers` WHERE `company-id` = %s"
            # Выполнить команду запроса (Execute Query).
            # есть пользователь с этим ником в базе
            res = cursor.execute(sql, (companyId))
            results = cursor.fetchall()
            return results
    finally:
        # Закрыть соединение (Close connection).
        connection.close()

####### выборка последних компаний, когда для резюме по его направлению
####### деятельности ничего не найдено #######
def searchAllLastComp ():
    # Подключиться к базе данных.
    connection = pymysql.connect(host='127.0.0.1',
                                 user='root',
                                 password='pass',
                                 db='jobbot',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)
    print ("connect successful searchAllLastComp!")
    try:
        with connection.cursor() as cursor:
            # SQL
            sql = "SELECT `id`, `company-name`, `line-business` FROM `companies`"
            # Выполнить команду запроса (Execute Query).
            # есть пользователь с этим ником в базе
            res = cursor.execute(sql)
            results = cursor.fetchall()
            return results
    finally:
        # Закрыть соединение (Close connection).
        connection.close()

####### выборка последних вакансий без привязки по id для предыдущей функции #######
####### когда для резюме по его направлению деятельности ничего не найдено #######
def searchAllLastEmpls (companyId):
    # Подключиться к базе данных.
    connection = pymysql.connect(host='127.0.0.1',
                                 user='root',
                                 password='pass',
                                 db='jobbot',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)
    print ("connect successful searchAllLastEmpls!")
    try:
        with connection.cursor() as cursor:
            # SQL
            sql = "SELECT `id`, `career-objective`, `desired-salary`, `workformat` FROM `employers` WHERE `company-id` = %s"
            # Выполнить команду запроса (Execute Query).
            # есть пользователь с этим ником в базе
            res = cursor.execute(sql, (companyId))
            results = cursor.fetchall()
            return results
    finally:
        # Закрыть соединение (Close connection).
        connection.close()

############# получение информации о вакансии по её id ################
def getOneEmplInfo (emplId):
    # Подключиться к базе данных.
    connection = pymysql.connect(host='127.0.0.1',
                                 user='root',
                                 password='pass',
                                 db='jobbot',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)
    print ("connect successful getOneEmplInfo!")
    try:
        with connection.cursor() as cursor:
            # SQL
            sql = "SELECT * FROM `employers` WHERE `id` = %s"
            # Выполнить команду запроса (Execute Query).
            # есть пользователь с этим ником в базе
            res = cursor.execute(sql, (emplId))
            results = cursor.fetchone()
            return results
    finally:
        # Закрыть соединение (Close connection).
        connection.close()

############# запись нового дополнительного образования для пользователя в базу ################
async def addNewEducation (state):
    # Подключиться к базе данных.
    connection = pymysql.connect(host='127.0.0.1',
                                 user='root',
                                 password='pass',
                                 db='jobbot',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)
    print ("connect successful addNewEducation!")
    cursor = connection.cursor()
    try:
        async with state.proxy() as data:
            # SQL
            sql = "INSERT INTO `newedus` "\
            "(`tg-id`, `tg-login`, `line-business`, `line-business-id`, `education-form`) "\
            "VALUES (%s, %s, %s, %s, %s)"
            # Выполнить команду запроса (Execute Query).
            # есть пользователь с этим ником в базе
            res = cursor.execute(sql, tuple(data.values()))
            connection.commit()
            return res
    finally:
        # Закрыть соединение (Close connection).
        connection.close()

######## получение из базы имя пункта резюме, который будет обновляться #######
def getApplDataByDataName (dataName, tg_id):
    # Подключиться к базе данных.
    connection = pymysql.connect(host='127.0.0.1',
                                 user='root',
                                 password='pass',
                                 db='jobbot',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)
    print ("connect successful applicants!")
    try:
        with connection.cursor() as cursor:
            # SQL
            sql = "SELECT `" + dataName + "` FROM `applicants` WHERE `tg-id` = %s"
            # Выполнить команду запроса (Execute Query).
            # выбрать значение по названию колонки
            res = cursor.execute(sql, (tg_id))
            results = cursor.fetchone()
            return results
    finally:
        # Закрыть соединение (Close connection).
        connection.close()

############# обновление резюме ################
async def updtApplInfo (state):

    # Подключиться к базе данных.
    connection = pymysql.connect(host='127.0.0.1',
                                 user='root',
                                 password='pass',
                                 db='jobbot',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)
    print ("connect successful updtApplInfo!")
    cursor = connection.cursor()
    try:
        async with state.proxy() as data:
            a = {'userData': data['userData'], 'tg-id': data['tg-id']}
            # SQL
            sql = "UPDATE `applicants` SET "\
            "`" + data['dataName'] + "` = %s WHERE `tg-id` = %s"
            # Выполнить команду запроса (Execute Query).
            # перевожу данные в кортеж для вставки
            res = cursor.execute(sql, tuple(a.values()))
            connection.commit()
            return res
    finally:
        # Закрыть соединение (Close connection).
        connection.close()

############# обновление pdf ################
async def updtPDFById (state):

    # Подключиться к базе данных.
    connection = pymysql.connect(host='127.0.0.1',
                                 user='root',
                                 password='pass',
                                 db='jobbot',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)
    print ("connect successful updtPDFById!")
    cursor = connection.cursor()
    try:
        async with state.proxy() as data:
            a = {'pdffile': data['pdfFile'], 'tg-id': data['tg_id']}
            # SQL
            sql = "UPDATE `applicants` SET "\
            "`pdf-file` = %s WHERE `tg-id` = %s"
            # Выполнить команду запроса (Execute Query).
            # перевожу данные в кортеж для вставки
            res = cursor.execute(sql, tuple(a.values()))
            connection.commit()
            return res
    finally:
        # Закрыть соединение (Close connection).
        connection.close()

############# удаление резюме из базы ################
async def deleteApplById (applId):
    # Подключиться к базе данных.
    connection = pymysql.connect(host='127.0.0.1',
                                 user='root',
                                 password='pass',
                                 db='jobbot',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)
    print ("connect successful deleteApplById!")
    cursor = connection.cursor()
    try:
        with connection.cursor() as cursor:
            # SQL
            sql = "DELETE FROM `applicants` WHERE `id` = %s"
            # Выполнить команду запроса (Execute Query).
            # перевожу данные в кортеж для вставки
            res = cursor.execute(sql, (applId))
            connection.commit()
            return res
    finally:
        # Закрыть соединение (Close connection).
        connection.close()

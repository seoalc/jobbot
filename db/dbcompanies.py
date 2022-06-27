import pymysql.cursors

############# проверка наличия компании в базе по tg id ################
def checkCompByTgId (tg_id):
    # Подключиться к базе данных.
    connection = pymysql.connect(host='127.0.0.1',
                                 user='root',
                                 password='pass',
                                 db='jobbot',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)
    print ("connect successful checkCompByTgId!")
    try:
        with connection.cursor() as cursor:
            # SQL
            sql = "SELECT `tg-login` FROM `companies` WHERE `tg-id` = %s"
            # Выполнить команду запроса (Execute Query).
            # есть пользователь с этим ником в базе
            res = cursor.execute(sql, (tg_id))
            return res
    finally:
        # Закрыть соединение (Close connection).
        connection.close()

############# проверка количества разовых работ у пользователя по его id ################
def checkOneTimeWorksByTGId (tg_id):
    # Подключиться к базе данных.
    connection = pymysql.connect(host='127.0.0.1',
                                 user='root',
                                 password='pass',
                                 db='jobbot',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)
    print ("connect successful checkOneTimeWorksByTGId!")
    try:
        with connection.cursor() as cursor:
            # SQL
            sql = "SELECT `id` FROM `onetimeworks` WHERE `tg-id` = %s"
            # Выполнить команду запроса (Execute Query).
            # есть пользователь с этим ником в базе
            res = cursor.execute(sql, (tg_id))
            return res
    finally:
        # Закрыть соединение (Close connection).
        connection.close()

############# проверка наличия резюме в базе по tg id ################
def checkEmplByTgId (tg_id):
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
            sql = "SELECT `id` FROM `employers` WHERE `tg-id` = %s"
            # Выполнить команду запроса (Execute Query).
            # есть пользователь с этим ником в базе
            res = cursor.execute(sql, (tg_id))
            return res
    finally:
        # Закрыть соединение (Close connection).
        connection.close()

############# получение id компании и города дислокации ################
def getIdAndCityComp (tg_id):
    # Подключиться к базе данных.
    connection = pymysql.connect(host='127.0.0.1',
                                 user='root',
                                 password='pass',
                                 db='jobbot',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)
    print ("connect successful getIdAndCityComp!")
    try:
        with connection.cursor() as cursor:
            # SQL
            sql = "SELECT id, city FROM `companies` WHERE `tg-id` = %s"
            # Выполнить команду запроса (Execute Query).
            # есть пользователь с этим ником в базе
            res = cursor.execute(sql, (tg_id))
            results = cursor.fetchone()
            return results
    finally:
        # Закрыть соединение (Close connection).
        connection.close()

############# получение название компании ################
def getNameComp (tg_id):
    # Подключиться к базе данных.
    connection = pymysql.connect(host='127.0.0.1',
                                 user='root',
                                 password='pass',
                                 db='jobbot',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)
    print ("connect successful getNameComp!")
    try:
        with connection.cursor() as cursor:
            # SQL
            sql = "SELECT `company-name` FROM `companies` WHERE `tg-id` = %s"
            # Выполнить команду запроса (Execute Query).
            # есть пользователь с этим ником в базе
            res = cursor.execute(sql, (tg_id))
            results = cursor.fetchone()
            return results
    finally:
        # Закрыть соединение (Close connection).
        connection.close()

############# получение данных о компании для просмотра соискателем ################
def getOneCompanyInfo (companyId):
    # Подключиться к базе данных.
    connection = pymysql.connect(host='127.0.0.1',
                                 user='root',
                                 password='pass',
                                 db='jobbot',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)
    print ("connect successful getOneCompanyInfo!")
    try:
        with connection.cursor() as cursor:
            # SQL
            sql = "SELECT `company-name`, `line-business`, `city` FROM `companies` WHERE `id` = %s"
            # Выполнить команду запроса (Execute Query).
            # есть пользователь с этим ником в базе
            res = cursor.execute(sql, (companyId))
            results = cursor.fetchone()
            return results
    finally:
        # Закрыть соединение (Close connection).
        connection.close()

############# получение данных о компании по tg id ################
def getOneCompanyInfoByTGID (tg_id):
    # Подключиться к базе данных.
    connection = pymysql.connect(host='127.0.0.1',
                                 user='root',
                                 password='pass',
                                 db='jobbot',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)
    print ("connect successful getOneCompanyInfo!")
    try:
        with connection.cursor() as cursor:
            # SQL
            sql = "SELECT `company-name`, `line-business`, `line-business-id`, `city` FROM `companies` WHERE `tg-id` = %s"
            # Выполнить команду запроса (Execute Query).
            # есть пользователь с этим ником в базе
            res = cursor.execute(sql, (tg_id))
            results = cursor.fetchone()
            return results
    finally:
        # Закрыть соединение (Close connection).
        connection.close()

############# получение значения параметра компании по tg id и названию столбца ################
def getCompDataByDataName (dataNameComp, tg_id):
    # Подключиться к базе данных.
    connection = pymysql.connect(host='127.0.0.1',
                                 user='root',
                                 password='pass',
                                 db='jobbot',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)
    print ("connect successful getCompDataByDataName!")
    try:
        with connection.cursor() as cursor:
            # SQL
            sql = "SELECT `"+dataNameComp+"` FROM `companies` WHERE `tg-id` = %s"
            # Выполнить команду запроса (Execute Query).
            # есть пользователь с этим ником в базе
            res = cursor.execute(sql, (tg_id))
            results = cursor.fetchone()
            return results
    finally:
        # Закрыть соединение (Close connection).
        connection.close()

####### получение всех вакансий для текущей фирмы по tg id #######
def getAllEmplsByTGID (tg_id):
    # Подключиться к базе данных.
    connection = pymysql.connect(host='127.0.0.1',
                                 user='root',
                                 password='pass',
                                 db='jobbot',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)
    print ("connect successful getAllEmplsByTGID!")
    try:
        with connection.cursor() as cursor:
            # SQL
            sql = "SELECT * FROM `employers` WHERE `tg-id` = %s"
            # Выполнить команду запроса (Execute Query).
            res = cursor.execute(sql, (tg_id))
            results = cursor.fetchall()
            return results
    finally:
        # Закрыть соединение (Close connection).
        connection.close()

############# получение полной информации по одной вакансии по ее id ################
def getOneEmplInfoById (id):
    # Подключиться к базе данных.
    connection = pymysql.connect(host='127.0.0.1',
                                 user='root',
                                 password='pass',
                                 db='jobbot',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)
    print ("connect successful getOneEmplInfoById!")
    try:
        with connection.cursor() as cursor:
            # SQL
            sql = "SELECT * FROM `employers` WHERE `id` = %s"
            # Выполнить команду запроса (Execute Query).
            # есть пользователь с этим ником в базе
            res = cursor.execute(sql, (id))
            results = cursor.fetchone()
            return results
    finally:
        # Закрыть соединение (Close connection).
        connection.close()

############# получение значения столбца из таблицы с вакансияами по названию столбца и id ################
def getEmplDataByDataName (dataNameEmpl, id):
    # Подключиться к базе данных.
    connection = pymysql.connect(host='127.0.0.1',
                                 user='root',
                                 password='pass',
                                 db='jobbot',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)
    print ("connect successful getEmplDataByDataName!")
    try:
        with connection.cursor() as cursor:
            # SQL
            sql = "SELECT `" + dataNameEmpl + "` FROM `employers` WHERE `id` = %s"
            # Выполнить команду запроса (Execute Query).
            # есть пользователь с этим ником в базе
            res = cursor.execute(sql, (id))
            results = cursor.fetchone()
            return results
    finally:
        # Закрыть соединение (Close connection).
        connection.close()

####### получение всех откликов на вакансию по ее id #######
def getResposesForEmplById (id):
    # Подключиться к базе данных.
    connection = pymysql.connect(host='127.0.0.1',
                                 user='root',
                                 password='pass',
                                 db='jobbot',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)
    print ("connect successful getResposesForEmplById!")
    try:
        with connection.cursor() as cursor:
            # SQL
            sql = "SELECT * FROM `responses` WHERE `empl-id` = %s"
            # Выполнить команду запроса (Execute Query).
            res = cursor.execute(sql, (id))
            results = cursor.fetchall()
            return results
    finally:
        # Закрыть соединение (Close connection).
        connection.close()

############# запись нового дополнительного образования для пользователя в базу ################
async def addNewCompany (data):
    # Подключиться к базе данных.
    connection = pymysql.connect(host='127.0.0.1',
                                 user='root',
                                 password='pass',
                                 db='jobbot',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)
    print ("connect successful addNewCompany!")
    cursor = connection.cursor()
    try:
        # async with state.proxy() as data:
        #     print(data)
        #     # SQL
        #     sql = "INSERT INTO `companies` "\
        #     "(`tg-id`, `tg-login`, `company-name`, `line-business`, `line-business-id`) "\
        #     "VALUES (%s, %s, %s, %s, %s)"
        #     # Выполнить команду запроса (Execute Query).
        #     # есть пользователь с этим ником в базе
        #     res = cursor.execute(sql, tuple(data.values()))
        #     connection.commit()
        #     return res
        # SQL
        sql = "INSERT INTO `companies` "\
        "(`tg-id`, `tg-login`, `company-name`, `line-business`, `line-business-id`, `city`) "\
        "VALUES (%s, %s, %s, %s, %s, %s)"
        # Выполнить команду запроса (Execute Query).
        # есть пользователь с этим ником в базе
        res = cursor.execute(sql, tuple(data.values()))
        connection.commit()
        return res
    finally:
        # Закрыть соединение (Close connection).
        connection.close()

############# запись новой разовой работы в базу ################
async def addNewOneTimeWork (state):
    # Подключиться к базе данных.
    connection = pymysql.connect(host='127.0.0.1',
                                 user='root',
                                 password='pass',
                                 db='jobbot',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)
    print ("connect successful addNewOneTimeWork!")
    cursor = connection.cursor()
    try:
        async with state.proxy() as data:
            print(data)
            # SQL
            sql = "INSERT INTO `onetimeworks` "\
            "(`tg-id`, `tg-login`, `company-id`, `onetime-name`, `meaningofwork`, `deadline`) "\
            "VALUES (%s, %s, %s, %s, %s, %s)"
            # Выполнить команду запроса (Execute Query).
            # есть пользователь с этим ником в базе
            res = cursor.execute(sql, tuple(data.values()))
            connection.commit()
            return res
    finally:
        # Закрыть соединение (Close connection).
        connection.close()

############# обновление данных о компании ################
async def updtCompInfo (state):

    # Подключиться к базе данных.
    connection = pymysql.connect(host='127.0.0.1',
                                 user='root',
                                 password='pass',
                                 db='jobbot',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)
    print ("connect successful updtCompInfo!")
    cursor = connection.cursor()
    try:
        async with state.proxy() as data:
            a = {'userData': data['userData'], 'tg-id': data['tg-id']}
            # SQL
            sql = "UPDATE `companies` SET "\
            "`" + data['dataName'] + "` = %s WHERE `tg-id` = %s"
            # Выполнить команду запроса (Execute Query).
            # перевожу данные в кортеж для вставки
            res = cursor.execute(sql, tuple(a.values()))
            connection.commit()
            return res
    finally:
        # Закрыть соединение (Close connection).
        connection.close()

############# обновление данных о компании для направления деятельности ################
async def updtCompInfo2 (lineBusiness, lineBusinessId, tg_id):

    # Подключиться к базе данных.
    connection = pymysql.connect(host='127.0.0.1',
                                 user='root',
                                 password='pass',
                                 db='jobbot',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)
    print ("connect successful updtCompInfo2!")
    cursor = connection.cursor()
    try:
        a = {'lineBusiness': lineBusiness, 'lineBusinessId': lineBusinessId, 'tg-id': tg_id}
        # SQL
        sql = "UPDATE `companies` SET "\
        "`line-business` = %s, `line-business-id` = %s WHERE `tg-id` = %s"
        # Выполнить команду запроса (Execute Query).
        # перевожу данные в кортеж для вставки
        res = cursor.execute(sql, tuple(a.values()))
        connection.commit()
        return res
    finally:
        # Закрыть соединение (Close connection).
        connection.close()

############# обновление данных о вакансии ################
async def updtEmplInfo (userData, dataName, id):

    # Подключиться к базе данных.
    connection = pymysql.connect(host='127.0.0.1',
                                 user='root',
                                 password='pass',
                                 db='jobbot',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)
    print ("connect successful updtEmplInfo!")
    cursor = connection.cursor()
    try:
        a = {'userData': userData, 'id': id}
        # SQL
        sql = "UPDATE `employers` SET "\
        "`" + dataName + "` = %s WHERE `id` = %s"
        # Выполнить команду запроса (Execute Query).
        # перевожу данные в кортеж для вставки
        res = cursor.execute(sql, tuple(a.values()))
        connection.commit()
        return res
    finally:
        # Закрыть соединение (Close connection).
        connection.close()

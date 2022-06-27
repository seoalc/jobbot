import pymysql.cursors

############# проверка наличия исполнителя в базе по tg id ################
def checkUserByTgId (tg_id):
    # Подключиться к базе данных.
    connection = pymysql.connect(host='127.0.0.1',
                                 user='root',
                                 password='pass',
                                 db='jobbot',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)
    print ("connect successful checkUserByTgId!")
    try:
        with connection.cursor() as cursor:
            # SQL
            sql = "SELECT `tg-login` FROM `users` WHERE `tg-id` = %s"
            # Выполнить команду запроса (Execute Query).
            # есть пользователь с этим ником в базе
            res = cursor.execute(sql, (tg_id))
            return res
    finally:
        # Закрыть соединение (Close connection).
        connection.close()

############# добавление нового написавшего пользователя в базу ################
def addNewNaked (tg_id, tg_login, tg_firstname):
    if tg_login == None:
        tg_login = 'None'
    # передаваемые в функцию переменные перевожу в ловарь для вставки в базу кортежем
    a = {'tg_id': tg_id, 'tg_login': tg_login, 'tg_firstname': tg_firstname}
    print(a)

    # Подключиться к базе данных.
    connection = pymysql.connect(host='127.0.0.1',
                                 user='root',
                                 password='pass',
                                 db='jobbot',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)
    print ("connect successful addNewNaked!")
    try:
        with connection.cursor() as cursor:
            # SQL
            sql = "INSERT INTO `users` (`tg-id`, `tg-login`, `firstname`) VALUES (%s, %s, %s)"
            # Выполнить команду запроса (Execute Query).
            # есть пользователь с этим ником в базе
            res = cursor.execute(sql, tuple(a.values()))
            connection.commit()
            return res
    finally:
        # Закрыть соединение (Close connection).
        connection.close()

############# запись нового резюме в базу ################
async def addNewApplicant (state):
    # Подключиться к базе данных.
    connection = pymysql.connect(host='127.0.0.1',
                                 user='root',
                                 password='pass',
                                 db='jobbot',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)
    print ("connect successful addNewApplicant!")
    cursor = connection.cursor()
    try:
        async with state.proxy() as data:
            # SQL
            sql = "INSERT INTO `applicants` "\
            "(`tg-id`, `tg-login`, `firstname`, `lastname`, `patronymic`, `line-business`, `line-business-id`, `education-form`, "\
            "`added-education-form`, `career-objective`, `desired-salary`, `city-work`, `distant-work`, `relocate`, `work-experience`, "\
            "`desired-work-schedule`, `phone`, `email`) "\
            "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            # Выполнить команду запроса (Execute Query).
            # есть пользователь с этим ником в базе
            res = cursor.execute(sql, tuple(data.values()))
            lastId = connection.insert_id()
            connection.commit()
            return lastId
    finally:
        # Закрыть соединение (Close connection).
        connection.close()

############# запись новой вакансии в базу ################
async def addNewEmployer (state):
    # Подключиться к базе данных.
    connection = pymysql.connect(host='127.0.0.1',
                                 user='root',
                                 password='pass',
                                 db='jobbot',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)
    print ("connect successful addNewEmployer!")
    cursor = connection.cursor()
    try:
        async with state.proxy() as data:
            # SQL
            sql = "INSERT INTO `employers` "\
            "(`tg-id`, `tg-login`, `company-id`, `career-objective`, `desired-salary`, "\
            "`workformat`, `employment`, `duties`, `requirements`, `working-conditions`, `fio`, `phone`, `email`) "\
            "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            # Выполнить команду запроса (Execute Query).
            # есть пользователь с этим ником в базе
            res = cursor.execute(sql, tuple(data.values()))
            emplId = connection.insert_id()
            connection.commit()
            return emplId
    finally:
        # Закрыть соединение (Close connection).
        connection.close()

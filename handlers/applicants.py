from aiogram import types, Dispatcher
from bot_create import dp, bot
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardRemove
from aiogram.types import ReplyKeyboardRemove
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher.filters import Text

from db import dbusers, dbapplicants, dbcommon, dbcompanies
from keyboards import inline_kb, first_kb, sendresumeaccept_kb, sendjobaccept_kb, cancelnewedu_kb
from keyboards import cancel_kb, skip_step, mainApplicant_kb, goToMain_kb, beforeApplicant_kb, beforeApplicant2_kb, mainCompany_kb, \
goToApplicant_kb, resumeWorking_kb

# @dp.message_handler(commands=['войти как соискатель'])
async def login_as_applicant(message : types.Message):
    try:
        tg_id = message.from_user.id
        countUs = dbusers.checkUserByTgId(tg_id)
        if countUs == 0:
            dbusers.addNewNaked(message.from_user.id, message.from_user.username, message.from_user.first_name)
            saluteText = 'Добро пожаловать!\njobbot создан для удобного сотрудничества исполнителей с \
            заказчиками.\n\nВы можете разместить свое резюме, или добавить вакансию.'
            await message.reply(saluteText, reply_markup=first_kb)
        else:
            countAppl = dbapplicants.checkApplByTgId(tg_id)
            if (countAppl > 0):
                saluteText = 'Вы вошли как соискатель'
                await message.reply(saluteText, reply_markup=mainApplicant_kb)
            else:
                saluteText = 'Приветствуем снова!\nВы еще не добавляли резюме и не публиковали вакансий. \
                \n\nХотите сделать это сейчас?'
                await message.reply(saluteText, reply_markup=first_kb)
    except:
        await message.reply('Возникла какая-то ошибка, попробуйте повторить команду /start')

# @dp.message_handler(commands=['вернуться в меню соискателя'])
async def go_to_mainappl_menu(message : types.Message):
    try:
        tg_id = message.from_user.id
        countUs = dbusers.checkUserByTgId(tg_id)
        if countUs == 0:
            dbusers.addNewNaked(message.from_user.id, message.from_user.username, message.from_user.first_name)
            saluteText = 'Добро пожаловать!\njobbot создан для удобного сотрудничества исполнителей с \
            заказчиками.\n\nВы можете разместить свое резюме, или добавить вакансию.'
            await message.reply(saluteText, reply_markup=first_kb)
        else:
            countAppl = dbapplicants.checkApplByTgId(tg_id)
            if (countAppl > 0):
                saluteText = 'Вы в меню соискателя'
                await message.reply(saluteText, reply_markup=mainApplicant_kb)
            else:
                saluteText = 'Приветствуем снова!\nВы еще не добавляли резюме и не публиковали вакансий. \
                \n\nХотите сделать это сейчас?'
                await message.reply(saluteText, reply_markup=first_kb)
    except:
        await message.reply('Возникла какая-то ошибка, попробуйте повторить команду /start')

# @dp.message_handler(commands=['найти вакансию'])
async def search_employers(message : types.Message):
    try:
        tg_id = message.from_user.id
        countUs = dbusers.checkUserByTgId(tg_id)
        if countUs == 0:
            dbusers.addNewNaked(message.from_user.id, message.from_user.username, message.from_user.first_name)
            saluteText = 'Добро пожаловать!\njobbot создан для удобного сотрудничества исполнителей с \
            заказчиками.\n\nВы можете разместить свое резюме, или добавить вакансию.'
            await message.reply(saluteText, reply_markup=first_kb)
        else:
            countAppl = dbapplicants.checkApplByTgId(tg_id)
            if (countAppl > 0):
                applsForUserByTGID = dbapplicants.getAllApplsForUserByTGID(tg_id)
                print(applsForUserByTGID)
                mainTxt = 'Выберите резюме, для которого хотите произвести поиска вакансий'\
                '\n\nНайдено резюме: ' + str(countAppl)
                await message.reply(mainTxt, reply_markup=goToMain_kb)
                for item in applsForUserByTGID:
                    buttons = InlineKeyboardMarkup(row_width=1)
                    oneApplText = 'Направление деятельности: <b>' + item['line-business'] + '</b>\nЖелаемая должность: <b>'\
                    + item['career-objective'] + '</b>'
                    buttons.add(InlineKeyboardButton(text='Искать',
                                                    callback_data='searchEmplForAppl_' + str(item['id']) + '_' + str(item['line-business-id'])))
                    await message.answer(oneApplText, reply_markup=buttons, parse_mode=types.ParseMode.HTML)
            else:
                saluteText = 'Приветствуем снова!\nВы еще не добавляли резюме и не публиковали вакансий. \
                \n\nХотите сделать это сейчас?'
                await message.reply(saluteText, reply_markup=first_kb)
    except:
        await message.reply('Возникла какая-то ошибка, попробуйте повторить команду /start')

# @dp.message_handler(commands=['вернуться в главное меню', 'перейти в главное меню'])
async def go_to_main(message : types.Message):
    try:
        tg_id = message.from_user.id
        countUs = dbusers.checkUserByTgId(tg_id)
        if countUs == 0:
            dbusers.addNewNaked(message.from_user.id, message.from_user.username, message.from_user.first_name)
            saluteText = 'Добро пожаловать!\njobbot создан для удобного сотрудничества исполнителей с \
            заказчиками.\n\nВы можете разместить свое резюме, или добавить вакансию.'
            await message.reply(saluteText, reply_markup=first_kb)
        else:
            countAppl = dbapplicants.checkApplByTgId(tg_id)
            if (countAppl > 0):
                mainTxt = 'Вы в главном меню соискателя'
                await message.reply(mainTxt, reply_markup=mainApplicant_kb)
            else:
                saluteText = 'Приветствуем снова!\nВы еще не добавляли резюме и не публиковали вакансий. \
                \n\nХотите сделать это сейчас?'
                await message.reply(saluteText, reply_markup=first_kb)
    except:
        await message.reply('Возникла какая-то ошибка, попробуйте повторить команду /start')

# по нажатию инлайн кнопки с резюме, проводится поиск подходящих вакансий для этого резюме
@dp.callback_query_handler(Text(startswith='searchEmplForAppl_'))
async def search_empls_for_appl(callback : types.CallbackQuery):
    try:
        tg_id = callback.from_user.id
        countUs = dbusers.checkUserByTgId(tg_id)
        if countUs == 0:
            dbusers.addNewNaked(callback.from_user.id, callback.from_user.username, callback.from_user.first_name)
            saluteText = 'Добро пожаловать!\njobbot создан для удобного сотрудничества исполнителей с \
            заказчиками.\n\nВы можете разместить свое резюме, или добавить вакансию.'
            await bot.send_message(callback.from_user.id, saluteText, reply_markup=first_kb)
            await callback.answer()
        else:
            countAppl = dbapplicants.checkApplByTgId(tg_id)
            if (countAppl > 0):
                applId = int(callback.data.split('_')[1])
                lineBusinessId = int(callback.data.split('_')[2])
                print(applId)
                print(lineBusinessId)
                # если направление деятельности не из стандартного списка
                if lineBusinessId > 0:
                    # applInfo = dbapplicants.getApplInfoById(applId)
                    # searchingEmpls = dbapplicants.searchAllEmplsByText(applInfo['line-business'], applInfo['career-objective'])
                    # searchingEmpls = dbapplicants.searchAllEmplsByLineBuissId(lineBusinessId)
                    # сначала вытаскиваю id компаний по данному направлению деятельности
                    searchingCompanies = dbapplicants.searchAllCompByLineBuissId(lineBusinessId)
                    emplsList = []
                    # затем перебираю их в цикле и по ним достаю информацию по вакансиям
                    for item in searchingCompanies:
                        searchingEmpls = dbapplicants.searchAllEmplsByCompId(item['id'])
                        for item2 in searchingEmpls:
                            emplsList.append(item2)
                            item2['company-name'] = item['company-name']
                            item2['line-business'] = item['line-business']
                    if len(emplsList) > 0:
                        mainTxt = 'Подходящие вакансии для выбранного резюме'
                        await bot.send_message(callback.from_user.id, mainTxt, reply_markup=goToMain_kb)
                        for item in emplsList:
                            buttons = InlineKeyboardMarkup(row_width=1)
                            buttons.add(InlineKeyboardButton(text='Смотреть вакансию полностью',
                                                            callback_data='viewEmplForOneAppl_' + str(item['id']) + '_' + str(applId)))
                            txtForOneAppl = '<b>Название компании: </b>' + item['company-name'] + '\n'\
                                            '<b>Направление деятельности:</b>\n' + item['line-business'] + '\n'\
                                            '<b>Должность: </b>' + item['career-objective'] + '\n'\
                                            '<b>Зарплата: </b>' + item['desired-salary']
                            await bot.send_message(callback.from_user.id, txtForOneAppl, reply_markup=buttons, parse_mode=types.ParseMode.HTML)
                            await callback.answer()
                    else:
                        buttons = InlineKeyboardMarkup(row_width=1)
                        buttons.add(InlineKeyboardButton(text='Посмотреть другие вакансии',
                                                        callback_data='lookOtherEmpls'))
                        mainTxt = 'Для данного резюме подходящих вакансий не найдено.'
                        await bot.send_message(callback.from_user.id, mainTxt, reply_markup=buttons)
            else:
                saluteText = 'Приветствуем снова!\nВы еще не добавляли резюме и не публиковали вакансий. \
                \n\nХотите сделать это сейчас?'
                await bot.send_message(callback.from_user.id, saluteText, reply_markup=first_kb)
                await callback.answer()
    except:
        await bot.send_message(callback.from_user.id, 'Возникла какая-то ошибка, попробуйте повторить команду /start')
        await callback.answer()

# кнопка просмотра других вакансий, если для данного направления ничего не найдено
@dp.callback_query_handler(text='lookOtherEmpls')
async def look_other_empls_command(callback : types.CallbackQuery):
    try:
        tg_id = callback.from_user.id
        countUs = dbusers.checkUserByTgId(tg_id)
        if countUs == 0:
            dbusers.addNewNaked(callback.from_user.id, callback.from_user.username, callback.from_user.first_name)
            saluteText = 'Добро пожаловать!\njobbot создан для удобного сотрудничества исполнителей с \
            заказчиками.\n\nВы можете разместить свое резюме, или добавить вакансию.'
            await bot.send_message(callback.from_user.id, saluteText, reply_markup=first_kb)
            await callback.answer()
        else:
            countAppl = dbapplicants.checkApplByTgId(tg_id)
            if (countAppl > 0):
                applId = int(callback.data.split('_')[1])
                # сначала вытаскиваю id последних компаний
                searchingCompanies = dbapplicants.searchAllLastComp()
                emplsList = []
                # затем перебираю их в цикле и по ним достаю информацию по вакансиям
                for item in searchingCompanies:
                    searchingEmpls = dbapplicants.searchAllLastEmpls(item['id'])
                    for item2 in searchingEmpls:
                        emplsList.append(item2)
                        item2['company-name'] = item['company-name']
                        item2['line-business'] = item['line-business']
                if len(emplsList) > 0:
                    mainTxt = 'Просмотр других вакансий'
                    await bot.send_message(callback.from_user.id, mainTxt, reply_markup=goToMain_kb)
                    for item in emplsList:
                        buttons = InlineKeyboardMarkup(row_width=1)
                        buttons.add(InlineKeyboardButton(text='Смотреть вакансию полностью',
                                                        callback_data='viewEmplForOneAppl_' + str(item['id']) + '_' + str(applId)))
                        txtForOneAppl = '<b>Название компании: </b>' + item['company-name'] + '\n'\
                                        '<b>Направление деятельности:</b>\n' + item['line-business'] + '\n'\
                                        '<b>Должность: </b>' + item['career-objective'] + '\n'\
                                        '<b>Зарплата: </b>' + item['desired-salary']
                        await bot.send_message(callback.from_user.id, txtForOneAppl, reply_markup=buttons, parse_mode=types.ParseMode.HTML)
                        await callback.answer()
            else:
                saluteText = 'Вашего резюме не найдено в боте'
                await bot.send_message(callback.from_user.id, saluteText, reply_markup=first2_kb)
                await callback.answer()
    except:
        await bot.send_message(callback.from_user.id, 'Возникла какая-то ошибка, попробуйте повторить команду /start')
        await callback.answer()


# по нажатию инлайн кнопки с для полного просмотра одной конкретной вакансии
@dp.callback_query_handler(Text(startswith='viewEmplForOneAppl_'))
async def view_one_empl(callback : types.CallbackQuery):
    try:
        tg_id = callback.from_user.id
        countUs = dbusers.checkUserByTgId(tg_id)
        if countUs == 0:
            dbusers.addNewNaked(callback.from_user.id, callback.from_user.username, callback.from_user.first_name)
            saluteText = 'Добро пожаловать!\njobbot создан для удобного сотрудничества исполнителей с \
            заказчиками.\n\nВы можете разместить свое резюме, или добавить вакансию.'
            await bot.send_message(callback.from_user.id, saluteText, reply_markup=first_kb)
            await callback.answer()
        else:
            countAppl = dbapplicants.checkApplByTgId(tg_id)
            if (countAppl > 0):
                applId = int(callback.data.split('_')[2])
                emplId = int(callback.data.split('_')[1])
                oneEmplInfo = dbapplicants.getOneEmplInfo(emplId)
                oneCompanyInfo = dbcompanies.getOneCompanyInfo(oneEmplInfo['company-id'])
                txtForOneEmpl = '<b>Название компании: </b>' + oneCompanyInfo['company-name'] + '\n'\
                                '<b>Направление деятельности:</b>\n' + oneCompanyInfo['line-business'] + '\n'\
                                '<b>Требуемая должность:</b>\n' + oneEmplInfo['career-objective'] + '\n'\
                                '<b>Зарплата: </b>' + oneEmplInfo['desired-salary'] + '\n'\
                                '<b>Город работы: </b> ' + oneCompanyInfo['city'] + '\n'\
                                '<b>Удаленная работа: </b>' + oneEmplInfo['workformat'] + '\n'\
                                '<b>Тип занятости: </b>' + oneEmplInfo['employment'] + '\n\n'\
                                '<b>Должностные обязанности:</b>\n' + oneEmplInfo['duties'] + '\n\n'\
                                '<b>Требования к кандидату:</b>\n' + oneEmplInfo['requirements'] + '\n\n'\
                                '<b>Условия работы:</b>\n' + oneEmplInfo['working-conditions']
                # кнопка откликнуться для одной вакансии в боте
                respondEmplInBot_kb = InlineKeyboardMarkup(row_width=1)
                respForEployerInBot = InlineKeyboardButton(text='Откликнуться',
                                                    callback_data='respForEmplInBot_' + str(oneEmplInfo['company-id']) + \
                                                    '_' + str(emplId) + '_' + str(applId))
                respondEmplInBot_kb.add(respForEployerInBot)
                await bot.send_message(callback.from_user.id, txtForOneEmpl, parse_mode=types.ParseMode.HTML, reply_markup=respondEmplInBot_kb)
                await callback.answer()
            else:
                saluteText = 'Приветствуем снова!\nВы еще не добавляли резюме и не публиковали вакансий. \
                \n\nХотите сделать это сейчас?'
                await bot.send_message(callback.from_user.id, saluteText, reply_markup=first_kb)
                await callback.answer()
    except:
        await bot.send_message(callback.from_user.id, 'Возникла какая-то ошибка, попробуйте повторить команду /start')
        await callback.answer()

# по нажатию инлайн кнопки с для отклика на вакансию в боте
@dp.callback_query_handler(Text(startswith='respForEmplInBot_'))
async def view_one_empl(callback : types.CallbackQuery):
    try:
        tg_id = callback.from_user.id
        countUs = dbusers.checkUserByTgId(tg_id)
        if countUs == 0:
            dbusers.addNewNaked(callback.from_user.id, callback.from_user.username, callback.from_user.first_name)
            saluteText = 'Добро пожаловать!\njobbot создан для удобного сотрудничества исполнителей с \
            заказчиками.\n\nВы можете разместить свое резюме, или добавить вакансию.'
            await bot.send_message(callback.from_user.id, saluteText, reply_markup=first_kb)
            await callback.answer()
        else:
            countAppl = dbapplicants.checkApplByTgId(tg_id)
            if (countAppl > 0):
                # из инлайн кнопки получаю id компании и вакансии и резюме
                compId = int(callback.data.split('_')[1])
                emplId = int(callback.data.split('_')[2])
                applId = int(callback.data.split('_')[3])
                checkingResponse = dbcommon.checkResponsesForApplicant(applId, emplId)
                if checkingResponse == 0:
                    # по id компании вытаскиваю TG id владельца компании
                    compTGId = dbapplicants.getCompTGIdByCompId(compId)
                    # по id вакансии вытаскиваю информацию об этой вакансии
                    oneEmplInfo = dbapplicants.getOneEmplInfo(emplId)
                    # по id резюме вытаскиваю информацию о ней
                    applInfo = dbapplicants.getApplInfoByApplId(applId)
                    # формирую текст для владельца компании
                    forCompTGText = '<b>На Вашу вакансию поступил отклик</b>\n\n'\
                                    '<b>Требуемая должность:</b>\n' + oneEmplInfo['career-objective'] + '\n'\
                                    '<b>Зарплата: </b>' + oneEmplInfo['desired-salary'] + '\n'\
                                    '<b>Должностные обязанности:</b>\n' + oneEmplInfo['duties'] + '\n\n'\
                                    '<b>от соискателя:</b>\n\n'\
                                    '<b>Имя:</b>\n' + applInfo['firstname'] + ' ' + applInfo['lastname'] + ' ' + applInfo['patronymic'] + '\n'\
                                    '<b>Направление деятельности:</b>\n' + applInfo['line-business'] + '\n'\
                                    '<b>Форма обучения:</b>\n' + applInfo['career-objective'] + '\n'\
                                    '<b>Опыт работы:</b>\n' + applInfo['work-experience']
                    # кнопка для просмотра полного резюме работодателем, которое откликнулось
                    lookResponAppl_kb = InlineKeyboardMarkup(row_width=1)
                    lookResponApplInBot = InlineKeyboardButton(text='Посмотреть резюме полностью',
                                                        callback_data='lookResponAppl_' + str(applId) + '_' + str(emplId))
                    lookResponAppl_kb.add(lookResponApplInBot)
                    await bot.send_message(compTGId['tg-id'], forCompTGText, parse_mode=types.ParseMode.HTML, reply_markup=lookResponAppl_kb)
                    # формирую текст для текущего отправщика отклика (соискателя)
                    forApplText = '<b>Вы успешно отправили отклик на вакансию</b>\n\n'\
                                    '<b>Требуемая должность:</b>\n' + oneEmplInfo['career-objective'] + '\n'\
                                    '<b>Зарплата: </b>' + oneEmplInfo['desired-salary'] + '\n'\
                                    '<b>Должностные обязанности:</b>\n' + oneEmplInfo['duties'] + '\n\n'\
                                    '<b>от резюме:</b>\n\n'\
                                    '<b>Имя:</b>\n' + applInfo['firstname'] + ' ' + applInfo['lastname'] + ' ' + applInfo['patronymic'] + '\n'\
                                    '<b>Направление деятельности:</b>\n' + applInfo['line-business'] + '\n'\
                                    '<b>Форма обучения:</b>\n' + applInfo['career-objective'] + '\n'\
                                    '<b>Опыт работы:</b>\n' + applInfo['work-experience']
                    await bot.send_message(callback.from_user.id, forApplText, parse_mode=types.ParseMode.HTML, reply_markup=goToApplicant_kb)
                    await dbcommon.addResponseForApplicant(applId, emplId)
                else:
                    await bot.send_message(callback.from_user.id, 'Вы уже откликались на эту вакансию', reply_markup=goToApplicant_kb)
                await callback.answer()
            else:
                saluteText = 'Приветствуем снова!\nВы еще не добавляли резюме и не публиковали вакансий. \
                \n\nХотите сделать это сейчас?'
                await bot.send_message(callback.from_user.id, saluteText, reply_markup=first_kb)
                await callback.answer()
    except:
        await bot.send_message(callback.from_user.id, 'Возникла какая-то ошибка, попробуйте повторить команду /start')
        await callback.answer()

# Загрузка дополнительного образования
class FSMAddedu(StatesGroup):
    edu = State()
    eduForm = State()

# Начало дилога загрузки дополнительного образования
# dp.register_message_handler(command_add_edu, Text(equals="добавить дополнительное образование", ignore_case=True), state=None)
@dp.message_handler(Text(equals="добавить дополнительное образование", ignore_case=True), state=None)
async def command_add_edu(message : types.Message):
    await FSMAddedu.edu.set()
    lineBusinessInfo = dbcommon.getAllLineBusiness()
    aboutLinesText = '''
    Укажите направление курса, который Вы закончили. Мы будем предлагать вакансии,
    связанные с этим направлением\n\nМожете выбрать подходящее из списка ниже, указав его цифру\n\n
    Либо напишите свое
    '''
    linesText = ''
    for item in lineBusinessInfo:
        linesText = linesText + str(item['id']) + ' - ' + item['name'] + '\n'
    await message.reply(aboutLinesText, reply_markup=cancel_kb)
    await message.answer(linesText, reply_markup=cancel_kb)

# Ловим первый ответ и пишем в словарь
# @dp.message_handler(state=FSMAddedu.firstname)
async def get_edu(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['tg_id'] = message.from_user.id
        if message.from_user.username == None:
            data['username'] = 'None'
        else:
            data['username'] = message.from_user.username
        lineBusinessInfo = dbcommon.getAllLineBusiness()
        for item in lineBusinessInfo:
            if (str(item['id']) == message.text):
                data['lineBusiness'] = item['name']
                data['lineBusinessId'] = int(item['id'])
                break
            else:
                data['lineBusiness'] = message.text
                data['lineBusinessId'] = 0
        # data['edu'] = message.text
    await FSMAddedu.next()
    await message.reply("Укажите форму обучения, которую Вы прошли по указанному направлению")

# Ловим форму обучения и пишем в словарь
# @dp.message_handler(state=FSMAddedu.eduForm)
async def get_eduform(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['eduForm'] = message.text
    print(data)
    await dbapplicants.addNewEducation(state)
    await state.finish()
    successText = '''
    Дополнительное образование добавлено\n\nНо вы можете добавить еще.
    '''
    await bot.send_message(message.from_user.id, successText, reply_markup=beforeApplicant_kb)

# действие по кнопке редактировать резюме
# @dp.message_handler(commands=['редактировать резюме'])
async def edit_my_appls(message : types.Message):
    try:
        tg_id = message.from_user.id
        countUs = dbusers.checkUserByTgId(tg_id)
        if countUs == 0:
            dbusers.addNewNaked(message.from_user.id, message.from_user.username, message.from_user.first_name)
            saluteText = 'Добро пожаловать!\njobbot создан для удобного сотрудничества исполнителей с \
            заказчиками.\n\nВы можете разместить свое резюме, или добавить вакансию.'
            await message.reply(saluteText, reply_markup=first_kb)
        else:
            countAppl = dbapplicants.checkApplByTgId(tg_id)
            if (countAppl > 0):
                applsForUserByTGID = dbapplicants.getAllApplsForUserByTGID(tg_id)
                mainTxt = 'Выберите резюме, которое хотите отредактировать'\
                '\n\nНайдено резюме: ' + str(countAppl)
                await message.reply(mainTxt, reply_markup=goToMain_kb)
                for item in applsForUserByTGID:
                    buttons = InlineKeyboardMarkup(row_width=1)
                    oneApplText = 'Направление деятельности: <b>' + item['line-business'] + '</b>\nЖелаемая должность: <b>'\
                    + item['career-objective'] + '</b>'
                    buttons.add(InlineKeyboardButton(text='Редактировать',
                                                    callback_data='editOneOfMyAppl_' + str(item['id'])))
                    await message.answer(oneApplText, reply_markup=buttons, parse_mode=types.ParseMode.HTML)
            else:
                saluteText = 'Приветствуем снова!\nВы еще не добавляли резюме и не публиковали вакансий. \
                \n\nХотите сделать это сейчас?'
                await message.reply(saluteText, reply_markup=first_kb)
    except:
        await message.reply('Возникла какая-то ошибка, попробуйте повторить команду /start')

# по нажатию инлайн кнопки для выбора действий по редактированию одного резюме
@dp.callback_query_handler(Text(startswith='editOneOfMyAppl_'))
async def edit_one_my_appl(callback : types.CallbackQuery):
    try:
        tg_id = callback.from_user.id
        countUs = dbusers.checkUserByTgId(tg_id)
        if countUs == 0:
            dbusers.addNewNaked(callback.from_user.id, callback.from_user.username, callback.from_user.first_name)
            saluteText = 'Добро пожаловать!\njobbot создан для удобного сотрудничества исполнителей с \
            заказчиками.\n\nВы можете разместить свое резюме, или добавить вакансию.'
            await bot.send_message(callback.from_user.id, saluteText, reply_markup=first_kb)
            await callback.answer()
        else:
            countAppl = dbapplicants.checkApplByTgId(tg_id)
            if (countAppl > 0):
                applId = int(callback.data.split('_')[1])
                # главное сообщение
                oneApplInfo = dbapplicants.getApplInfoById(applId)
                txtForOneEmpl = 'Вы выбрали резюме:\n'\
                                'Направление деятельности:\n<b>' + oneApplInfo['line-business'] + '</b>\n'\
                                'Желаемая должность:\n<b>' + oneApplInfo['career-objective'] + '</b>\n'
                await bot.send_message(callback.from_user.id, txtForOneEmpl, parse_mode=types.ParseMode.HTML)
                whatDoTxt = 'Какие действия Вы хотите произвести с этим резюме?'
                await bot.send_message(callback.from_user.id, whatDoTxt)
                # сообщение с кнопкой для редактирования
                forEditText = 'Редактировать резюме'
                forEditTextButton = InlineKeyboardMarkup(row_width=1)
                forEditTextButton.add(InlineKeyboardButton(text='Редактировать',
                                                callback_data='editThis_' + str(applId)))
                await bot.send_message(callback.from_user.id, forEditText, reply_markup=forEditTextButton)
                # сообщение с кнопкой для добавления pdf
                forSendPDFText = 'Загрузить pdf-файл для этого резюме'
                forSendPDFButton = InlineKeyboardMarkup(row_width=1)
                forSendPDFButton.add(InlineKeyboardButton(text='Загрузить pdf файл резюме',
                                                callback_data='sendPDF_' + str(applId)))
                await bot.send_message(callback.from_user.id, forSendPDFText, reply_markup=forSendPDFButton)
                # сообщение с кнопкой для удаления резюме
                forDelApplText = 'Удалить резюме'
                forDelApplButton = InlineKeyboardMarkup(row_width=1)
                forDelApplButton.add(InlineKeyboardButton(text='Удалить резюме',
                                                callback_data='deleteAppl_' + str(applId)))
                await bot.send_message(callback.from_user.id, forDelApplText, reply_markup=forDelApplButton)
                await callback.answer()
            else:
                saluteText = 'Приветствуем снова!\nВы еще не добавляли резюме и не публиковали вакансий. \
                \n\nХотите сделать это сейчас?'
                await bot.send_message(callback.from_user.id, saluteText, reply_markup=first_kb)
                await callback.answer()
    except:
        await bot.send_message(callback.from_user.id, 'Возникла какая-то ошибка, попробуйте повторить команду /start')
        await callback.answer()

# по нажатию инлайн кнопки для выбора параметров для редактирования в резюме
@dp.callback_query_handler(Text(startswith='editThis_'))
async def edit_one_my_appl(callback : types.CallbackQuery):
    try:
        tg_id = callback.from_user.id
        countUs = dbusers.checkUserByTgId(tg_id)
        if countUs == 0:
            dbusers.addNewNaked(callback.from_user.id, callback.from_user.username, callback.from_user.first_name)
            saluteText = 'Добро пожаловать!\njobbot создан для удобного сотрудничества исполнителей с \
            заказчиками.\n\nВы можете разместить свое резюме, или добавить вакансию.'
            await bot.send_message(callback.from_user.id, saluteText, reply_markup=first_kb)
            await callback.answer()
        else:
            countAppl = dbapplicants.checkApplByTgId(tg_id)
            if (countAppl > 0):
                applId = int(callback.data.split('_')[1])
                # кнопка с выбором тех данных, которые нужно отредактировать
                applData1 = InlineKeyboardButton(text='Имя', callback_data='applData_firstname_')
                applData2 = InlineKeyboardButton(text='Фамилия', callback_data='applData_lastname_')
                applData3 = InlineKeyboardButton(text='Отчество', callback_data='applData_patronymic_')
                applData4 = InlineKeyboardButton(text='Направление деятельности', callback_data='applData_linebusiness_')
                applData5 = InlineKeyboardButton(text='Форма обучения', callback_data='applData_educationform_')
                applData6 = InlineKeyboardButton(text='Желаемая должность', callback_data='applData_careerobjective_')
                applData7 = InlineKeyboardButton(text='Желаемая зарплата', callback_data='applData_desiredsalary_')
                applData8 = InlineKeyboardButton(text='Город работы', callback_data='applData_citywork_')
                applData9 = InlineKeyboardButton(text='Опыт работы', callback_data='applData_workexperience_')
                applData10 = InlineKeyboardButton(text='Желаемый график работы', callback_data='applData_desiredworkschedule_')
                applData11 = InlineKeyboardButton(text='Телефон', callback_data='applData_phone_')
                applData12 = InlineKeyboardButton(text='E-mail', callback_data='applData_email_')
                send_applData_for_edit = InlineKeyboardMarkup(row_width=1).row(applData1, applData2, applData3).row(applData4).row(applData5)\
                                                            .row(applData6).row(applData7).row(applData8, applData9)\
                                                            .row(applData10).row(applData11, applData12)
                await bot.send_message(callback.from_user.id, 'Выберите какой из пунктов резюме хотите отредактировать', reply_markup=send_applData_for_edit)
            else:
                saluteText = 'Приветствуем снова!\nВы еще не добавляли резюме и не публиковали вакансий. \
                \n\nХотите сделать это сейчас?'
                await bot.send_message(callback.from_user.id, saluteText, reply_markup=first_kb)
                await callback.answer()
    except:
        await bot.send_message(callback.from_user.id, 'Возникла какая-то ошибка, попробуйте повторить команду /start')
        await callback.answer()

class FSMGotoeditappldata(StatesGroup):
    updtdata = State()
# по нажатию инлайн кнопки с выбранным параметром для редактирования,
# название этого параметра (str) отправится в базу
@dp.callback_query_handler(Text(startswith='applData_'))
async def send_appl_data_for_edit(callback : types.CallbackQuery):
    try:
        tg_id = callback.from_user.id
        countUs = dbusers.checkUserByTgId(tg_id)
        if countUs == 0:
            dbusers.addNewNaked(callback.from_user.id, callback.from_user.username, callback.from_user.first_name)
            saluteText = 'Добро пожаловать!\njobbot создан для удобного сотрудничества исполнителей с \
            заказчиками.\n\nВы можете разместить свое резюме, или добавить вакансию.'
            await bot.send_message(callback.from_user.id, saluteText, reply_markup=first_kb)
            await callback.answer()
        else:
            countAppl = dbapplicants.checkApplByTgId(tg_id)
            if (countAppl > 0):
                # объявляю глобальные переменные для передачи в машину состояний
                # dataName это само название редактируемого поля в таблице с данными пользователя
                # usersDataByDataName это значение этого поля из таблицы, которое он хочет изменить
                global changeSuccessText
                global dataName
                dataName = callback.data.split('_')[1]
                if dataName == 'firstname':
                    changeAlert = 'Последний раз Вы указали имя - '
                    changeSuccessText = 'Ваше имя изменено на - '
                elif dataName == 'lastname':
                    changeAlert = 'Последний раз Вы указали фамилию - '
                    changeSuccessText = 'Ваша фамилия изменена на - '
                elif dataName == 'patronymic':
                    changeAlert = 'Последний раз Вы указали отчество - '
                    changeSuccessText = 'Ваше отчество изменено на - '
                elif dataName == 'linebusiness':
                    changeAlert = 'Последний раз Вы указали направление деятельности - '
                    changeSuccessText = 'Направление деятельности изменено на - '
                    dataName = 'line-business'
                elif dataName == 'educationform':
                    changeAlert = 'Последний раз Вы указали форму обучения - '
                    changeSuccessText = 'Форма обучения изменена на - '
                    dataName = 'education-form'
                elif dataName == 'careerobjective':
                    changeAlert = 'Последний раз Вы указали желаемую должность - '
                    changeSuccessText = 'Желаемая должность изменена на - '
                    dataName = 'career-objective'
                elif dataName == 'desiredsalary':
                    changeAlert = 'Последний раз Вы указали желаемую зарплату - '
                    changeSuccessText = 'Желаемая зарплата изменена на - '
                    dataName = 'desired-salary'
                elif dataName == 'citywork':
                    changeAlert = 'Последний раз Вы указали город работы - '
                    changeSuccessText = 'Ваш город работы изменен на - '
                    dataName = 'city-work'
                elif dataName == 'workexperience':
                    changeAlert = 'Последний раз Вы указали опыт работы - '
                    changeSuccessText = 'Ваш опыт работы изменен на - '
                    dataName = 'work-experience'
                elif dataName == 'desiredworkschedule':
                    changeAlert = 'Последний раз Вы указали желаемый график работы - '
                    changeSuccessText = 'Желаемый график работы изменен на - '
                    dataName = 'desired-work-schedule'
                elif dataName == 'phone':
                    changeAlert = 'Последний раз Вы указали телефон - '
                    changeSuccessText = 'Телефон изменен на - '
                elif dataName == 'email':
                    changeAlert = 'Последний раз Вы указали e-mail - '
                    changeSuccessText = 'E-mail изменен на - '
                applDataByDataName = dbapplicants.getApplDataByDataName(dataName, tg_id)
                await FSMGotoeditappldata.updtdata.set()
                await bot.send_message(callback.from_user.id, changeAlert + str(applDataByDataName[dataName]) + \
                                        '\n\nВведите новое значение', reply_markup=cancel_kb)
                await callback.answer()
            else:
                saluteText = 'Приветствуем снова!\nВы еще не добавляли резюме и не публиковали вакансий. \
                \n\nХотите сделать это сейчас?'
                await bot.send_message(callback.from_user.id, saluteText, reply_markup=first_kb)
                await callback.answer()
    except:
        await bot.send_message(callback.from_user.id, 'Возникла какая-то ошибка, попробуйте повторить команду /start')
        await callback.answer()

# Продолжение машинного состояния по ловле изменяемого пункта резюме
# @dp.message_handler(state=FSMGotoeditappldata.updtdata)
async def get_new_appl_data(callback : types.CallbackQuery, state: FSMGotoeditappldata):
    async with state.proxy() as data:
        data['tg-id'] = callback.from_user.id
        data['userData'] = callback.text
        data['dataName'] = dataName
    await dbapplicants.updtApplInfo(state)
    await state.finish()
    await bot.send_message(callback.from_user.id, changeSuccessText + data['userData'], reply_markup=goToMain_kb)

class FSMNewpdffile(StatesGroup):
    pdffile = State()
# по нажатию инлайн кнопки для загрузки pdf файла резюме
@dp.callback_query_handler(Text(startswith='sendPDF_'))
async def edit_one_my_appl(callback : types.CallbackQuery):
    try:
        tg_id = callback.from_user.id
        countUs = dbusers.checkUserByTgId(tg_id)
        if countUs == 0:
            dbusers.addNewNaked(callback.from_user.id, callback.from_user.username, callback.from_user.first_name)
            saluteText = 'Добро пожаловать!\njobbot создан для удобного сотрудничества исполнителей с \
            заказчиками.\n\nВы можете разместить свое резюме, или добавить вакансию.'
            await bot.send_message(callback.from_user.id, saluteText, reply_markup=first_kb)
            await callback.answer()
        else:
            countAppl = dbapplicants.checkApplByTgId(tg_id)
            countComp = dbcompanies.checkCompByTgId(tg_id)
            if countAppl == 0:
                makedJobText = 'Ваше резюме не найдено'
                await bot.send_message(callback.from_user.id, makedJobText, reply_markup=highMenu_kb)
                await callback.answer()
            elif countAppl > 0:
                applId = int(callback.data.split('_')[1])
                # проверка на наличие pdf
                pdfId = dbapplicants.getPDFById(applId)
                if pdfId['pdf-file'] == 'empty':
                    await FSMNewpdffile.pdffile.set()
                    await bot.send_message(callback.from_user.id, 'Выберите файл на Вашем устройстве и отправьте его', reply_markup=cancel_kb)
                    await callback.answer()
                else:
                    warnText = '''
                    Вы уже загружали PDF-файл.\n\nВыберите и отправьте новый, если хотите заменить его, либо нажмите ОТМЕНА
                    '''
                    await FSMNewpdffile.pdffile.set()
                    await bot.send_document(callback.from_user.id, pdfId['pdf-file'], caption=warnText, reply_markup=cancel_kb)
                    await callback.answer()
    except:
        await bot.send_message(callback.from_user.id, 'Возникла какая-то ошибка, попробуйте повторить команду /start')
        await callback.answer()

# продолжение машинного состояния по ловле PDF-файла, отправленного пользователем
# @dp.message_handler(content_types=['document'], state=FSMNewpdffile.pdffile)
async def load_pdffile(message: types.Message, state=FSMContext):
    async with state.proxy() as data:
        data['tg_id'] = message.from_user.id
        data['pdfFile'] = message.document.file_id
    if (message.document['mime_type'] == 'application/pdf'):
        # await dbapplicants.updtPDFById(state)
        await state.finish()
        successText = '''
        PDF-файл успешно загружен
        '''
        await bot.send_message(message.from_user.id, successText, reply_markup=beforeApplicant2_kb)
    else:
        successText = '''
        Вы выбрали не PDF-файл
        '''
        await bot.send_message(message.from_user.id, successText)

# по нажатию инлайн кнопки удалить резюме
@dp.callback_query_handler(Text(startswith='deleteAppl_'))
async def edit_one_my_appl(callback : types.CallbackQuery):
    try:
        tg_id = callback.from_user.id
        countUs = dbusers.checkUserByTgId(tg_id)
        if countUs == 0:
            dbusers.addNewNaked(callback.from_user.id, callback.from_user.username, callback.from_user.first_name)
            saluteText = 'Добро пожаловать!\njobbot создан для удобного сотрудничества исполнителей с \
            заказчиками.\n\nВы можете разместить свое резюме, или добавить вакансию.'
            await bot.send_message(callback.from_user.id, saluteText, reply_markup=first_kb)
            await callback.answer()
        else:
            countAppl = dbapplicants.checkApplByTgId(tg_id)
            countComp = dbcompanies.checkCompByTgId(tg_id)
            if countAppl == 0:
                makedJobText = 'Ваше резюме не найдено'
                await bot.send_message(callback.from_user.id, makedJobText, reply_markup=highMenu_kb)
                await callback.answer()
            elif countAppl > 0:
                applId = int(callback.data.split('_')[1])
                # запрос к базе на удаление резюме
                await dbapplicants.deleteApplById(applId)
                await bot.send_message(callback.from_user.id, 'Резюме удалено', reply_markup=goToApplicant_kb)
                await callback.answer()
    except:
        await bot.send_message(callback.from_user.id, 'Возникла какая-то ошибка, попробуйте повторить команду /start')
        await callback.answer()

# создание разовой работы соискателем
class FSMNewonetimeforappl(StatesGroup):
    onetName = State()
    meaningwork = State()
    deadlineforappl = State()
# Начало дилога загрузки разовой работы от лица соискателя
@dp.callback_query_handler(text='oneTForAppl')
async def command_reg_onetappl(callback : types.Message):
    await FSMNewonetimeforappl.onetName.set()
    await bot.send_message(callback.from_user.id, "Введите название работы", reply_markup=cancel_kb)

# Ловим название и пишем в словарь
# @dp.message_handler(state=FSMNewonetimeforappl.onetName)
async def get_onetime_name_forappl(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['tg_id'] = message.from_user.id
        if message.from_user.username == None:
            data['tg-login'] = 'None'
        else:
            data['tg-login'] = message.from_user.username
        applInfo = dbapplicants.getIdAndNameAppl(data['tg_id'])
        data['companyId'] = applInfo['id']
        # data['companyName'] = applInfo['firstname'] + applInfo['lastname']
        data['onetimeName'] = message.text
    await FSMNewonetimeforappl.next()
    await message.reply("Распишите более подробно суть работы", reply_markup=cancel_kb)

# Ловим суть работы и пишем в словарь
# @dp.message_handler(state=FSMNewonetimeforappl.meaningwork)
async def get_meaningwork(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['meaningofwork'] = message.text
    await FSMNewonetimeforappl.next()
    await message.reply("Укажите дедлайн", reply_markup=cancel_kb)

# Пишем дедлайн в словарь, и закрываем машинное состояние
# @dp.message_handler(state=FSMNewonetimeforappl.deadlineforappl)
async def get_deadlineforappl(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['deadline'] = message.text
    await dbcompanies.addNewOneTimeWork(state)
    applInfo = dbapplicants.getIdAndNameAppl(data['tg_id'])
    # кнопка откликнуться для канала
    respond_kb = InlineKeyboardMarkup(row_width=1)
    respForOneTime = InlineKeyboardButton(text='Откликнуться', callback_data='respForOneTimeWork_'+str(data['tg_id']))
    respond_kb.add(respForOneTime)
    # Постинг поста о новой работе в канал
    forChannelText = 'Появилась новая работа\n\nНазвание: ' + data['onetimeName'] + \
                    '\nКомпания: ' + applInfo['firstname'] + applInfo['lastname'] +\
                    '\nСуть работы: ' + data['meaningofwork'] + '\nДедлайн: ' + data['deadline']
    await bot.send_message(-1001683304908, forChannelText, reply_markup=respond_kb)
    await state.finish()
    successText = '''
    Работа успешно создана и доступна соискателям
    '''
    await bot.send_message(message.from_user.id, successText, reply_markup=mainApplicant_kb)

# @dp.message_handler(commands=['работа с резюме'])
async def resume_working(message : types.Message):
    try:
        tg_id = message.from_user.id
        countUs = dbusers.checkUserByTgId(tg_id)
        if countUs == 0:
            dbusers.addNewNaked(message.from_user.id, message.from_user.username, message.from_user.first_name)
            saluteText = 'Добро пожаловать!\njobbot создан для удобного сотрудничества исполнителей с \
            заказчиками.\n\nВы можете разместить свое резюме, или добавить вакансию.'
            await message.reply(saluteText, reply_markup=first_kb)
        else:
            countAppl = dbapplicants.checkApplByTgId(tg_id)
            if (countAppl > 0):
                mainTxt = 'Выберите действие, которое Вы хотите произвести с Вашими резюме'
                await message.reply(mainTxt, reply_markup=resumeWorking_kb)
            else:
                saluteText = 'Приветствуем снова!\nВы еще не добавляли резюме и не публиковали вакансий. \
                \n\nХотите сделать это сейчас?'
                await message.reply(saluteText, reply_markup=first_kb)
    except:
        await message.reply('Возникла какая-то ошибка, попробуйте повторить команду /start')

# по нажатию инлайн кнопки с откликом на разовую работу в канале телеграм
@dp.callback_query_handler(Text(startswith='respForOneTimeWork_'))
async def resp_for_onetimework_channel(callback : types.CallbackQuery):
    tg_id = callback.from_user.id
    countUs = dbusers.checkUserByTgId(tg_id)
    if countUs == 0:
        dbusers.addNewNaked(callback.from_user.id, callback.from_user.username, callback.from_user.first_name)
        saluteText = 'Добро пожаловать!\njobbot создан для удобного сотрудничества исполнителей с \
        заказчиками.\n\nВы можете разместить свое резюме, или добавить вакансию.'
        await bot.send_message(callback.from_user.id, saluteText, reply_markup=first_kb)
        await callback.answer()
    else:
        countAppl = dbapplicants.checkApplByTgId(tg_id)
        countComp = dbcompanies.checkCompByTgId(tg_id)
        if countComp == 0:
            if countAppl == 0:
                makedJobText = 'У Вас еще нет резюме, чтобы откликаться на вакансии.\n'\
                                'Можете создать его'
                await bot.send_message(callback.from_user.id, makedJobText, reply_markup=sendcomaccept_kb)
                await callback.answer()
            elif countAppl > 0:
                user_tg_id = int(callback.data.split('_')[1])
                if tg_id == user_tg_id:
                    saluteText = 'Нельзя откликнуться на свою работу'
                    await bot.send_message(callback.from_user.id, saluteText, reply_markup=mainApplicant_kb)
                else:
                    # отправка сообщения работодателю, что на его работу был отклик
                    # с данными соискателя
                    allApplInfo = dbapplicants.getAllApplInfoById(user_tg_id)
                    print(allApplInfo)
                    forUserText = 'На Вашу работу поступил новый отклик'
                    await bot.send_message(user_tg_id, forUserText, reply_markup=mainApplicant_kb)
                    forUserText2 = '<b>Соискатель:</b> ' + allApplInfo['firstname'] + ' ' + allApplInfo['lastname'] + '\n\n' +\
                                    '<b>Направление деятельности:</b> ' + allApplInfo['line-business'] + '\n\n' +\
                                    '<b>Форма обучения:</b> ' + allApplInfo['education-form'] + '\n\n' +\
                                    '<b>Желаемая должность:</b> ' + allApplInfo['career-objective'] + '\n\n' +\
                                    '<b>Город работы:</b> ' + allApplInfo['city-work'] + '\n\n' +\
                                    '<b>Возможность работать удаленно:</b> ' + allApplInfo['distant-work'] + '\n\n' +\
                                    '<b>Готовность к переезду:</b> ' + allApplInfo['relocate'] + '\n\n' +\
                                    '<b>Опыт работы:</b> ' + allApplInfo['work-experience']
                    await bot.send_message(user_tg_id, forUserText2, reply_markup=mainApplicant_kb, parse_mode=types.ParseMode.HTML)
                    # сообщение соискателю, что его отклик успешно отправлен
                    saluteText = 'Ваш отклик отправлен работодателю'
                    await bot.send_message(callback.from_user.id, saluteText, reply_markup=mainApplicant_kb)
        elif countComp == 1:
            user_tg_id = int(callback.data.split('_')[1])
            if tg_id == user_tg_id:
                saluteText = 'Нельзя откликнуться на свою работу'
                await bot.send_message(callback.from_user.id, saluteText, reply_markup=mainCompany_kb)
            else:
                saluteText = 'Ваш отклик отправлен работодателю'
                await bot.send_message(callback.from_user.id, saluteText, reply_markup=mainApplicant_kb)


def register_handlers_client(dp : Dispatcher):
    dp.register_message_handler(login_as_applicant, Text(equals="войти как соискатель", ignore_case=True))
    dp.register_message_handler(go_to_mainappl_menu, Text(equals="вернуться в меню соискателя", ignore_case=True))
    dp.register_message_handler(search_employers, Text(equals="найти вакансию", ignore_case=True))
    dp.register_message_handler(go_to_main, Text(equals="вернуться в главное меню", ignore_case=True))
    dp.register_message_handler(go_to_main, Text(equals="перейти в главное меню", ignore_case=True))
    dp.register_message_handler(resume_working, Text(equals="работа с резюме", ignore_case=True))
    # dp.register_message_handler(command_add_edu, Text(equals="добавить дополнительное образование", ignore_case=True), state=None)
    dp.register_message_handler(edit_my_appls, Text(equals="редактировать резюме", ignore_case=True), state=None)
    dp.register_message_handler(get_edu, state=FSMAddedu.edu)
    dp.register_message_handler(get_eduform, state=FSMAddedu.eduForm)
    dp.register_message_handler(get_new_appl_data, state=FSMGotoeditappldata.updtdata)
    dp.register_message_handler(load_pdffile, content_types=['document'], state=FSMNewpdffile.pdffile)
    dp.register_message_handler(get_onetime_name_forappl, state=FSMNewonetimeforappl.onetName)
    dp.register_message_handler(get_meaningwork, state=FSMNewonetimeforappl.meaningwork)
    dp.register_message_handler(get_deadlineforappl, state=FSMNewonetimeforappl.deadlineforappl)

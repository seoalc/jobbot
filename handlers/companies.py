from aiogram import types, Dispatcher
from bot_create import dp, bot
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.types import ReplyKeyboardRemove
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher.filters import Text

from db import dbusers, dbcommon, dbapplicants, dbcompanies
from keyboards import cancel_kb, skip_step, mainApplicant_kb, mainCompany_kb, onetimeforappl_kb, cancelwithyes_kb, first2_kb, firstComp_kb, \
goToApplicant_kb, editCompData_kb, respWorking_kb

# @dp.message_handler(commands=['войти как работодатель'])
async def login_as_company(message : types.Message):
    try:
        tg_id = message.from_user.id
        countUs = dbusers.checkUserByTgId(tg_id)
        if countUs == 0:
            dbusers.addNewNaked(message.from_user.id, message.from_user.username, message.from_user.first_name)
            saluteText = 'Добро пожаловать!\njobbot создан для удобного сотрудничества исполнителей с \
            заказчиками.\n\nВы можете разместить свое резюме, или добавить вакансию.'
            await message.reply(saluteText, reply_markup=first2_kb)
        else:
            countComp = dbcompanies.checkCompByTgId(tg_id)
            if countComp == 0:
                saluteText = 'Приветствуем снова!\nВы еще не зарегистрировали компанию. \
                \n\nХотите сделать это сейчас?'
                await message.reply(saluteText, reply_markup=firstComp_kb)
            elif countComp == 1:
                saluteText = 'Вы вошли как работодатель'
                await message.reply(saluteText, reply_markup=mainCompany_kb)
    except:
        await message.reply('Возникла какая-то ошибка, попробуйте повторить команду /start')

# @dp.message_handler(commands=['вернуться в меню компании'])
async def go_to_main_comp_menu(message : types.Message):
    try:
        tg_id = message.from_user.id
        countUs = dbusers.checkUserByTgId(tg_id)
        if countUs == 0:
            dbusers.addNewNaked(message.from_user.id, message.from_user.username, message.from_user.first_name)
            saluteText = 'Добро пожаловать!\njobbot создан для удобного сотрудничества исполнителей с \
            заказчиками.\n\nВы можете разместить свое резюме, или добавить вакансию.'
            await message.reply(saluteText, reply_markup=first_kb)
        else:
            countComp = dbcompanies.checkCompByTgId(tg_id)
            if countComp > 0:
                mainTxt = 'Вы в главном меню компании'
                await message.reply(mainTxt, reply_markup=mainCompany_kb)
            else:
                saluteText = 'Приветствуем снова!\nВы еще не добавляли резюме и не публиковали вакансий. \
                \n\nХотите сделать это сейчас?'
                await message.reply(saluteText, reply_markup=first_kb)
    except:
        await message.reply('Возникла какая-то ошибка, попробуйте повторить команду /start')

# создание новой вакансии
class FSMNewemployer(StatesGroup):
    careerObjective2 = State()
    desiredSalary2 = State()
    workFormat = State()
    employment = State()
    duties = State()
    requirements = State()
    workingConditions = State()
    fio = State()
    phone2 = State()
    email2 = State()
# @dp.message_handler(commands=['создать вакансию'])
async def create_empl(message : types.Message):
    try:
        tg_id = message.from_user.id
        countUs = dbusers.checkUserByTgId(tg_id)
        if countUs == 0:
            dbusers.addNewNaked(message.from_user.id, message.from_user.username, message.from_user.first_name)
            saluteText = 'Добро пожаловать!\njobbot создан для удобного сотрудничества исполнителей с \
            заказчиками.\n\nВы можете разместить свое резюме, или добавить вакансию.'
            await message.reply(saluteText, reply_markup=first_kb)
        elif countUs == 1:
            countComp = dbcompanies.checkCompByTgId(tg_id)
            if countComp == 0:
                saluteText = 'Вы еще не регистрировали компанию. \
                \n\nХотите сделать это сейчас?'
                await message.reply(saluteText, reply_markup=first2_kb)
            elif countComp == 1:
                await FSMNewemployer.careerObjective2.set()
                await message.reply("Введите должность, на которую требуется сотрудник", reply_markup=cancel_kb)
                # saluteText = 'Главное меню работодателя'
                # await message.reply(saluteText, reply_markup=mainCompany_kb)
    except:
        await message.reply('Возникла какая-то ошибка, попробуйте повторить команду /start')

# Ловим должность и пишем в словарь
# @dp.message_handler(state=FSMNewemployer.careerObjective2)
async def get_careerobjective2(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['tg_id'] = message.from_user.id
        if message.from_user.username == None:
            data['tg-login'] = 'None'
        else:
            data['tg-login'] = message.from_user.username
        companyInfo = dbcompanies.getIdAndCityComp(data['tg_id'])
        data['companyId'] = companyInfo['id']
        data['careerObjective2'] = message.text
    await FSMNewemployer.next()
    await message.reply("Укажите зарплату", reply_markup=cancel_kb)

# Ловим зарплату и пишем в словарь
# @dp.message_handler(state=FSMNewemployer.desiredSalary2)
async def get_desiredsalary2(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['desiredSalary2'] = message.text
        companyInfo = dbcompanies.getIdAndCityComp(data['tg_id'])
        wanText = 'Вы указали город дислокации компании - ' + companyInfo["city"] + \
        '\n\nУкажите возможен ли удаленный формат работы'
    await FSMNewemployer.next()
    await message.reply(wanText, reply_markup=cancelwithyes_kb)

# Ловим формат работы
# @dp.message_handler(state=FSMNewemployer.cityWork2)
async def get_work_format(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['workFormat'] = message.text
    await FSMNewemployer.next()
    await message.reply("Укажите график работы\n\nНапример, 5/2", reply_markup=cancel_kb)

# Пишем формат занятости в словарь
# @dp.message_handler(state=FSMNewemployer.employment)
async def get_employments(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['employment'] = message.text
    await FSMNewemployer.next()
    await message.reply("Распишите обязанности для данного сотрудника", reply_markup=cancel_kb)

# Пишем обязанности в словарь
# @dp.message_handler(state=FSMNewemployer.duties)
async def get_duties(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['duties'] = message.text
    await FSMNewemployer.next()
    await message.reply("Укажите требования для соискателя на данную должность (наличие каких-либо документов и т.д.)", reply_markup=cancel_kb)

# Пишем требования в словарь
# @dp.message_handler(state=FSMNewemployer.requirements)
async def get_requirement(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['requirements'] = message.text
    await FSMNewemployer.next()
    await message.reply("Укажите условия работы", reply_markup=cancel_kb)

# Пишем условия работы в словарь
# @dp.message_handler(state=FSMNewemployer.workingConditions)
async def get_workingconditions(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['workingConditions'] = message.text
    await FSMNewemployer.next()
    await message.reply("Укажите ФИО контактного лица (необязательно)\n\nЛибо пропустите шаг", reply_markup=skip_step)

# Пишем ФИО в словарь
# @dp.message_handler(state=FSMNewemployer.fio)
async def get_fio(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        if message.text == 'Пропустить':
            data['fio'] = 'empty'
        else:
            data['fio'] = message.text
    await FSMNewemployer.next()
    await message.reply("Укажите телефон контактного лица для связи (необязательно)\n\nЛибо пропустите шаг", reply_markup=skip_step)

# Пишем телефон контактного лица в словарь
# @dp.message_handler(state=FSMNewemployer.phone2)
async def get_phone2(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        if message.text == 'Пропустить':
            data['phone2'] = 'empty'
        else:
            data['phone2'] = message.text
    await FSMNewemployer.next()
    await message.reply("Укажите email контактного лица (необязательно)\n\nЛибо пропустите шаг", reply_markup=skip_step)

# Пишем email контактного лица в словарь, и закрываем машинное состояние
# @dp.message_handler(state=FSMNewemployer.email2)
async def get_email2(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        if message.text == 'Пропустить':
            data['email2'] = 'empty'
        else:
            data['email2'] = message.text
    await bot.send_message(message.from_user.id, "Идет отправка данных на сервер...")
    emplId = await dbusers.addNewEmployer(state)
    # кнопка откликнуться для канала
    respond_kb = InlineKeyboardMarkup(row_width=1)
    respForEmplInChannel = InlineKeyboardButton(text='Откликнуться', callback_data='respForEmplInChannel_'+\
                                        str(data['tg_id'])+'_'+str(data['companyId'])+'_'+str(emplId))
    respond_kb.add(respForEmplInChannel)
    # Постинг поста о новой работе в канал
    companyInfo = dbcompanies.getNameComp(data['tg_id'])
    forChannelText = '<b>Появилась новая вакансия</b>\n\n<b>Компания: </b>' + companyInfo['company-name'] + \
                    '\n<b>Должность: </b>' + data['careerObjective2'] +\
                    '\n<b>Удаленный формат: </b>' + data['workFormat'] +\
                    '\n<b>Зарплата: </b>' + data['desiredSalary2'] + \
                    '\n\n<b>Обязанности:</b>\n' + data['duties'] +\
                    '\n\n<b>Условия:</b>\n' + data['workingConditions']
    await bot.send_message(-1001683304908, forChannelText, reply_markup=respond_kb, parse_mode=types.ParseMode.HTML)
    await state.finish()
    successText = '''
    Вакансия успешно создана и доступна соискателям
    '''
    await bot.send_message(message.from_user.id, successText, reply_markup=mainCompany_kb)

class FSMNewonetimework(StatesGroup):
    onetimeName = State()
    meaningofwork = State()
    deadline = State()

# @dp.message_handler(commands=['создать разовую работу'])
async def create_onetmwrk(message : types.Message):
    tg_id = message.from_user.id
    countUs = dbusers.checkUserByTgId(tg_id)
    if countUs == 0:
        dbusers.addNewNaked(message.from_user.id, message.from_user.username, message.from_user.first_name)
        saluteText = 'Добро пожаловать!\njobbot создан для удобного сотрудничества исполнителей с \
        заказчиками.\n\nВы можете разместить свое резюме, или добавить вакансию.'
        await message.reply(saluteText, reply_markup=first_kb)
    elif countUs == 1:
        countComp = dbcompanies.checkCompByTgId(tg_id)
        if countComp == 0:
            countAppl = dbapplicants.checkApplByTgId(tg_id)
            if (countAppl > 0):
                await message.answer("ok", reply_markup=goToApplicant_kb)
                saluteText = 'Вы создаете разовую работу с аккаунта соискателя\nПодтвердите действие'
                await message.reply(saluteText, reply_markup=onetimeforappl_kb)
            else:
                saluteText = 'Вы еще не регистрировали компанию и не создавали резюме. \
                \n\nХотите сделать это сейчас?'
                await message.reply(saluteText, reply_markup=first2_kb)
        elif countComp == 1:
            await FSMNewonetimework.onetimeName.set()
            await message.reply("Введите название работы", reply_markup=cancel_kb)
            # saluteText = 'Главное меню работодателя'
            # await message.reply(saluteText, reply_markup=mainCompany_kb)

# Ловим название и пишем в словарь
# @dp.message_handler(state=FSMNewonetimework.onetimeName)
async def get_onetime_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['tg_id'] = message.from_user.id
        if message.from_user.username == None:
            data['tg-login'] = 'None'
        else:
            data['tg-login'] = message.from_user.username
        companyInfo = dbcompanies.getIdAndCityComp(data['tg_id'])
        data['companyId'] = companyInfo['id']
        data['onetimeName'] = message.text
    await FSMNewonetimework.next()
    await message.reply("Распишите более подробно суть работы", reply_markup=cancel_kb)

# Ловим суть работы и пишем в словарь
# @dp.message_handler(state=FSMNewonetimework.meaningofwork)
async def get_meaningofwork(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['meaningofwork'] = message.text
    await FSMNewonetimework.next()
    await message.reply("Укажите дедлайн", reply_markup=cancel_kb)

# Пишем дедлайн в словарь, и закрываем машинное состояние
# @dp.message_handler(state=FSMNewonetimework.deadline)
async def get_deadline(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['deadline'] = message.text
    await dbcompanies.addNewOneTimeWork(state)
    # Постинг поста о новой работе в канал
    companyInfo = dbcompanies.getNameComp(data['tg_id'])
    # кнопка откликнуться для канала
    respond_kb = InlineKeyboardMarkup(row_width=1)
    respForOneTime = InlineKeyboardButton(text='Откликнуться', callback_data='respForOneTimeWork_'+str(data['tg_id']))
    respond_kb.add(respForOneTime)
    forChannelText = 'Появилась новая работа\n\nНазвание: ' + data['onetimeName'] + '\nКомпания: ' + companyInfo['company-name'] +\
                    '\nСуть работы: ' + data['meaningofwork'] + '\nДедлайн: ' + data['deadline']
    await bot.send_message(-1001683304908, forChannelText, reply_markup=respond_kb)
    await state.finish()
    successText = '''
    Работа успешно создана и доступна соискателям
    '''
    await bot.send_message(message.from_user.id, successText, reply_markup=mainCompany_kb)

# по нажатию инлайн кнопки с для просмотра резюме того, кто откликнулся
@dp.callback_query_handler(Text(startswith='lookResponAppl_'))
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
                # из инлайн кнопки получаю id компании и вакансии
                applId = int(callback.data.split('_')[1])
                emplId = int(callback.data.split('_')[2])
                # кнопка принять отклик на вакансию работодателем
                applyresp_kb = InlineKeyboardMarkup(row_width=1)
                applyRespForVac = InlineKeyboardButton(text='Принять отклик', callback_data='applyRespForVacancy_'+str(applId)+'_'+str(emplId))
                applyresp_kb.add(applyRespForVac)
                applInfo = dbapplicants.getApplInfoByApplId(applId)
                if applInfo['tg-login'] == 'None':
                    applInfo['tg-login'] = 'Не указано'
                forEmplText = '<b>Имя:</b>\n' + applInfo['firstname'] + ' ' + applInfo['lastname'] + ' ' + applInfo['patronymic'] + '\n'\
                                '<b>Направление деятельности:</b>\n' + applInfo['line-business'] + '\n'\
                                '<b>Программа обучения:</b>\n' + applInfo['education-form'] + '\n'\
                                '<b>Желаемая должность:</b>\n' + applInfo['career-objective'] + '\n'\
                                '<b>Желаемая зарплата:</b>\n' + applInfo['desired-salary'] + '\n'\
                                '<b>Опыт работы:</b>\n' + applInfo['work-experience'] + '\n'\
                                '<b>Город:</b>\n' + applInfo['city-work'] + '\n'\
                                '<b>Возможность работать удаленно:</b>\n' + applInfo['distant-work'] + '\n'\
                                '<b>Готовность к переезду:</b>\n' + applInfo['relocate'] + '\n'\
                                '<b>Логин в телеграме:</b>\n' + applInfo['tg-login'] + '\n'
                await bot.send_message(callback.from_user.id, forEmplText, parse_mode=types.ParseMode.HTML, reply_markup=applyresp_kb)
                await callback.answer()
            else:
                saluteText = 'Приветствуем снова!\nВы еще не добавляли резюме и не публиковали вакансий. \
                \n\nХотите сделать это сейчас?'
                await bot.send_message(callback.from_user.id, saluteText, reply_markup=first_kb)
                await callback.answer()
    except:
        await bot.send_message(callback.from_user.id, 'Возникла какая-то ошибка, попробуйте повторить команду /start')
        await callback.answer()

# по нажатию инлайн кнопки принять отклик на вакансию
@dp.callback_query_handler(Text(startswith='applyRespForVacancy_'))
async def apply_resp_for_vacancy(callback : types.CallbackQuery):
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
                # из инлайн кнопки получаю id компании и вакансии
                applId = int(callback.data.split('_')[1])
                emplId = int(callback.data.split('_')[2])
                applInfo = dbapplicants.getApplInfoByApplId(applId)
                oneEmplInfo = dbapplicants.getOneEmplInfo(emplId)
                forEmplText = 'Вы приняли ' + applInfo['firstname'] + ' ' + applInfo['lastname'] + ' ' + applInfo['patronymic'] + '\n\n'\
                                'на вакансию:\n'\
                                '<b>Требуемая должность:</b>\n' + oneEmplInfo['career-objective'] + '\n'\
                                '<b>Должностные обязанности:</b>\n' + oneEmplInfo['duties'] + '\n\n'\
                                '<b>Требования к кандидату:</b>\n' + oneEmplInfo['requirements'] + '\n\n'
                await bot.send_message(callback.from_user.id, forEmplText, parse_mode=types.ParseMode.HTML)
                await bot.send_message(callback.from_user.id, 'Эта вакансия теперь будет недоступна другим соискателям')
                await callback.answer()
            else:
                saluteText = 'Приветствуем снова!\nВы еще не добавляли резюме и не публиковали вакансий. \
                \n\nХотите сделать это сейчас?'
                await bot.send_message(callback.from_user.id, saluteText, reply_markup=first_kb)
                await callback.answer()
    except:
        await bot.send_message(callback.from_user.id, 'Возникла какая-то ошибка, попробуйте повторить команду /start')
        await callback.answer()

# @dp.message_handler(commands=['работа с данными компании'])
async def comp_data_edit_menu(message : types.Message):
    try:
        tg_id = message.from_user.id
        countUs = dbusers.checkUserByTgId(tg_id)
        if countUs == 0:
            dbusers.addNewNaked(message.from_user.id, message.from_user.username, message.from_user.first_name)
            saluteText = 'Добро пожаловать!\njobbot создан для удобного сотрудничества исполнителей с \
            заказчиками.\n\nВы можете разместить свое резюме, или добавить вакансию.'
            await message.reply(saluteText, reply_markup=first_kb)
        else:
            countComp = dbcompanies.checkCompByTgId(tg_id)
            if countComp > 0:
                mainTxt = 'Выберите действие, которое Вы хотите произвести с данными о Вашей компании или вакансиях'
                await message.reply(mainTxt, reply_markup=editCompData_kb)
            else:
                saluteText = 'Приветствуем снова!\nВы еще не добавляли резюме и не публиковали вакансий. \
                \n\nХотите сделать это сейчас?'
                await message.reply(saluteText, reply_markup=first_kb)
    except:
        await message.reply('Возникла какая-то ошибка, попробуйте повторить команду /start')

# @dp.message_handler(commands=['редакитровать данные о компании'])
async def comp_data_edit_now(message : types.Message):
    try:
        tg_id = message.from_user.id
        countUs = dbusers.checkUserByTgId(tg_id)
        if countUs == 0:
            dbusers.addNewNaked(message.from_user.id, message.from_user.username, message.from_user.first_name)
            saluteText = 'Добро пожаловать!\njobbot создан для удобного сотрудничества исполнителей с \
            заказчиками.\n\nВы можете разместить свое резюме, или добавить вакансию.'
            await message.reply(saluteText, reply_markup=first_kb)
        else:
            countComp = dbcompanies.checkCompByTgId(tg_id)
            if countComp > 0:
                compInfo = dbcompanies.getOneCompanyInfoByTGID(tg_id)
                # кнопка с выбором тех данных, которые нужно отредактировать
                applData1 = InlineKeyboardButton(text='Название компании', callback_data='compData_compname_')
                applData2 = InlineKeyboardButton(text='Направление деятельности',
                                                callback_data='compData_linebusiness_'+\
                                                str(compInfo['line-business-id']))
                applData3 = InlineKeyboardButton(text='Город', callback_data='compData_city_')
                send_compData_for_edit = InlineKeyboardMarkup(row_width=1).row(applData1).row(applData2).row(applData3)
                mainTxt = 'Выберите какой из пунктов о компании хотите отредактировать'
                await message.reply(mainTxt, reply_markup=send_compData_for_edit)
            else:
                saluteText = 'Приветствуем снова!\nВы еще не добавляли резюме и не публиковали вакансий. \
                \n\nХотите сделать это сейчас?'
                await message.reply(saluteText, reply_markup=first_kb)
    except:
        await message.reply('Возникла какая-то ошибка, попробуйте повторить команду /start')

class FSMGotoeditcompdata(StatesGroup):
    updtdatacomp = State()
# по нажатию инлайн кнопки с параметром для редактирования данных о компании
@dp.callback_query_handler(Text(startswith='compData_'))
async def comp_data_edit_get(callback : types.CallbackQuery):
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
                global changeSuccessText2
                global dataNameComp
                dataNameComp = callback.data.split('_')[1]
                if dataNameComp == 'compname':
                    changeAlert = 'Последний раз Вы указали имя - '
                    changeSuccessText2 = 'Ваше имя изменено на - '
                    dataNameComp = 'company-name'
                elif dataNameComp == 'linebusiness':
                    changeAlert = 'Последний раз Вы указали направление деятельности - '
                    changeSuccessText2 = 'Направление деятельности изменено на - '
                    dataNameComp = 'line-business'
                    lineBusinessInfo = dbcommon.getAllLineBusiness()
                    listEmp = []
                    for item in lineBusinessInfo:
                        listEmp.append(item['id'])
                    linesText = ''
                    for item in lineBusinessInfo:
                        linesText = linesText + str(item['id']) + ' - ' + item['name'] + '\n'
                elif dataNameComp == 'city':
                    changeAlert = 'Последний раз Вы указали город - '
                    changeSuccessText2 = 'Город изменен на - '
                compDataByDataName = dbcompanies.getCompDataByDataName(dataNameComp, tg_id)
                await FSMGotoeditcompdata.updtdatacomp.set()
                if 'linesText' in locals():
                    await bot.send_message(callback.from_user.id, changeAlert + str(compDataByDataName[dataNameComp]) + \
                                            '\n\nУкажите цифру нового значения', reply_markup=cancel_kb)
                    await bot.send_message(callback.from_user.id, linesText, reply_markup=cancel_kb)
                else:
                    await bot.send_message(callback.from_user.id, changeAlert + str(compDataByDataName[dataNameComp]) + \
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

# Продолжение машинного состояния по ловле изменяемого пункта данных о компании
# @dp.message_handler(state=FSMGotoeditcompdata.updtdatacomp)
async def get_new_comp_data(callback : types.CallbackQuery, state: FSMGotoeditcompdata):
    async with state.proxy() as data:
        data['tg-id'] = callback.from_user.id
        data['userData'] = callback.text
        data['dataName'] = dataNameComp
    if dataNameComp == 'line-business':
        lineBusinessInfo = dbcommon.getAllLineBusiness()
        listEmp = []
        for item in lineBusinessInfo:
            listEmp.append(item['id'])
        if int(callback.text) in listEmp:
            oneLineBusinessInfo = dbcommon.getLineBusinessById(int(callback.text))
            print(oneLineBusinessInfo)
            # data['lineBusiness'] = oneLineBusinessInfo[0]['name']
            # data['lineBusinessId'] = int(oneLineBusinessInfo[0]['id'])
            await dbcompanies.updtCompInfo2(oneLineBusinessInfo[0]['name'], int(oneLineBusinessInfo[0]['id']), data['tg-id'])
            await state.finish()
            await bot.send_message(callback.from_user.id, changeSuccessText2 + oneLineBusinessInfo[0]['name'], reply_markup=editCompData_kb)
            await callback.answer()
        else:
            await message.reply("Некорректно указан номер направления деятельности", reply_markup=cancel_kb)
            await callback.answer()
    else:
        await dbcompanies.updtCompInfo(state)
        await state.finish()
        await bot.send_message(callback.from_user.id, changeSuccessText2 + data['userData'], reply_markup=editCompData_kb)
        await callback.answer()

# @dp.message_handler(commands=['редакитровать вакансии'])
async def select_empl_for_edit(message : types.Message):
    try:
        tg_id = message.from_user.id
        countUs = dbusers.checkUserByTgId(tg_id)
        if countUs == 0:
            dbusers.addNewNaked(message.from_user.id, message.from_user.username, message.from_user.first_name)
            saluteText = 'Добро пожаловать!\njobbot создан для удобного сотрудничества исполнителей с \
            заказчиками.\n\nВы можете разместить свое резюме, или добавить вакансию.'
            await message.reply(saluteText, reply_markup=first_kb)
        else:
            countComp = dbcompanies.checkCompByTgId(tg_id)
            if countComp > 0:
                countEmpls = dbcompanies.checkEmplByTgId(tg_id)
                if countEmpls > 0:
                    allEmpls = dbcompanies.getAllEmplsByTGID(tg_id)
                    checkingText = "<b>Найдено Ваших вакансий:</b> " + str(countEmpls) +\
                                    "\n\nВыберите из списка ниже какую хотите отредактировать"
                    await message.reply(checkingText, parse_mode=types.ParseMode.HTML, reply_markup=editCompData_kb)
                    for item in allEmpls:
                        forEmplText = '<b>Требуемая должность:</b>\n' + item['career-objective'] + '\n'\
                                        '<b>Должностные обязанности:</b>\n' + item['duties'] + '\n'\
                                        '<b>Требования к кандидату:</b>\n' + item['requirements']
                        button = InlineKeyboardMarkup(row_width=1)
                        button.add(InlineKeyboardButton(text='Редактировать',
                                                        callback_data='editOneOfMyEmpl_' + str(item['id'])))
                        await message.answer(forEmplText, parse_mode=types.ParseMode.HTML, reply_markup=button)
                else:
                    mainTxt = 'Опубликованных Вами вакансий не найдено в боте'
                    await message.reply(mainTxt, reply_markup=editCompData_kb)
            else:
                saluteText = 'Приветствуем снова!\nВы еще не добавляли резюме и не публиковали вакансий. \
                \n\nХотите сделать это сейчас?'
                await message.reply(saluteText, reply_markup=first_kb)
    except:
        await message.reply('Возникла какая-то ошибка, попробуйте повторить команду /start')

# по нажатию инлайн кнопки выбор параметров вакансии, что нужно отредактить
@dp.callback_query_handler(Text(startswith='editOneOfMyEmpl_'))
async def select_edit_of_vacancy(callback : types.CallbackQuery):
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
            countComp = dbcompanies.checkCompByTgId(tg_id)
            if (countComp > 0):
                emplId = callback.data.split('_')[1]
                emplInfo = dbcompanies.getOneEmplInfoById(emplId)
                # кнопка с выбором тех данных, которые нужно отредактировать
                emplData1 = InlineKeyboardButton(text='Направление деятельности', callback_data='emplData_careerobjective_'+emplId)
                emplData2 = InlineKeyboardButton(text='Зарплата', callback_data='emplData_desiredsalary_'+emplId)
                emplData3 = InlineKeyboardButton(text='Возможность удаленной работы', callback_data='emplData_workformat_'+emplId)
                emplData4 = InlineKeyboardButton(text='График работы', callback_data='emplData_employment_'+emplId)
                emplData5 = InlineKeyboardButton(text='Обязанности', callback_data='emplData_duties_'+emplId)
                emplData6 = InlineKeyboardButton(text='Требования к кандидату', callback_data='emplData_requirements_'+emplId)
                emplData7 = InlineKeyboardButton(text='Условия работы', callback_data='emplData_workingconditions_'+emplId)
                send_emplData_for_edit = InlineKeyboardMarkup(row_width=1).row(emplData1).row(emplData2).row(emplData3).\
                                                                        row(emplData4).row(emplData5).row(emplData6).row(emplData7)
                mainTxt = 'Выберите какой из пунктов о вакансии хотите отредактировать'
                await bot.send_message(callback.from_user.id, mainTxt, reply_markup=send_emplData_for_edit)
            else:
                saluteText = 'Приветствуем снова!\nВы еще не добавляли резюме и не публиковали вакансий. \
                \n\nХотите сделать это сейчас?'
                await bot.send_message(callback.from_user.id, saluteText, reply_markup=first_kb)
                await callback.answer()
    except:
        await bot.send_message(callback.from_user.id, 'Возникла какая-то ошибка, попробуйте повторить команду /start')
        await callback.answer()

class FSMGotoeditempldata(StatesGroup):
    updtdataempl = State()
# по нажатию инлайн кнопки с параметром для редактирования данных о резюме
@dp.callback_query_handler(Text(startswith='emplData_'))
async def empl_data_edit_get(callback : types.CallbackQuery):
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
            countComp = dbcompanies.checkCompByTgId(tg_id)
            if countComp > 0:
                global changeSuccessText2
                global dataNameEmpl
                global emplId
                dataNameEmpl = callback.data.split('_')[1]
                emplId = callback.data.split('_')[2]
                if dataNameEmpl == 'careerobjective':
                    changeAlert = 'Последний раз Вы указали должность - '
                    changeSuccessText2 = 'Должность изменена на - '
                    dataNameEmpl = 'career-objective'
                elif dataNameEmpl == 'desiredsalary':
                    changeAlert = 'Последний раз Вы указали зарплату - '
                    changeSuccessText2 = 'Зарплата изменена на - '
                    dataNameEmpl = 'desired-salary'
                elif dataNameEmpl == 'workformat':
                    changeAlert = 'Последний раз Вы указали возможность удаленной работы - '
                    changeSuccessText2 = 'Возможность удаленной работы изменена на - '
                elif dataNameEmpl == 'employment':
                    changeAlert = 'Последний раз Вы указали график работы - '
                    changeSuccessText2 = 'График работы изменен на - '
                elif dataNameEmpl == 'duties':
                    changeAlert = 'Последний раз Вы указали обязанности - \n'
                    changeSuccessText2 = 'Обязанности изменены на - '
                elif dataNameEmpl == 'requirements':
                    changeAlert = 'Последний раз Вы указали требования к кандидату - \n'
                    changeSuccessText2 = 'Требования к кандидату изменены на - '
                elif dataNameEmpl == 'workingconditions':
                    changeAlert = 'Последний раз Вы указали условия работы - \n'
                    changeSuccessText2 = 'Условия работы изменены на - '
                    dataNameEmpl = 'working-conditions'
                emplDataByDataName = dbcompanies.getEmplDataByDataName(dataNameEmpl, emplId)
                print(emplDataByDataName)
                print(dataNameEmpl)
                await FSMGotoeditempldata.updtdataempl.set()
                await bot.send_message(callback.from_user.id, changeAlert + str(emplDataByDataName[dataNameEmpl]) + \
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

# Продолжение машинного состояния по ловле изменяемого пункта данных о вакансии
# @dp.message_handler(state=FSMGotoeditempldata.updtdataempl)
async def get_new_empl_data(callback : types.CallbackQuery, state: FSMGotoeditcompdata):
    async with state.proxy() as data:
        data['userData'] = callback.text
        data['dataName'] = dataNameEmpl
        data['emplId'] = emplId
        await dbcompanies.updtEmplInfo(data['userData'], data['dataName'], data['emplId'])
        await state.finish()
        await bot.send_message(callback.from_user.id, changeSuccessText2 + callback.text, reply_markup=editCompData_kb)

# @dp.message_handler(commands=['работа с откликами'])
async def responses_working_menu(message : types.Message):
    try:
        tg_id = message.from_user.id
        countUs = dbusers.checkUserByTgId(tg_id)
        if countUs == 0:
            dbusers.addNewNaked(message.from_user.id, message.from_user.username, message.from_user.first_name)
            saluteText = 'Добро пожаловать!\njobbot создан для удобного сотрудничества исполнителей с \
            заказчиками.\n\nВы можете разместить свое резюме, или добавить вакансию.'
            await message.reply(saluteText, reply_markup=first_kb)
        else:
            countComp = dbcompanies.checkCompByTgId(tg_id)
            if countComp > 0:
                mainText = 'Вы в меню работы с откликами'
                await message.answer(mainText, reply_markup=respWorking_kb)
            else:
                saluteText = 'Приветствуем снова!\nВы еще не добавляли резюме и не публиковали вакансий. \
                \n\nХотите сделать это сейчас?'
                await message.reply(saluteText, reply_markup=first_kb)
    except:
        await message.reply('Возникла какая-то ошибка, попробуйте повторить команду /start')

# @dp.message_handler(commands=['посмотреть отклики'])
async def look_responses_menu(message : types.Message):
    try:
        tg_id = message.from_user.id
        countUs = dbusers.checkUserByTgId(tg_id)
        if countUs == 0:
            dbusers.addNewNaked(message.from_user.id, message.from_user.username, message.from_user.first_name)
            saluteText = 'Добро пожаловать!\njobbot создан для удобного сотрудничества исполнителей с \
            заказчиками.\n\nВы можете разместить свое резюме, или добавить вакансию.'
            await message.reply(saluteText, reply_markup=first_kb)
        else:
            countComp = dbcompanies.checkCompByTgId(tg_id)
            if countComp > 0:
                countEmpls = dbcompanies.checkEmplByTgId(tg_id)
                if countEmpls > 0:
                    allEmpls = dbcompanies.getAllEmplsByTGID(tg_id)
                    checkingText = "<b>Найдено Ваших вакансий:</b> " + str(countEmpls) +\
                                    "\n\nВыберите из списка ниже, отклики к которой хотите посмотреть"
                    await message.reply(checkingText, parse_mode=types.ParseMode.HTML, reply_markup=editCompData_kb)
                    for item in allEmpls:
                        forEmplText = '<b>Требуемая должность:</b>\n' + item['career-objective'] + '\n'\
                                        '<b>Должностные обязанности:</b>\n' + item['duties'] + '\n'\
                                        '<b>Требования к кандидату:</b>\n' + item['requirements']
                        button = InlineKeyboardMarkup(row_width=1)
                        button.add(InlineKeyboardButton(text='Смотреть',
                                                        callback_data='looktEmplResp_' + str(item['id'])))
                        await message.answer(forEmplText, parse_mode=types.ParseMode.HTML, reply_markup=button)
                else:
                    mainTxt = 'Опубликованных Вами вакансий не найдено в боте'
                    await message.reply(mainTxt, reply_markup=editCompData_kb)
            else:
                saluteText = 'Приветствуем снова!\nВы еще не добавляли резюме и не публиковали вакансий. \
                \n\nХотите сделать это сейчас?'
                await message.reply(saluteText, reply_markup=first_kb)
    except:
        await message.reply('Возникла какая-то ошибка, попробуйте повторить команду /start')

# по нажатию инлайн кнопки просмотра откликов для одной конкретной вакансии
@dp.callback_query_handler(Text(startswith='looktEmplResp_'))
async def look_empl_resp(callback : types.CallbackQuery):
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
            countComp = dbcompanies.checkCompByTgId(tg_id)
            if (countComp > 0):
                emplId = callback.data.split('_')[1]
                emplResps = dbcompanies.getResposesForEmplById(emplId)
                countResps = len(emplResps)
                mainTxt = 'На вакансию найдено '+str(countResps)+" откликов:"
                await bot.send_message(callback.from_user.id, mainTxt, reply_markup=respWorking_kb)
                for item in emplResps:
                    # кнопка для просмотра полного резюме работодателем, которое откликнулось
                    lookResponAppl_kb = InlineKeyboardMarkup(row_width=1)
                    lookResponApplInBot = InlineKeyboardButton(text='Посмотреть резюме полностью',
                                                        callback_data='lookResponAppl_' + str(item['appl-id']) + '_' + str(emplId))
                    lookResponAppl_kb.add(lookResponApplInBot)
                    oneApplInfo = dbapplicants.getApplInfoByApplId(item['appl-id'])
                    print(oneApplInfo)
                    applText = '<b>Имя:</b> '+oneApplInfo['firstname']+' '+oneApplInfo['lastname']+' '+oneApplInfo['patronymic']+'\n'+\
                                '<b>Направление деятельности:</b> '+oneApplInfo['line-business']+'\n'+\
                                '<b>Желаемая должность:</b> '+oneApplInfo['career-objective']
                    await bot.send_message(callback.from_user.id, applText, parse_mode=types.ParseMode.HTML, reply_markup=lookResponAppl_kb)
            else:
                saluteText = 'Приветствуем снова!\nВы еще не добавляли резюме и не публиковали вакансий. \
                \n\nХотите сделать это сейчас?'
                await bot.send_message(callback.from_user.id, saluteText, reply_markup=first_kb)
                await callback.answer()
    except:
        await bot.send_message(callback.from_user.id, 'Возникла какая-то ошибка, попробуйте повторить команду /start')
        await callback.answer()





def register_handlers_client(dp : Dispatcher):
    dp.register_message_handler(login_as_company, Text(equals="войти как работодатель", ignore_case=True))
    dp.register_message_handler(go_to_main_comp_menu, Text(equals="вернуться в меню компании", ignore_case=True))
    dp.register_message_handler(create_empl, Text(equals="создать вакансию", ignore_case=True))
    # запись новой вакансии в базу
    # dp.register_message_handler(get_companyname, state=FSMNewemployer.companyName)
    # dp.register_message_handler(get_linebizz, state=FSMNewemployer.lineBizz)
    dp.register_message_handler(get_careerobjective2, state=FSMNewemployer.careerObjective2)
    dp.register_message_handler(get_desiredsalary2, state=FSMNewemployer.desiredSalary2)
    dp.register_message_handler(get_work_format, state=FSMNewemployer.workFormat)
    dp.register_message_handler(get_employments, state=FSMNewemployer.employment)
    dp.register_message_handler(get_duties, state=FSMNewemployer.duties)
    dp.register_message_handler(get_requirement, state=FSMNewemployer.requirements)
    dp.register_message_handler(get_workingconditions, state=FSMNewemployer.workingConditions)
    dp.register_message_handler(get_fio, state=FSMNewemployer.fio)
    dp.register_message_handler(get_phone2, state=FSMNewemployer.phone2)
    dp.register_message_handler(get_email2, state=FSMNewemployer.email2)
    # запись новой разовой работы в базу
    dp.register_message_handler(create_onetmwrk, Text(equals="создать разовую работу", ignore_case=True))
    dp.register_message_handler(get_onetime_name, state=FSMNewonetimework.onetimeName)
    dp.register_message_handler(get_meaningofwork, state=FSMNewonetimework.meaningofwork)
    dp.register_message_handler(get_deadline, state=FSMNewonetimework.deadline)
    dp.register_message_handler(comp_data_edit_menu, Text(equals="работа с данными компании", ignore_case=True))
    dp.register_message_handler(comp_data_edit_now, Text(equals="редактировать данные о компании", ignore_case=True))
    dp.register_message_handler(get_new_comp_data, state=FSMGotoeditcompdata.updtdatacomp)
    dp.register_message_handler(select_empl_for_edit, Text(equals="редактировать вакансии", ignore_case=True))
    dp.register_message_handler(get_new_empl_data, state=FSMGotoeditempldata.updtdataempl)
    dp.register_message_handler(responses_working_menu, Text(equals="работа с откликами", ignore_case=True))
    dp.register_message_handler(look_responses_menu, Text(equals="посмотреть отклики", ignore_case=True))

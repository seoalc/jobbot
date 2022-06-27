from aiogram import types, Dispatcher
from bot_create import dp, bot
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.types import ReplyKeyboardRemove
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher.filters import Text

from db import dbusers, dbcommon, dbapplicants, dbcompanies
from keyboards import inline_kb, first_kb, first2_kb, sendresumeaccept_kb, sendjobaccept_kb, sendcomaccept_kb
from keyboards import cancel_kb, skip_step, mainApplicant_kb, beforeApplicant_kb, beforeApplicant2_kb, mainCompany_kb, highMenu_kb, \
cancelwithyes_kb, editCompData_kb


# @dp.message_handler(commands=['start', 'help'])
async def command_start(message : types.Message):
    try:
        tg_id = message.from_user.id
        countUs = dbusers.checkUserByTgId(tg_id)
        if countUs == 0:
            dbusers.addNewNaked(message.from_user.id, message.from_user.username, message.from_user.first_name)
            saluteText = 'Добро пожаловать!\njobbot создан для удобного сотрудничества исполнителей с \
            заказчиками.\n\nВы можете разместить свое резюме, или добавить компанию.'
            await message.reply(saluteText, reply_markup=first2_kb)
        elif countUs == 1:
            countAppl = dbapplicants.checkApplByTgId(tg_id)
            countComp = dbcompanies.checkCompByTgId(tg_id)
            if countComp == 0:
                if countAppl == 0:
                    saluteText = 'Приветствуем снова!\nВы еще не зарегистрировались ни в качестве соискателя, ни в качестве работодателя. \
                    \n\nХотите сделать это сейчас?'
                    await message.reply(saluteText, reply_markup=first2_kb)
                elif countAppl > 0:
                    saluteText = 'Вы в главном меню.\nМожете войти как соискатель или работодатель'
                    await message.reply(saluteText, reply_markup=highMenu_kb)
            elif countComp == 1:
                saluteText = 'Вы в главном меню.\nМожете войти как соискатель или работодатель'
                await message.reply(saluteText, reply_markup=highMenu_kb)
    except:
        await message.reply('Возникла какая-то ошибка, попробуйте повторить команду /start')

# @dp.message_handler(commands=['вернуться в главное меню'])
async def go_to_high(message : types.Message):
    try:
        tg_id = message.from_user.id
        countUs = dbusers.checkUserByTgId(tg_id)
        if countUs == 0:
            dbusers.addNewNaked(message.from_user.id, message.from_user.username, message.from_user.first_name)
            saluteText = 'Добро пожаловать!\njobbot создан для удобного сотрудничества исполнителей с \
            заказчиками.\n\nВы можете разместить свое резюме, или добавить компанию.'
            await message.reply(saluteText, reply_markup=first2_kb)
        elif countUs == 1:
            countAppl = dbapplicants.checkApplByTgId(tg_id)
            countComp = dbcompanies.checkCompByTgId(tg_id)
            if countComp == 0:
                if countAppl == 0:
                    saluteText = 'Приветствуем снова!\nВы еще не зарегистрировались ни в качестве соискателя, ни в качестве работодателя. \
                    \n\nХотите сделать это сейчас?'
                    await message.reply(saluteText, reply_markup=first2_kb)
                elif countAppl > 0:
                    saluteText = 'Вы в главном меню.\nМожете войти как соискатель или работодатель'
                    await message.reply(saluteText, reply_markup=highMenu_kb)
            elif countComp == 1:
                saluteText = 'Вы в главном меню.\nМожете войти как соискатель или работодатель'
                await message.reply(saluteText, reply_markup=highMenu_kb)
    except:
        await message.reply('Возникла какая-то ошибка, попробуйте повторить команду /start')

# @dp.message_handler(commands=['добавить резюме'])
async def create_new_resum(message : types.Message):
    tg_id = message.from_user.id
    countUs = dbusers.checkUserByTgId(tg_id)
    if countUs == 0:
        dbusers.addNewNaked(message.from_user.id, message.from_user.username, message.from_user.first_name)
        saluteText = 'Добро пожаловать!\njobbot создан для удобного сотрудничества исполнителей с \
        заказчиками.\n\nВы можете разместить свое резюме, или добавить вакансию.'
        await message.reply(saluteText, reply_markup=first_kb)
    elif countUs == 1:
        countAppl = dbapplicants.checkApplByTgId(tg_id)
        countComp = dbcompanies.checkCompByTgId(tg_id)
        if countAppl > 0:
            makedResumeText = 'Рады, что Вы решили разместить свое резюме у нас 😉\n'\
            'Желаем удачи в поиске работы!\n\nРаботая с нами вы соглашаетесь с условиями оферты\\прикрепленный файл'
            await message.reply(makedResumeText, reply_markup=sendresumeaccept_kb)
        elif countAppl == 3:
            saluteText = 'У Вас уже есть 3 резюме.\nВы в главном меню соискателя меню соискателя'
            await message.reply(saluteText, reply_markup=mainApplicant_kb)

@dp.callback_query_handler(text='createResume')
async def createresume_command(callback : types.CallbackQuery):
    tg_id = callback.from_user.id
    countUs = dbusers.checkUserByTgId(tg_id)
    if countUs == 0:
        dbusers.addNewNaked(message.from_user.id, message.from_user.username, message.from_user.first_name)
        saluteText = 'Добро пожаловать!\njobbot создан для удобного сотрудничества исполнителей с \
        заказчиками.\n\nВы можете разместить свое резюме, или добавить вакансию.'
        await bot.send_message(saluteText, reply_markup=first_kb)
    elif countUs == 1:
        countAppl = dbapplicants.checkApplByTgId(tg_id)
        countComp = dbcompanies.checkCompByTgId(tg_id)
        if countAppl > 0:
            makedResumeText = 'Рады, что Вы решили разместить свое резюме у нас 😉\n'\
            'Желаем удачи в поиске работы!\n\nРаботая с нами вы соглашаетесь с условиями оферты\\прикрепленный файл'
            await bot.send_message(callback.from_user.id, makedResumeText, reply_markup=sendresumeaccept_kb)
            await callback.answer()
        elif countAppl == 3:
            saluteText = 'У Вас уже есть 3 резюме.\nВы в главном меню соискателя меню соискателя'
            await bot.send_message(callback.from_user.id, saluteText, reply_markup=mainApplicant_kb)

class FSMNewapplicant(StatesGroup):
    firstname = State()
    lastname = State()
    patronymic = State()
    lineBusiness = State()
    educationForm = State()
    addedEducationForm = State()
    careerObjective = State()
    desiredSalary = State()
    cityWork = State()
    distantWork = State()
    relocate = State()
    workExperience = State()
    desiredWorkSchedule = State()
    phone = State()
    email = State()

# Начало дилога загрузки при регистрации нового резюме соискателя
@dp.callback_query_handler(text='sendResumeAcc')
async def command_register(callback : types.Message):
    tg_id = callback.from_user.id
    countUs = dbusers.checkUserByTgId(tg_id)
    if countUs == 0:
        dbusers.addNewNaked(message.from_user.id, message.from_user.username, message.from_user.first_name)
        saluteText = 'Добро пожаловать!\njobbot создан для удобного сотрудничества исполнителей с \
        заказчиками.\n\nВы можете разместить свое резюме, или добавить вакансию.'
        await bot.send_message(saluteText, reply_markup=first_kb)
    elif countUs == 1:
        countAppl = dbapplicants.checkApplByTgId(tg_id)
        countComp = dbcompanies.checkCompByTgId(tg_id)
        if countAppl > 0:
            await FSMNewapplicant.firstname.set()
            await bot.send_message(callback.from_user.id, 'Введите Ваше реальное имя', reply_markup=cancel_kb)
            await callback.answer()
        elif countAppl == 3:
            saluteText = 'У Вас уже есть 3 резюме.\nВы в главном меню соискателя'
            await bot.send_message(callback.from_user.id, saluteText, reply_markup=mainApplicant_kb)

# Выход из состояний
# @dp.message_handler(state="*", commands="отмена")
# @dp.message_handler(Text(equals="отмена", ignore_case=True), state="*")
async def cancel_handler(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    # получаю имя главного стэйта, по нему будут работать отмены для всех состояний
    stName = current_state.split(':')[0]
    tg_id = message.from_user.id
    if current_state is None:
        return
    await state.finish()
    if stName == 'FSMNewapplicant':
        messTxt = 'Вы отменили отправку резюме, можете вернуться к этому шагу позже'
        await message.reply(messTxt, reply_markup=first2_kb)
    elif stName == 'FSMNewemployer':
        messTxt = 'Вы отменили добавление вакансии, можете добавить ее позже'
        await message.reply(messTxt, reply_markup=mainCompany_kb)
    elif stName == 'FSMNewonetimework':
        # countAppl = dbapplicants.checkApplByTgId(tg_id)
        # countComp = dbcompanies.checkCompByTgId(tg_id)
        # if countComp == 0:
        #     if countAppl == 0:
        #         makedResumeText = 'Вы еще не добавляли резюме и не публиковали вакансий'
        #         await message.reply(callback.from_user.id, makedResumeText, reply_markup=first_kb)
        #     elif countAppl > 0:
        #         saluteText = 'Вы отменили добавление разовой работы, можете вернуться к этому шагу позже'
        #         await message.reply(saluteText, reply_markup=mainApplicant_kb)
        # elif countComp == 1:
        #     messTxt = 'Вы отменили добавление разовой работы, можете вернуться к этому шагу позже'
        #     await message.reply(messTxt, reply_markup=mainCompany_kb)
        messTxt = 'Вы отменили добавление разовой работы, можете вернуться к этому шагу позже'
        await message.reply(messTxt, reply_markup=mainCompany_kb)
    elif stName == 'FSMAddedu':
        messTxt = 'Вы отменили добавление дополнительного образования, можете вернуться к этому шагу позже'
        await message.reply(messTxt, reply_markup=mainApplicant_kb)
    elif stName == 'FSMGotoeditappldata':
        messTxt = 'Вы отменили редактирование резюме, можете вернуться к этому шагу позже'
        await message.reply(messTxt, reply_markup=mainApplicant_kb)
    elif stName == 'FSMNewcompany':
        messTxt = 'Вы отменили регистрацию компании, можете вернуться к этому шагу позже'
        await message.reply(messTxt, reply_markup=first2_kb)
    elif stName == 'FSMNewpdffile':
        messTxt = 'Вы отменили отправку PDF-файла резюме'
        await message.reply(messTxt, reply_markup=mainApplicant_kb)
    elif stName == 'FSMNewonetimeforappl':
        messTxt = 'Вы отменили создание разовой работы\n\nВы вглавном меню соискателя'
        await message.reply(messTxt, reply_markup=mainApplicant_kb)
    elif stName == 'FSMGotoeditcompdata':
        messTxt = 'Вы отменили изменение данных о компании\n\nВы в меню работы с данными'
        await message.reply(messTxt, reply_markup=editCompData_kb)
    elif stName == 'FSMGotoeditempldata':
        messTxt = 'Вы отменили изменение данных о вакансии\n\nВы в меню работы с данными'
        await message.reply(messTxt, reply_markup=editCompData_kb)

# Ловим первый ответ и пишем в словарь
# @dp.message_handler(state=FSMNewapplicant.firstname)
async def get_firstname(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['tg_id'] = message.from_user.id
        if message.from_user.username == None:
            data['tg-login'] = 'None'
        else:
            data['tg-login'] = message.from_user.username
        data['firstname'] = message.text
    await FSMNewapplicant.next()
    await message.reply("Введите фамилию", reply_markup=cancel_kb)

# Ловим фамилию и пишем в словарь
# @dp.message_handler(state=FSMNewapplicant.lastname)
async def get_lastname(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['lastname'] = message.text
    await FSMNewapplicant.next()
    await message.reply("Введите отчество", reply_markup=cancel_kb)

# Ловим отчество и пишем в словарь
# @dp.message_handler(state=FSMNewapplicant.patronymic)
# async def get_patronymic(message: types.Message, state: FSMContext):
#     async with state.proxy() as data:
#         data['patronymic'] = message.text
#     await FSMNewapplicant.next()
#     lineBusinessInfo = dbcommon.getAllLineBusiness()
#     aboutLinesText = '''
#     Укажите направление вашей деятельности\n\nМожете выбрать подходящее из списка ниже, указав его цифру\n\n
#     Либо напишите свое
#     '''
#     linesText = ''
#     for item in lineBusinessInfo:
#         linesText = linesText + str(item['id']) + ' - ' + item['name'] + '\n'
#     await message.reply(aboutLinesText, reply_markup=cancel_kb)
#     await message.answer(linesText, reply_markup=cancel_kb)
async def get_patronymic(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['patronymic'] = message.text
    await FSMNewapplicant.next()
    lineBusinessInfo = dbcommon.getAllLineBusiness()
    aboutLinesText = '''
    Укажите направление курса, который Вы закончили. Мы будем предлагать вакансии, связанные с этим направлением
    \n\nВыбрерите подходящее из списка ниже, указав его цифру\n\n
    '''
    linesText = ''
    for item in lineBusinessInfo:
        linesText = linesText + str(item['id']) + ' - ' + item['name'] + '\n'
    await message.reply(aboutLinesText, reply_markup=cancel_kb)
    await message.answer(linesText, reply_markup=cancel_kb)

# Ловим направление деятельности и пишем в словарь
# @dp.message_handler(state=FSMNewapplicant.lineBusiness)
# async def get_linebusiness(message: types.Message, state: FSMContext):
#     async with state.proxy() as data:
#         lineBusinessInfo = dbcommon.getAllLineBusiness()
#         for item in lineBusinessInfo:
#             if (str(item['id']) == message.text):
#                 data['lineBusiness'] = item['name']
#                 data['lineBusinessId'] = int(item['id'])
#                 break
#             else:
#                 data['lineBusiness'] = message.text
#                 data['lineBusinessId'] = 0
#         # data['lineBusiness'] = message.text
#     await FSMNewapplicant.next()
#     await message.reply("Укажите форму обучения, которую Вы прошли по указанному направлению", reply_markup=cancel_kb)
async def get_linebusiness(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        lineBusinessInfo = dbcommon.getAllLineBusiness()
        listEmp = []
        for item in lineBusinessInfo:
            listEmp.append(item['id'])
        if int(message.text) in listEmp:
            oneLineBusinessInfo = dbcommon.getLineBusinessById(int(message.text))
            data['lineBusiness'] = oneLineBusinessInfo[0]['name']
            data['lineBusinessId'] = int(oneLineBusinessInfo[0]['id'])
            print(data)
            await FSMNewapplicant.next()
            await message.reply("Напишите программу обучения, которую Вы прошли по указанному направлению", reply_markup=cancel_kb)
        else:
            await message.reply("Некорректно указан номер направления деятельности", reply_markup=cancel_kb)
            # if (str(item['id']) == message.text):
            #     data['lineBusiness'] = item['name']
            #     data['lineBusinessId'] = int(item['id'])
            #     await FSMNewapplicant.next()
            #     await message.reply("Укажите форму обучения, которую Вы прошли по указанному направлению", reply_markup=cancel_kb)
            #     break
            # else:
            #     await message.reply("Некорректно указан номер направления деятельности", reply_markup=cancel_kb)
        # data['lineBusiness'] = message.text

# Ловим программу обучения и пишем в словарь
async def get_educationform(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['educationForm'] = message.text
    await FSMNewapplicant.next()
    newLinesText = '''
    Может Вы прошли дополнительную программу обучения?\n\nМожете указать ее здесь, либо пропустить шаг\n\n
    '''
    await message.reply(newLinesText, reply_markup=skip_step)

# Ловим дополнительную программу и пишем в словарь
# @dp.message_handler(state=FSMNewapplicant.educationForm)
async def get_addededucationform(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['addedEducationForm'] = message.text
        if message.text == 'Пропустить':
            data['addedEducationForm'] = 'empty'
        else:
            data['addedEducationForm'] = message.text
    await FSMNewapplicant.next()
    await message.reply("Напишите желаемую должность", reply_markup=cancel_kb)

# Ловим должность и пишем в словарь
# @dp.message_handler(state=FSMNewapplicant.careerObjective)
async def get_careerobjective(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['careerObjective'] = message.text
    await FSMNewapplicant.next()
    await message.reply("Напишите желаемую заработную плату (за месяц, за час, либо за проект)", reply_markup=cancel_kb)

# Ловим желаемую зарплату и пишем в словарь
# @dp.message_handler(state=FSMNewapplicant.desiredSalary)
async def get_desiredsalary(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['desiredSalary'] = message.text
    await FSMNewapplicant.next()
    await message.reply("Укажите город, из которого готовы работать", reply_markup=cancel_kb)

# Ловим город работы и пишем в словарь
# @dp.message_handler(state=FSMNewapplicant.cityWork)
async def get_citywork(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['cityWork'] = message.text
    await FSMNewapplicant.next()
    await message.reply("Готовы ли Вы работать удалённо?", reply_markup=cancelwithyes_kb)

# Ловим готовность или неготовность работать удалённо и пишем в словарь
# @dp.message_handler(state=FSMNewapplicant.distantWork)
async def get_distantwork(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['distantWork'] = message.text
    await FSMNewapplicant.next()
    await message.reply("Готовы ли Вы к переезду?", reply_markup=cancelwithyes_kb)

# Ловим готовность или неготовность к переезду и пишем в словарь
# @dp.message_handler(state=FSMNewapplicant.relocate)
async def get_relocate(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['relocate'] = message.text
    await FSMNewapplicant.next()
    await message.reply("Напишите Ваш опыт работы", reply_markup=cancel_kb)

# Ловим опыт работы и пишем в словарь
# @dp.message_handler(state=FSMNewapplicant.workExperience)
async def get_workexperience(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['workExperience'] = message.text
    await FSMNewapplicant.next()
    await message.reply("Укажите желаемый график работы\n\nНапример, 5/2", reply_markup=cancel_kb)

# Ловим график работы и пишем в словарь
# @dp.message_handler(state=FSMNewapplicant.desiredWorkSchedule)
async def get_desiredworkschedule(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['desiredWorkSchedule'] = message.text
    await FSMNewapplicant.next()
    await message.reply("Укажите ваш номер телефона (необязательно)\n\nЛибо пропустите шаг", reply_markup=skip_step)

# Ловим номер телефона и пишем в словарь
# @dp.message_handler(state=FSMNewapplicant.phone)
async def get_phone(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        if message.text == 'Пропустить':
            data['phone'] = 'empty'
        else:
            data['phone'] = message.text
    await FSMNewapplicant.next()
    await message.reply("Укажите ваш e-mail адрес (необязательно)\n\nЛибо пропустите шаг", reply_markup=skip_step)

# Ловим e-mail и пишем в словарь
# @dp.message_handler(state=FSMNewapplicant.email)
async def get_email(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        if message.text == 'Пропустить':
            data['email'] = 'empty'
        else:
            data['email'] = message.text
    applId = await dbusers.addNewApplicant(state)
    await state.finish()
    # сообщение с кнопкой для добавления pdf
    forSendPDFText = 'Загрузить pdf-файл для этого резюме'
    forSendPDFButton = InlineKeyboardMarkup(row_width=1)
    forSendPDFButton.add(InlineKeyboardButton(text='Загрузить pdf файл резюме', callback_data='sendPDF_' + str(applId)))
    successText = '''
    Ваше резюме успешно создано\n\nУ Вас есть резюме в виде PDF-файла?\n\nМожете его добавить.
    '''
    await bot.send_message(message.from_user.id, successText, reply_markup=beforeApplicant2_kb)
    await bot.send_message(message.from_user.id, forSendPDFText, reply_markup=forSendPDFButton)
    # await FSMNewapplicant.next()
    # await message.reply("Можете загрузить резюме в формате PDF (необязательно)\n\nЛибо пропустите шаг", reply_markup=skip_step)

# продолжение машинного состояния по ловле видеофайла, отправленного пользователем
# @dp.message_handler(content_types=['document'], state=FSMNewapplicant.pdfFile)
# async def load_pdffile(message: types.Message, state=FSMContext):
#     async with state.proxy() as data:
#         if message.text == 'Пропустить':
#             data['pdfFile'] = 'empty'
#         else:
#             data['pdfFile'] = message.document.file_id
#     print(data)
    # await dbusers.addNewApplicant(state)
    # await state.finish()
    # successText = '''
    # Ваше резюме успешно создано\n\nПосле проверки модератором оно станет доступно работодателям
    # '''
    # successText = '''
    # Ваше резюме успешно создано
    # '''
    # await bot.send_message(message.from_user.id, successText)

@dp.callback_query_handler(text='createCom')
async def createjob_command(callback : types.CallbackQuery):
    tg_id = callback.from_user.id
    countUs = dbusers.checkUserByTgId(tg_id)
    if countUs == 0:
        dbusers.addNewNaked(callback.from_user.id, callback.from_user.username, callback.from_user.first_name)
        saluteText = 'Добро пожаловать!\njobbot создан для удобного сотрудничества исполнителей с \
        заказчиками.\n\nВы можете разместить свое резюме, или добавить вакансию.'
        await bot.send_message(callback.from_user.id, saluteText, reply_markup=first_kb)
    elif countUs == 1:
        countComp = dbcompanies.checkCompByTgId(tg_id)
        if countComp == 0:
            makedJobText = 'Рады, что Вы решили разместить свою компанию\n'\
            'Желаем удачи в поиске сотрудника для Вашей работы!\n\nРаботая с нами вы соглашаетесь с условиями оферты\\прикрепленный файл'
            await bot.send_message(callback.from_user.id, makedJobText, reply_markup=sendcomaccept_kb)
            await callback.answer()
        elif countComp == 1:
            saluteText = 'Вы уже регистрировали компанию ранее, можете отредактировать её'
            await bot.send_message(callback.from_user.id, saluteText, reply_markup=mainCompany_kb)

class FSMNewcompany(StatesGroup):
    compname = State()
    lineBuiss = State()
    city = State()

# Начало дилога загрузки при регистрации новой компании
@dp.callback_query_handler(text='sendComAcc')
async def command_register(callback : types.Message):
    tg_id = callback.from_user.id
    countUs = dbusers.checkUserByTgId(tg_id)
    if countUs == 0:
        dbusers.addNewNaked(callback.from_user.id, callback.from_user.username, callback.from_user.first_name)
        saluteText = 'Добро пожаловать!\njobbot создан для удобного сотрудничества исполнителей с \
        заказчиками.\n\nВы можете разместить свое резюме, или добавить вакансию.'
        await bot.send_message(callback.from_user.id, saluteText, reply_markup=first_kb)
    elif countUs == 1:
        countComp = dbcompanies.checkCompByTgId(tg_id)
        if countComp == 0:
            await FSMNewcompany.compname.set()
            await bot.send_message(callback.from_user.id, 'Введите название Вашей компании', reply_markup=cancel_kb)
            await callback.answer()
        elif countComp == 1:
            saluteText = 'Вы уже регистрировали компанию ранее, можете отредактировать её'
            await bot.send_message(callback.from_user.id, saluteText, reply_markup=mainCompany_kb)

# Ловим первый ответ и пишем в словарь
# @dp.message_handler(state=FSMNewemployer.companyName)
async def get_compname(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['tg_id'] = message.from_user.id
        if message.from_user.username == None:
            data['tg-login'] = 'None'
        else:
            data['tg-login'] = message.from_user.username
        data['compname'] = message.text
    await FSMNewcompany.next()
    lineBizzes = dbcommon.getAllLineBusiness()
    aboutLinesText = '''
    Укажите направление вашей деятельности\n\nВыберите подходящее из списка ниже, указав его цифру\n\n
    Либо напишите свое
    '''
    linesText = ''
    for item in lineBizzes:
        linesText = linesText + str(item['id']) + ' - ' + item['name'] + '\n'
    await message.reply(aboutLinesText, reply_markup=cancel_kb)
    await message.answer(linesText, reply_markup=cancel_kb)

# Ловим направление деятельности и пишем в словарь
# @dp.message_handler(state=FSMNewcompany.lineBuiss)
async def get_linebuiss(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        lineBusinessInfo = dbcommon.getAllLineBusiness()
        listEmp = []
        for item in lineBusinessInfo:
            listEmp.append(item['id'])
        if int(message.text) in listEmp:
            oneLineBusinessInfo = dbcommon.getLineBusinessById(int(message.text))
            # print(oneLineBusinessInfo)
            data['lineBuissName'] = oneLineBusinessInfo[0]['name']
            data['lineBuissId'] = int(oneLineBusinessInfo[0]['id'])
            # print(data)
            await FSMNewcompany.next()
            successText = '''
            Укажите город дислокации Вашей компании
            '''
            await bot.send_message(message.from_user.id, successText, reply_markup=cancel_kb)
        else:
            await message.reply("Некорректно указан номер направления деятельности")

# Ловим направление деятельности и пишем в словарь
# @dp.message_handler(state=FSMNewcompany.lineBuiss)
async def get_city(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['city'] = message.text
        compId = await dbcompanies.addNewCompany(data)
        print(data)
        await state.finish()
        successText = '''
        Компания успешно зарегистрирована
        '''
        await bot.send_message(message.from_user.id, successText, reply_markup=mainCompany_kb)




@dp.callback_query_handler(text='createJob')
async def createjob_command(callback : types.CallbackQuery):
    makedJobText = 'Рады, что Вы решили разместить свою вакансию у нас 😉\n'\
    'Желаем удачи в поиске сотрудника для Вашей работы!\n\nРаботая с нами вы соглашаетесь с условиями оферты\\прикрепленный файл'
    await bot.send_message(callback.from_user.id, makedJobText, reply_markup=sendjobaccept_kb)
    await callback.answer()

# class FSMNewemployer(StatesGroup):
#     companyName = State()
#     lineBizz = State()
#     careerObjective2 = State()
#     desiredSalary2 = State()
#     cityWork2 = State()
#     employment = State()
#     duties = State()
#     requirements = State()
#     workingConditions = State()
#     fio = State()
#     phone2 = State()
#     email2 = State()
#
# # Начало дилога загрузки при регистрации новой вакансии соискателя
# @dp.callback_query_handler(text='sendJobAcc')
# async def command_register(callback : types.Message):
#     await FSMNewemployer.companyName.set()
#     await bot.send_message(callback.from_user.id, 'Введите название Вашей компании', reply_markup=cancel_kb)
#
# # Ловим первый ответ и пишем в словарь
# # @dp.message_handler(state=FSMNewemployer.companyName)
# async def get_companyname(message: types.Message, state: FSMContext):
#     async with state.proxy() as data:
#         data['tg_id'] = message.from_user.id
#         data['tg-login'] = message.from_user.username
#         data['companyName'] = message.text
#     await FSMNewemployer.next()
#     lineBusinessInfo2 = dbcommon.getAllLineBusiness()
#     aboutLinesText = '''
#     Укажите направление вашей деятельности\n\nМожете выбрать подходящее из списка ниже, указав его цифру\n\n
#     Либо напишите свое
#     '''
#     linesText = ''
#     for item in lineBusinessInfo2:
#         linesText = linesText + str(item['id']) + ' - ' + item['name'] + '\n'
#     await message.reply(aboutLinesText, reply_markup=cancel_kb)
#     await message.answer(linesText, reply_markup=cancel_kb)
#
# # Ловим направление деятельности и пишем в словарь
# # @dp.message_handler(state=FSMNewapplicant.lineBizz)
# async def get_linebizz(message: types.Message, state: FSMContext):
#     async with state.proxy() as data:
#         lineBizzInfo = dbcommon.getAllLineBusiness()
#         for item in lineBizzInfo:
#             if (item['id'] == message.text):
#                 data['lineBizz'] = item['name']
#                 data['lineBizzId'] = int(item['id'])
#                 break
#             else:
#                 data['lineBizz'] = message.text
#                 data['lineBizzId'] = 0
#         # data['lineBusiness'] = message.text
#     await FSMNewemployer.next()
#     await message.reply("Введите должность, на которую требуется сотрудник", reply_markup=cancel_kb)
#
# # Ловим должность и пишем в словарь
# # @dp.message_handler(state=FSMNewemployer.careerObjective2)
# async def get_careerobjective2(message: types.Message, state: FSMContext):
#     async with state.proxy() as data:
#         data['careerObjective2'] = message.text
#     await FSMNewemployer.next()
#     await message.reply("Укажите зарплату", reply_markup=cancel_kb)
#
# # Ловим зарплату и пишем в словарь
# # @dp.message_handler(state=FSMNewemployer.desiredSalary2)
# async def get_desiredsalary2(message: types.Message, state: FSMContext):
#     async with state.proxy() as data:
#         data['desiredSalary2'] = message.text
#     await FSMNewemployer.next()
#     await message.reply("Укажите город работы сотрудника (либо удаленный формат)", reply_markup=cancel_kb)
#
# # Ловим город работы (либо удаленка) и пишем в словарь
# # @dp.message_handler(state=FSMNewemployer.cityWork2)
# async def get_citywork2(message: types.Message, state: FSMContext):
#     async with state.proxy() as data:
#         data['cityWork2'] = message.text
#     await FSMNewemployer.next()
#     await message.reply("Укажите занятость для требуемого сотрудника (полная или частичная)", reply_markup=cancel_kb)
#
# # Пишем формат занятости в словарь
# # @dp.message_handler(state=FSMNewemployer.employment)
# async def get_employments(message: types.Message, state: FSMContext):
#     async with state.proxy() as data:
#         data['employment'] = message.text
#     await FSMNewemployer.next()
#     await message.reply("Распишите обязанности для данного сотрудника", reply_markup=cancel_kb)
#
# # Пишем обязанности в словарь
# # @dp.message_handler(state=FSMNewemployer.duties)
# async def get_duties(message: types.Message, state: FSMContext):
#     async with state.proxy() as data:
#         data['duties'] = message.text
#     await FSMNewemployer.next()
#     await message.reply("Укажите требования для соискателя на данную должность (наличие каких-либо документов и т.д.)", reply_markup=cancel_kb)
#
# # Пишем требования в словарь
# # @dp.message_handler(state=FSMNewemployer.requirements)
# async def get_requirement(message: types.Message, state: FSMContext):
#     async with state.proxy() as data:
#         data['requirements'] = message.text
#     await FSMNewemployer.next()
#     await message.reply("Укажите условия работы", reply_markup=cancel_kb)
#
# # Пишем условия работы в словарь
# # @dp.message_handler(state=FSMNewemployer.workingConditions)
# async def get_workingconditions(message: types.Message, state: FSMContext):
#     async with state.proxy() as data:
#         data['workingConditions'] = message.text
#     await FSMNewemployer.next()
#     await message.reply("Укажите ФИО контактного лица (необязательно)\n\nЛибо пропустите шаг", reply_markup=skip_step)
#
# # Пишем ФИО в словарь
# # @dp.message_handler(state=FSMNewemployer.fio)
# async def get_fio(message: types.Message, state: FSMContext):
#     async with state.proxy() as data:
#         if message.text == 'Пропустить':
#             data['fio'] = 'empty'
#         else:
#             data['fio'] = message.text
#     await FSMNewemployer.next()
#     await message.reply("Укажите телефон контактного лица для связи (необязательно)\n\nЛибо пропустите шаг", reply_markup=skip_step)
#
# # Пишем телефон контактного лица в словарь
# # @dp.message_handler(state=FSMNewemployer.phone2)
# async def get_phone2(message: types.Message, state: FSMContext):
#     async with state.proxy() as data:
#         if message.text == 'Пропустить':
#             data['phone2'] = 'empty'
#         else:
#             data['phone2'] = message.text
#     await FSMNewemployer.next()
#     await message.reply("Укажите email контактного лица (необязательно)\n\nЛибо пропустите шаг", reply_markup=skip_step)
#
# # Пишем email контактного лица в словарь, и закрываем машинное состояние
# # @dp.message_handler(state=FSMNewemployer.email2)
# async def get_email2(message: types.Message, state: FSMContext):
#     async with state.proxy() as data:
#         if message.text == 'Пропустить':
#             data['email2'] = 'empty'
#         else:
#             data['email2'] = message.text
#     await dbusers.addNewEmployer(state)
#     await state.finish()
#     successText = '''
#     Вакансия успешно создана и доступна соискателям
#     '''
#     await bot.send_message(message.from_user.id, successText)



def register_handlers_client(dp : Dispatcher):
    dp.register_message_handler(command_start, commands=['start', 'help'])
    dp.register_message_handler(go_to_high, Text(equals="вернуться в главное меню", ignore_case=True))
    dp.register_message_handler(cancel_handler, Text(equals="отмена", ignore_case=True), state="*")
    dp.register_message_handler(cancel_handler, state="*", commands="отмена")
    dp.register_message_handler(get_firstname, state=FSMNewapplicant.firstname)
    dp.register_message_handler(get_lastname, state=FSMNewapplicant.lastname)
    dp.register_message_handler(get_patronymic, state=FSMNewapplicant.patronymic)
    dp.register_message_handler(get_linebusiness, state=FSMNewapplicant.lineBusiness)
    dp.register_message_handler(get_educationform, state=FSMNewapplicant.educationForm)
    dp.register_message_handler(get_addededucationform, state=FSMNewapplicant.addedEducationForm)
    dp.register_message_handler(get_careerobjective, state=FSMNewapplicant.careerObjective)
    dp.register_message_handler(get_desiredsalary, state=FSMNewapplicant.desiredSalary)
    dp.register_message_handler(get_citywork, state=FSMNewapplicant.cityWork)
    dp.register_message_handler(get_distantwork, state=FSMNewapplicant.distantWork)
    dp.register_message_handler(get_relocate, state=FSMNewapplicant.relocate)
    dp.register_message_handler(get_workexperience, state=FSMNewapplicant.workExperience)
    dp.register_message_handler(get_desiredworkschedule, state=FSMNewapplicant.desiredWorkSchedule)
    dp.register_message_handler(get_phone, state=FSMNewapplicant.phone)
    dp.register_message_handler(get_email, state=FSMNewapplicant.email)
    # dp.register_message_handler(load_pdffile, content_types=['document'], state=FSMNewapplicant.pdfFile)
    # запись новой компании
    dp.register_message_handler(get_compname, state=FSMNewcompany.compname)
    dp.register_message_handler(get_linebuiss, state=FSMNewcompany.lineBuiss)
    dp.register_message_handler(get_city, state=FSMNewcompany.city)
    dp.register_message_handler(create_new_resum, Text(equals="добавить резюме", ignore_case=True))
    # запись новой вакансии в базу
    # dp.register_message_handler(get_companyname, state=FSMNewemployer.companyName)
    # dp.register_message_handler(get_linebizz, state=FSMNewemployer.lineBizz)
    # dp.register_message_handler(get_careerobjective2, state=FSMNewemployer.careerObjective2)
    # dp.register_message_handler(get_desiredsalary2, state=FSMNewemployer.desiredSalary2)
    # dp.register_message_handler(get_citywork2, state=FSMNewemployer.cityWork2)
    # dp.register_message_handler(get_employments, state=FSMNewemployer.employment)
    # dp.register_message_handler(get_duties, state=FSMNewemployer.duties)
    # dp.register_message_handler(get_requirement, state=FSMNewemployer.requirements)
    # dp.register_message_handler(get_workingconditions, state=FSMNewemployer.workingConditions)
    # dp.register_message_handler(get_fio, state=FSMNewemployer.fio)
    # dp.register_message_handler(get_phone2, state=FSMNewemployer.phone2)
    # dp.register_message_handler(get_email2, state=FSMNewemployer.email2)

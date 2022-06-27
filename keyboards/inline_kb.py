from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from db import dbcommon

# кнопка для первого выбора создать резюме, либо опубликовать вакансию
first_kb = InlineKeyboardMarkup(row_width=1)
becomeApplicant = InlineKeyboardButton(text='Создать резюме', callback_data='createResume')
becomeEmployer = InlineKeyboardButton(text='Создать вакансию', callback_data='createJob')
first_kb.add(becomeApplicant).add(becomeEmployer)

# кнопка для первого выбора создать резюме, либо зарегистрировать компанию
first2_kb = InlineKeyboardMarkup(row_width=1)
becomeApplicant2 = InlineKeyboardButton(text='Создать резюме', callback_data='createResume')
createCompany = InlineKeyboardButton(text='Зарегистрировать компанию', callback_data='createCom')
first2_kb.add(becomeApplicant2).add(createCompany)

# кнопка для первой регистрации компании если ее неготовность
# когда вошел как работодатель
firstComp_kb = InlineKeyboardMarkup(row_width=1)
createCompany = InlineKeyboardButton(text='Зарегистрировать компанию', callback_data='createCom')
firstComp_kb.add(createCompany)

# кнопка с согласием с условиями и на отправку резюме
sendresumeaccept_kb = InlineKeyboardMarkup(row_width=1)
sendResumeAccept = InlineKeyboardButton(text='Согласен', callback_data='sendResumeAcc')
sendresumeaccept_kb.add(sendResumeAccept)

# кнопка с согласием с условиями и на размещение вакансии
cancelnewedu_kb = InlineKeyboardMarkup(row_width=1)
cancEdu = InlineKeyboardButton(text='Отмена', callback_data='cancelNewEdu')
cancelnewedu_kb.add(cancEdu)

# кнопка с согласием с условиями и на размещение вакансии
sendjobaccept_kb = InlineKeyboardMarkup(row_width=1)
sendJobAccept = InlineKeyboardButton(text='Согласен', callback_data='sendJobAcc')
sendjobaccept_kb.add(sendJobAccept)

# кнопка с согласием с условиями и на регистрацию своей компании
sendcomaccept_kb = InlineKeyboardMarkup(row_width=1)
sendComAccept = InlineKeyboardButton(text='Согласен', callback_data='sendComAcc')
sendcomaccept_kb.add(sendComAccept)

# кнопка для подтверждения создания разовой работы соискателем
onetimeforappl_kb = InlineKeyboardMarkup(row_width=1)
oneTForAppl = InlineKeyboardButton(text='Создать', callback_data='oneTForAppl')
onetimeforappl_kb.add(oneTForAppl)

# кнопка откликнуться для канала
respond_kb = InlineKeyboardMarkup(row_width=1)
respForOneTime = InlineKeyboardButton(text='Откликнуться', callback_data='respForOneTimeWork')
respond_kb.add(respForOneTime)


# dbcommon.getAllLineBusiness()
def lineBusinessButtons ():
    buttons = InlineKeyboardMarkup(row_width=1)
    lineBusinessInfo = dbcommon.getAllLineBusiness()
    for item in lineBusinessInfo:
        buttons.add(InlineKeyboardButton(text=item['name'], callback_data='lineBiz_' + str(item['id'])))
    return buttons

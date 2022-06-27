from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

cancel = KeyboardButton('отмена')
cancel_kb = ReplyKeyboardMarkup(resize_keyboard=True)
cancel_kb.add(cancel)

# кнопка для пропуска шага в машине состояний
b2 = KeyboardButton('Пропустить')
skip_step = ReplyKeyboardMarkup(resize_keyboard=True)
skip_step.add(cancel).add(b2)

# клавиатура после создания резюме
addEdu = KeyboardButton('Добавить дополнительное образование')
b4 = KeyboardButton('Перейти в главное меню')
beforeApplicant_kb = ReplyKeyboardMarkup(resize_keyboard=True)
beforeApplicant_kb.add(addEdu).add(b4)

# новая клавиатура после создания резюме
# addPDF = KeyboardButton('Загрузить pdf файл резюме')
b4 = KeyboardButton('Перейти в главное меню')
beforeApplicant2_kb = ReplyKeyboardMarkup(resize_keyboard=True)
beforeApplicant2_kb.add(b4)

# клавиатура главного меню соискателя
searchEmpl = KeyboardButton('Найти вакансию')
createOneTimeWork = KeyboardButton('Создать разовую работу')
resumeWorking = KeyboardButton('Работа с резюме')
goToHighMenu = KeyboardButton('Вернуться в главное меню')
mainApplicant_kb = ReplyKeyboardMarkup(resize_keyboard=True)
mainApplicant_kb.add(searchEmpl).add(createOneTimeWork).add(resumeWorking).add(goToHighMenu)

# клавиатура возврата в главное меню соискателя
b3 = KeyboardButton('Вернуться в главное меню')
goToMain_kb = ReplyKeyboardMarkup(resize_keyboard=True)
goToMain_kb.add(b3)

cancel = KeyboardButton('отмена')
yeah = KeyboardButton('да')
noo = KeyboardButton('нет')
cancelwithyes_kb = ReplyKeyboardMarkup(resize_keyboard=True)
cancelwithyes_kb.row(yeah, noo).add(cancel)

# клавиатура главного меню компании
createJob = KeyboardButton('Создать вакансию')
editCompMenu = KeyboardButton('Работа с данными компании')
respWorkingMenu = KeyboardButton('Работа с откликами')
mainCompany_kb = ReplyKeyboardMarkup(resize_keyboard=True)
mainCompany_kb.add(createJob).add(createOneTimeWork).add(editCompMenu).add(respWorkingMenu).add(goToHighMenu)

#клавиатура работы со своими данными для компании (данные о компании, вакансии)
editCompInfo = KeyboardButton('Редактировать данные о компании')
editEmpls = KeyboardButton('Редактировать вакансии')
goToMainCompMenu = KeyboardButton('Вернуться в меню компании')
editCompData_kb = ReplyKeyboardMarkup(resize_keyboard=True)
editCompData_kb.add(editCompInfo).add(editEmpls).add(goToMainCompMenu)

#клавиатура работы с откликами для компании
lookResp = KeyboardButton('Посмотреть отклики')
goToMainCompMenu = KeyboardButton('Вернуться в меню компании')
respWorking_kb = ReplyKeyboardMarkup(resize_keyboard=True)
respWorking_kb.add(lookResp).add(goToMainCompMenu)

# клавиатура главного верхнего меню
goToApplMenu = KeyboardButton('Войти как соискатель')
goToCompMenu = KeyboardButton('Войти как работодатель')
highMenu_kb = ReplyKeyboardMarkup(resize_keyboard=True)
highMenu_kb.add(goToApplMenu).add(goToCompMenu)

# кнопка возврата в меню соискателя
goToApplMenu = KeyboardButton('Вернуться в меню соискателя')
goToApplicant_kb = ReplyKeyboardMarkup(resize_keyboard=True)
goToApplicant_kb.add(goToApplMenu)

# клавиатура работы с резюме
editRes = KeyboardButton('Редактировать резюме')
addNewResum = KeyboardButton('Добавить резюме')
resumeWorking_kb = ReplyKeyboardMarkup(resize_keyboard=True)
resumeWorking_kb.add(editRes).add(addNewResum).add(goToApplMenu)

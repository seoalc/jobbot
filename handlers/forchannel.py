from aiogram import types, Dispatcher
from bot_create import dp, bot
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardRemove
from aiogram.types import ReplyKeyboardRemove
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher.filters import Text

from db import dbusers, dbapplicants, dbcommon
from keyboards import goToApplicant_kb

# по нажатию инлайн кнопки с для отклика на вакансию в боте
@dp.callback_query_handler(Text(startswith='respForEmplInChannel_'))
async def resp_for_empl_in_channel(callback : types.CallbackQuery):
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
                compId = int(callback.data.split('_')[2])
                emplId = int(callback.data.split('_')[3])
                compTGId = int(callback.data.split('_')[1])
                if tg_id == compTGId:
                    saluteText = 'Нельзя откликнуться на свою работу'
                    await bot.send_message(callback.from_user.id, saluteText, reply_markup=mainApplicant_kb)
                else:
                    if countAppl == 1:
                        applId = dbapplicants.getIdAndNameAppl(tg_id)
                        applId = applId['id']
                        checkingResponse = dbcommon.checkResponsesForApplicant(applId, emplId)
                        if checkingResponse == 0:
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
                            await bot.send_message(compTGId, forCompTGText, parse_mode=types.ParseMode.HTML, reply_markup=lookResponAppl_kb)
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
                    elif countAppl > 1:
                        # по id вакансии вытаскиваю информацию об этой вакансии
                        oneEmplInfo = dbapplicants.getOneEmplInfo(emplId)
                        # формирую текст для текущего отправщика отклика (соискателя)
                        forApplText = '<b>Вы хотите откликнуться на вакансию:</b>\n\n'\
                                        '<b>Требуемая должность:</b>\n' + oneEmplInfo['career-objective'] + '\n'\
                                        '<b>Зарплата: </b>' + oneEmplInfo['desired-salary'] + '\n'\
                                        '<b>Должностные обязанности:</b>\n' + oneEmplInfo['duties'] + '\n\n'\
                                        '<b>у Вас больше одного резюме.</b> '\
                                        'Выберите из списка ниже от какого резюме хотите отправить отклик на эту вакансию\n\n'
                        await bot.send_message(callback.from_user.id, forApplText, parse_mode=types.ParseMode.HTML, reply_markup=goToApplicant_kb)
                        # по tg-id пользователя вытаскиваю все его резюме
                        allAppls = dbapplicants.getAllApplsForUserByTGID(tg_id)
                        # затем перебираю их в цикле и по ним достаю информацию по каждому резюме
                        for item in allAppls:
                            applInfo = dbapplicants.getApplInfoByApplId(item['id'])
                            # кнопка для отклика с конкретного резюме, когда их больше одного
                            respForEmplFromCh_kb = InlineKeyboardMarkup(row_width=1)
                            respForEmplFromChannel = InlineKeyboardButton(text='Откликнуться',
                                                                callback_data='respForEmplInBot_' + str(oneEmplInfo['company-id']) + '_' + \
                                                                str(oneEmplInfo['id']) + '_' + str(applInfo['id']))
                            respForEmplFromCh_kb.add(respForEmplFromChannel)
                            forApplText = '<b>Имя:</b>\n' + applInfo['firstname'] + ' ' + applInfo['lastname'] + ' ' + applInfo['patronymic'] + '\n'\
                                        '<b>Направление деятельности:</b>\n' + applInfo['line-business'] + '\n'\
                                        '<b>Форма обучения:</b>\n' + applInfo['career-objective'] + '\n'\
                                        '<b>Опыт работы:</b>\n' + applInfo['work-experience']
                            await bot.send_message(callback.from_user.id,
                                                forApplText, parse_mode=types.ParseMode.HTML, reply_markup=respForEmplFromCh_kb)
                await callback.answer()
            else:
                saluteText = 'Приветствуем снова!\nВы еще не добавляли резюме и не публиковали вакансий. \
                \n\nХотите сделать это сейчас?'
                await bot.send_message(callback.from_user.id, saluteText, reply_markup=first_kb)
                await callback.answer()
    except:
        await bot.send_message(callback.from_user.id, 'Возникла какая-то ошибка, попробуйте повторить команду /start')
        await callback.answer()



def register_handlers_client(dp : Dispatcher):
    dp.register_message_handler(resp_for_empl_in_channel, Text(startswith='respForEmplInChannel_'))

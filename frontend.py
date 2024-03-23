#####################################
#            Created by             #
#               zzsxd               #
#####################################
import telebot
from telebot import types


#####################################

class Bot_inline_btns:
    def __init__(self):
        super(Bot_inline_btns, self).__init__()
        self.__markup = types.InlineKeyboardMarkup(row_width=1)

    def start_btns(self):
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        poizon = types.KeyboardButton('Заказать с Poizon')
        cost = types.KeyboardButton('Рассчитать стоимость')
        discount = types.KeyboardButton('Скидки')
        taobao = types.KeyboardButton('Заказать с TaoBao/1688')
        support = types.KeyboardButton('Помощь')
        reviews = types.KeyboardButton('Отзывы')
        keyboard.add(poizon, cost, discount, taobao, support, reviews)
        return keyboard

    def cost_btns(self):
        boots = types.InlineKeyboardButton('Кроссовки', callback_data="boots")
        shoes = types.InlineKeyboardButton('Футболки/Кофты/Худи', callback_data="shoes")
        trousers = types.InlineKeyboardButton('Штаны', callback_data='trousers')
        accessory = types.InlineKeyboardButton('Аксессуары', callback_data='accessory')
        self.__markup.add(boots, shoes, trousers, accessory)
        return self.__markup

    def test_questone_btns(self):
        first = types.InlineKeyboardButton('1967г.', callback_data='not_true1')
        second = types.InlineKeyboardButton('1970г.', callback_data='not_true2')
        third = types.InlineKeyboardButton('1964г.', callback_data='true1')
        fourth = types.InlineKeyboardButton('1960г', callback_data='not_true3')
        self.__markup.add(first, second, third, fourth)
        return self.__markup
    def test_questsecond_btns(self):
        first = types.InlineKeyboardButton('Майк', callback_data='not_true4')
        second = types.InlineKeyboardButton('Адольф', callback_data='true2')
        third = types.InlineKeyboardButton('Джесси', callback_data='not_true5')
        fourth = types.InlineKeyboardButton('Адам', callback_data='not_true6')
        self.__markup.add(first, second, third, fourth)
        return self.__markup

    def test_questthird_btns(self):
        first = types.InlineKeyboardButton('Stan Smith', callback_data='true3')
        second = types.InlineKeyboardButton('Performance', callback_data='not_true7')
        third = types.InlineKeyboardButton('Originals', callback_data='not_true8')
        fourth = types.InlineKeyboardButton('YEEZY', callback_data='not_true9')
        self.__markup.add(first, second, third, fourth)
        return self.__markup

    def test_questfour_btns(self):
        first = types.InlineKeyboardButton('Оуэна Уилсона', callback_data='not_true10')
        second = types.InlineKeyboardButton('Билл Оуэнс', callback_data='not_true11')
        third = types.InlineKeyboardButton('Джек Смит', callback_data='not_true12')
        fourth = types.InlineKeyboardButton('Рик Оуэнс', callback_data='true4')
        self.__markup.add(first, second, third, fourth)
        return self.__markup

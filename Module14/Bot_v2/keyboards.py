from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Рассчитать'),
            KeyboardButton(text='Информация'),
            KeyboardButton(text='Купить')
        ]
    ], resize_keyboard=True
)

inline_keyboard = InlineKeyboardMarkup(
    row_width=1,
    inline_keyboard=[
        [InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='calories')],
        [InlineKeyboardButton(text='Формулы расчета', callback_data='formulas')]
    ]
)

products_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Vitamin A', callback_data='product_buying')],
        [InlineKeyboardButton(text='Vitamin C', callback_data='product_buying')],
        [InlineKeyboardButton(text='Vitamin D', callback_data='product_buying')],
        [InlineKeyboardButton(text='Vitamin E', callback_data='product_buying')]
    ]
)
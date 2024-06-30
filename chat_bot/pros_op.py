import os
from telegram.ext import Updater, CommandHandler, ApplicationBuilder, MessageHandler, filters
from generator_math import *
from generator_phys import *
import img_gen 
from telegram import ReplyKeyboardMarkup, KeyboardButton

# Создание бота
app = ApplicationBuilder().token("7327645399:AAFDw1wUz2FPQ4QBDXSJZHlPt2ICWKnjIls").build() 

async def start(update, context):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Добро пожаловать! Выберите задание на прохождение", reply_markup=get_main_menu())

# Функции для генерации вопросов
# Математика:
async def matrix_2(update, context):
    question = deter_gen_2()
    row_matrix = [[question["raw_data"][0],question["raw_data"][1]],[question["raw_data"][2],question["raw_data"][3]]]
    img_gen.gen_matrix_img(row_matrix,"temp")
    await context.bot.send_photo(chat_id=update.effective_chat.id, photo=open('temp.png', 'rb'))
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Найдите детерменант матрицы второго порядка")
    context.user_data["calc"] = question["calc"]

async def matrix_3(update, context):
    question = deter_gen_3()
    row_matrix = [[question["raw_data"][0],question["raw_data"][1],question["raw_data"][2]],[question["raw_data"][3],question["raw_data"][4],question["raw_data"][5]],[question["raw_data"][6],question["raw_data"][7],question["raw_data"][8]]]
    img_gen.gen_matrix_img(row_matrix,"temp")
    await context.bot.send_photo(chat_id=update.effective_chat.id, photo=open('temp.png', 'rb'))
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Найдите детерменант матрицы третьего порядка")
    context.user_data["calc"] = question["calc"]

async def div_urav(update, context):
    question = simple_div_equation_gen()
    simple_urav = question["raw_data"]
    img_gen.gen_simple_eq_img(simple_urav,"/","temp")
    await context.bot.send_photo(chat_id=update.effective_chat.id, photo=open('temp.png', 'rb'))
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Найдите X")
    context.user_data["calc"] = question["calc"]
    
async def mult_urav(update, context):
    question = simple_mult_equation_gen()
    simple_urav = question["raw_data"]
    img_gen.gen_simple_eq_img(simple_urav,"*","temp")
    await context.bot.send_photo(chat_id=update.effective_chat.id, photo=open('temp.png', 'rb'))
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Найдите X")
    context.user_data["calc"] = question["calc"]

async def sub_urav(update, context):
    question = simple_sub_equation_gen()
    simple_urav = question["raw_data"]
    img_gen.gen_simple_eq_img(simple_urav,"-","temp")
    await context.bot.send_photo(chat_id=update.effective_chat.id, photo=open('temp.png', 'rb'))
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Найдите X")
    context.user_data["calc"] = question["calc"]

async def sum_urav(update, context):
    question = simple_sum_equation_gen()
    simple_urav = question["raw_data"]
    img_gen.gen_simple_eq_img(simple_urav,"+","temp")
    await context.bot.send_photo(chat_id=update.effective_chat.id, photo=open('temp.png', 'rb'))
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Найдите X")
    context.user_data["calc"] = question["calc"]

async def triangle(update, context):
    question = triangle_S_gen()
    simple_urav = question["raw_data"]
    img_gen.gen_simple_eq_img(simple_urav,"+","temp")
    await context.bot.send_photo(chat_id=update.effective_chat.id, photo=open('temp.png', 'rb'))
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Найдите X")
    context.user_data["calc"] = question["calc"]

async def square_urav(update, context):
    question = square_equasion_gen()
    simple_urav = question["raw_data"]
    img_gen.gen_simple_eq_img(simple_urav,"+","temp")
    await context.bot.send_photo(chat_id=update.effective_chat.id, photo=open('temp.png', 'rb'))
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Найдите X")
    context.user_data["calc"] = question["calc"]

# Физика:
async def power_question(update, context):
    question = power()
    await context.bot.send_message(chat_id=update.effective_chat.id, text=question["text"])
    context.user_data["calc"] = question["ans"]

async def work_question(update, context):
    question = work()
    await context.bot.send_message(chat_id=update.effective_chat.id, text=question["text"])
    context.user_data["calc"] = question["ans"]

async def curr_strength_question(update, context):
    question = current_strength()
    await context.bot.send_message(chat_id=update.effective_chat.id, text=question["text"])
    context.user_data["calc"] = question["ans"]

async def resistance_question(update, context):
    question = resistance()
    await context.bot.send_message(chat_id=update.effective_chat.id, text=question["text"])
    context.user_data["calc"] = question["ans"]

async def voltage_question(update, context):
    question = voltage()
    await context.bot.send_message(chat_id=update.effective_chat.id, text=question["text"])
    context.user_data["calc"] = question["ans"]

async def charges_amount_question(update, context):
    question = charges_amount()
    await context.bot.send_message(chat_id=update.effective_chat.id, text=question["text"])
    context.user_data["calc"] = question["ans"]

async def resistance_2_question(update, context):
    question = resistance_2()
    await context.bot.send_message(chat_id=update.effective_chat.id, text=question["text"])
    context.user_data["calc"] = question["ans"]

async def curr_strength_2_question(update, context):
    question = current_strength_2()
    await context.bot.send_message(chat_id=update.effective_chat.id, text=question["text"])
    context.user_data["calc"] = question["ans"]

async def inductance_question(update, context):
    question = inductance()
    await context.bot.send_message(chat_id=update.effective_chat.id, text=question["text"])
    context.user_data["calc"] = question["ans"]

async def resistance_3_question(update, context):
    question = resistance_3()
    await context.bot.send_message(chat_id=update.effective_chat.id, text=question["text"])
    context.user_data["calc"] = question["ans"]

# Функция для обработки сообщений от пользователя
async def handle_message(update, context):
    print(handle_message)
    user_message = update.message.text
    
    # Проверяем, является ли сообщение ответом на предыдущий вопрос
    if context.user_data["calc"]:
        # Получаем правильный ответ из контекста
        correct_answer = context.user_data['calc']
        
        # Сравниваем ответ пользователя с правильным ответом
        if int(user_message) == correct_answer:
            await context.bot.send_message(chat_id=update.effective_chat.id, text="Правильно!")
        else:
            await context.bot.send_message(chat_id=update.effective_chat.id, text=f"Неправильно. Правильный ответ: {correct_answer}")
        
        # Очищаем контекст пользователя
        context.user_data.pop('calc')
    else:
        # Если сообщение не является ответом на вопрос, игнорируем его
        pass  

# Функция для инициализации меню
def get_main_menu():
    buttons = [
        [KeyboardButton('/matrix_2'), KeyboardButton('/matrix_3')],
        [KeyboardButton('/div_urav'), KeyboardButton('/mult_urav')],
        [KeyboardButton('/sub_urav'), KeyboardButton('/sum_urav')],
        [KeyboardButton('/square_urav'), KeyboardButton('/triangle')],
        [KeyboardButton('/power'), KeyboardButton('/work')],
        [KeyboardButton('/current_strength'), KeyboardButton('/resistance')],
        [KeyboardButton('/voltage'), KeyboardButton('/charges_amount')],
        [KeyboardButton('/resistance_2'), KeyboardButton('/current_strength_2')],
        [KeyboardButton('/inductance'), KeyboardButton('/resistance_3')]
    ]
    return ReplyKeyboardMarkup(buttons, resize_keyboard=True)

# Добавление команд по математике
app.add_handler(CommandHandler('matrix_2', matrix_2))
app.add_handler(CommandHandler('matrix_3', matrix_3))
app.add_handler(CommandHandler('div_urav', div_urav))
app.add_handler(CommandHandler('mult_urav', mult_urav))
app.add_handler(CommandHandler('sub_urav', sub_urav))
app.add_handler(CommandHandler('sum_urav', sum_urav))
app.add_handler(CommandHandler('square_urav', square_urav))
app.add_handler(CommandHandler('triangle', triangle))
# Добавление команд по физике
app.add_handler(CommandHandler('power', power_question))
app.add_handler(CommandHandler('work', work_question))
app.add_handler(CommandHandler('current_strength', curr_strength_question))
app.add_handler(CommandHandler('resistance', resistance_question))
app.add_handler(CommandHandler('voltage', voltage_question))
app.add_handler(CommandHandler('charges_amount', charges_amount_question))
app.add_handler(CommandHandler('resistance_2', resistance_2_question))
app.add_handler(CommandHandler('current_strength_2', curr_strength_2_question))
app.add_handler(CommandHandler('inductance', inductance_question))
app.add_handler(CommandHandler('resistance_3', resistance_3_question))
# Добавление считывания ответов
app.add_handler(MessageHandler(filters.ALL, handle_message)) 

app.run_polling()
import os
from telegram.ext import Updater, CommandHandler, ApplicationBuilder, MessageHandler, filters
from generator_math import *
import img_gen 
# Функция для генерации вопросов
async def matrix_2(update, context):
    # Используйте загруженную модель для генерации вопроса
    question = deter_gen_2()
    row_matrix = [[question["raw_data"][0],question["raw_data"][1]],[question["raw_data"][2],question["raw_data"][3]]]
    img_gen.gen_matrix_img(row_matrix,"temp")
    await context.bot.send_photo(chat_id=update.effective_chat.id, photo=open('temp.png', 'rb'))
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Найдите детерменант матрицы второго порядка")
    context.user_data["calc"] = question["calc"]
async def matrix_3(update, context):
    # Используйте загруженную модель для генерации вопроса
    question = deter_gen_3()
    row_matrix = [[question["raw_data"][0],question["raw_data"][1],question["raw_data"][2]],[question["raw_data"][3],question["raw_data"][4],question["raw_data"][5]],[question["raw_data"][6],question["raw_data"][7],question["raw_data"][8]]]
    img_gen.gen_matrix_img(row_matrix,"temp")
    await context.bot.send_photo(chat_id=update.effective_chat.id, photo=open('temp.png', 'rb'))
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Найдите детерменант матрицы третьего порядка")
    context.user_data["calc"] = question["calc"]

async def div_urav(update, context):
    # Используйте загруженную модель для генерации вопроса
    question = simple_div_equation_gen()
    simple_urav = question["raw_data"]
    img_gen.gen_simple_eq_img(simple_urav,"/","temp")
    await context.bot.send_photo(chat_id=update.effective_chat.id, photo=open('temp.png', 'rb'))
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Найдите X")
    context.user_data["calc"] = question["calc"]
    
async def mult_urav(update, context):
    # Используйте загруженную модель для генерации вопроса
    question = simple_mult_equation_gen()
    simple_urav = question["raw_data"]
    img_gen.gen_simple_eq_img(simple_urav,"*","temp")
    await context.bot.send_photo(chat_id=update.effective_chat.id, photo=open('temp.png', 'rb'))
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Найдите X")
    context.user_data["calc"] = question["calc"]

async def sub_urav(update, context):
    # Используйте загруженную модель для генерации вопроса
    question = simple_sub_equation_gen()
    simple_urav = question["raw_data"]
    img_gen.gen_simple_eq_img(simple_urav,"-","temp")
    await context.bot.send_photo(chat_id=update.effective_chat.id, photo=open('temp.png', 'rb'))
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Найдите X")
    context.user_data["calc"] = question["calc"]

async def sum_urav(update, context):
    # Используйте загруженную модель для генерации вопроса
    question = simple_sum_equation_gen()
    simple_urav = question["raw_data"]
    img_gen.gen_simple_eq_img(simple_urav,"+","temp")
    await context.bot.send_photo(chat_id=update.effective_chat.id, photo=open('temp.png', 'rb'))
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Найдите X")
    context.user_data["calc"] = question["calc"]


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
# Добавляем обработчик сообщений  


app = ApplicationBuilder().token("7327645399:AAFDw1wUz2FPQ4QBDXSJZHlPt2ICWKnjIls").build() 
# updater = Updater(Bot(token='7327645399:AAFDw1wUz2FPQ4QBDXSJZHlPt2ICWKnjIls'), Queue())
# dispatcher = Dispatcher
app.add_handler(CommandHandler('matrix_2', matrix_2))
app.add_handler(CommandHandler('matrix_3', matrix_3))
app.add_handler(CommandHandler('div_urav', div_urav))
app.add_handler(CommandHandler('mult_urav', mult_urav))
app.add_handler(CommandHandler('sub_urav', sub_urav))
app.add_handler(CommandHandler('sum_urav', sum_urav))
app.add_handler(MessageHandler(filters.ALL, handle_message)) 

app.run_polling()
from telegram.ext import CommandHandler, ApplicationBuilder, MessageHandler, filters
from generator_math import *
from generator_phys import *
from triganom_math import *
import img_gen 
from telegram import ReplyKeyboardMarkup, KeyboardButton

from tqdm.auto import tqdm
from haystack.nodes import QuestionGenerator, FARMReader
from haystack.document_stores import ElasticsearchDocumentStore
from haystack.pipelines import (
    QuestionGenerationPipeline,
    QuestionAnswerGenerationPipeline,
)

# Создание бота
app = ApplicationBuilder().token("7327645399:AAFDw1wUz2FPQ4QBDXSJZHlPt2ICWKnjIls").build() 

async def start(update, context):
    context.user_data["questions_took"] = 0
    context.user_data["correct_answers"] = 0
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Добро пожаловать! Выберите задание на прохождение", reply_markup=get_main_menu())

# Функции для генерации вопросов
# TODO: добавить чтение статистики пользователя (добавить поля "total questions" и "correct answers" в user_context)
### Английский:
def generate_QA(text):
  docs = [{"content": text}]
  document_store = ElasticsearchDocumentStore(
     host="localhost",
     port=9200)
  document_store.delete_documents()
  document_store.write_documents(docs)
  question_generator = QuestionGenerator()
  question_generation_pipeline = QuestionGenerationPipeline(question_generator)
  reader = FARMReader("deepset/roberta-base-squad2")
  qag_pipeline = QuestionAnswerGenerationPipeline(question_generator, reader)
  for idx, document in enumerate(tqdm(document_store)):

      print(f"\n * Generating questions and answers for document {idx}: {document.content[:100]}...\n")
      result = qag_pipeline.run(documents=[document])
      question_list = result["queries"]
      answer_list = list(map(lambda x: x[0].answer, result["answers"]))
      return  {
          "questions": result["queries"],
          "answers": list(map(lambda x: x[0].answer, result["answers"]))
          }

async def english_text(update, context):
    text = "Nikola Tesla (Serbian Cyrillic: Никола Тесла; 10 July 1856 – 7 January 1943) was a Serbian American inventor, electrical engineer, mechanical engineer, physicist, and futurist best known for his contributions to the design of the modern alternating current (AC) electricity supply system."
    question = generate_QA(text)

    id = random.randint(0,len(question["questions"])-1)

    await context.bot.send_message(chat_id=update.effective_chat.id, text=text)
    await context.bot.send_message(chat_id=update.effective_chat.id, text=question["questions"][id])
    context.user_data["calc"] = question["answers"][id]
    if context.user_data["questions_took"]:
        context.user_data["questions_took"] += 1
    else:
        context.user_data["questions_took"] = 1

### Математика:
# TODO: проверять на правильность введённых данных и обработку исключений
# Причина: после введения команды /matrix_2 и вслед за ней команды /start бот считал команду /start как ответ на вопрос
# и выдал ошибку, не проверив ответ до конца и не выставив оценку
async def matrix_2(update, context):
    question = deter_gen_2()
    row_matrix = [[question["raw_data"][0],question["raw_data"][1]],[question["raw_data"][2],question["raw_data"][3]]]
    img_gen.gen_matrix_img(row_matrix,"temp")
    await context.bot.send_photo(chat_id=update.effective_chat.id, photo=open('temp.png', 'rb'))
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Найдите детерменант матрицы второго порядка")
    context.user_data["calc"] = question["calc"]
    if context.user_data["questions_took"]:
        context.user_data["questions_took"] += 1
    else:
        context.user_data["questions_took"] = 1

async def matrix_3(update, context):
    question = deter_gen_3()
    row_matrix = [[question["raw_data"][0],question["raw_data"][1],question["raw_data"][2]],[question["raw_data"][3],question["raw_data"][4],question["raw_data"][5]],[question["raw_data"][6],question["raw_data"][7],question["raw_data"][8]]]
    img_gen.gen_matrix_img(row_matrix,"temp")
    await context.bot.send_photo(chat_id=update.effective_chat.id, photo=open('temp.png', 'rb'))
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Найдите детерменант матрицы третьего порядка")
    context.user_data["calc"] = question["calc"]
    if context.user_data["questions_took"]:
        context.user_data["questions_took"] += 1
    else:
        context.user_data["questions_took"] =1

async def div_urav(update, context):
    question = simple_div_equation_gen()
    simple_urav = question["raw_data"]
    img_gen.gen_simple_eq_img(simple_urav,"/","temp")
    await context.bot.send_photo(chat_id=update.effective_chat.id, photo=open('temp.png', 'rb'))
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Найдите X")
    context.user_data["calc"] = question["calc"]
    if context.user_data["questions_took"]:
        context.user_data["questions_took"] += 1
    else:
        context.user_data["questions_took"] =1
    
async def mult_urav(update, context):
    question = simple_mult_equation_gen()
    simple_urav = question["raw_data"]
    img_gen.gen_simple_eq_img(simple_urav,"*","temp")
    await context.bot.send_photo(chat_id=update.effective_chat.id, photo=open('temp.png', 'rb'))
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Найдите X")
    context.user_data["calc"] = question["calc"]
    if context.user_data["questions_took"]:
        context.user_data["questions_took"] += 1
    else:
        context.user_data["questions_took"] =1

async def sub_urav(update, context):
    question = simple_sub_equation_gen()
    simple_urav = question["raw_data"]
    img_gen.gen_simple_eq_img(simple_urav,"-","temp")
    await context.bot.send_photo(chat_id=update.effective_chat.id, photo=open('temp.png', 'rb'))
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Найдите X")
    context.user_data["calc"] = question["calc"]
    if context.user_data["questions_took"]:
        context.user_data["questions_took"] += 1
    else:
        context.user_data["questions_took"] =1

async def sum_urav(update, context):
    question = simple_sum_equation_gen()
    simple_urav = question["raw_data"]
    img_gen.gen_simple_eq_img(simple_urav,"+","temp")
    await context.bot.send_photo(chat_id=update.effective_chat.id, photo=open('temp.png', 'rb'))
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Найдите X")
    context.user_data["calc"] = question["calc"]
    if context.user_data["questions_took"]:
        context.user_data["questions_took"] += 1
    else:
        context.user_data["questions_took"] =1

async def triangle(update, context):
    question = triangle_S_gen()
    simple_urav = question["raw_data"]
    img_gen.gen_simple_eq_img(simple_urav,"+","temp")
    await context.bot.send_photo(chat_id=update.effective_chat.id, photo=open('temp.png', 'rb'))
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Найдите X")
    context.user_data["calc"] = question["calc"]
    if context.user_data["questions_took"]:
        context.user_data["questions_took"] += 1
    else:
        context.user_data["questions_took"] =1

async def square_urav(update, context):
    question = square_equasion_gen()
    simple_urav = question["raw_data"]
    img_gen.gen_simple_eq_img(simple_urav,"+","temp")
    await context.bot.send_photo(chat_id=update.effective_chat.id, photo=open('temp.png', 'rb'))
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Найдите X. Если решений нет, напишите \"Нет решений\"")
    if question["calc"] == []:
        context.user_data["calc"] = "Нет решений"
    else:
        context.user_data["calc"] = question["calc"]
    if context.user_data["questions_took"]:
        context.user_data["questions_took"] += 1
    else:
        context.user_data["questions_took"] =1

### Физика:
async def power_question(update, context):
    question = power()
    await context.bot.send_message(chat_id=update.effective_chat.id, text=question["text"])
    context.user_data["calc"] = question["ans"]
    if context.user_data["questions_took"]:
        context.user_data["questions_took"] += 1
    else:
        context.user_data["questions_took"] =1

async def work_question(update, context):
    question = work()
    await context.bot.send_message(chat_id=update.effective_chat.id, text=question["text"])
    context.user_data["calc"] = question["ans"]
    if context.user_data["questions_took"]:
        context.user_data["questions_took"] += 1
    else:
        context.user_data["questions_took"] =1

async def curr_strength_question(update, context):
    question = current_strength()
    await context.bot.send_message(chat_id=update.effective_chat.id, text=question["text"])
    context.user_data["calc"] = question["ans"]
    if context.user_data["questions_took"]:
        context.user_data["questions_took"] += 1
    else:
        context.user_data["questions_took"] =1

async def resistance_question(update, context):
    question = resistance()
    await context.bot.send_message(chat_id=update.effective_chat.id, text=question["text"])
    context.user_data["calc"] = question["ans"]
    if context.user_data["questions_took"]:
        context.user_data["questions_took"] += 1
    else:
        context.user_data["questions_took"] =1

async def voltage_question(update, context):
    question = voltage()
    await context.bot.send_message(chat_id=update.effective_chat.id, text=question["text"])
    context.user_data["calc"] = question["ans"]
    if context.user_data["questions_took"]:
        context.user_data["questions_took"] += 1
    else:
        context.user_data["questions_took"] =1

async def charges_amount_question(update, context):
    question = charges_amount()
    await context.bot.send_message(chat_id=update.effective_chat.id, text=question["text"])
    context.user_data["calc"] = question["ans"]
    if context.user_data["questions_took"]:
        context.user_data["questions_took"] += 1
    else:
        context.user_data["questions_took"] =1

async def resistance_2_question(update, context):
    question = resistance_2()
    await context.bot.send_message(chat_id=update.effective_chat.id, text=question["text"])
    context.user_data["calc"] = question["ans"]
    if context.user_data["questions_took"]:
        context.user_data["questions_took"] += 1
    else:
        context.user_data["questions_took"] =1

async def curr_strength_2_question(update, context):
    question = current_strength_2()
    await context.bot.send_message(chat_id=update.effective_chat.id, text=question["text"])
    context.user_data["calc"] = question["ans"]
    if context.user_data["questions_took"]:
        context.user_data["questions_took"] += 1
    else:
        context.user_data["questions_took"] =1

async def inductance_question(update, context):
    question = inductance()
    await context.bot.send_message(chat_id=update.effective_chat.id, text=question["text"])
    context.user_data["calc"] = question["ans"]
    if context.user_data["questions_took"]:
        context.user_data["questions_took"] += 1
    else:
        context.user_data["questions_took"] =1

async def resistance_3_question(update, context):
    question = resistance_3()
    await context.bot.send_message(chat_id=update.effective_chat.id, text=question["text"])
    context.user_data["calc"] = question["ans"]
    if context.user_data["questions_took"]:
        context.user_data["questions_took"] += 1
    else:
        context.user_data["questions_took"] =1


# Тригонометрия 
async def trig_equation_cos_question(update, context):
    question = trig_equation_cos_gen()
    simple_urav = question["raw_data"]
    img_gen.gen_trigonom_eq_img(simple_urav,"cos","temp")
    await context.bot.send_photo(chat_id=update.effective_chat.id, photo=open('temp.png', 'rb'))
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Найдите X. Если решений нет, напишите \"Нет решений\"")
    if question["solutions"] == []:
        context.user_data["calc"] = "Нет решений"
    else:
        context.user_data["calc"] = question["solutions"]
    if context.user_data["questions_took"]:
        context.user_data["questions_took"] += 1
    else:
        context.user_data["questions_took"] = 1

async def trig_equation_sin_question(update, context):
    question = trig_equation_sin_gen()
    simple_urav = question["raw_data"]
    img_gen.gen_trigonom_eq_img(simple_urav,"sin","temp")
    await context.bot.send_photo(chat_id=update.effective_chat.id, photo=open('temp.png', 'rb'))
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Найдите X. Если решений нет, напишите \"Нет решений\"")
    if question["solutions"] == []:
        context.user_data["calc"] = "Нет решений"
    else:
        context.user_data["calc"] = question["solutions"]
    if context.user_data["questions_took"]:
        context.user_data["questions_took"] += 1
    else:
        context.user_data["questions_took"] = 1

async def trig_equation_tan_question(update, context):
    question = trig_equation_tan_gen()
    simple_urav = question["raw_data"]
    img_gen.gen_trigonom_eq_img(simple_urav,"tg","temp")
    await context.bot.send_photo(chat_id=update.effective_chat.id, photo=open('temp.png', 'rb'))
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Найдите X. Если решений нет, напишите \"Нет решений\"")
    if question["solutions"] == []:
        context.user_data["calc"] = "Нет решений"
    else:
        context.user_data["calc"] = question["solutions"]
    if context.user_data["questions_took"]:
        context.user_data["questions_took"] += 1
    else:
        context.user_data["questions_took"] = 1

async def trig_equation_cot_question(update, context):
    question = trig_equation_cot_gen()
    simple_urav = question["raw_data"]
    img_gen.gen_trigonom_eq_img(simple_urav,"ctg","temp")
    await context.bot.send_photo(chat_id=update.effective_chat.id, photo=open('temp.png', 'rb'))
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Найдите X. Если решений нет, напишите \"Нет решений\"")
    if question["solutions"] == []:
        context.user_data["calc"] = "Нет решений"
    else:
        context.user_data["calc"] = question["solutions"]
    if context.user_data["questions_took"]:
        context.user_data["questions_took"] += 1
    else:
        context.user_data["questions_took"] = 1

async def log_equation_question(update, context):
    question = log_equation_gen()
    simple_urav = question["raw_data"]
    img_gen.gen_log_eq_img(simple_urav,"temp")
    await context.bot.send_photo(chat_id=update.effective_chat.id, photo=open('temp.png', 'rb'))
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Найдите X. Если решений нет, напишите \"Нет решений\"")
    if question["solutions"] == []:
        context.user_data["calc"] = "Нет решений"
    else:
        context.user_data["calc"] = question["solutions"]
    if context.user_data["questions_took"]:
        context.user_data["questions_took"] += 1
    else:
        context.user_data["questions_took"] = 1

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
            if context.user_data["correct_answers"]:
                context.user_data["correct_answers"] += 1
            else:
                context.user_data["correct_answers"] = 1
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
        [KeyboardButton('/inductance'), KeyboardButton('/resistance_3')],
        [KeyboardButton('/sin_urav'), KeyboardButton('/cos_urav')],
        [KeyboardButton('/tg_urav'), KeyboardButton('/ctg_urav')],
        [KeyboardButton('/log_urav'), KeyboardButton('/english_text')],
        
    ]
    return ReplyKeyboardMarkup(buttons, resize_keyboard=True)

# Добавление команды для старта и получения клавиатуры
app.add_handler(CommandHandler('start', start))

# Добавление команд по английскому языку
app.add_handler(CommandHandler('english_text', english_text))

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

# Добавление команд по тригонометрии
app.add_handler(CommandHandler('sin_urav', trig_equation_sin_question))
app.add_handler(CommandHandler('cos_urav', trig_equation_cos_question))
app.add_handler(CommandHandler('tg_urav', trig_equation_tan_question))
app.add_handler(CommandHandler('ctg_urav', trig_equation_cot_question))
app.add_handler(CommandHandler('log_urav', log_equation_question))

# Добавление считывания ответов
app.add_handler(MessageHandler(filters.ALL, handle_message))


app.run_polling()
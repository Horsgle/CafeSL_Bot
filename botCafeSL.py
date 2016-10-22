import logging
import telegram
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Mensagem de start com botões de opção.
def start(bot, update):
    keyboard =  [
                [InlineKeyboardButton("Programação", callback_data="prog")],
                [InlineKeyboardButton("Lista de palestrantes", callback_data="palestrantes")]
                ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    update.message.reply_text('Ações que podem lhe ajudar:', reply_markup=reply_markup)

# Error
def error(bot, update, error):
    logging.warning('Update "%s" caused error "%s"' % (update, error))

# Metodos das ações resposta do retorno da listaPalestrantes()
def douglas(bot, update):
    query = update.callback_query
    bot.sendPhoto(query.message.chat_id, "https://blusol.org/csl2016/wp-content/uploads/2016/09/douglas-150x150.jpg", "Douglas Gelsleichter")
    bot.editMessageText(text="Aplicações Híbridas utilizando Ionic\nIonic é um framework open source para criar apps híbridos para Android e IOS utizando HTML5, CSS, AngularJS e Javascript. Sou  formado em Sistemas da Informação na Fameblu , desenvolvedor front-end a 5 anos nos ultimos dois anos desenvolvendo aplicativos híbridos utilizando Ionic e AngularJS.",
                        chat_id=query.message.chat_id,
                        message_id=query.message.message_id)

def elton(bot, update):
    query = update.callback_query
    bot.sendPhoto(query.message.chat_id, "https://blusol.org/csl2016/wp-content/uploads/2016/07/elton-minetto-150x150.jpg", "Elton Minetto")
    bot.editMessageText(text="Do monolito ao micro serviço\nNesta palestra vamos ver a evolução das arquiteturas de sistemas e como criar aplicativos modernos e escaláveis usando containers e os 12 Fatores.",
                        chat_id=query.message.chat_id,
                        message_id=query.message.message_id)

def andre(bot, update):
    query = update.callback_query
    bot.sendPhoto(query.message.chat_id, "https://blusol.org/csl2016/wp-content/uploads/2016/09/andre-rafael-1-150x75.png", "André Luís Otto | Rafael Scolari Maciel")
    bot.editMessageText(text="Flyway DB Version - Faça seu banco voar\nO Flyway é desenvolvido com Java e tem uma integração perfeita com sistemas construídos nessa linguagem. Inclusive usá-lo através do ANT ou Maven, claro, também tem uma API Java. Além disso, pode ser usado via linha de comando (Linux/Windows). Ele gerencia a evolução do banco de dados por meio de arquivos de versões (migrates) que contém scripts SQL.",
                        chat_id=query.message.chat_id,
                        message_id=query.message.message_id)

def eduardo(bot, update):
    query = update.callback_query
    bot.sendPhoto(query.message.chat_id, "https://blusol.org/csl2016/wp-content/uploads/2016/09/eduardo-hernacki-150x150.jpg", "Eduardo Hernacki")
    bot.editMessageText(text="Gestão de Logs\nNesta palestra vamos enfrentar o dilema da gestão de logs, aprender a importância de gerenciá-los corretamente e explorar o seu potencial de valor para a TI e para o Negócio - utilizando ferramentas abertas, é claro!",
                        chat_id=query.message.chat_id,
                        message_id=query.message.message_id)

def alan(bot, update):
    query = update.callback_query
    bot.sendPhoto(query.message.chat_id, "https://blusol.org/csl2016/wp-content/uploads/2016/07/alan-150x150.jpg", "Alan Crisley Besen")
    bot.editMessageText(text="oVirt/KVM - Xiii, isto não vai funcionar\nIrei dar uma breve introdução à virtualização e apresentar brevemente o oVirt/KVM e todo o projeto em si. Apresentar os desafios de capacitação e busca de profissionais. E, a importância de compartilhar o conhecimento adquirido e a experiência.",
                        chat_id=query.message.chat_id,
                        message_id=query.message.message_id)

def marcio(bot, update):
    query = update.callback_query
    bot.sendPhoto(query.message.chat_id, "https://blusol.org/csl2016/wp-content/uploads/2016/08/marcio-300x255-150x150.jpg", "Marcio Junior Vieira")
    bot.editMessageText(text="Pentaho Business Intelligence e Business Analytics Open Source\nO Pentaho Open Source Business Intelligence (BI) é uma plataforma de código aberto, que permite buscar, tratar, analisar, monitorar, transformar e apresentar informações com independência e flexibilidade, para projetos de BI ou BigData.",
                        chat_id=query.message.chat_id,
                        message_id=query.message.message_id)

def henrique(bot, update):
    query = update.callback_query
    bot.sendPhoto(query.message.chat_id, "https://blusol.org/csl2016/wp-content/uploads/2016/09/HenriqueBastos-150x150.jpeg", "Henrique Bastos")
    bot.editMessageText(text="Quanto dinheiro você está perdendo por não fazer Software Livre?\nOs desperdícios no setor tecnológico são gigantescos. Com o mundo cada vez mais conectado, com novas oportunidades surgindo a todo tempo, ficar preso nas armadilhas tradicionais da propriedade do software pode inviabilizar sua vida. Nessa apresentação, vamos conversar sobre como Software Livre é uma grande alavanca para te abrir portas inesperadas e te ajudar a esculpir a sua carreira para você viver a vida do seu jeito.",
                        chat_id=query.message.chat_id,
                        message_id=query.message.message_id)
# Fim dos metodos dos palestrantes


# Controle de Callback dos botões selecionados
def callbackPalestrantes(bot, update):
    query = update.callback_query
    if query.data == "palestrantes":
        sendlistPalestrantes(bot, update)
    elif query.data == "prog":
        sendprog(bot, update)
    elif query.data == "douglas":
        douglas(bot, update)
    elif query.data == "elton":
        elton(bot, update)
    elif query.data == "andre":
        andre(bot, update)
    elif query.data == "eduardo":
        eduardo(bot, update)
    elif query.data == "alan":
        alan(bot, update)
    elif query.data == "marcio":
        marcio(bot, update)
    elif query.data == "henrique":
        henrique(bot, update)
        
# Envia os locais de almoço 
def locaisAlmocar(bot, update):
    latitude = -26.8811842
    longitude = -49.2448961
    bot.sendLocation(update.message.chat_id, latitude, longitude)
    bot.sendMessage(update.message.chat_id, "Churrascaria Ataliba")

    latitude = -26.8838362
    longitude = -49.2459579
    bot.sendLocation(update.message.chat_id, latitude, longitude)
    bot.sendMessage(update.message.chat_id, "Supermercado Cooper – Filial Nações")

def sendlistPalestrantes(bot, update):
    query = update.callback_query
    keyboard =  [
                [InlineKeyboardButton("Douglas Gelsleichter", callback_data='douglas')],
                [InlineKeyboardButton("Elton Minetto", callback_data='elton')],
                [InlineKeyboardButton("André Luís Otto | Rafael Scolari Maciel", callback_data='andre')],
                [InlineKeyboardButton("Eduardo Hernacki", callback_data='eduardo')],
                [InlineKeyboardButton("Alan Crisley Besen", callback_data='alan')],
                [InlineKeyboardButton("Marcio Junior Vieira", callback_data='marcio')],
                [InlineKeyboardButton("Henrique Bastos", callback_data='henrique')]
                ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    bot.sendMessage(query.message.chat_id, 'Lista de palestrantes', reply_markup=reply_markup)

# Lista de palestrantes, cada palestrante é um botão
def listPalestrantes(bot, update):
    keyboard =  [
                [InlineKeyboardButton("Douglas Gelsleichter", callback_data='douglas')],
                [InlineKeyboardButton("Elton Minetto", callback_data='elton')],
                [InlineKeyboardButton("André Luís Otto | Rafael Scolari Maciel", callback_data='andre')],
                [InlineKeyboardButton("Eduardo Hernacki", callback_data='eduardo')],
                [InlineKeyboardButton("Alan Crisley Besen", callback_data='alan')],
                [InlineKeyboardButton("Marcio Junior Vieira", callback_data='marcio')],
                [InlineKeyboardButton("Henrique Bastos", callback_data='henrique')]
                ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    update.message.reply_text('Lista de palestrantes', reply_markup=reply_markup)

# Este metodo vai somente enviar um texto como mensagem.
def prog(bot, update):
    update.message.reply_text('*08:00 – 09:00* `Check in & Café de Boas Vindas`\n'
                              +'*09:00 – 09:15* `Keynote`\n'
                              +'*09:15 – 10:15* `Aplicações Híbridas utilizando Ionic com Douglas Gelsleichter`\n'
                              +'*10:15 – 11:15* `oVirt/KVM – Xiii, isto não vai funcionar com Alan Crisley Besen`\n'
                              +'*11:15 – 12:15* `Do monolito ao micro serviço com Elton Minetto`\n'
                              +'*12:15 – 13:30* `Almoço`\n'
                              +'*13:30 – 14:30* `Flyway DB Version – Faça seu banco voar com André Luís Otto | Rafael Scolari Maciel`\n'
                              +'*14:30 – 15:30* `Gestão de Logs com Eduardo Hernacki`\n'
                              +'*15:30 – 16:00* `Coffee Break`\n'
                              +'*16:00 – 17:00* `Pentaho Business Intelligence e Business Analytics Open Source com Marcio Junior Vieira`\n'
                              +'*17:00 – 18:00* `Quanto dinheiro você está perdendo por não fazer Software Livre? com Henrique Bastos`',
                              parse_mode=telegram.ParseMode.MARKDOWN)

# Este metodo vai substituir a mensagem enviada pelo bot anteriormente, com base no Callback
def sendprog(bot, update):
    query = update.callback_query
    bot.editMessageText('*08:00 – 09:00* `Check in & Café de Boas Vindas`\n'
                         +'*09:00 – 09:15* `Keynote`\n'
                         +'*09:15 – 10:15* `Aplicações Híbridas utilizando Ionic com Douglas Gelsleichter`\n'
                         +'*10:15 – 11:15* `oVirt/KVM – Xiii, isto não vai funcionar com Alan Crisley Besen`\n'
                         +'*11:15 – 12:15* `Do monolito ao micro serviço com Elton Minetto`\n'
                         +'*12:15 – 13:30* `Almoço`\n'
                         +'*13:30 – 14:30* `Flyway DB Version – Faça seu banco voar com André Luís Otto | Rafael Scolari Maciel`\n'
                         +'*14:30 – 15:30* `Gestão de Logs com Eduardo Hernacki`\n'
                         +'*15:30 – 16:00* `Coffee Break`\n'
                         +'*16:00 – 17:00* `Pentaho Business Intelligence e Business Analytics Open Source com Marcio Junior Vieira`\n'
                         +'*17:00 – 18:00* `Quanto dinheiro você está perdendo por não fazer Software Livre? com Henrique Bastos`',
                         parse_mode=telegram.ParseMode.MARKDOWN,
                         chat_id=query.message.chat_id,
                         message_id=query.message.message_id)

# Envia o link do site da Oktoberfest e a localização
def oktoberfest(bot, update):
    query = update.callback_query
    bot.sendMessage(update.message.chat_id, 'http://www.oktoberfestblumenau.com.br/festa-2016/programacao/#setor1-data-22')
    latitude = -26.9176092
    longitude = -49.0845429
    bot.sendLocation(update.message.chat_id, latitude, longitude)

# Create the Updater and pass it your bot's token.
updater = Updater("180628982:AAFd0anxqRO4rFtGzreU-8yChdB1jWqTaZo")

updater.dispatcher.add_handler(CommandHandler('programacao', prog))
updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('palestrantes', listPalestrantes))
updater.dispatcher.add_handler(CommandHandler('almocar', locaisAlmocar))
updater.dispatcher.add_handler(CommandHandler('oktoberfest', oktoberfest))
updater.dispatcher.add_handler(CallbackQueryHandler(callbackPalestrantes))
updater.dispatcher.add_error_handler(error)

# Start Bot
updater.start_polling()
updater.idle()

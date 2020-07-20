#!/urs/bin/env python3

import os
import time
import random
import pickle
import matplotlib.pyplot as plt
from antlr4 import *
from skyline import Skyline
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import sys

sys.path.append('./cl/')
from EvalVisitor import EvalVisitor
from SkylineLexer import SkylineLexer
from SkylineParser import SkylineParser

data = {}
debug = False
start_time = 0


def start(update, context):
    """ Dona la benvinguda a l'usuari """
    first_name = update.effective_chat.first_name
    txt = "SkyLineBot! \nBenvingut %s!" % first_name
    context.bot.send_message(chat_id=update.effective_chat.id, text=txt)


def author(update, context):
    """ Mostra la informació de l'autor """
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="SkyLineBot! \n" +
             "@ Nahum Manuel Martín Vegas, 2020\n" +
             "nahum.manuel.martin@est.fib.upc.edu")


def helpInfo(update, context):
    """ Mostra les comandes del bot """
    startInfo = "   /start   Inicia l'aplicació i saluda."
    authorInfo = "   /author   Indica la informació de l'autor."
    helpinfo = "   /help   Mostra aquesta informació d'ajuda."
    lstInfo = "   /lst   Mostra la llista de d'identificadors i la seva àrea en unitats quadrades."
    cleanInfo = "   /clean   Esborra tots els identificadors."
    saveInfo = "   /save id   Guarda els identificadors a un fitxer."
    loadInfo = "   /load id   Carrega els identificadors de un fitxer."
    txt = ("Comandes implementades:\n" +
           startInfo + "\n" +
           authorInfo + "\n" +
           helpinfo + "\n" +
           lstInfo + "\n" +
           cleanInfo + "\n" +
           saveInfo + "\n" +
           loadInfo)
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=txt)


def __printSkyline(update, context, s):
    """ Imprimeix un Skyline (s) i les seves dades """
    try:
        x, y = [], []
        hLine = s.getHLine()
        for i in hLine:
            x.append(i[0])
            y.append(i[1])
        plt.bar(x, y,
                width=1,
                align='edge',
                linewidth=1,
                facecolor='r',
                orientation='vertical')
        fitxer = "%d.png" % random.randint(1000000, 9999999)
        plt.savefig(fitxer, bbox_inches='tight')
        # plt.savefig(fitxer)
        context.bot.send_photo(chat_id=update.effective_chat.id,
                               photo=open(fitxer, 'rb'))
        os.remove(fitxer)
        txt = "area: %s\nalçada: %s" % (s.getArea(), s.getH())
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=txt)
        plt.close()
        if debug:
            global start_time
            print("--- %s seconds ---" % (time.time() - start_time))
    except Exception as e:
        print(e)
        context.bot.send_message(chat_id=update.effective_chat.id, text='💣')


def calc(update, context):
    """ Realitza la crida al interpret de llenguatge, demana el seu càlcul,
     i crida a la impressió del resultat. """
    opTxt = str(update.message.text)
    if debug:
        print(opTxt)
        global start_time
        start_time = time.time()
    try:
        result = calcInput(update, opTxt)
        if type(result) is Skyline:
            __printSkyline(update, context, result)
        elif type(result) is tuple:
            memVar(update, result)
            key, value = result
            if debug:
                print('Key: ', key)
                print('Value: ', value)
            if type(value) is Skyline:
                __printSkyline(update, context, value)
            else:
                txt = ('%s := %s' % (key, value))
                context.bot.send_message(
                    chat_id=update.effective_chat.id,
                    text=txt)
        else:
            txt = str(result)
            print(txt)
            context.bot.send_message(
                chat_id=update.effective_chat.id,
                text=txt)
    except Exception as e:
        print(e)
        context.bot.send_message(chat_id=update.effective_chat.id, text='💣')


def calcInput(update, inp):
    """ Mitjançant la entrada String (inp) crida a l'interpret de llenguatge
     per resoldre el càlcul """
    if debug:
        print('calcInput: ', inp)
    first_name = update.effective_chat.first_name
    last_name = update.effective_chat.last_name
    if not (first_name + " " + last_name) in data:
        data[first_name + " " + last_name] = {}

    input_stream = InputStream(inp)
    lexer = SkylineLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = SkylineParser(token_stream)
    tree = parser.root()
    if debug:
        print('EvalVisitor para ', first_name + " " + last_name)
    visitor = EvalVisitor(data[first_name + " " + last_name])
    result = visitor.visit(tree)
    if debug:
        print('Result: ', result)
    return result


def memVar(update, sl):
    """ Realitza el guardat de la dada en memoria (data)"""
    first_name = update.effective_chat.first_name
    last_name = update.effective_chat.last_name
    if not (first_name + " " + last_name) in data:
        data[first_name + " " + last_name] = {}
    key, value = sl
    data[first_name + " " + last_name][key] = value


def lst(update, context):
    """ Llista les variables guardades en memoria """
    first_name = update.effective_chat.first_name
    last_name = update.effective_chat.last_name
    if debug:
        print('Len(data[usr])', len(data[first_name + " " + last_name]))
    if len(data[first_name + " " + last_name]) > 0:
        txt = ""
    else:
        txt = "No hi han variables en memoria"
    for i in data[first_name + " " + last_name]:
        txt += ("%s: %s u²\n" % (i, data[first_name + " " + last_name][i].getArea()))
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=txt)


def clean(update, context):
    """ Esborra les dades de memoria """
    first_name = update.effective_chat.first_name
    last_name = update.effective_chat.last_name
    data[first_name + " " + last_name] = {}
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="S'han esborrat els Skylines de " + first_name + " " + last_name + ".")


def save(update, context):
    """ Guarda una variable de memoria a un fitxer amb el su ID i extensió .sky """
    first_name = update.effective_chat.first_name
    last_name = update.effective_chat.last_name
    txt = ""
    for i in context.args:
        if (first_name + " " + last_name) in data and \
                i in data[first_name + " " + last_name]:
            filename = i + ".sky"
            fexist = False
            if os.path.exists(filename):
                fexist = True
            file = open(filename, 'wb')
            dataID = data[first_name + " " + last_name][i]
            pickle.dump(dataID, file)
            file.close()
            if fexist:
                txt = "L'axiu " + filename + " s'ha sobreescrit correctament"
            else:
                txt = "L'arxiu " + filename + " s'ha guardat correctament."
        else:
            txt = "Skyline " + i + " no existeix a la llista d'identificadors"
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=txt)


def load(update, context):
    """ Carrega a memoria una variable d'un fitxer indicat per l'usuari """
    if len(context.args) == 0:
        txt = "S'ha d'especificar almenys un identificador d'Skyline."
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=txt)
    else:
        for i in context.args:
            filename = i + ".sky"
            if not os.path.exists(filename):
                txt = "L'axiu " + filename + " no existeix"
            else:
                first_name = update.effective_chat.first_name
                last_name = update.effective_chat.last_name
                file = open(filename, 'rb')
                dataID = pickle.load(file)
                file.close()
                if not (first_name + " " + last_name) in data:
                    data[first_name + " " + last_name] = {}
                data[first_name + " " + last_name][i] = dataID
                txt = "L'Skyline \"" + i + "\" ha sigut carregat."
            context.bot.send_message(
                chat_id=update.effective_chat.id,
                text=txt)


if __name__ == '__main__':
    """ Funció principal Main """
    # hack pel Mac
    # matplotlib.use('Agg')

    TOKEN = open('token.txt').read().strip()
    updater = Updater(token=TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(CommandHandler('author', author))
    dispatcher.add_handler(CommandHandler('help', helpInfo))
    dispatcher.add_handler(CommandHandler('lst', lst))
    dispatcher.add_handler(CommandHandler('clean', clean))
    dispatcher.add_handler(CommandHandler('save', save))
    dispatcher.add_handler(CommandHandler('load', load))

    dispatcher.add_handler(MessageHandler(Filters.text, calc))

    updater.start_polling()

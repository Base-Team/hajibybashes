import telebot
from telebot import types
from telebot import util
import sys
import json
import os
import random
import base64
import urllib
import urllib2
import redis
import requests as req
reload(sys)
sys.setdefaultencoding("utf-8")
bot= telebot.TeleBot("302653751:AAESoUiKytv9Pnh9lozXdLOJfK-v_EgCXtA")
redis = redis.StrictRedis(host='localhost', port=6379, db=0, decode_responses=True)
#######################################################################
markupinfo = types.InlineKeyboardMarkup()
markupinfo.add(types.InlineKeyboardButton('MrPourya', callback_data="General"), types.InlineKeyboardButton('Channel', callback_data="Hidden1"))
markupinfo.add(types.InlineKeyboardButton('ninjahacker', callback_data="SohyDev"), types.InlineKeyboardButton('Hidden', callback_data="Hidden2"))
########################################################################
@bot.message_handler(commands=['stats'])
def send_stats(m):
    if m.from_user.id ==  307395482:
        users = str(redis.scard('memberspy'))
        text = '`Users` : *{}*'.format(users)
        bot.send_message(m.chat.id,text,parse_mode='Markdown')
########################################################################
@bot.message_handler(commands=['start'])
def test(call):
    id = call.from_user.id
    redis.sadd('memberspy',id)
    bot.send_message(call.chat.id,'*Hello*\n\n`Welcome To` *Lite Team Bot*',reply_markup=markupinfo, parse_mode='markdown')
@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
        if call.message:
            if call.data == "MrPourya":
                markup = types.InlineKeyboardMarkup()
                markup.add(types.InlineKeyboardButton('back', callback_data='back'))
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text="_Creator Team :)_",reply_markup=markup, parse_mode='markdown')
        if call.message:
            if call.data == "Channel":
                markup = types.InlineKeyboardMarkup()
                markup.add(types.InlineKeyboardButton('back', callback_data='back'))
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="_Lite Team Channel :_ @LiteTM",reply_markup=markup, parse_mode="markdown")
        if call.message:
            if call.data == "General":
                markup = types.InlineKeyboardMarkup()
                markup.add(types.InlineKeyboardButton('back', callback_data='back'))
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="*LOCK*", reply_markup=markup, parse_mode="markdown")
        if call.message:
            if call.data == "SohyDev":
                markup = types.InlineKeyboardMarkup()
                markup.add(types.InlineKeyboardButton('back', callback_data='back'))
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="*LOCK*", reply_markup=markup, parse_mode="markdown")
        if call.message:
            if call.data == "Hidden":
                markup = types.InlineKeyboardMarkup()
                markup.add(types.InlineKeyboardButton('back', callback_data='back'))
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="*Mr Hidden*", reply_markup=markup, parse_mode="markdown")
            if call.data == "back":
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text="*Return To Home Page.*\n\n`Use The Following Buttons.`",reply_markup=markupinfo, parse_mode='markdown')
############################################################
@bot.inline_handler(lambda query: len(query.query) is 0)
def default_query(msg):
    try:
        a = types.InlineQueryResultArticle('1', 'PvSuDo', types.InputTextMessageContent("", parse_mode="markdown"))
        bot.answer_inline_query(msg.id, [a])
    except Exception as e:
        print(e)
@bot.inline_handler(lambda query: len(query.query) is 0)
def default_query(msg):
    try:
	a = types.InlineQueryResultArticle('2', 'solid', types.InputTextMessageContent("", parse_mode="markdown"))
        bot.answer_inline_query(msg.id, [a])
    except Exception as e:
        print(e)
#############################################################
bot.polling(True)
from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes 

TOKEN: Final = '8040455584:AAG2VnLf-Cva9f4m-ozAEdUWqn7xKnSXKM8'
BOT_USERNAME: Final = '@bbananaabot'

#Commands

async def start_command(update:Update, ontext: ContextTypes.DEFAULT_TYPE):
	await update.message.reply_text('Hello! Thanks for chatting with me! I am a banana.')

async def help_command(update:Update, ontext: ContextTypes.DEFAULT_TYPE):
	await update.message.reply_text('I am a banana. Please type something so I can respond.')

async def custom_command(update:Update, ontext: ContextTypes.DEFAULT_TYPE):
	await update.message.reply_text('This is a custom command!.')


#Responses

def handle_response(text:str) -> str:

	processed:str = text.lower()

	if 'hello' in processed:
		return 'Hey there!'

	if 'how are you' in processed:
		return 'I am good!'

	if 'i love python' in processed:
		return 'Remember to subscribe!'

	return 'i do not understand what you wrote...'

#Messages

async def handle_message(update:Update, context: ContextTypes.DEFAULT_TYPE):
	message_type:str=update.message.chat.type
	text: str=update.message.text

	print(f'User ({update.message.chat.id}) in {message_type}: {text}')

	if message_type == 'group':
		if(BOT_USERNAME in text):
			new_text:str=text_replace(BOT_USERNAME,'').strip()
			response:str=handle_response(new_text)
		else:
			return
	else:
		response:str=handle_response(text)

	print('Bot: ',response)

	await update.message.reply_text(response)

#Error
async def error(update:Update, context: ContextTypes.DEFAULT_TYPE):
	print(f'Update {update} caused error: {context.error}')



if __name__ == '__main__':
	app = Application.builder().token(TOKEN).build()

	print('Starting banana bot...')

	# Commands
	app.add_handler(CommandHandler("start", start_command))
	app.add_handler(CommandHandler("help", help_command))
	app.add_handler(CommandHandler("custom", custom_command))

	# Messages
	app.add_handler(MessageHandler(filters.TEXT, handle_message))


	# Errors 
	app.add_error_handler(error)

	#Polls the bot
	print("Polling...")
	app.run_polling(poll_interval=3)
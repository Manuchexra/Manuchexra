
Token="7253815810:AAEXKs5xVZUJvl8Lvkc7ZRS992j-434Axxg"
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext 

@csrf_exempt
def start(update: Update, context: CallbackContext):
    chat_id = update.effective_chat.id
    username = update.message.from_user.username
    first_name = update.message.from_user.first_name
    
    # Save user information in the TelegramUser model
    from .models import TelegramUser
    user, created = TelegramUser.objects.get_or_create(
        chat_id=chat_id,
        defaults={'username': username, 'first_name': first_name}
    )
    if created:
        message = 'Assalomu alaykum! Siz muvaffaqiyatli ro\'yxatdan o\'tdingiz.'
    else:
        message = 'Salom, qaytadan xush kelibsiz!'
    
    update.message.reply_text(message,chat_id)
# chat_id = Update.effective_chat.id
# Update.message.reply_text("hi")
def main():
    # Replace "YOUR_BOT_TOKEN" with your actual bot token
    updater = Updater(Token,update_queue=None)
    
    # Get the dispatcher from the updater object
    dp= updater.dispatcher
    
    dp.add_handler(CommandHandler("start", start))
    
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
# 

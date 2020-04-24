import logging
import os
import random
import sys

from telegram.ext import Updater, CommandHandler

# Enabling logging
logging.basicConfig(level=logging.INFO,
                    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logger = logging.getLogger()

# Getting mode, so we could define run function for local and Heroku setup

def run(updater):
    updater.start_polling()



def start_handler(update, context):
    # Creating a handler-function for /start command 
    logger.info("User {} started bot".format(update))
    update.message.reply_text("Hello {} {}!\n Welcome to the LookUp tarot".format(update._effective_user.first_name, update._effective_user.last_name))

def repeat_handler(update, context):
    user_says = " ".join(context.args)
    update.message.reply_text("Repeating: " + user_says)

def send_image(update, context):
    context.bot.send_photo(chat_id=update.effective_chat.id, photo=open('mystictarot/cups-01.jpg', 'rb'))

def one_of_cup(update, context):
    context.bot.send_photo(chat_id=update.effective_chat.id, photo=open('mystictarot/cups-01.jpg', 'rb'))
    update.message.reply_text("One of Cups\n Welcome to the world of emotions")

def the_fool(update, context):
    context.bot.send_photo(chat_id=update.effective_chat.id, photo=open('mystictarot/major-00.jpg', 'rb'))
    update.message.reply_text("00 - The Fool\nMajor Arcana\nNaive and free.\n\nUpright: Innocence, intuition, spontaneity, new beginning, carefree.\n\nYou are in the path of discovery and wonder. The gods and angels conspire to guide and nurture you. Now is the moment to let yourself be grateful for all that you have been given in life. Use your intuition to find the answers you’ve been seeking and complete your journey.\n\nReversed: Recklessness, hasty, audacious, adventurous.\n\nListen to warning signs before making any rash decision. Your instinct may be telling you one thing but you must be aware of hidden traps along the way.")

def the_magician(update, context):
    context.bot.send_photo(chat_id=update.effective_chat.id, photo=open('mystictarot/major-01.jpg', 'rb'))
    update.message.reply_text("01 - The Magician\nMajor Arcana\nMaster of illusions.\n\nUpright: Insights, revelation, materialization.\n\nYou have all the tools needed to begin the process of materializing your ideas. It will require a lot of hard work behind the scenes. Your work has the potential to look effortless and perfect. First impression is everything. Work out all the details and test your projects before making an appearance.\n\nReversed: Control, disorganization, missing the big picture.\n\nDon’t try to control every aspect of the projects you have in mind. Let other people in. Let go of any need to control or any belief of perfection. Try to maximize your abilities and true potential. Hard work and honesty is key. Don’t take shortcuts.")

def the_high_priestess(update, context):
    context.bot.send_photo(chat_id=update.effective_chat.id, photo=open('mystictarot/major-02.jpg', 'rb'))
    update.message.reply_text("02 - The High Priestess\n\nShe will guide you between the spiritual and earthly realms. \n\nUpright: Divine, cherish, sublime, subconscious.\n\nLet all things spiritual touch you. Awaken your senses with meditation, music, visual arts, incenses, simple foods and exercise. Allow your mortal body to experience all that enriches and guides you to become the best version of yourself. Nature and art is the key to finding spirituality. They are therapy to the soul. You will gain divine inspiration and the confidence to let the spirit guide you to feel and perform in ways you’ve never thought you could.\n\nReversed: Mysterious, obscure, disguised.\n\nIt’s time to quiet down the noise from the world and have a moment of introspection. Your mind will become clear and slowly you will begin to realize your instincts are correct. There is also possible gossips, hidden agendas or secrets being kept from you. Try to let these things go. If you decide to confront these issues, make sure to do so with an open mind.")

def the_empress(update, context):
    context.bot.send_photo(chat_id=update.effective_chat.id, photo=open('mystictarot/major-03.jpg', 'rb'))
    update.message.reply_text("03 - The Emperess\n\nMajor Arcana\n\nMother charm, love and beauty\n\nUpright: Beauty, loving, care.\n\nThis is your chance to love and grow. Possible pregnancy, adoption or opportunity to nurture and care for someone. Your life will be filled with abundance and quality time.\n\nReversed: Tension, trust, habits.\n\nTake some time-off. Let things be and go have some fun. Remember to love yourself. Try to recharge your energy so you can better take care of those who depend on you. Try not to worry too much and be less controlling or overprotective.")

def the_emperor(update, context):
    context.bot.send_photo(chat_id=update.effective_chat.id, photo=open('mystictarot/major-04.jpg', 'rb'))
    update.message.reply_text("04 - The Emperor\n\nMajor Arcana\n\nFather love, energy, peace.\n\nUpright: Authority, stability.\n\nPeople look up to you and value your skills and the peace of mind you bring. You will be granted the connections needed to achieve the things you have envisioned. Hard work and great ethics will prepare you to direct and communicate well. Make yourself available regularly to discuss issues or concerns.\n\nReversed: Prepotency, excessive control.\n\nTry not to take too many tasks by yourself. Accept feedback. Be trustworthy and respectful. Use the knowledge you’ve acquired to mentor and help others achieve goals just as you have achieved yours.")

def the_hierophant(update, context):
    context.bot.send_photo(chat_id=update.effective_chat.id, photo=open('mystictarot/major-05.jpg', 'rb'))
    update.message.reply_text("05 - The Hierophant\n\nMajor Arcana\n\nReligious figure.\n\nUpright: Spirituality, submission, tradition.\n\nYou have the power and all the tools to influence those around you with goodness. If you choose to use this gift, your actions will have eternal repercussions. \n\nReversed: inner soul search, free thinking.\n\nTake a step back to organize your thoughts and mind. Increase your knowledge gradually. Be patient and don’t be scared of challenging your beliefs.")

def the_lovers(update, context):
    context.bot.send_photo(chat_id=update.effective_chat.id, photo=open('mystictarot/major-06.jpg', 'rb'))
    update.message.reply_text("06 - The Lovers\n\nMajor Arcana \n\nAffection, Romance\n\nUpright: Love, understanding.\n\nEmotions, joy and love will come to you. Be confident and positive and all things good will come. Chose to be with someone you loves and respect you. Enjoy every little moment and do what makes you feel happy in love.\n\nReversed: Clash, incompatibility.\n\nTrust your heart. Let go of all fear and doubt. Surround yourself with people who love and support you. Know that all things pass and let all sad and negative feelings pass.")

def the_chariot(update, context):
    context.bot.send_photo(chat_id=update.effective_chat.id, photo=open('mystictarot/major-07.jpg', 'rb'))
    update.message.reply_text("07 - The Chariot\n\nMajor Arcana\n\nDetermination, strength \n\nUpright: Accomplishment, determination\n\nYou will conquer and achieve your goals. Apply discipline and dedication. You will be successful. Don’t take shortcuts. Victory is within your capacity. Triumph over all obstacles.\n\nReversed: Obstacles, competition\n\nChallenges may come your way. Stay focused and stay your course steadfastly. Take a few steps back if you need to redirect yourself into the right direction. Take a breather and be open to new pathways opening up to you.")

def strength(update, context):
    context.bot.send_photo(chat_id=update.effective_chat.id, photo=open('mystictarot/major-08.jpg', 'rb'))
    update.message.reply_text("08 - Strength\n\nMajor Arcana\n\nInner strength, compassion \n\nUpright: Influence, dominion \n\nYou have in your heart the inner strength to keep pushing forward, to calm down any troubled heart and to persuade any soul to do the right thing. Take your time to realize that you can overcome anything that challenges you. Be confident that the role you play is one of great importance.\n\nReversed: Apathy, weakness\n\nDo not hold on to grudges. Be careful when dealing with strong emotions that have been bottled up. These can weigh you down. Replenish your soul with forgiveness and love.")

def the_hermit(update, context):
    context.bot.send_photo(chat_id=update.effective_chat.id, photo=open('mystictarot/major-09.jpg', 'rb'))
    update.message.reply_text("09 - The Hermit\n\nMajor Arcana\n\nUpright: Introspection \n\nAllow yourself to find the answers you’ve been searching for by leaving behind worldly distractions and re-evaluating your personal goals and where do you want to go. Be more aware of yourself. Be receptive to change and renew your mind with positive emotions.\n\nReversed: Isolation, withdraw, solitude\n\nDo not force or overthink things. Follow your natural inclinations. Leave behind the worldly distractions. You will find freedom by thinking positive and removing barriers within. Be receptive to change and listen to your intuition.")

def wheel_of_fortune(update, context):
    context.bot.send_photo(chat_id=update.effective_chat.id, photo=open('mystictarot/major-10.jpg', 'rb'))
    update.message.reply_text("Wheel of Fortune\n\nMajor Arcana\n\nUpright: Destiny, future, serendipity\n\nThe doors to your destiny are open. Whether or not you choose to take it will bring you new perspectives. Feel your way through life and you will find freedom. Opportunities may arise. Be ready to take them.\n\nReversed: New circle, stagnation \n\nRefuse to hold yourself back. Accept the fact that changes are inevitable. Break all negative cycles and start fresh in an authentic way. Accept your responsibilities in the role you play in society with positivity.")

def justice(update, context):
    context.bot.send_photo(chat_id=update.effective_chat.id, photo=open('mystictarot/major-11.jpg', 'rb'))
    update.message.reply_text("11 - Justice\n\nMajor Arcana\n\nUpright: Integrity, fair treatment\n\nAlign your inner thoughts with truth and it’s beauty. It is not always explicit and straightforward but you can take a moment to evaluate your actions and accept consequences.\n\nReversed: Corruption, dishonesty.\n\nSeek closure for any unfair, discriminatory, immoral or injustice that may have occurred.\nJustice will take its course one way or the other (Karma is a bitch).") 

def the_hanged_man(update, context):
    context.bot.send_photo(chat_id=update.effective_chat.id, photo=open('mystictarot/major-12.jpg', 'rb'))
    update.message.reply_text("12 - The Hanged Man\n\nMajor Arcana\n\nUpright: Prospect, attitude\n\nPotential situation to look outside the box. Be opened minded to many possible outcomes. Be curious. Accept change. \n\nReversed: Yield, concede\n\nStep back and let go of old ideas. Develop your creativity. Make a plan and act. Do not wait. Make everyday count.")

def death(update, context):
    context.bot.send_photo(chat_id=update.effective_chat.id, photo=open('mystictarot/major-13.jpg', 'rb'))
    update.message.reply_text("13 - Death\n\nMajor Arcana\n\nUpright: End, cusp, ultimate\n\nLet go and part ways with the past and start a new chapter in your life. Don’t replay or look back at old emotions. Move forward. Move on. \n\nReversed: self evaluate, resolution\n\nGrant the unknown a chance to rise. Rid yourself of old ways. Take a new direction and start fresh.")

def temperance(update, context):
    context.bot.send_photo(chat_id=update.effective_chat.id, photo=open('mystictarot/major-14.jpg', 'rb'))
    update.message.reply_text("14 - Temperance\n\nMajor Arcana\n\nUpright: Harmony, equilibrium \n\nEngage in calming activities that promote a tranquil state of mind. Don’t let small things get to you. Seek balance and harmony\n\nLet things or yourself blend in just enough to merge aspects that may enrich your life.\n\nReversed: Instability, fluidity \n\nLearn self-restraint from the things that can cause you to lose focus.  There is no need to be highly opinionated. Analyse your patterns and restore moderation in your daily life.")

def devil(update, context):
    context.bot.send_photo(chat_id=update.effective_chat.id, photo=open('mystictarot/major-15.jpg', 'rb'))
    update.message.reply_text("15 - Devil\n\n Major Arcano\n\nUpright: attachment, restrictions\n\nBreak free from the things you know are detrimental to your body or soul. It takes tremendous strength to pull away from the influence of what can be causing you to be imprisoned in the flesh, mind or soul. Steer clear from things you desire but you feel it might be bad for you.\n\nReversed: New beliefs, letting go\n\nSpend more time with people that help you feel at ease. Find ways to build yourself from within. Let go you old thinking that you once thought were good for you. Let go of guilt.")

def tower(update, context):
    context.bot.send_photo(chat_id=update.effective_chat.id, photo=open('mystictarot/major-16.jpg', 'rb'))
    update.message.reply_text("16 - Tower\n\n Major Arcano\n\nUpright: Things revealed, chaos\n\nExpect change in the most unexpected way. A revolution of feelings and direction. Life will surprise with abrupt occurrence that may shake your emotional, spiritual or physical state. Trust that there is growth with change and rebuild your new perspectives in a healthy manner. Allow yourself to receive revelation and be tuned to positive vibes and letting go of anything that may be keeping you from achieving your goals.\n\nReversed: Resistance to changes, personal growth\n\nAwakening to new understanding will challenge you to rebuild on new perspectives. You’re maturing and able to break down all illusions and lies that you once constructed in your mind. Once walls are broken you will find yourself healing and forgiving.")

def the_star(update, context):
    context.bot.send_photo(chat_id=update.effective_chat.id, photo=open('mystictarot/major-17.jpg', 'rb'))
    update.message.reply_text("17 - The Star\n\nMajor Arcano\n\nUpright: Hope, renewal, confidence\n\nFeel the peace and comfort that the universe wants you to feel and enjoy. Anything is possible. Rediscover where you inspirations derive from. Share your passion with others. Nourish these pure feelings.\n\nReversed: despair, misery, sorrow \n\nDon’t lose faith in what you once believed was possible. If you want peace in your life it will come. In the meantime, take good care of yourself physically, mentally and spiritually. Trust the universe.")

def the_moon(update, context):
    context.bot.send_photo(chat_id=update.effective_chat.id, photo=open('mystictarot/major-18.jpg', 'rb'))
    update.message.reply_text("18 - The Moon\n\nMajor Arcano\n\nUpright: Anxiety, intuition, suspense\n\nTrust your intuition and do what you feel is genuinely best for you or your loved ones. Make sure you ran by a few facts so you be at peace. Proceed with caution as sometimes intuition can lead to illusions if we are led by fear or unrealistic expectations.\n\nReversed: Confounding, surrender\n\nYou may have been revealed ideas or directions that may help your trajectory in life. If you still feel unsure about which path to take, go back to your initial thought process and how you felt about it before complex thinking took over. That sensibility should help you overcome a stuck path.")

def the_sun(update, context):
    context.bot.send_photo(chat_id=update.effective_chat.id, photo=open('mystictarot/major-19.jpg', 'rb'))
    update.message.reply_text("19 - The Sun\n\nMajor Arcano\n\nUpright: Warmth, success\n\nLet the sun bathe you in enthusiasm and vitality. Your warmth and radiant energy is felt by others. This makes up of your most noble qualities. Use them to influence people in a positive way.\n\nReversed:essential nature, optimistic soul\n\nYour essential nature of when you were a child may have been forgotten and is waiting for it to be revived and felt")

def error_callback(update, context):
    logger.warning('Update "%s" caused error "%s"', update, context.error)

if __name__ == '__main__':
    logger.info("Starting bot")
    TOKEN = os.getenv("./env/TOKEN")
    updater = Updater(TOKEN, use_context=True)
    updater.dispatcher.add_handler(CommandHandler('start', start_handler))
    updater.dispatcher.add_handler(CommandHandler('repeat', repeat_handler))
    updater.dispatcher.add_handler(CommandHandler('sendImage', send_image))
    updater.dispatcher.add_handler(CommandHandler(['1ofcups'], one_of_cup))
    updater.dispatcher.add_handler(CommandHandler(['thefool', 'fool'], the_fool))
    updater.dispatcher.add_handler(CommandHandler(['themagician', 'magician'], the_magician))
    updater.dispatcher.add_handler(CommandHandler(['thehighpriestess', 'highpriestess', 'priestess'], the_high_priestess))
    updater.dispatcher.add_handler(CommandHandler(['theempress', 'empress'], the_empress))
    updater.dispatcher.add_handler(CommandHandler(['theemperor', 'emperor'], the_emperor))
    updater.dispatcher.add_handler(CommandHandler(['thehierophant', 'hierophant'], the_hierophant))
    updater.dispatcher.add_handler(CommandHandler(['thelovers', 'lovers'], the_lovers))
    updater.dispatcher.add_handler(CommandHandler(['thechariot', 'chariot'], the_chariot))
    updater.dispatcher.add_handler(CommandHandler('strength', strength))
    updater.dispatcher.add_handler(CommandHandler(['thehermit', 'hermit'], the_hermit))
    updater.dispatcher.add_handler(CommandHandler(['wheelfortune','wheelfortune','wheeloffortune', 'wheel', 'fortune'], wheel_of_fortune))
    updater.dispatcher.add_handler(CommandHandler(['justice'], justice))
    updater.dispatcher.add_handler(CommandHandler(['thehangedman', 'hangedman', 'hanged'], the_hanged_man))
    updater.dispatcher.add_handler(CommandHandler(['death'], death))
    updater.dispatcher.add_handler(CommandHandler(['temperance'], temperance))
    updater.dispatcher.add_handler(CommandHandler(['devil'], devil))
    updater.dispatcher.add_handler(CommandHandler(['tower'], tower))
    updater.dispatcher.add_handler(CommandHandler(['thestar', 'star'], the_star))
    updater.dispatcher.add_handler(CommandHandler(['themoon', 'moon'], the_moon))
    updater.dispatcher.add_handler(CommandHandler(['thesun', 'sun'], the_sun))
    updater.dispatcher.add_error_handler(error_callback)

    run(updater)
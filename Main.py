import disnake
from disnake.ext import commands
import random

intents = disnake.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='/', intents=intents)


@bot.event
async def on_ready():
    print(f'Бот {bot.user} подключен к Discord!')

@bot.slash_command(name="игра", description="Начать игру Камень, ножницы, бумага")
async def start_game(ctx):
    bot.game_started = True
    await ctx.send("Игра началась! Выберите: камень, ножницы или бумагу.")

@bot.slash_command(name="камень", description="Выбрать камень в игре Камень, ножницы, бумага")
async def rock(ctx):
    await play(ctx, "камень")

@bot.slash_command(name="ножницы", description="Выбрать ножницы в игре Камень, ножницы, бумага")
async def scissors(ctx):
    await play(ctx, "ножницы")

@bot.slash_command(name="бумага", description="Выбрать бумагу в игре Камень, ножницы, бумага")
async def paper(ctx):
    await play(ctx, "бумага")

async def play(ctx, choice):
    if not hasattr(bot, 'game_started') or not bot.game_started:
        await ctx.send("Игра еще не началась! Для начала игры используйте команду `/игра`.")
        return

    choices = ['камень', 'ножницы', 'бумага']
    bot_choice = random.choice(choices)

    if choice.lower() not in choices:
        await ctx.send("Неправильный выбор! Попробуйте снова: камень, ножницы или бумага.")
        return

    await ctx.send(f"Вы выбрали: {choice}. Бот выбрал: {bot_choice}.")

    if choice.lower() == bot_choice:
        await ctx.send("Ничья!")
    elif (choice.lower() == 'камень' and bot_choice == 'ножницы') or \
        (choice.lower() == 'ножницы' and bot_choice == 'бумага') or \
        (choice.lower() == 'бумага' and bot_choice == 'камень'):
        await ctx.send("Вы победили!")
    else:
        await ctx.send("Бот победил!")


token = ''
bot.run(token)

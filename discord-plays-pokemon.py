import os
import discord
import time
from discord.ext import commands
from pynput.keyboard import Key, Controller
import asyncio
import time

token = "insert token here"

bot = commands.Bot(command_prefix='!', case_insensitive=True)

print("Started bot")

keyboard = Controller()

async def test(message):
    print(message)

async def EmuInput(name):
    name = name.lower()
    InputDic = {
        'up': 'w',
        'down': 's',
        'left': 'a',
        'right': 'd',
        'a': 'z',
        'b': 'x',
        'start': 'r',
        'select': 't',
        'lb' : '1',
        'rb' : '2',
        'save' : '9'
        }
    try:
        Input = InputDic[name]
        keyboard.press(Input)
        await asyncio.sleep(0.1)
        keyboard.release(Input)
    except:
        print("Error finding input")

@bot.command(name='Up', help='Presses Up on the emulator D-Pad')
async def UpInput(ctx):
    await EmuInput('up')

@bot.command(name='Down', help='Presses Down on the emulator D-Pad')
async def DownInput(ctx):
    await EmuInput('down')

@bot.command(name='Left', help='Presses Left on the emulator D-Pad')
async def LeftInput(ctx):
    await EmuInput('left')

@bot.command(name='Right', help='Presses Right on the emulator D-Pad')
async def RightInput(ctx):
    await EmuInput('right')

@bot.command(name='A', help='Presses A on the emulator D-Pad')
async def AInput(ctx):
    await EmuInput('a')

@bot.command(name='B', help='Presses B on the emulator D-Pad')
async def BInput(ctx):
    await EmuInput('b')

@bot.command(name='Start', help='Presses Start on the emulator D-Pad')
async def StartInput(ctx):
    await EmuInput('start')

@bot.command(name='Select', help='Presses Select on the emulator D-Pad')
async def SelectInput(ctx):
    await EmuInput('select')

@bot.command(name='LB', help='Presses Left Bumper on the emulator D-Pad')
async def LeftBumper(ctx):
    await EmuInput('lb')

@bot.command(name='RB', help='Presses Right Bumper on the emulator D-Pad')
async def RightBumper(ctx):
    await EmuInput('rb')

@bot.command(name='PokeHelp', help='Lists commands available')
async def HelpText(ctx):
    List = 'The available commands are Up, Down, Left, Right, A, B, Start, Select'
    await ctx.send(List)

async def QuickSave(ctx):
    await EmuInput('save')
    await asyncio.sleep(10 * 60)
    await QuickSave(ctx)

bot.loop.create_task(QuickSave(bot))

bot.run(token)

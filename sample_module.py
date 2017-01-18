#!/usr/bin/env python3
from sopel import module

"""
    The first line imports the sopel.module library. In this module, we only really need this for the next line. This is called a decorator, and associates the command "helloworld" with the function that comes right after it. A command in Sopel is triggered when a line said in a channel starts with a period, followed by the command 
"""
@module.commands('helloworld')
def helloworld(bot, trigger):
    bot.say('Hello, world!')

"""
    Have the bot repeat whatever comes after .echo or .repeat in the channel
"""
@module.commands('echo','repeat')
def echo(bot,trigger):
    bot.reply(trigger.group(2))

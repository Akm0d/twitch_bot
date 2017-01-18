#!/usr/bin/env python3
import sopel

config = soepl.config.Config("~/.sopel/default.cfg",validate=True)
bot = sopel.bot.Sopel(config,daemon=False)

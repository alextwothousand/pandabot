# PandaBot.py
Source code for PandaBot, a Discord Bot created by myself in Python.
# REQUIREMENTS
    The latest version of discord.py (THIS DOES NOT USE DISCORD.PY REWRITE!)
    You will need Python 3.5.3 or above (as a general rule of thumb you should stick with 3.6.6)
    It is preferred that this bot is hosted on a VPS rather than your PC locally, if to be made commercial.   
# NOTES
All of the commands OTHER THAN THE `$hello` command will show up in the `$help` list. This is due to the fact that hello uses `def on_message` rather than defining it as a command. You may also get a error in the console due to the `$hello` command not being defined as a command however that can be ignored. This can be easily fixed by using `ctx/context`, you can read up on at the discord.py API.

Under the `$hello` command you can put in your client ID so that it shows `'Hello there my father, my creator, my overlord'` rather than `'Hello there NAME'`.

The token is easily changeable by modifying `botprefix` and the `$hello` command however I may push a new update in the future which turns `$hello` into an actual defined command.

This probably wasn't programmed the best way possible and you could probably incorporate it with some sort of database, for example, asyncpg (PostrgeSQL with async - which is reccomended as SQLite and MySQL are blocking), to add a sort of credits system or something similar to that.

If there are any further issues or you wish to contact me create a `issue` and I will respond asap. Enjoy and have fun!
# LICENSE
    Copyright (c) 2018 Infin1tyy (github)

    Permission is hereby granted, free of charge, to any person obtaining a copy
    of this software and associated documentation files (the "Software"), to deal
    in the Software without restriction, including without limitation the rights
    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
    copies of the Software, and to permit persons to whom the Software is
    furnished to do so, subject to the following conditions:

    The above copyright notice and this permission notice shall be included in all
    copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
    SOFTWARE.
    

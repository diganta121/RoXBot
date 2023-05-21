# RoXBot
# Just a bot for Roblox clients
---

RoxBot is a roblox bot that uses the Roblox client to perform actions automatically.
It uses `pygetwindow` to focus on Roblox and send keypresses to it.

It also has a neat little interface made using `pygame`, other than those it has no dependencies.

---
### Security Notice
Since it only uses keypresses, RoXBot does **not** require administrator privileges or
require you to enter credentials.

---

### Installation
- Ensure that you have downloaded (and installed!) Python 3.6 or later (3.8+ recommended).
  - **This includes adding it to your path!**
- Ensure that you have the latest version of git installed.
- Clone the repository with `git clone https://github.com/`.
- Enter the newly created directory with `cd RoXBot`.
- Install the dependencies via pip: `python -m pip install -r requirements.txt`.

### Usage
**Before attempting to start the bot, make sure you have a window open! It will raise `errors.NoRobloxInstance` otherwise.**

- Join a new Roblox game and wait for it to load completely.
- Double click (or launch by terminal) the `main.py` file.
  - Please note this could take a few seconds to initialize.
- Once started, you can use the GUI that shows up on your screen.

You can also provide some options to the bot.
To do this, make sure you're launching the bot via terminal.

To add an option, call the bot like so: `python main.py [options]`

**Available Options:**
  - `-q` *or* `--quiet`, disables chat output.
---

### API
for more info on the api visit `https://github.com/`


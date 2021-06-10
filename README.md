# pypatbot

## Dependices
```poetry```

```python3```

Poetry will handle the installing of all of the needed python libaries 

# Stuff to do first
Get a bot token from discord's dev portal. There are many tutorals online that can help you with that.

Sign Up for a RapidAPI account and sign up for whatever plan you want for the below API
https://rapidapi.com/Gramzivi/api/covid-19-data
make sure to record your API key.

## Disabling HeadPat Command!
If you want to disable the headpat command, you can add your server ID to the HeadPadoff file.

## Installing/Cloning
I am assuming you are runninng this on Linux.
You will need Potery and python3 installed. I assume you already have python3 installed. To install poetry, run the below command. 
```curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python3```

then. clone the repo.
```git clone https://github.com/LakesideMiners/pypatbot.git```
then cd into the folder
```cd pypatbot```
next, set up your env vars.

```cd cogs```
then
```poetry install```
# Setting Up The API Strings And Reddit Useragent
Create a file named ".env" 
```nano .env```
paste the below text into the file
```
DISCORD_BOT_SECRET="aaa"
x_rapidapi_key="bbb"
UA="CCCBot\d.d.d"
```
replacing ```aaa``` with your bot token
replacing ```bbb``` with your rapidapi token
Repacling ```CCC``` with a short name that will be used as the bots useragent for the Reddit API
and ```d.d.d``` with a version number. e.g 1.3.0
MAKE SURE TO INCLUDE THE QUOTES
Save the file. 

## Inviting to your server
There is a section on your bots page on the discord dev portal to create a URL to invite your bot, right now, you need to give it the abaitly to send and read messages. as well as use embeds. 
## Running
In the folder with main.py. run

```poetry run python main.py```



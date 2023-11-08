from telegram.ext import Updater, CommandHandler, CallbackQueryHandler
from dotenv import load_dotenv
import os
import subprocess
import json

load_dotenv()

dockerReturn = subprocess.getoutput("docker ps")
dockerReturnList = dockerReturn.split("\n")
dockerReturnTitle = dockerReturnList[0].split("   ")

dockerReturnData = {}
dockerReturnNewTitle = []

for i in range(len(dockerReturnTitle)):
    if dockerReturnTitle[i] != "":
        dockerReturnNewTitle.append(dockerReturnTitle[i].strip())


for i in range(1, len(dockerReturnList)):

    dockerReturnNewList = []

    for j in range(len(dockerReturnList[i].split("   "))):
        if dockerReturnList[i].split("   ")[j] != "":
            dockerReturnNewList.append(dockerReturnList[i].split("   ")[j].strip())
    
    dockerReturnData[dockerReturnList[i].split("   ")[0]] = {
        dockerReturnNewTitle[1] : dockerReturnNewList[1],
        dockerReturnNewTitle[2] : dockerReturnNewList[2],
        dockerReturnNewTitle[3] : dockerReturnNewList[3],
        dockerReturnNewTitle[4] : dockerReturnNewList[4],
        dockerReturnNewTitle[5] : dockerReturnNewList[5],
        dockerReturnNewTitle[6] : dockerReturnNewList[6],

    }

response = f"Status : OK 4/{len(dockerReturnData)}\n  STATUS              NAMES\n"

for container in dockerReturnData:
    response += f"  {dockerReturnData[container]['STATUS']} {dockerReturnData[container]['NAMES']}\n"


def main(response):

    updater = Updater(os.getenv("BOT_CONFIG_TOKEN"), use_context=True)

    dp = updater.dispatcher
    bot = updater.bot

    bot.send_message(chat_id=os.getenv("ADMIN_TELEGRAM_ID"), text=response)

    updater.start_polling()


if __name__ == '__main__':
    main(response)

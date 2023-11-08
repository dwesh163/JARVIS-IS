from dotenv import load_dotenv
import os
import subprocess
import json


load_dotenv()

print(os.getenv("BOT_CONFIG_TOKEN"))

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
        print(dockerReturnList[i])
        if dockerReturnList[i].split("   ")[j] != "":
            dockerReturnNewList.append(dockerReturnList[i].split("   ")[j].strip())
    
    dockerReturnData[dockerReturnList[i].split("   ")[0]] = {
        dockerReturnNewTitle[1] : dockerReturnNewList[0],
        dockerReturnNewTitle[2] : dockerReturnNewList[1],
        dockerReturnNewTitle[3] : dockerReturnNewList[2],
        dockerReturnNewTitle[4] : dockerReturnNewList[3],
        dockerReturnNewTitle[5] : dockerReturnNewList[4],
        dockerReturnNewTitle[6] : dockerReturnNewList[5],

    }


print(dockerReturnData)



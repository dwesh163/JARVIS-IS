from dotenv import load_dotenv
import os
import subprocess


load_dotenv()

print(os.getenv("BOT_CONFIG_TOKEN"))

dockerReturn = subprocess.getoutput("docker ps")
dockerReturnList = dockerReturn.split("\n")
dockerReturnTitle = dockerReturnList[0].split("   ")

dockerReturnData = {}

for i in range(1, len(dockerReturnList)):
    dockerReturnData[dockerReturnList[i].split("   ")[0]] = {
        dockerReturnTitle[1] : dockerReturnList[i].split("   ")[1],
        dockerReturnTitle[4] : dockerReturnList[i].split("   ")[2],
        dockerReturnTitle[10] : dockerReturnList[i].split("   ")[3],
        dockerReturnTitle[12] : dockerReturnList[i].split("   ")[4],
        dockerReturnTitle[18] : dockerReturnList[i].split("   ")[5],
        dockerReturnTitle[31] : dockerReturnList[i].split("   ")[7],

    }

print(dockerReturnData)



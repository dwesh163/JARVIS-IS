from dotenv import load_dotenv
import os 

load_dotenv()

print(os.getenv("BOT_CONFIG_TOKEN"))


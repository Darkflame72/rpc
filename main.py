import time
from time import mktime
import rpc

print("Obsidion discord invite")
client_id = "691589447074054224"
rpc_obj = rpc.DiscordIpcClient.for_platform(client_id)
print("RPC connection successful.")

time.sleep(5)
start_time = mktime(time.localtime())
while True:
    activity = {
        "details": "Minecraft Discord Bot",
        "assets": {"large_image": "logo"},
        "buttons": [
            {
                "label": "Add Obsidion",
                "url": "https://discord.com/oauth2/authorize?client_id=691589447074054224&scope=bot&permissions=314448",
            },
            {"label": "Discord Server", "url": "https://discord.com/invite/7BTbHcTEch"},
        ],
    }
    rpc_obj.set_activity(activity)
    time.sleep(30)
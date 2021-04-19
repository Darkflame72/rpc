import time
from time import mktime
import rpc

print("Obsidion discord invite")
client_id = "691589447074054224"
while True:
    try:
        rpc_obj = rpc.DiscordIpcClient.for_platform(client_id)
        print("RPC connection successful.")

        time.sleep(5)
        while True:
            activity = {
                "details": "Minecraft Discord Bot",
                "assets": {"large_image": "logo"},
                "buttons": [
                    {
                        "label": "Add Obsidion",
                        "url": "https://discord.com/oauth2/authorize?client_id=691589447074054224&scope=bot+applications.commands&permissions=19520&response_type=code&redirect_uri=https%3A%2F%2Fdiscord.obsidion-dev.com",
                    },
                    {
                        "label": "Discord Server",
                        "url": "https://discord.com/invite/7BTbHcTEch",
                    },
                ],
            }
            rpc_obj.set_activity(activity)
            time.sleep(30)
    except OSError:
        pass
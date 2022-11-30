import asyncio
import subprocess
import os

from libqtile import hook

@hook.subscribe.startup_once
def start_once():
    home = os.path.expanduser("~")
    subprocess.call([home + "/.config/qtile/scripts/autostart.sh"])

@hook.subscribe.client_new
async def client_new(client):
    await asyncio.sleep(0.5)
    print(client)
    if client.name == 'Spotify':
        print('--------- Matched spotify ---------')
        # client.toGroup(5)

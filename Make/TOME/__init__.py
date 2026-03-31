from TOME.core.bot import KIM
from TOME.core.dir import dirr
from pyromod import listen
from TOME.core.userbot import Userbot
from TOME.misc import dbb, heroku
from TOME.logging import LOGGER

dirr()
dbb()
heroku()

app = KIM()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()

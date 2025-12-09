from PRISHA_MUSIC.core.bot import PRISHA_MUSIC
from PRISHA_MUSIC.core.dir import dirr
from PRISHA_MUSIC.core.git import git
from PRISHA_MUSIC.core.userbot import Userbot
from PRISHA_MUSIC.misc import dbb, heroku

from SafoneAPI import SafoneAPI
from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = PRISHA_MUSIC()
api = SafoneAPI()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()

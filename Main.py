
import Constants

from dotenv import load_dotenv
from twitchio.ext import commands


load_dotenv()

class TwitchBot(commands.Bot):
    def __init__(self):
        super().__init__(token=Constants.ACCESS_TOKEN,
                         prefix=Constants.BOT_PREFIX,
                         initial_channels=[Constants.CHANNEL])
                        
        async def event_ready(self):
            print('{} is online.'.format(Constants.BOT_NICK))


        @commands.command(name="hello")
        async def hello(self, ctx: commands.Context):
            await ctx.send(f'Hello {ctx.author.name}!')


if __name__ == "__main__":
    print("Starting..")
    bot = TwitchBot()
    bot.run()


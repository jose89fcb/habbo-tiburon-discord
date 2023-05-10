import urllib
import json
import requests
import discord
from discord.ext import commands
import datetime
import io
 
from urllib import parse, request
from PIL import Image, ImageDraw, ImageFont, ImageFile
import time
from discord_slash import SlashCommand
from discord_slash.utils.manage_commands import create_choice, create_option
from discord_slash import SlashCommand, SlashContext


with open("configuracion.json") as f:
    config = json.load(f)

bot = commands.Bot(command_prefix='!', description="ayuda bot") #Comando
bot.remove_command("help") # Borra el comando por defecto !help

slash = SlashCommand(bot, sync_commands=True)
@slash.slash(
    name="tiburon", description="tiburon habbo hotel",
    options=[
                create_option(
                  name="keko",
                  description="Escribe el keko",
                  option_type=3,
                  required=True,
                ),
                create_option(
                  name="hotel",
                  description="Elige él hotel",
                  option_type=3,
                  required=True,
                  choices=[
                      create_choice(
                          name="ES - Hotel España",
                          value="es"
                      ),
                      create_choice(
                          name="BR - Hotel Brasil",
                          value="com.br"
                      ),
                      create_choice(
                          name="COM - Hotel Estados unidos",
                          value="com"
                      ),
                      create_choice(
                          name="DE - Hotel Aleman",
                          value="de"
                      ),
                      create_choice(
                          name="FR - Hotel Frances",
                          value="fr"
                      ),
                      create_choice(
                          name="FI - Hotel Finalandia",
                          value="fi"
                      ),
                      create_choice(
                          name="IT - Hotel Italiano",
                          value="it"
                      ),
                      create_choice(
                          name="TR - Hotel Turquia",
                          value="com.tr"
                      ),
                      create_choice(
                          name="NL - Hotel Holandés",
                          value="nl"
                      )
                  ]
                
               
                  
                )
             ])


async def _tiburon(ctx:SlashContext, keko:str, hotel:str):
    
    
    
    
    
    response = requests.get(f"https://www.habbo.{hotel}/api/public/users?name={keko}")
   
    try:

     habbo = response.json()['figureString']
    except KeyError:
       await ctx.send("El keko no existe!") 
   

   
    

    
    
   
    try:
        
     url = "https://www.habbo.com/habbo-imaging/avatarimage?size=l&figure="+ habbo +"&action=none&direction=4&head_direction=4&gesture=std&size=m"
     img1 = Image.open(io.BytesIO(requests.get(url).content))
     img1 = img1.resize((64,110), Image.ANTIALIAS)#tamaño del keko 1
    
    
    


    
    


    

   

    

    
    
    



     img2 = img1.copy()
    
    
    ###
    
     tiburon = Image.open(r"imagenes/tiburon.png").convert("RGBA") #imagen de la trozo
     img1 = tiburon.resize((145,136), Image.ANTIALIAS)#tamaño de tiburon

 
     img1.paste(img2,(22,5), mask = img2) #Posicion del keko 

     img1.paste(tiburon,(0,0), mask = tiburon) #Posicion del tiburon

    

    
    
    
    
   
    

    
   
    ###
    

   

 
    
    

    




    

    
    
    
   
    
   
       


      
    
       
      

      
    
       
            
        
        
        
       
        
     with io.BytesIO() as image_binary:
        img1.save(image_binary, 'PNG')
        image_binary.seek(0)

        await ctx.send(f"            `{keko}`", file=discord.File(fp=image_binary, filename='keko.png'))
    except UnboundLocalError:
       url=":("
         
        
        
        
        


@bot.event
async def on_ready():
    print("BOT listo!")
    
bot.run(config["tokendiscord"])   
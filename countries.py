from ast import Await
from importlib.resources import contents
from pickle import TRUE
from re import A
from turtle import delay
import discord
import time
import random as r 
from countrieslist import countries 
from discord.ext import commands



intents = discord.Intents.default()
intents.members = True
intents.messages = True
intents.message_content = True
bot = commands.Bot(command_prefix='-', intents=intents)
client = discord.Client(intents=intents)

   
mode="off"
temp=0

asked="off"
        

    

    
@client.event



async def on_ready():
        
        
    print(f'We have logged in as {client.user}')
questions = [
{
"name":"is the country landlocked (it has no coastline)",
"is the country landlocked (it has no coastline)": True,
},
{
"name":"is the country in africa",
 "is the country in africa":True,
},
{ 
"name":"is the country in oceania",
"is the country in oceania":True, 
},
{ 
"name":"is the country in europe",
 "is the country in europe":True,
},
{ 
"name":"is the country in north america",
"is the country in north america":True, 
},
{
"name":"is the country in south america",
 "is the country in south america":True,
},
{ 
"name":"is the country in asia",
"is the country in asia":True, 
},
{
"name":"is the country in the northern hemesphere",
 "is the country in the northern hemesphere":True, 
},
{
"name":"is the country in the southern hemesphere",
 "is the country in the southern hemesphere":True,
},]
        

            
      

    
                      
    
def thequestion():
    global asked
    global questions
    plain_string_questions = [q["name"] for q in questions]
    asked = r.choice(plain_string_questions)
    questions = [question for question in questions if question["name"] != asked]
    print(asked)




        
temp=0

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    asking_question = False
   
    #landlocked
    #bigger than "country" by size
    #smaller than "country" by size
    #smaller than "country" by population
    #bigger than "country" by population
    #in "continent"
    #in "hemesphere"
    #higer gdp than "country"
    #lower gdp than "country""
    global temp
    if message.content==("stop"):
        temp=0
    if message.content==("!country"):
        global original_length
        global new_length
        global countries
        
        
        global botcountry
        global mode
        temp=1
        await message.channel.send('Guess the country game has now started. You think of a country and i will try to guess it type yes or no to the questions. Type Start to get started')

    if message.content==("start"):
        if temp==1:
            await message.channel.send('Now you will chose if i should guess your country or if you should guess my country. Type 1 and i will be guessing Type 2 and you will be guessing.')        
            temp=2
    if message.content==("1"):
            
        if temp==2: 
            await message.channel.send('Alright i will guess the country. Now you have to think of a country and ill be asking questions about it. I will now go ahead and ask the first question')  
            mode=1 
            
            temp=3
            
            thequestion()
            print (asked)
            await message.channel.send(asked)
            global countries
            #is the country landlocked (it has no coastline)", "is the country in africa", "is the country in oceania",
            #  "is the country in europe", "is the country in north america", "is the country in south america", 
            # "is the country in asia", "is the country in the northern hemesphere", "is the country in the southern hemesphere
            temp=("1question")
    if message.content==("yes"):
        if temp == "1question" and not asking_question:
            #asking_question = True
            if asked=="is the country in europe":
                print("Before Filtering:")
                for country in countries:
                    print(country["name"])

                print("NEXT")
                original_length = len(countries)
                countries = [country for country in countries if country["ineurope"] == True]
                new_length = len(countries)
                if new_length==0:
                    await message.channel.send("Is your country one of these?")
                    #for country in countries:
                    await message.channel.send(country["name"])

                    temp=0
                print("After Filtering (Countries in Europe):")
                for country in countries:
                    print(country["name"])
                await message.channel.send("Okay 👍")
                time.sleep(2)
                thequestion()
            
                print (asked)
                await message.channel.send(asked)

    elif message.content==("no"):
        if temp == "1question" and not asking_question:
            #asking_question = True
            if asked=="is the country in europe":
                print("Before Filtering:")
                for country in countries:
                    print(country["name"])

                print("NEXT")
                original_length = len(countries)
       
                countries = [country for country in countries if country["ineurope"] == False]
                new_length = len(countries)
                if new_length==0:
                    await message.channel.send("Is your country one of these?")
                    for country in countries:
                        await message.channel.send(country["name"])
                    temp=0
             
                for country in countries:
                    print(country["name"])
                await message.channel.send("Okay 👍")
                time.sleep(2)
                thequestion()
            
                print (asked)
                await message.channel.send(asked)           

                #asked= r.choice(questions)
                #await message.channel.send(asked)
    if message.content==("yes"):
        if temp == "1question" and not asking_question:
            #asking_question = True
            if asked=="is the country in north america":
                
                print("Before Filtering:")
                for country in countries:
                    print(country["name"])

                print("NEXT")
                original_length = len(countries)
                countries = [country for country in countries if country["innorthamerica"] == True]
                new_length = len(countries)
                if new_length==0:
                    await message.channel.send("Is your country one of these?")
                    for country in countries:
                        await message.channel.send(country["name"])
                    temp=0
                print("After Filtering (Countries in Europe):")
                for country in countries:
                    print(country["name"])
                await message.channel.send("Okay 👍")
                time.sleep(2)
                thequestion()
            
                print (asked)
                await message.channel.send(asked)
    elif message.content==("no"):
        if temp == "1question" and not asking_question:
            #asking_question = True
            if asked=="is the country in north america":
                print("Before Filtering:")
                for country in countries:
                    print(country["name"])

                print("NEXT")
                original_length = len(countries)
                countries = [country for country in countries if country["innorthamerica"] == False]
                new_length = len(countries)
                if new_length==0:
                    await message.channel.send("Is your country one of these?")
                    for country in countries:
                        await message.channel.send(country["name"])
                    temp=0
                print("After Filtering (Countries in Europe):")
                for country in countries:
                    print(country["name"])
                            

                #asked= r.choice(questions)
                #await message.channel.send(asked)
                await message.channel.send("Okay 👍")
                time.sleep(2)
                thequestion()
            
                print (asked)
                await message.channel.send(asked)
    if message.content==("yes"):
        if temp == "1question" and not asking_question:
            #asking_question = True
            if asked=="is the country in south america":
                
                print("Before Filtering:")
                for country in countries:
                    print(country["name"])

                print("NEXT")
                original_length = len(countries)
                countries = [country for country in countries if country["insouthamerica"] == True]
                new_length = len(countries)
                if new_length==0:
                    await message.channel.send("Is your country one of these?")
                    for country in countries:
                        await message.channel.send(country["name"])
                    temp=0
                print("After Filtering (Countries in Europe):")
                for country in countries:
                    print(country["name"])
                await message.channel.send("Okay 👍")
                time.sleep(2)
                thequestion()
            
                print (asked)
                await message.channel.send(asked)

    elif message.content==("no"):
        if temp == "1question" and not asking_question:
            #asking_question = True
            if asked=="is the country in south america":
                print("Before Filtering:")
                for country in countries:
                    print(country["name"])

                print("NEXT")
                original_length = len(countries)
                countries = [country for country in countries if country["insouthamerica"] == False]
                new_length = len(countries)
                if new_length==0:
                    await message.channel.send("Is your country one of these?")
                    for country in countries:
                        await message.channel.send(country["name"])
                    temp=0
                print("After Filtering (Countries in Europe):")
                for country in countries:
                    print(country["name"])
                            

                #asked= r.choice(questions)
                #await message.channel.send(asked)
                await message.channel.send("Okay 👍")
                time.sleep(2)
                thequestion()
            
                print (asked)
                await message.channel.send(asked)
    if message.content==("yes"):
        if temp == "1question" and not asking_question:
            #asking_question = True
            if asked=="is the country in asia":
                
                print("Before Filtering:")
                for country in countries:
                    print(country["name"])

                print("NEXT")
                original_length = len(countries)
                countries = [country for country in countries if country["inasia"] == True]
                new_length = len(countries)
                if new_length==0:
                    await message.channel.send("Is your country one of these?")
                    for country in countries:
                        await message.channel.send(country["name"])
                    temp=0
                print("After Filtering (Countries in Europe):")
                for country in countries:
                    print(country["name"])
                await message.channel.send("Okay 👍")
                time.sleep(2)
                thequestion()
            
                print (asked)
                await message.channel.send(asked)

    elif message.content==("no"):
        if temp == "1question" and not asking_question:
            #asking_question = True
            if asked=="is the country in asia":
                print("Before Filtering:")
                for country in countries:
                    print(country["name"])

                print("NEXT")
                original_length = len(countries)
                countries = [country for country in countries if country["inasia"] == False]
                new_length = len(countries)
                if new_length==0:
                    await message.channel.send("Is your country one of these?")
                    for country in countries:
                        await message.channel.send(country["name"])
                    temp=0
                print("After Filtering (Countries in Europe):")
                for country in countries:
                    print(country["name"])
                            

                #asked= r.choice(questions)
                #await message.channel.send(asked)
                await message.channel.send("Okay 👍")
                time.sleep(2)
                thequestion()
            
                print (asked)
                await message.channel.send(asked)
    if message.content==("yes"):
        if temp == "1question" and not asking_question:
            #asking_question = True
            if asked=="is the country in oceania":
                
                print("Before Filtering:")
                for country in countries:
                    print(country["name"])

                print("NEXT")
                original_length = len(countries)
                countries = [country for country in countries if country["inoceania"] == True]
                new_length = len(countries)
                if new_length==0:
                    await message.channel.send("Is your country one of these?")
                    for country in countries:
                        await message.channel.send(country["name"])
                    temp=0
                print("After Filtering (Countries in Europe):")
                for country in countries:
                    print(country["name"])
                await message.channel.send("Okay 👍")
                time.sleep(2)
                thequestion()
            
                print (asked)
                await message.channel.send(asked)

    elif message.content==("no"):
        if temp == "1question" and not asking_question:
            #asking_question = True
            if asked=="is the country in oceania":
                print("Before Filtering:")
                for country in countries:
                    print(country["name"])

                print("NEXT")
                original_length = len(countries)
                countries = [country for country in countries if country["inoceania"] == False]    
                new_length = len(countries)          
                if new_length==0:
                    await message.channel.send("Is your country one of these?")
                    for country in countries:
                        await message.channel.send(country["name"])
                    temp=0
                print("After Filtering (Countries in Europe):")
                for country in countries:
                    print(country["name"])
                            

                #asked= r.choice(questions)
                #await message.channel.send(asked)
                await message.channel.send("Okay 👍")
                time.sleep(2)
                thequestion()
            
                print (asked)
                await message.channel.send(asked)
    if message.content==("yes"):
        if temp == "1question" and not asking_question:
            #asking_question = True
            if asked=="is the country in africa":
                
                print("Before Filtering:")
                for country in countries:
                    print(country["name"])

                print("NEXT")
                original_length = len(countries)
                countries = [country for country in countries if country["inafrica"] == True]
                new_length = len(countries)
                if new_length==0:
                    await message.channel.send("Is your country one of these?")
                    for country in countries:
                        await message.channel.send(country["name"])
                    temp=0
                print("After Filtering (Countries in Europe):")
                for country in countries:
                    print(country["name"])
                await message.channel.send("Okay 👍")
                time.sleep(2)
                thequestion()
            
                print (asked)
                await message.channel.send(asked)

    elif message.content==("no"):
        if temp == "1question" and not asking_question:
            #asking_question = True
            if asked=="is the country in africa":
                print("Before Filtering:")
                for country in countries:
                    print(country["name"])

                print("NEXT")
                original_length = len(countries)
                countries = [country for country in countries if country["inafrica"] == False]
                new_length = len(countries)
                if new_length==0:
                    await message.channel.send("Is your country one of these?")
                    for country in countries:
                        await message.channel.send(country["name"])
                    temp=0
                print("After Filtering (Countries in Europe):")
                for country in countries:
                    print(country["name"])
                            

                #asked= r.choice(questions)
                #await message.channel.send(asked)
                await message.channel.send("Okay 👍")
                time.sleep(2)
                thequestion()
            
                print (asked)
                await message.channel.send(asked)
    if message.content==("yes"):
        if temp == "1question" and not asking_question:
            #asking_question = True
            if asked=="is the country landlocked (it has no coastline)":
                
                print("Before Filtering:")
                for country in countries:
                    print(country["name"])

                print("NEXT")
                original_length = len(countries)
                countries = [country for country in countries if country["landlocked"] == True]
                new_length = len(countries)
                if new_length==0:
                    await message.channel.send("Is your country one of these?")
                    for country in countries:
                        await message.channel.send(country["name"])
                    temp=0
                print("After Filtering (Countries in Europe):")
                for country in countries:
                    print(country["name"])
                await message.channel.send("Okay 👍")
                time.sleep(2)
                thequestion()
            
                print (asked)
                await message.channel.send(asked)

    elif message.content==("no"):
        if temp == "1question" and not asking_question:
            #asking_question = True
            if asked=="is the country landlocked (it has no coastline)":
                print("Before Filtering:")
                for country in countries:
                    print(country["name"])

                print("NEXT")
                original_length = len(countries)
                countries = [country for country in countries if country["landlocked"] == False]
                new_length = len(countries)
                if new_length==0:
                    await message.channel.send("Is your country one of these?")
                    for country in countries:
                        await message.channel.send(country["name"])
                    temp=0
                print("After Filtering (Countries in Europe):")
                for country in countries:
                    print(country["name"])
                            

                #asked= r.choice(questions)
                #await message.channel.send(asked)
                await message.channel.send("Okay 👍")
                time.sleep(2)
                thequestion()
            
                print (asked)
                await message.channel.send(asked)
                
    if message.content==("yes"):
        if temp == "1question" and not asking_question:
            #asking_question = True
            if asked=="is the country in the northern hemesphere":
                
                print("Before Filtering:")
                for country in countries:
                    print(country["name"])

                print("NEXT")
                original_length = len(countries)
                countries = [country for country in countries if country["northernhemesphere"] == True]
                new_length = len(countries)
                if new_length==0:
                    await message.channel.send("Is your country one of these?")
                    for country in countries:
                        await message.channel.send(country["name"])
                    temp=0
                print("After Filtering (Countries in Europe):")
                for country in countries:
                    print(country["name"])
                await message.channel.send("Okay 👍")
                time.sleep(2)
                thequestion()
            
                print (asked)
                await message.channel.send(asked)

    elif message.content==("no"):
        if temp == "1question" and not asking_question:
            #asking_question = True
            if asked=="is the country in the northern hemesphere":
                print("Before Filtering:")
                for country in countries:
                    print(country["name"])

                print("NEXT")
                original_length = len(countries)
                countries = [country for country in countries if country["northernhemesphere"] == False]
                new_length = len(countries)
                if new_length==0:
                    await message.channel.send("Is your country one of these?")
                    for country in countries:
                        await message.channel.send(country["name"])
                    temp=0
                print("After Filtering (Countries in Europe):")
                for country in countries:
                    print(country["name"])
                            

                #asked= r.choice(questions)
                #await message.channel.send(asked)
                await message.channel.send("Okay 👍")
                time.sleep(2)
                thequestion()
            
                print (asked)
                await message.channel.send(asked)
    if message.content==("yes"):
        if temp == "1question" and not asking_question:
            #asking_question = True
            if asked=="is the country in the southern hemesphere":
                
                print("Before Filtering:")
                for country in countries:
                    print(country["name"])

                print("NEXT")
                original_length = len(countries)
                countries = [country for country in countries if country["southernhemesphere"] == True]
                new_length = len(countries)
                if new_length==0:
                    await message.channel.send("Is your country one of these?")
                    for country in countries:
                        await message.channel.send(country["name"])
                    temp=0
                print("After Filtering (Countries in Europe):")
                for country in countries:
                    print(country["name"])
                await message.channel.send("Okay 👍")
                time.sleep(2)
                thequestion()
            
                print (asked)
                await message.channel.send(asked)

    elif message.content==("no"):
        if temp == "1question" and not asking_question:
            #asking_question = True
            if asked=="is the country in the southern hemesphere":
                print("Before Filtering:")
                for country in countries:
                    print(country["name"])

                print("NEXT")
                original_length = len(countries)
                countries = [country for country in countries if country["southernhemesphere"] == False]
                new_length = len(countries)
                if new_length==0:
                    await message.channel.send("Is your country one of these?")
                    for country in countries:
                        await message.channel.send(country["name"])
                    temp=0
                print("After Filtering (Countries in Europe):")
                for country in countries:
                    print(country["name"])
                            

                #asked= r.choice(questions)
                #await message.channel.send(asked)
                await message.channel.send("Okay 👍")
                time.sleep(2)
                thequestion()
            
                print (asked)
                await message.channel.send(asked)
    #asking_question = True
    if message.content==("2"):
        mode=2
        if temp==2:
            await message.channel.send('Sure you will guess the country. I will now think of a country and you will have to guess it by typing a number reprecenting the question you want to ask.')
            temp=3
            botcountry= r.choice(countries)
            print("bot chose "+botcountry)
            await message.channel.send("."+"\n"+"The questions you can ask are: landlocked, population, size, inafrica, ineroupe, innorthamerica, insouthamerica, inasia, inoceania, innorthernhemesphere, insouthernhemesphere")
    if mode==2:
        if message.content==("landlocked"):
            ()

client.run('MTAzNTg1MDY2NDgwNDM3MjUxMA.Gta8Wm.n3pudYLaFTGWd6c_d5vXzlcN363pKcCoz97zyY')
    


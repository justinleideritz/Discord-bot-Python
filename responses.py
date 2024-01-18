import random

def get_response(message: str) -> str:
    #count = 26
    p_message = message.lower()
#coinflip
    if p_message == '!coinflip':
        random_number = random.randint(0, 10)
        if random_number <= 5:
            return 'heads'
        else: 
            return 'tails'

#diceroll
    if p_message == '!roll':
        return str(random.randint(1, 6))

#idk
    #if p_message == "nigger":
        count += 1
        print("+1 to the count")
    
    #if p_message == '!niggercount':
        return f'Nigger has been said for {count} times'
    
    if p_message == 'fuck you':
        return 'fuck you too'
    
    if p_message == '!rob':
        return 'Rob, a rugged outdoorsman with a deep affinity for hunting kids, grew up in a small rural town surrounded by vast a lot of gay people. Inspired by his father and his father, he developed a passion for the sport at a young age. As he matured, Rob honed his skills as a child predator and became an ardent advocate for responsible hunting practices. With each hunting expedition, he embraced the solitude and connection with nature, instilling in him a profound appreciation for the delicate balance of ecosystems. Rob\'s love for the kids and his commitment to conservation remain unwavering, as he continues to seek both adventure and harmony in the great outdoors.'
    
    if p_message == '!space':
        return 'mY CoUnTRY iS SO mUch BetTer ThAn YoUR CoUntRy AnD i KnOw EverYthInG AbOut WaR \n https://tenor.com/view/spongebob-cartoon-chicken-funny-dance-gif-14242277'
    
    if p_message == '!bitchnigger':
        return 'https://media.tenor.com/iid9WLcvDA0AAAAd/burger-king-man-on-plane.gif'
    
    if p_message == '!killyourself':
        return 'https://media.discordapp.net/attachments/934662346578743337/1129244257941717053/dMkhpV1.gif'
    
    if p_message == '!commands':
        return '`All the commands: \n !rob \n !space \n !bitchnigger \n !killyourself \n !count \n !roll \n !coinflip`'
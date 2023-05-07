# https://github.com/TT-Tutorials | https://github.com/TT-Tutorials/GANG-Nuker
# Coded / Dev / Owner: ††#1792
# Copyright © GANG-Nuker
#########################################################

import os

# r = Fore.RESET

#########################################################

def Spinner():
	l = ['|', '/', '-', '\\', ' ']
	for i in l+l+l:
		sys.stdout.write(f"""\r {i}""")
		sys.stdout.flush()
		time.sleep(0.1)

global cls
def cls():
 os.system('cls' if os.name=='nt' else 'clear')

def tool():
  os.system('cls' if os.name=='nt' else 'clear')

def clearConsole(): return os.system(
    'cls' if os.name in ('nt', 'dos') else 'clear')

global useragent
def useragent():
    file = open('data/useragent.txt','r')
    useragent = (random.choice(list(file)))
    useragent2 = []
    useragent2.append(useragent)
    useragent1 = []

#########################################################

try:
    with open('data/logins.json') as f:
        config = json.load(f)
except:
    with open('data/logins.json', 'w') as f:
            print(f"\n[{g}#\x1b[95m\x1B[37m] Logging Into GANG-Nuker")
            login = input("[\x1b[95m#\x1b[95m\x1B[37m] Enter A Username: ")
            json.dump({"Login": login}, f, indent=4)
    input(f"\n[\x1b[95m#\x1b[95m\x1B[37m] Successfully Logged in as: [{m}{login}{w}]\n[\x1b[95m>\x1b[95m\x1B[37m] Press ENTER to Continue: ")
    pass
with open('data/logins.json') as f:
    config = json.load(f)
login = config.get('Login')

languages = {
    'da'    : 'Danish, Denmark',
    'de'    : 'German, Germany',
    'en-GB' : 'English, United Kingdom',
    'en-US' : 'English, United States',
    'aud'   : 'English, Austrlia',
    'es-ES' : 'Spanish, Spain',
    'fr'    : 'French, France',
    'hr'    : 'Croatian, Croatia',
    'lt'    : 'Lithuanian, Lithuania',
    'hu'    : 'Hungarian, Hungary',
    'nl'    : 'Dutch, Netherlands',
    'no'    : 'Norwegian, Norway',
    'pl'    : 'Polish, Poland',
    'pt-BR' : 'Portuguese, Brazilian, Brazil',
    'ro'    : 'Romanian, Romania',
    'fi'    : 'Finnish, Finland',
    'sv-SE' : 'Swedish, Sweden',
    'vi'    : 'Vietnamese, Vietnam',
    'tr'    : 'Turkish, Turkey',
    'cs'    : 'Czech, Czechia, Czech Republic',
    'el'    : 'Greek, Greece',
    'bg'    : 'Bulgarian, Bulgaria',
    'ru'    : 'Russian, Russia',
    'uk'    : 'Ukranian, Ukraine',
    'th'    : 'Thai, Thailand',
    'zh-CN' : 'Chinese, China',
    'ja'    : 'Japanese',
    'zh-TW' : 'Chinese, Taiwan',
    'ko'    : 'Korean, Korea'
}

regions = [
    'brazil',
    'hongkong',
    'india',
    'japan',
    'rotterdam',
    'russia',
    'singapore',
    'southafrica',
    'sydney',
    'us-central',
    'us-east',
    'us-south',
    'us-west'
]


def spammer():
    global threads
    setTitle(f"")
    asc = asyncio.get_event_loop()
    tokens = open('tokens.txt', 'r').read().splitlines()
    clear = lambda: os.system('cls')
    clear()

    colorama.init()
    Write.Print(f'{login}\n', Colors.blue_to_purple,  interval=0.000)
    print('')
    print('')
    Write.Print("                                      /$$$$$$   /$$$$$$  /$$   /$$  /$$$$$$\n", Colors.purple_to_blue, interval=0.000)
    Write.Print("                                     /$$__  $$ /$$__  $$| $$$ | $$ /$$__  $$\n", Colors.purple_to_blue, interval=0.000)
    Write.Print("                                    | $$  \__/| $$  \ $$| $$$$| $$| $$  \__/\n", Colors.purple_to_blue, interval=0.000)
    Write.Print("                                    | $$ /$$$$| $$$$$$$$| $$ $$ $$| $$ /$$$$\n", Colors.purple_to_blue, interval=0.000)
    Write.Print("                                    | $$|_  $$| $$__  $$| $$  $$$$| $$|_  $$\n", Colors.purple_to_blue, interval=0.000)
    Write.Print(f' > [v{THIS_VERSION}]                         | $$  \ $$| $$  | $$| $$\  $$$| $$  \ $$\n', Colors.purple_to_blue, interval=0.000)
    Write.Print(f' > [gangnuker.org]                  |  $$$$$$/| $$  | $$| $$ \  $$|  $$$$$$/\n', Colors.purple_to_blue, interval=0.000)
    Write.Print(" > [Github.com/TT-Tutorials]         \______/ |__/  |__/|__/  \__/ \______/ \n", Colors.purple_to_blue, interval=0.000)
    Write.Print("════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════", Colors.purple_to_blue, interval=0.000)
    print(f'''{m}'''.replace('$', f'{m}${w}') + f'''
{m}[{w}1{Fore.RESET}{m}]{Fore.RESET} Server Joiner   {b}|{Fore.RESET}{m}[{w}9{Fore.RESET}{m}]{Fore.RESET}  Channel Spammer   {b}|{Fore.RESET}{m}[{w}17{Fore.RESET}{m}]{Fore.RESET} Patch Notes{Fore.RESET}         {b}|{Fore.RESET}{m}[{w}25{Fore.RESET}{m}]{Fore.RESET} Token Generator{Fore.RESET}
{m}[{w}2{Fore.RESET}{m}]{Fore.RESET} Server Leaver   {b}|{Fore.RESET}{m}[{w}10{Fore.RESET}{m}]{Fore.RESET} DM Spammer        {b}|{Fore.RESET}{m}[{w}18{Fore.RESET}{m}]{Fore.RESET} About/Activity{Fore.RESET}      {b}|{Fore.RESET}{m}[{w}26{Fore.RESET}{m}]{Fore.RESET} Nitro Generator{Fore.RESET}
{m}[{w}3{Fore.RESET}{m}]{Fore.RESET} Token Checker   {b}|{Fore.RESET}{m}[{w}11{Fore.RESET}{m}]{Fore.RESET} Friend Spammer    {b}|{Fore.RESET}{m}[{w}19{Fore.RESET}{m}]{Fore.RESET} Server Lookup{Fore.RESET}       {b}|{Fore.RESET}{m}[{w}27{Fore.RESET}{m}]{Fore.RESET} QR Token Grabber{Fore.RESET}
{m}[{w}4{Fore.RESET}{m}]{Fore.RESET} Token Onliner   {b}|{Fore.RESET}{m}[{w}12{Fore.RESET}{m}]{Fore.RESET} HypeSquad Joiner  {b}|{Fore.RESET}{m}[{w}20{Fore.RESET}{m}]{Fore.RESET} Token Infomation{Fore.RESET}    {b}|{Fore.RESET}{m}[{w}28{Fore.RESET}{m}]{Fore.RESET} Member ID Scraper{Fore.RESET}
{m}[{w}5{Fore.RESET}{m}]{Fore.RESET} Token Grabber   {b}|{Fore.RESET}{m}[{w}13{Fore.RESET}{m}]{Fore.RESET} Reaction Spammer  {b}|{Fore.RESET}{m}[{w}21{Fore.RESET}{m}]{Fore.RESET} Status Changer{Fore.RESET}      {b}|{Fore.RESET}{m}[{w}29{Fore.RESET}{m}]{Fore.RESET} PFP Changer{Fore.RESET}
{m}[{w}6{Fore.RESET}{m}]{Fore.RESET} Server MassDM   {b}|{Fore.RESET}{m}[{w}14{Fore.RESET}{m}]{Fore.RESET} NickName Changer  {b}|{Fore.RESET}{m}[{w}22{Fore.RESET}{m}]{Fore.RESET} Group Spammer{Fore.RESET}       {b}|{Fore.RESET}{m}[{w}30{Fore.RESET}{m}]{Fore.RESET} About{Fore.RESET}
{m}[{w}7{Fore.RESET}{m}]{Fore.RESET} Account Nuker   {b}|{Fore.RESET}{m}[{w}15{Fore.RESET}{m}]{Fore.RESET} Webhook Spammer   {b}|{Fore.RESET}{m}[{w}23{Fore.RESET}{m}]{Fore.RESET} Auto Login{Fore.RESET}          {b}|{Fore.RESET}{m}[{w}31{Fore.RESET}{m}]{Fore.RESET}{lr} THREADS{Fore.RESET}
{m}[{w}8{Fore.RESET}{m}]{Fore.RESET} Server Nuker    {b}|{Fore.RESET}{m}[{w}16{Fore.RESET}{m}]{Fore.RESET} VC Spammer        {b}|{Fore.RESET}{m}[{w}24{Fore.RESET}{m}]{Fore.RESET} DM Deleter{Fore.RESET}          {b}|{Fore.RESET}{m}[{w}32{Fore.RESET}{m}]{Fore.RESET}{lr} EXIT{Fore.RESET}''')
    Write.Print("════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════", Colors.blue_to_purple, interval=0.000)
    choice = input(f'{m}[{w}>{m}]{w} Choice?: ')
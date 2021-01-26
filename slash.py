import requests
url = "https://discord.com/api/v8/applications/769606923091181569/commands"
def get():
    headers = {
    "Authorization": "Bot NzY5NjA2OTIzMDkxMTgxNTY5.X5ReTQ.DufMbEBus51oThS3F_l_6GE3eX8"
    }
    r = requests.get(url, headers=headers)
    print(r.json())
def create(name, description, subcommand_name, subcommand_description, guild, guild_id, subcommand_name1, subcommand_name2, subcommand_name3 ):
    
    if guild == "yes":
        guild_completer = "/guilds/" + guild_id
        print(guild_completer)
    else:
        guild_id = "" 
        guild_completer = " "
    url = f"https://discord.com/api/v8/applications/769606923091181569{guild_completer}/commands"
    print(url)
    json = {
        "name": f"{name}",
        "description": f"{description}",
        "options": [
            {
                "name": f"{subcommand_name}",
                "description": f"{subcommand_description}",
                "type": 3,
                "required": False,
                "choices": [
                    {
                        "name": f"{subcommand_name1}",
                        "value": "animal_dog"
                    },
                    {
                        "name": f"{subcommand_name2}",
                        "value": f"{subcommand_name2}"
                    },
                    {
                        "name": f"{subcommand_name3}",
                        "value": f"{subcommand_name3}"
                    }
                ]
            },
        ]
    }

    # For authorization, you can use either your bot token 
    headers = {
        "Authorization": "Bot NzY5NjA2OTIzMDkxMTgxNTY5.X5ReTQ.DufMbEBus51oThS3F_l_6GE3eX8"
    }
    r = requests.post(url, headers=headers, json=json)
    print(r.json())

def init():
    name = input("Enter name: ") 
    description = input("Enter description: ") 
    subcommand_name = input("Enter subcommand_name: ") 
    subcommand_description = input("Enter subcommand_description: ") 
    subcommand_name1 = input("Enter subcommand_name1: ") 
    subcommand_name2 = input("Enter subcommand_name2: ") 
    subcommand_name3 = input("Enter subcommand_name3: ") 
    guild = input("Guild? (yes/n): ") 
    guild_id = input("Enter guild_id: ") 
    create(name, description, subcommand_name, subcommand_description, guild, guild_id, subcommand_name1, subcommand_name2, subcommand_name3)
init()
get()
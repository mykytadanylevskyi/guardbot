import json
from re import L
from typing import Any

JSON_PATH = 'config.json'

def get_cities() -> dict[str, int]:
    with open(JSON_PATH, 'r', encoding = 'utf-8') as f:
        config: dict = json.load(f)
        return config["cities"]
        
def add_city(city: str, chat_id: int):
    with open(JSON_PATH, 'r', encoding = 'utf-8') as f:
        config = json.load(f)
    
    config["cities"][city] = chat_id
        
    with open(JSON_PATH, 'w', encoding = 'utf-8') as f:
        json.dump(config, f, indent = 4, ensure_ascii=True)

def remove_city(city: str):
    with open(JSON_PATH, 'r', encoding = 'utf-8') as f:
        config = json.load(f)

    del config["cities"][city]
        
    with open(JSON_PATH, 'w', encoding = 'utf-8') as f:
        json.dump(config, f, indent = 4, ensure_ascii=True)

def add_new_alarm(id: int, max: int, customer_id: int):
    with open(JSON_PATH, 'r', encoding = 'utf-8') as f:
        config = json.load(f)
    
    if not config["alarms"].get(id):
        config["alarms"][id] = {
            "guards": [],
            "max": max,
            "customer": customer_id
        }
        
        with open(JSON_PATH, 'w', encoding = 'utf-8') as f:
            json.dump(config, f, indent = 4, ensure_ascii=True)

def add_guard_to_alarm(id: int, guard_id: int):
    with open(JSON_PATH, 'r', encoding = 'utf-8') as f:
        config = json.load(f)
    
    alarm: list = config["alarms"].get(str(id))
    if alarm:
        alarm["guards"].append(guard_id)
        config["alarms"][str(id)]["guards"] = alarm["guards"]
        
        with open(JSON_PATH, 'w', encoding = 'utf-8') as f:
            json.dump(config, f, indent = 4, ensure_ascii=True)

def get_cont_of_active_guards(alarm_id: int):
    with open(JSON_PATH, 'r', encoding = 'utf-8') as f:
        config = json.load(f)

    return list(config["accepted_alarms"].values()).count(str(alarm_id))

def remove_alarm(id: int):
    with open(JSON_PATH, 'r', encoding = 'utf-8') as f:
        config = json.load(f)
    
    alarm: list = config["alarms"].get(str(id))
    if alarm:
        del config["alarms"][str(id)]

        with open(JSON_PATH, 'w', encoding = 'utf-8') as f:
            json.dump(config, f, indent = 4, ensure_ascii = True)


def get_alarm_guards(id: int) -> list[int] | None:
    with open(JSON_PATH, 'r', encoding = 'utf-8') as f:
        config = json.load(f)
    
    alarm: list = config["alarms"].get(str(id))
    if alarm:
        return alarm["guards"]
    return None

def get_max_alarm_guards(id: int) -> int | None:
    with open(JSON_PATH, 'r', encoding = 'utf-8') as f:
        config = json.load(f)
    
    alarm: list = config["alarms"].get(str(id))
    if alarm:
        return alarm["max"]
    return None

def get_alarm_customer(id: int) -> str | None:
    with open(JSON_PATH, 'r', encoding = 'utf-8') as f:
        config = json.load(f)
    
    alarm: list = config["alarms"].get(str(id))
    if alarm:
        return alarm["customer"]
    return None


def get_alarm_by_customer_id(user_id: int) -> str | None:
    with open(JSON_PATH, 'r', encoding = 'utf-8') as f:
        config = json.load(f)
    
    alarms: dict[str, Any] = config["alarms"]
    user = list(filter(lambda alarm: int(alarm[1]['customer']) == user_id, alarms.items()))
    if user:
        return user[0][0]

        
def add_to_accepted_alarms(guard_id: int, alarm_id: int):
    with open(JSON_PATH, 'r', encoding = 'utf-8') as f:
        config = json.load(f)
    
    config["accepted_alarms"][str(guard_id)] = str(alarm_id)
    
    with open(JSON_PATH, 'w', encoding = 'utf-8') as f:
        json.dump(config, f, indent = 4, ensure_ascii=True)


def get_from_accepted_alarms(guard_id: int) -> str | None:
    with open(JSON_PATH, 'r', encoding = 'utf-8') as f:
        config = json.load(f)

    accepted_alarm: str = config["accepted_alarms"].get(str(guard_id))
    return accepted_alarm
  

def remove_from_accepted_alarms(guard_id: int):
    with open(JSON_PATH, 'r', encoding = 'utf-8') as f:
        config = json.load(f)
    
    if config["accepted_alarms"].get(str(guard_id)):
        del config["accepted_alarms"][str(guard_id)]

    with open(JSON_PATH, 'w', encoding = 'utf-8') as f:
        json.dump(config, f, indent = 4, ensure_ascii=True)




import uuid
from models import QuestItem
import utils
import config

def get_quest_json(quest_id: uuid.UUID, item: QuestItem, default_name: str, default_desc: str) -> dict:
    high, low = utils.uuid_to_high_low(quest_id)

    reward_item = {
        "Count:3": 1,
        "Damage:2": item.reward_meta,
        "OreDict:8": "",
        "id:8": item.reward_id
    }

    if item.reward_nbt:
        reward_item["tag:10"] = utils.parse_nbt_to_bq_tags(item.reward_nbt)

    return {
        "preRequisites:9": {},
        "properties:10": {
            "betterquesting:10": {
                "autoClaim:1": 0,
                "completion_animation:8": "default",
                "completion_particle:8": "default",
                "confetti_icon:10": {
                    "Count:3": 0,
                    "Damage:2": 0,
                    "OreDict:8": "",
                    "id:8": "minecraft:stick"
                },
                "countAsQuest:1": 1,
                "desc:8": default_desc,
                "globalShare:1": 0,
                "icon:10": reward_item.copy(),
                "isMain:1": 0,
                "isSilent:1": 0,
                "lockedProgress:1": 0,
                "name:8": default_name,
                "notification_duration:5": -1.0,
                "notification_effect:3": -1,
                "notification_fade_in:5": -1.0,
                "notification_fade_out:5": -1.0,
                "notification_icon_offset_y:3": -2147483648,
                "notification_icon_scale:5": -1.0,
                "notification_pos_x:3": -2147483648,
                "notification_pos_y:3": -2147483648,
                "notification_show_icon:8": "default",
                "notification_style:8": "default",
                "notification_subtitle:8": "",
                "notification_subtitle_scale:5": -1.0,
                "notification_title:8": "",
                "notification_title_scale:5": -1.0,
                "particle_count:3": -1,
                "questLogic:8": "AND",
                "repeatTime:3": 0,
                "repeat_relative:1": 1,
                "simultaneous:1": 0,
                "snd_complete:8": "random.levelup",
                "snd_update:8": "random.levelup",
                "taskLogic:8": "AND",
                "visibility:8": "NORMAL"
            }
        },
        "questIDHigh:4": high,
        "questIDLow:4": low,
        "rewards:9": {
            "0:10": {
                "ignoreDisabled:1": 0,
                "index:3": 0,
                "rewardID:8": "bq_standard:item",
                "rewards:9": {
                    "0:10": reward_item
                }
            }
        },
        "tasks:9": {
            "0:10": {
                "autoConsume:1": 0,
                "consume:1": 1,
                "groupDetect:1": 0,
                "ignoreNBT:1": 1,
                "index:3": 0,
                "partialMatch:1": 1,
                "requireOnlyOneItem:1": 0,
                "requiredItems:9": {
                    "0:10": {
                        "Count:3": item.cost_amount,
                        "Damage:2": config.CURRENCY_META,
                        "OreDict:8": "",
                        "id:8": config.CURRENCY_ID
                    }
                },
                "taskID:8": "bq_standard:retrieval"
            }
        }
    }

def get_questline_entry_json(quest_id: uuid.UUID, x: int, y: int) -> dict:
    high, low = utils.uuid_to_high_low(quest_id)
    return {
        "questIDHigh:4": high,
        "questIDLow:4": low,
        "sizeX:3": config.GRID_SIZE,
        "sizeY:3": config.GRID_SIZE,
        "x:3": x,
        "y:3": y
    }
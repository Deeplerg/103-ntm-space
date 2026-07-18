import uuid
import base64
import struct
from config import NAMESPACE_BQ

def generate_deterministic_uuid(internal_name: str) -> uuid.UUID:
    """Generates a UUIDv5 based on our fixed namespace and the item's internal name."""
    return uuid.uuid5(NAMESPACE_BQ, internal_name)

def uuid_to_high_low(u: uuid.UUID) -> tuple[int, int]:
    """Converts a 16-byte UUID into two signed 64-bit integers (Java UUID format)."""
    high, low = struct.unpack(">qq", u.bytes)
    return high, low

def uuid_to_b64(u: uuid.UUID) -> str:
    """Converts a UUID to a URL-safe Base64 string, preserving padding (==) exactly as BQ expects."""
    return base64.urlsafe_b64encode(u.bytes).decode('utf-8')

def snake_to_camel(snake_str: str) -> str:
    """Converts 'chlorine_pinwheel' to 'ChlorinePinwheel'."""
    components = snake_str.split('_')
    return "".join(x.title() for x in components)

def parse_nbt_to_bq_tags(nbt_dict: dict) -> dict:
    """Recursively converts a standard dict into BQ's type-tagged dict format."""
    res = {}
    for k, v in nbt_dict.items():
        if isinstance(v, str):
            res[f"{k}:8"] = v
        elif isinstance(v, bool):
            res[f"{k}:1"] = 1 if v else 0
        elif isinstance(v, int):
            res[f"{k}:3"] = v
        elif isinstance(v, float):
            res[f"{k}:5"] = v
        elif isinstance(v, dict):
            res[f"{k}:10"] = parse_nbt_to_bq_tags(v)
    return res
import uuid

# BetterQuesting QuestLine folder name
QUESTLINE_DIR_NAME = "AdminShop-AoTW_N_4T8esuIXYcFrQDw=="

# Currency details
CURRENCY_ID = "universalcoins:item.iron_coin"
CURRENCY_META = 0

BASE_COINS_PER_HOUR = 10.0
ADMIN_PREMIUM = 2.5
GLOBAL_REWARD_MODIFIER = 2.0
EFFICIENCY_MODIFIER = 2.0

# Layout details
GRID_SIZE = 24
CENTER_EMPTY_RADIUS = 5  # Skips this many grid units from the center

# Deterministic UUID Namespace.
# WARNING: Do not change this after your first real generation, or all quest UUIDs will change!
NAMESPACE_BQ = uuid.UUID("2efdf9de-18c4-4bf2-8de3-b44f358583c5")

# Languages to process. The script will look for `data/lang_{code}.json`
LANGUAGES = ["ru_ru", "en_us"]
DEFAULT_LANGUAGE = "en_us"
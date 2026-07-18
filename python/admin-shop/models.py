from pydantic import BaseModel
from typing import Dict, Any, Optional
import config

class QuestItem(BaseModel):
    internal_name: str
    reward_id: str
    reward_meta: int = 0
    reward_nbt: Optional[Dict[str, Any]] = None
    hours_to_acquire: float

    @property
    def cost_amount(self) -> int:
        """Calculates the final cost based on the economy modifiers."""
        if config.GLOBAL_REWARD_MODIFIER <= 0:
            raise ValueError("GLOBAL_REWARD_MODIFIER must be strictly positive (> 0)")

        raw_cost = (self.hours_to_acquire
                    * config.BASE_COINS_PER_HOUR
                    * config.EFFICIENCY_MODIFIER
                    * config.ADMIN_PREMIUM
                    * config.GLOBAL_REWARD_MODIFIER)

        # Round to the nearest whole coin, ensuring a minimum cost of 1
        return max(1, int(round(raw_cost)))

class LangEntry(BaseModel):
    name: str
    desc: str

LangFile = Dict[str, LangEntry]
from enum import Enum


class CategoryName(str, Enum):
    GAMING = "Gaming"
    TECH = "Tech"
    HEALTH = "Health"
    NUTRITION = "Nutrition"
    FASHION = "Fashion"
    FINANCE = "Finance"


class PayoutType(str, Enum):
    CPA = "cpa"
    FIXED = "fixed"
    CPA_FIXED = "cpa_fixed"

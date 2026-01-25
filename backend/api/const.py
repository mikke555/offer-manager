offer_create_examples = {
    "example1": {
        "summary": "CPA crypto exchange sign-up",
        "value": {
            "title": "CoinWave Exchange Sign-Up",
            "description": "Register and complete KYC on CoinWave crypto exchange",
            "categories": ["Finance", "Tech"],
            "payout": {
                "type": "cpa",
                "cpa_amount": 25,
                "country_overrides": [
                    {"country_code": "DE", "cpa_amount": 35},
                    {"country_code": "US", "cpa_amount": 30},
                ],
            },
        },
    },
    "example2": {
        "summary": "Fixed payout e-commerce promotion",
        "value": {
            "title": "UrbanStyle Fashion Store",
            "description": "Promote seasonal fashion collections and exclusive discounts",
            "categories": ["Fashion"],
            "payout": {
                "type": "fixed",
                "fixed_amount": 40,
                "country_overrides": [],
            },
        },
    },
    "example3": {
        "summary": "CPA mobile gaming install offer",
        "value": {
            "title": "Dragon Realm Mobile RPG",
            "description": "Install and complete tutorial in a fantasy mobile RPG",
            "categories": ["Gaming"],
            "payout": {
                "type": "cpa",
                "cpa_amount": 15,
                "country_overrides": [
                    {"country_code": "DE", "cpa_amount": 20},
                    {"country_code": "US", "cpa_amount": 18},
                ],
            },
        },
    },
    "example4": {
        "summary": "CPA+Fixed fitness subscription offer",
        "value": {
            "title": "FitLife Nutrition & Fitness App",
            "description": "Sign up and start a premium fitness and nutrition plan",
            "categories": ["Health", "Nutrition"],
            "payout": {
                "type": "cpa_fixed",
                "cpa_amount": 12,
                "fixed_amount": 30,
                "country_overrides": [
                    {"country_code": "GB", "cpa_amount": 15},
                ],
            },
        },
    },
    "example5": {
        "summary": "Fixed SaaS product promotion",
        "value": {
            "title": "AI Resume Builder Pro",
            "description": "Promote an AI-powered resume and cover letter builder",
            "categories": ["Tech", "Finance"],
            "payout": {
                "type": "fixed",
                "fixed_amount": 50,
                "country_overrides": [],
            },
        },
    },
    "example6": {
        "summary": "CPA budgeting app sign-up",
        "value": {
            "title": "Smart Budget Tracker",
            "description": "Register and connect a bank account to track expenses",
            "categories": ["Finance", "Tech"],
            "payout": {
                "type": "cpa",
                "cpa_amount": 10,
                "country_overrides": [
                    {"country_code": "SE", "cpa_amount": 14},
                    {"country_code": "NO", "cpa_amount": 13},
                ],
            },
        },
    },
}

offer_patch_examples = {
    "example1": {
        "summary": "Update title",
        "value": {
            "title": "Title updated",
        },
    },
    "example2": {
        "summary": "Update description",
        "value": {
            "description": "Description updated",
        },
    },
    "example3": {
        "summary": "Update categories",
        "value": {
            "categories": ["Gaming", "Tech"],
        },
    },
    "example4": {
        "summary": "Change payout type to fixed",
        "value": {
            "payout": {
                "type": "fixed",
                "fixed_amount": 75,
                "country_overrides": [],
            },
        },
    },
    "example5": {
        "summary": "Change payout to CPA with country overrides",
        "value": {
            "payout": {
                "type": "cpa",
                "cpa_amount": 20,
                "country_overrides": [
                    {"country_code": "FR", "cpa_amount": 28},
                    {"country_code": "IT", "cpa_amount": 26},
                ],
            },
        },
    },
    "example6": {
        "summary": "Change payout to CPA + Fixed with country overrides",
        "value": {
            "payout": {
                "type": "cpa_fixed",
                "cpa_amount": 10,
                "fixed_amount": 100,
                "country_overrides": [
                    {"country_code": "SE", "cpa_amount": 30},
                    {"country_code": "NO", "cpa_amount": 35},
                ],
            },
        },
    },
}

custom_payout_put_examples = {
    "example1": {
        "summary": "Change custom payout to CPA + Fixed with country overrides",
        "value": {
            "payout": {
                "type": "cpa_fixed",
                "cpa_amount": 10,
                "fixed_amount": 100,
                "country_overrides": [{"country_code": "DE", "cpa_amount": 30.00}],
            }
        },
    },
}

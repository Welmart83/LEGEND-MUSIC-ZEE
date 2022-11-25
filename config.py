#

import os
from dotenv import load_dotenv


load_dotenv()


class Config:
    def __init__(self) -> None:
        self.API_ID: 15638315
        self.API_HASH: 1ab900848c1e5f3529f79f729e88b621
        self.SESSION:  BQC3rIM0sBvLsR1_afGxY26i8OHUmgH3blZBcZaOO-6KlCtdJN_YgkGrgNGY6cSiPFTqlmi3kJpJqp3LsfT0wukQe_0U1c8VBHJiVZUHjB7f2NosuFSGuUZDwJzEEJYMKgvwxEiMAQKy-4UMG9ZpKgLBrQoUCt3L1HJkRBMSEzpbMIthbAnBfTmRN8SujNniqnOV0bbiRnAmh5GG1NHlqExNO1AOYzhTxTRJfG_mKGvKXZdQdaIOYbAQgHNIvH1mO6S_2MrVC_w9VwxtaewxRDDvdzrm2kf_LQld4H7hiu5EEFKw7kBSlkbls4YF-zHPGeid8suCGaw3krcd5acrOsxhfKUcwQA
        self.BOT_TOKEN: 5245012700:AAFvOT_XmlL6n75rQb8aE0b04FwNt46sqbI
        self.SUDOERS: list = 1992156749
            int(id) for id in os.environ.get("SUDOERS", " ").split() if id.isnumeric()
        ]
        if not self.SESSION or not self.API_ID or not self.API_HASH:
            print("ERROR: SESSION, API_ID and API_HASH is required!")
            quit(0)
        self.SPOTIFY: bool = False
        self.QUALITY: str = os.environ.get("QUALITY", "high").lower()
        self.PREFIXES: list = os.environ.get("PREFIX", "!").split()
        self.LANGUAGE: str = os.environ.get("LANGUAGE", "en").lower()
        self.STREAM_MODE: str = (
            "audio"
            if (os.environ.get("STREAM_MODE", "audio").lower() == "audio")
            else "video"
        )
        self.ADMINS_ONLY: bool = os.environ.get("ADMINS_ONLY", False)
        self.SPOTIFY_CLIENT_ID: str = os.environ.get("SPOTIFY_CLIENT_ID", None)
        self.SPOTIFY_CLIENT_SECRET: str = os.environ.get("SPOTIFY_CLIENT_SECRET", None)


config = Config()

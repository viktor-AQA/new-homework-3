from dataclasses import dataclass

@dataclass
class APIConfig:
    BASE_URL: str = "https://api.example.com"

api_config = APIConfig()

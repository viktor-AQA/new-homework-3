from dataclasses import dataclass

@dataclass
class APIConfig:
    BASE_URL: str = "https://api.pomidor-stage.ru"

api_config = APIConfig()

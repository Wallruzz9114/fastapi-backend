from fastapi import Depends, FastAPI

from app.config import Settings, get_settings

app = FastAPI()


# Take note of settings: Settings = Depends(get_settings).
# Here, the Depends function is a dependency that declares another dependency, get_settings.
# Put another way, Depends depends on the result of get_settings.
# The value returned, Settings, is then assigned to the settings parameter.
@app.get('/ping')
def pong(settings: Settings = Depends(get_settings)):
    return {
        "ping": "pong!",
        "environment": settings.environment,
        "testing": settings.testing
    }

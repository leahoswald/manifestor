import asyncio

from homeassistant.core import HomeAssistant
from homeassistant.helpers.typing import ConfigType

DOMAIN="manifestor"

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool:
    """Set short_name to location name configured via lovelace"""
    hass.components.frontend.add_manifest_json_key('short_name', hass.config.location_name)
    return True

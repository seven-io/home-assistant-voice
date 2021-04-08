"""Sms77 Voice for notify component."""
import logging

import requests
import voluptuous

from homeassistant.components.notify import PLATFORM_SCHEMA, BaseNotificationService
from homeassistant.const import (
    CONF_API_KEY,
    CONF_RECIPIENT,
    CONF_SENDER,
    HTTP_OK,
)
import homeassistant.helpers.config_validation as cv

_LOGGER = logging.getLogger(__name__)
BASE_API_URL = "https://gateway.sms77.io/api/"
TIMEOUT = 5
PLATFORM_SCHEMA = voluptuous.Schema(voluptuous.All(PLATFORM_SCHEMA.extend({
    voluptuous.Required(CONF_API_KEY): cv.string,
    voluptuous.Required(CONF_RECIPIENT): cv.string,
    voluptuous.Optional(CONF_SENDER, default="491771783130"): cv.string,
})))


def get_service(hass, config, discovery_info=None):
    """Get the Sms77 Voice notification service."""
    if not _authenticate(config):
        _LOGGER.error("You are not authorized to access Sms77")
        return None
    return Sms77VoiceNotificationService(config)


class Sms77VoiceNotificationService(BaseNotificationService):
    """Implementation of a notification service for Sms77."""

    def __init__(self, config):
        """Initialize the service."""
        setattr(self, CONF_API_KEY, config[CONF_API_KEY])
        setattr(self, CONF_RECIPIENT, config[CONF_RECIPIENT])
        setattr(self, CONF_SENDER, config[CONF_SENDER])

    def send_message(self, message="", **kwargs):
        def _fallback(key):
            return (kwargs['data'][key]
                    if kwargs['data'] is not None and key in kwargs['data']
                    else getattr(self, key))

        """Issue a text-to-speech call to a certain phone number."""
        res = requests.post(
            f"{BASE_API_URL}voice",
            data={
                "from": _fallback(CONF_SENDER),
                "text": message,
                "to": _fallback(CONF_RECIPIENT),
            },
            headers=_build_headers(getattr(self, CONF_API_KEY)),
            timeout=TIMEOUT,
        )

        if res.status_code != HTTP_OK:
            _LOGGER.error("Expected %s but got %s", HTTP_OK, res.status_code)
            return

        code = int(res.text.splitlines()[0])
        if 100 != code:
            _LOGGER.error("Unexpected API code %s", code)
            return


def _authenticate(config):
    """Authenticate with Sms77."""
    res = requests.get(
        f"{BASE_API_URL}balance",
        headers=_build_headers(config[CONF_API_KEY]),
        timeout=TIMEOUT,
    )

    return res.status_code == HTTP_OK and "." in res.text


def _build_headers(api_key, sent_with="home-assistant"):
    return {"X-Api-Key": api_key, "SentWith": sent_with}

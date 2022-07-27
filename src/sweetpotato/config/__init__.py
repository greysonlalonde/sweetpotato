"""Default sweetpotato settings and current version.

Attributes:
    settings (Settings): default settings instance for app.

Todo:
    * Consider consolidating settings to a flask-esque configuration.
"""
from sweetpotato.config.default_settings import Settings

settings = Settings()  #: default settings instance for app.

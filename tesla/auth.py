from __future__ import annotations

from dataclasses import dataclass
from typing import Literal, TypeAlias

from .core import AsyncAuthScheme, AuthScheme


@dataclass(frozen=True, slots=True, kw_only=True)
class AuthSchemes:
    bearer_auth: AuthScheme
    thirdpartytoken_authorization_code: AuthScheme
    thirdpartytoken_client_credentials: AuthScheme


@dataclass(frozen=True, slots=True, kw_only=True)
class AsyncAuthSchemes:
    bearer_auth: AsyncAuthScheme
    thirdpartytoken_authorization_code: AsyncAuthScheme
    thirdpartytoken_client_credentials: AsyncAuthScheme


ThirdpartytokenAuthorizationCodeScope: TypeAlias = Literal[
    "openid",
    "offline_access",
    "user_data",
    "vehicle_device_data",
    "vehicle_location",
    "vehicle_cmds",
    "vehicle_charging_cmds",
    "vehicle_specs",
    "energy_device_data",
    "energy_cmds",
    "enterprise_management",
]
"""``openid``: Allow Tesla customers to sign in to the application with their Tesla credentials. ``offline_access``:
Allow getting a refresh token without needing user to log in again. ``user_data``: Contact information, home address,
profile picture, and referral information. ``vehicle_device_data``: Allow access to your vehicle’s live data, service
history, service scheduling data, service communications, eligible upgrades, nearby Superchargers and ownership details.
``vehicle_location``: Allow access to vehicle location information, including precise and coarse location data.
``vehicle_cmds``: Commands like add/remove driver, access Live Camera, unlock, wake up, remote start, and schedule
software updates. ``vehicle_charging_cmds``: Vehicle charging history, billed amount, charging location, and commands to
schedule, start, or stop charging. ``vehicle_specs``: Access detailed vehicle specifications. Partner tokens only;
usable without owner authorization. ``energy_device_data``: Energy live status, site info, backup history, energy
history, and charge history. ``energy_cmds``: Update energy settings like backup reserve percent, operation mode, and
storm mode. ``enterprise_management``: Allow access to enterprise management functions for businesses."""

ThirdpartytokenClientCredentialsScope: TypeAlias = Literal[
    "vehicle_device_data",
    "vehicle_location",
    "vehicle_cmds",
    "vehicle_charging_cmds",
    "vehicle_specs",
    "energy_device_data",
    "energy_cmds",
    "enterprise_management",
    "openid",
    "offline_access",
    "user_data",
]
"""``vehicle_device_data``: Allow access to your vehicle’s live data, service history, service scheduling data, service
communications, eligible upgrades, nearby Superchargers and ownership details. ``vehicle_location``: Allow access to
vehicle location information, including precise and coarse location data. ``vehicle_cmds``: Commands like add/remove
driver, access Live Camera, unlock, wake up, remote start, and schedule software updates. ``vehicle_charging_cmds``:
Vehicle charging history, billed amount, charging location, and commands to schedule, start, or stop charging.
``vehicle_specs``: Access detailed vehicle specifications. Partner tokens only; usable without owner authorization.
``energy_device_data``: Energy live status, site info, backup history, energy history, and charge history.
``energy_cmds``: Update energy settings like backup reserve percent, operation mode, and storm mode.
``enterprise_management``: Allow access to enterprise management functions for businesses. ``openid``.
``offline_access``. ``user_data``."""

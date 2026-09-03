<!-- Generated file — do not edit; regenerated with the SDK. -->

# VehicleCommands — operations

Accessor: `client.vehicle_commands` · Source: `tesla_fleet_management_api/apis/vehicle_commands.py` · 21 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.vehicle_commands.actuatetrunk

- **Route**: `POST /api/1/vehicles/{vehicle_tag}/command/actuate_trunk`
- **Auth**: `thirdpartytoken_authorization_code` OR `thirdpartytoken_client_credentials`
- **Signature**: `def actuatetrunk(vehicle_tag: str, body: ActuateTrunkRequest | ActuateTrunkRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `vehicle_tag`, `body`
- **Params**: `vehicle_tag` — path · `body` — JSON body
- **Returns (parsed)**: `CommandResponse`
- **Returns (raw)**: `ApiResult[CommandResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ActuateTrunkRequest` | `tesla_fleet_management_api/models/actuate_trunk_request.py` |
| `ActuateTrunkRequestDict` | `tesla_fleet_management_api/models/actuate_trunk_request.py` |
| `CommandResponse` | `tesla_fleet_management_api/models/command_response.py` |

### client.vehicle_commands.addchargeschedule

- **Route**: `POST /api/1/vehicles/{vehicle_tag}/command/add_charge_schedule`
- **Auth**: `thirdpartytoken_authorization_code` OR `thirdpartytoken_client_credentials`
- **Signature**: `def addchargeschedule(vehicle_tag: str, body: AddChargeScheduleRequest | AddChargeScheduleRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `vehicle_tag`, `body`
- **Params**: `vehicle_tag` — path · `body` — JSON body
- **Returns (parsed)**: `CommandResponse`
- **Returns (raw)**: `ApiResult[CommandResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `AddChargeScheduleRequest` | `tesla_fleet_management_api/models/add_charge_schedule_request.py` |
| `AddChargeScheduleRequestDict` | `tesla_fleet_management_api/models/add_charge_schedule_request.py` |
| `CommandResponse` | `tesla_fleet_management_api/models/command_response.py` |

### client.vehicle_commands.addpreconditionschedule

- **Route**: `POST /api/1/vehicles/{vehicle_tag}/command/add_precondition_schedule`
- **Auth**: `thirdpartytoken_authorization_code` OR `thirdpartytoken_client_credentials`
- **Signature**: `def addpreconditionschedule(vehicle_tag: str, body: AddPreconditionScheduleRequest | AddPreconditionScheduleRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `vehicle_tag`, `body`
- **Params**: `vehicle_tag` — path · `body` — JSON body
- **Returns (parsed)**: `CommandResponse`
- **Returns (raw)**: `ApiResult[CommandResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `AddPreconditionScheduleRequest` | `tesla_fleet_management_api/models/add_precondition_schedule_request.py` |
| `AddPreconditionScheduleRequestDict` | `tesla_fleet_management_api/models/add_precondition_schedule_request.py` |
| `CommandResponse` | `tesla_fleet_management_api/models/command_response.py` |

### client.vehicle_commands.adjustmediavolume

- **Route**: `POST /api/1/vehicles/{vehicle_tag}/command/adjust_volume`
- **Auth**: `thirdpartytoken_authorization_code` OR `thirdpartytoken_client_credentials`
- **Signature**: `def adjustmediavolume(vehicle_tag: str, body: AdjustVolumeRequest | AdjustVolumeRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `vehicle_tag`, `body`
- **Params**: `vehicle_tag` — path · `body` — JSON body
- **Returns (parsed)**: `CommandResponse`
- **Returns (raw)**: `ApiResult[CommandResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `AdjustVolumeRequest` | `tesla_fleet_management_api/models/adjust_volume_request.py` |
| `AdjustVolumeRequestDict` | `tesla_fleet_management_api/models/adjust_volume_request.py` |
| `CommandResponse` | `tesla_fleet_management_api/models/command_response.py` |

### client.vehicle_commands.cancelsoftwareupdate

- **Route**: `POST /api/1/vehicles/{vehicle_tag}/command/cancel_software_update`
- **Auth**: `thirdpartytoken_authorization_code` OR `thirdpartytoken_client_credentials`
- **Signature**: `def cancelsoftwareupdate(vehicle_tag: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `vehicle_tag`
- **Params**: `vehicle_tag` — path
- **Returns (parsed)**: `CommandResponse`
- **Returns (raw)**: `ApiResult[CommandResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `CommandResponse` | `tesla_fleet_management_api/models/command_response.py` |

### client.vehicle_commands.chargemaxrange

- **Route**: `POST /api/1/vehicles/{vehicle_tag}/command/charge_max_range`
- **Auth**: `thirdpartytoken_authorization_code` OR `thirdpartytoken_client_credentials`
- **Signature**: `def chargemaxrange(vehicle_tag: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `vehicle_tag`
- **Params**: `vehicle_tag` — path
- **Returns (parsed)**: `CommandResponse`
- **Returns (raw)**: `ApiResult[CommandResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `CommandResponse` | `tesla_fleet_management_api/models/command_response.py` |

### client.vehicle_commands.chargestandard

- **Route**: `POST /api/1/vehicles/{vehicle_tag}/command/charge_standard`
- **Auth**: `thirdpartytoken_authorization_code` OR `thirdpartytoken_client_credentials`
- **Signature**: `def chargestandard(vehicle_tag: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `vehicle_tag`
- **Params**: `vehicle_tag` — path
- **Returns (parsed)**: `CommandResponse`
- **Returns (raw)**: `ApiResult[CommandResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `CommandResponse` | `tesla_fleet_management_api/models/command_response.py` |

### client.vehicle_commands.clear_pi_nto_drive_admin

- **Route**: `POST /api/1/vehicles/{vehicle_tag}/command/clear_pin_to_drive_admin`
- **Auth**: `thirdpartytoken_authorization_code` OR `thirdpartytoken_client_credentials`
- **Signature**: `def clear_pi_nto_drive_admin(vehicle_tag: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `vehicle_tag`
- **Params**: `vehicle_tag` — path
- **Returns (parsed)**: `CommandResponse`
- **Returns (raw)**: `ApiResult[CommandResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `CommandResponse` | `tesla_fleet_management_api/models/command_response.py` |

### client.vehicle_commands.closechargeportdoor

- **Route**: `POST /api/1/vehicles/{vehicle_tag}/command/charge_port_door_close`
- **Auth**: `thirdpartytoken_authorization_code` OR `thirdpartytoken_client_credentials`
- **Signature**: `def closechargeportdoor(vehicle_tag: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `vehicle_tag`
- **Params**: `vehicle_tag` — path
- **Returns (parsed)**: `CommandResponse`
- **Returns (raw)**: `ApiResult[CommandResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `CommandResponse` | `tesla_fleet_management_api/models/command_response.py` |

### client.vehicle_commands.enableordisable_guest_mode

- **Route**: `POST /api/1/vehicles/{vehicle_tag}/command/guest_mode`
- **Auth**: `thirdpartytoken_authorization_code` OR `thirdpartytoken_client_credentials`
- **Signature**: `def enableordisable_guest_mode(vehicle_tag: str, body: GuestModeRequest | GuestModeRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `vehicle_tag`, `body`
- **Params**: `vehicle_tag` — path · `body` — JSON body
- **Returns (parsed)**: `CommandResponse`
- **Returns (raw)**: `ApiResult[CommandResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `GuestModeRequest` | `tesla_fleet_management_api/models/guest_mode_request.py` |
| `GuestModeRequestDict` | `tesla_fleet_management_api/models/guest_mode_request.py` |
| `CommandResponse` | `tesla_fleet_management_api/models/command_response.py` |

### client.vehicle_commands.eraseuserdata

- **Route**: `POST /api/1/vehicles/{vehicle_tag}/command/erase_user_data`
- **Auth**: `thirdpartytoken_authorization_code` OR `thirdpartytoken_client_credentials`
- **Signature**: `def eraseuserdata(vehicle_tag: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `vehicle_tag`
- **Params**: `vehicle_tag` — path
- **Returns (parsed)**: `CommandResponse`
- **Returns (raw)**: `ApiResult[CommandResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `CommandResponse` | `tesla_fleet_management_api/models/command_response.py` |

### client.vehicle_commands.flashlights

- **Route**: `POST /api/1/vehicles/{vehicle_tag}/command/flash_lights`
- **Auth**: `thirdpartytoken_authorization_code` OR `thirdpartytoken_client_credentials`
- **Signature**: `def flashlights(vehicle_tag: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `vehicle_tag`
- **Params**: `vehicle_tag` — path
- **Returns (parsed)**: `CommandResponse`
- **Returns (raw)**: `ApiResult[CommandResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `CommandResponse` | `tesla_fleet_management_api/models/command_response.py` |

### client.vehicle_commands.honkhorn

- **Route**: `POST /api/1/vehicles/{vehicle_tag}/command/honk_horn`
- **Auth**: `thirdpartytoken_authorization_code` OR `thirdpartytoken_client_credentials`
- **Signature**: `def honkhorn(vehicle_tag: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `vehicle_tag`
- **Params**: `vehicle_tag` — path
- **Returns (parsed)**: `CommandResponse`
- **Returns (raw)**: `ApiResult[CommandResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `CommandResponse` | `tesla_fleet_management_api/models/command_response.py` |

### client.vehicle_commands.lockdoors

- **Route**: `POST /api/1/vehicles/{vehicle_tag}/command/door_lock`
- **Auth**: `thirdpartytoken_authorization_code` OR `thirdpartytoken_client_credentials`
- **Signature**: `def lockdoors(vehicle_tag: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `vehicle_tag`
- **Params**: `vehicle_tag` — path
- **Returns (parsed)**: `CommandResponse`
- **Returns (raw)**: `ApiResult[CommandResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `CommandResponse` | `tesla_fleet_management_api/models/command_response.py` |

### client.vehicle_commands.nextfavoritemediatrack

- **Route**: `POST /api/1/vehicles/{vehicle_tag}/command/media_next_fav`
- **Auth**: `thirdpartytoken_authorization_code` OR `thirdpartytoken_client_credentials`
- **Signature**: `def nextfavoritemediatrack(vehicle_tag: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `vehicle_tag`
- **Params**: `vehicle_tag` — path
- **Returns (parsed)**: `CommandResponse`
- **Returns (raw)**: `ApiResult[CommandResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `CommandResponse` | `tesla_fleet_management_api/models/command_response.py` |

### client.vehicle_commands.openchargeportdoor

- **Route**: `POST /api/1/vehicles/{vehicle_tag}/command/charge_port_door_open`
- **Auth**: `thirdpartytoken_authorization_code` OR `thirdpartytoken_client_credentials`
- **Signature**: `def openchargeportdoor(vehicle_tag: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `vehicle_tag`
- **Params**: `vehicle_tag` — path
- **Returns (parsed)**: `CommandResponse`
- **Returns (raw)**: `ApiResult[CommandResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `CommandResponse` | `tesla_fleet_management_api/models/command_response.py` |

### client.vehicle_commands.startcharging

- **Route**: `POST /api/1/vehicles/{vehicle_tag}/command/charge_start`
- **Auth**: `thirdpartytoken_authorization_code` OR `thirdpartytoken_client_credentials`
- **Signature**: `def startcharging(vehicle_tag: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `vehicle_tag`
- **Params**: `vehicle_tag` — path
- **Returns (parsed)**: `CommandResponse`
- **Returns (raw)**: `ApiResult[CommandResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `CommandResponse` | `tesla_fleet_management_api/models/command_response.py` |

### client.vehicle_commands.startclimatepreconditioning

- **Route**: `POST /api/1/vehicles/{vehicle_tag}/command/auto_conditioning_start`
- **Auth**: `thirdpartytoken_authorization_code` OR `thirdpartytoken_client_credentials`
- **Signature**: `def startclimatepreconditioning(vehicle_tag: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `vehicle_tag`
- **Params**: `vehicle_tag` — path
- **Returns (parsed)**: `CommandResponse`
- **Returns (raw)**: `ApiResult[CommandResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `CommandResponse` | `tesla_fleet_management_api/models/command_response.py` |

### client.vehicle_commands.stopcharging

- **Route**: `POST /api/1/vehicles/{vehicle_tag}/command/charge_stop`
- **Auth**: `thirdpartytoken_authorization_code` OR `thirdpartytoken_client_credentials`
- **Signature**: `def stopcharging(vehicle_tag: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `vehicle_tag`
- **Params**: `vehicle_tag` — path
- **Returns (parsed)**: `CommandResponse`
- **Returns (raw)**: `ApiResult[CommandResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `CommandResponse` | `tesla_fleet_management_api/models/command_response.py` |

### client.vehicle_commands.stopclimatepreconditioning

- **Route**: `POST /api/1/vehicles/{vehicle_tag}/command/auto_conditioning_stop`
- **Auth**: `thirdpartytoken_authorization_code` OR `thirdpartytoken_client_credentials`
- **Signature**: `def stopclimatepreconditioning(vehicle_tag: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `vehicle_tag`
- **Params**: `vehicle_tag` — path
- **Returns (parsed)**: `CommandResponse`
- **Returns (raw)**: `ApiResult[CommandResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `CommandResponse` | `tesla_fleet_management_api/models/command_response.py` |

### client.vehicle_commands.unlockdoors

- **Route**: `POST /api/1/vehicles/{vehicle_tag}/command/door_unlock`
- **Auth**: `thirdpartytoken_authorization_code` OR `thirdpartytoken_client_credentials`
- **Signature**: `def unlockdoors(vehicle_tag: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `vehicle_tag`
- **Params**: `vehicle_tag` — path
- **Returns (parsed)**: `CommandResponse`
- **Returns (raw)**: `ApiResult[CommandResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `CommandResponse` | `tesla_fleet_management_api/models/command_response.py` |


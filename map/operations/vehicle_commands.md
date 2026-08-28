<!-- Generated file — do not edit; regenerated with the SDK. -->

# VehicleCommands — operations

Accessor: `client.vehicle_commands` · Source: `tesla/apis/vehicle_commands.py` · 21 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.vehicle_commands.actuatetrunk

- **Route**: `POST /api/1/vehicles/{vehicle_tag}/command/actuate_trunk`
- **Signature**: `def actuatetrunk(vehicle_tag: str, body: ActuateTrunkRequest | ActuateTrunkRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `vehicle_tag`, `body`
- **Params**: `vehicle_tag` — path · `body` — JSON body
- **Returns (parsed)**: `CommandResponse`
- **Returns (raw)**: `ApiResult[CommandResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ActuateTrunkRequest` | `tesla/models/actuate_trunk_request.py` |
| `ActuateTrunkRequestDict` | `tesla/models/actuate_trunk_request.py` |
| `CommandResponse` | `tesla/models/command_response.py` |

### client.vehicle_commands.addchargeschedule

- **Route**: `POST /api/1/vehicles/{vehicle_tag}/command/add_charge_schedule`
- **Signature**: `def addchargeschedule(vehicle_tag: str, body: AddChargeScheduleRequest | AddChargeScheduleRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `vehicle_tag`, `body`
- **Params**: `vehicle_tag` — path · `body` — JSON body
- **Returns (parsed)**: `CommandResponse`
- **Returns (raw)**: `ApiResult[CommandResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `AddChargeScheduleRequest` | `tesla/models/add_charge_schedule_request.py` |
| `AddChargeScheduleRequestDict` | `tesla/models/add_charge_schedule_request.py` |
| `CommandResponse` | `tesla/models/command_response.py` |

### client.vehicle_commands.addpreconditionschedule

- **Route**: `POST /api/1/vehicles/{vehicle_tag}/command/add_precondition_schedule`
- **Signature**: `def addpreconditionschedule(vehicle_tag: str, body: AddPreconditionScheduleRequest | AddPreconditionScheduleRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `vehicle_tag`, `body`
- **Params**: `vehicle_tag` — path · `body` — JSON body
- **Returns (parsed)**: `CommandResponse`
- **Returns (raw)**: `ApiResult[CommandResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `AddPreconditionScheduleRequest` | `tesla/models/add_precondition_schedule_request.py` |
| `AddPreconditionScheduleRequestDict` | `tesla/models/add_precondition_schedule_request.py` |
| `CommandResponse` | `tesla/models/command_response.py` |

### client.vehicle_commands.adjustmediavolume

- **Route**: `POST /api/1/vehicles/{vehicle_tag}/command/adjust_volume`
- **Signature**: `def adjustmediavolume(vehicle_tag: str, body: AdjustVolumeRequest | AdjustVolumeRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `vehicle_tag`, `body`
- **Params**: `vehicle_tag` — path · `body` — JSON body
- **Returns (parsed)**: `CommandResponse`
- **Returns (raw)**: `ApiResult[CommandResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `AdjustVolumeRequest` | `tesla/models/adjust_volume_request.py` |
| `AdjustVolumeRequestDict` | `tesla/models/adjust_volume_request.py` |
| `CommandResponse` | `tesla/models/command_response.py` |

### client.vehicle_commands.cancelsoftwareupdate

- **Route**: `POST /api/1/vehicles/{vehicle_tag}/command/cancel_software_update`
- **Signature**: `def cancelsoftwareupdate(vehicle_tag: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `vehicle_tag`
- **Params**: `vehicle_tag` — path
- **Returns (parsed)**: `CommandResponse`
- **Returns (raw)**: `ApiResult[CommandResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `CommandResponse` | `tesla/models/command_response.py` |

### client.vehicle_commands.chargemaxrange

- **Route**: `POST /api/1/vehicles/{vehicle_tag}/command/charge_max_range`
- **Signature**: `def chargemaxrange(vehicle_tag: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `vehicle_tag`
- **Params**: `vehicle_tag` — path
- **Returns (parsed)**: `CommandResponse`
- **Returns (raw)**: `ApiResult[CommandResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `CommandResponse` | `tesla/models/command_response.py` |

### client.vehicle_commands.chargestandard

- **Route**: `POST /api/1/vehicles/{vehicle_tag}/command/charge_standard`
- **Signature**: `def chargestandard(vehicle_tag: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `vehicle_tag`
- **Params**: `vehicle_tag` — path
- **Returns (parsed)**: `CommandResponse`
- **Returns (raw)**: `ApiResult[CommandResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `CommandResponse` | `tesla/models/command_response.py` |

### client.vehicle_commands.clear_pi_nto_drive_admin

- **Route**: `POST /api/1/vehicles/{vehicle_tag}/command/clear_pin_to_drive_admin`
- **Signature**: `def clear_pi_nto_drive_admin(vehicle_tag: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `vehicle_tag`
- **Params**: `vehicle_tag` — path
- **Returns (parsed)**: `CommandResponse`
- **Returns (raw)**: `ApiResult[CommandResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `CommandResponse` | `tesla/models/command_response.py` |

### client.vehicle_commands.closechargeportdoor

- **Route**: `POST /api/1/vehicles/{vehicle_tag}/command/charge_port_door_close`
- **Signature**: `def closechargeportdoor(vehicle_tag: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `vehicle_tag`
- **Params**: `vehicle_tag` — path
- **Returns (parsed)**: `CommandResponse`
- **Returns (raw)**: `ApiResult[CommandResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `CommandResponse` | `tesla/models/command_response.py` |

### client.vehicle_commands.enableordisable_guest_mode

- **Route**: `POST /api/1/vehicles/{vehicle_tag}/command/guest_mode`
- **Signature**: `def enableordisable_guest_mode(vehicle_tag: str, body: GuestModeRequest | GuestModeRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `vehicle_tag`, `body`
- **Params**: `vehicle_tag` — path · `body` — JSON body
- **Returns (parsed)**: `CommandResponse`
- **Returns (raw)**: `ApiResult[CommandResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `GuestModeRequest` | `tesla/models/guest_mode_request.py` |
| `GuestModeRequestDict` | `tesla/models/guest_mode_request.py` |
| `CommandResponse` | `tesla/models/command_response.py` |

### client.vehicle_commands.eraseuserdata

- **Route**: `POST /api/1/vehicles/{vehicle_tag}/command/erase_user_data`
- **Signature**: `def eraseuserdata(vehicle_tag: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `vehicle_tag`
- **Params**: `vehicle_tag` — path
- **Returns (parsed)**: `CommandResponse`
- **Returns (raw)**: `ApiResult[CommandResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `CommandResponse` | `tesla/models/command_response.py` |

### client.vehicle_commands.flashlights

- **Route**: `POST /api/1/vehicles/{vehicle_tag}/command/flash_lights`
- **Signature**: `def flashlights(vehicle_tag: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `vehicle_tag`
- **Params**: `vehicle_tag` — path
- **Returns (parsed)**: `CommandResponse`
- **Returns (raw)**: `ApiResult[CommandResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `CommandResponse` | `tesla/models/command_response.py` |

### client.vehicle_commands.honkhorn

- **Route**: `POST /api/1/vehicles/{vehicle_tag}/command/honk_horn`
- **Signature**: `def honkhorn(vehicle_tag: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `vehicle_tag`
- **Params**: `vehicle_tag` — path
- **Returns (parsed)**: `CommandResponse`
- **Returns (raw)**: `ApiResult[CommandResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `CommandResponse` | `tesla/models/command_response.py` |

### client.vehicle_commands.lockdoors

- **Route**: `POST /api/1/vehicles/{vehicle_tag}/command/door_lock`
- **Signature**: `def lockdoors(vehicle_tag: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `vehicle_tag`
- **Params**: `vehicle_tag` — path
- **Returns (parsed)**: `CommandResponse`
- **Returns (raw)**: `ApiResult[CommandResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `CommandResponse` | `tesla/models/command_response.py` |

### client.vehicle_commands.nextfavoritemediatrack

- **Route**: `POST /api/1/vehicles/{vehicle_tag}/command/media_next_fav`
- **Signature**: `def nextfavoritemediatrack(vehicle_tag: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `vehicle_tag`
- **Params**: `vehicle_tag` — path
- **Returns (parsed)**: `CommandResponse`
- **Returns (raw)**: `ApiResult[CommandResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `CommandResponse` | `tesla/models/command_response.py` |

### client.vehicle_commands.openchargeportdoor

- **Route**: `POST /api/1/vehicles/{vehicle_tag}/command/charge_port_door_open`
- **Signature**: `def openchargeportdoor(vehicle_tag: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `vehicle_tag`
- **Params**: `vehicle_tag` — path
- **Returns (parsed)**: `CommandResponse`
- **Returns (raw)**: `ApiResult[CommandResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `CommandResponse` | `tesla/models/command_response.py` |

### client.vehicle_commands.startcharging

- **Route**: `POST /api/1/vehicles/{vehicle_tag}/command/charge_start`
- **Signature**: `def startcharging(vehicle_tag: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `vehicle_tag`
- **Params**: `vehicle_tag` — path
- **Returns (parsed)**: `CommandResponse`
- **Returns (raw)**: `ApiResult[CommandResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `CommandResponse` | `tesla/models/command_response.py` |

### client.vehicle_commands.startclimatepreconditioning

- **Route**: `POST /api/1/vehicles/{vehicle_tag}/command/auto_conditioning_start`
- **Signature**: `def startclimatepreconditioning(vehicle_tag: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `vehicle_tag`
- **Params**: `vehicle_tag` — path
- **Returns (parsed)**: `CommandResponse`
- **Returns (raw)**: `ApiResult[CommandResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `CommandResponse` | `tesla/models/command_response.py` |

### client.vehicle_commands.stopcharging

- **Route**: `POST /api/1/vehicles/{vehicle_tag}/command/charge_stop`
- **Signature**: `def stopcharging(vehicle_tag: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `vehicle_tag`
- **Params**: `vehicle_tag` — path
- **Returns (parsed)**: `CommandResponse`
- **Returns (raw)**: `ApiResult[CommandResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `CommandResponse` | `tesla/models/command_response.py` |

### client.vehicle_commands.stopclimatepreconditioning

- **Route**: `POST /api/1/vehicles/{vehicle_tag}/command/auto_conditioning_stop`
- **Signature**: `def stopclimatepreconditioning(vehicle_tag: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `vehicle_tag`
- **Params**: `vehicle_tag` — path
- **Returns (parsed)**: `CommandResponse`
- **Returns (raw)**: `ApiResult[CommandResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `CommandResponse` | `tesla/models/command_response.py` |

### client.vehicle_commands.unlockdoors

- **Route**: `POST /api/1/vehicles/{vehicle_tag}/command/door_unlock`
- **Signature**: `def unlockdoors(vehicle_tag: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `vehicle_tag`
- **Params**: `vehicle_tag` — path
- **Returns (parsed)**: `CommandResponse`
- **Returns (raw)**: `ApiResult[CommandResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `CommandResponse` | `tesla/models/command_response.py` |


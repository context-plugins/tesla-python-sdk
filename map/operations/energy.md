<!-- Generated file — do not edit; regenerated with the SDK. -->

# Energy — operations

Accessor: `client.energy` · Source: `tesla_fleet_management_api/apis/energy.py` · 11 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.energy.adjust_site_s_backup_reserve

- **Route**: `POST /api/1/energy_sites/{energy_site_id}/backup`
- **Auth**: `thirdpartytoken_authorization_code` OR `thirdpartytoken_client_credentials`
- **Signature**: `def adjust_site_s_backup_reserve(energy_site_id: str, body: BackupRequest | BackupRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `energy_site_id`, `body`
- **Params**: `energy_site_id` — path · `body` — JSON body
- **Returns (parsed)**: `BackupResponse`
- **Returns (raw)**: `ApiResult[BackupResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `BackupRequest` | `tesla_fleet_management_api/models/backup_request.py` |
| `BackupRequestDict` | `tesla_fleet_management_api/models/backup_request.py` |
| `BackupResponse` | `tesla_fleet_management_api/models/backup_response.py` |

### client.energy.adjust_site_s_off_grid_vehicle_charging_reserve

- **Route**: `POST /api/1/energy_sites/{energy_site_id}/off_grid_vehicle_charging_reserve`
- **Auth**: `thirdpartytoken_authorization_code` OR `thirdpartytoken_client_credentials`
- **Signature**: `def adjust_site_s_off_grid_vehicle_charging_reserve(energy_site_id: str, body: OffGridVehicleChargingReserveRequest | OffGridVehicleChargingReserveRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `energy_site_id`, `body`
- **Params**: `energy_site_id` — path · `body` — JSON body
- **Returns (parsed)**: `GenericUpdateResponse`
- **Returns (raw)**: `ApiResult[GenericUpdateResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `OffGridVehicleChargingReserveRequest` | `tesla_fleet_management_api/models/off_grid_vehicle_charging_reserve_request.py` |
| `OffGridVehicleChargingReserveRequestDict` | `tesla_fleet_management_api/models/off_grid_vehicle_charging_reserve_request.py` |
| `GenericUpdateResponse` | `tesla_fleet_management_api/models/generic_update_response.py` |

### client.energy.allow_disallow_charging_from_the_grid_and_exporting_energy_to_the_grid

- **Route**: `POST /api/1/energy_sites/{energy_site_id}/grid_import_export`
- **Auth**: `thirdpartytoken_authorization_code` OR `thirdpartytoken_client_credentials`
- **Signature**: `def allow_disallow_charging_from_the_grid_and_exporting_energy_to_the_grid(energy_site_id: str, *, body: Any | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `energy_site_id`
- **Params**: `energy_site_id` — path · `body` — JSON body
- **Returns (parsed)**: `GenericUpdateResponse`
- **Returns (raw)**: `ApiResult[GenericUpdateResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `GenericUpdateResponse` | `tesla_fleet_management_api/models/generic_update_response.py` |

### client.energy.get_backup_or_energy_history

- **Route**: `GET /api/1/energy_sites/{energy_site_id}/calendar_history`
- **Auth**: `thirdpartytoken_authorization_code` OR `thirdpartytoken_client_credentials`
- **Signature**: `def get_backup_or_energy_history(energy_site_id: str, kind: KindOrStr, start_date: RFC3339DateTime, end_date: RFC3339DateTime, *, period: str | None = None, time_zone: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `energy_site_id`, `kind`, `start_date`, `end_date`
- **Params**: `energy_site_id` — path · `kind` — query · `start_date` — query · `end_date` — query · `period` — query · `time_zone` — query
- **Returns (parsed)**: `CalendarHistoryResponse`
- **Returns (raw)**: `ApiResult[CalendarHistoryResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `KindOrStr` | `tesla_fleet_management_api/models/enums/kind.py` |
| `CalendarHistoryResponse` | `tesla_fleet_management_api/models/calendar_history_response.py` |

### client.energy.get_live_site_status

- **Route**: `GET /api/1/energy_sites/{energy_site_id}/live_status`
- **Auth**: `thirdpartytoken_authorization_code` OR `thirdpartytoken_client_credentials`
- **Signature**: `def get_live_site_status(energy_site_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `energy_site_id`
- **Params**: `energy_site_id` — path
- **Returns (parsed)**: `LiveStatusResponse`
- **Returns (raw)**: `ApiResult[LiveStatusResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `LiveStatusResponse` | `tesla_fleet_management_api/models/live_status_response.py` |

### client.energy.get_site_information_assets_settings_features

- **Route**: `GET /api/1/energy_sites/{energy_site_id}/site_info`
- **Auth**: `thirdpartytoken_authorization_code` OR `thirdpartytoken_client_credentials`
- **Signature**: `def get_site_information_assets_settings_features(energy_site_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `energy_site_id`
- **Params**: `energy_site_id` — path
- **Returns (parsed)**: `SiteInfoResponse`
- **Returns (raw)**: `ApiResult[SiteInfoResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `SiteInfoResponse` | `tesla_fleet_management_api/models/site_info_response.py` |

### client.energy.get_user_products_vehicles_energy_sites

- **Route**: `GET /api/1/products`
- **Auth**: `thirdpartytoken_authorization_code` OR `thirdpartytoken_client_credentials`
- **Signature**: `def get_user_products_vehicles_energy_sites(*, request_options: RequestOptionsOrDict | None = None)`
- **Returns (parsed)**: `ProductsResponse`
- **Returns (raw)**: `ApiResult[ProductsResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ProductsResponse` | `tesla_fleet_management_api/models/products_response.py` |

### client.energy.get_wall_connector_charging_history

- **Route**: `GET /api/1/energy_sites/{energy_site_id}/telemetry_history`
- **Auth**: `thirdpartytoken_authorization_code` OR `thirdpartytoken_client_credentials`
- **Signature**: `def get_wall_connector_charging_history(energy_site_id: str, kind: KindGetWallConnectorChargingHistoryOrStr, start_date: RFC3339DateTime, end_date: RFC3339DateTime, *, time_zone: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `energy_site_id`, `kind`, `start_date`, `end_date`
- **Params**: `energy_site_id` — path · `kind` — query · `start_date` — query · `end_date` — query · `time_zone` — query
- **Returns (parsed)**: `ChargeHistoryResponse`
- **Returns (raw)**: `ApiResult[ChargeHistoryResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `KindGetWallConnectorChargingHistoryOrStr` | `tesla_fleet_management_api/models/enums/kind_get_wall_connector_charging_history.py` |
| `ChargeHistoryResponse` | `tesla_fleet_management_api/models/charge_history_response.py` |

### client.energy.set_site_mode_autonomous_or_self_consumption

- **Route**: `POST /api/1/energy_sites/{energy_site_id}/operation`
- **Auth**: `thirdpartytoken_authorization_code` OR `thirdpartytoken_client_credentials`
- **Signature**: `def set_site_mode_autonomous_or_self_consumption(energy_site_id: str, body: OperationRequest | OperationRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `energy_site_id`, `body`
- **Params**: `energy_site_id` — path · `body` — JSON body
- **Returns (parsed)**: `GenericUpdateResponse`
- **Returns (raw)**: `ApiResult[GenericUpdateResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `OperationRequest` | `tesla_fleet_management_api/models/operation_request.py` |
| `OperationRequestDict` | `tesla_fleet_management_api/models/operation_request.py` |
| `GenericUpdateResponse` | `tesla_fleet_management_api/models/generic_update_response.py` |

### client.energy.update_storm_watch_participation

- **Route**: `POST /api/1/energy_sites/{energy_site_id}/storm_mode`
- **Auth**: `thirdpartytoken_authorization_code` OR `thirdpartytoken_client_credentials`
- **Signature**: `def update_storm_watch_participation(energy_site_id: str, body: StormModeRequest | StormModeRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `energy_site_id`, `body`
- **Params**: `energy_site_id` — path · `body` — JSON body
- **Returns (parsed)**: `GenericUpdateResponse`
- **Returns (raw)**: `ApiResult[GenericUpdateResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `StormModeRequest` | `tesla_fleet_management_api/models/storm_mode_request.py` |
| `StormModeRequestDict` | `tesla_fleet_management_api/models/storm_mode_request.py` |
| `GenericUpdateResponse` | `tesla_fleet_management_api/models/generic_update_response.py` |

### client.energy.update_time_of_use_tou_settings

- **Route**: `POST /api/1/energy_sites/{energy_site_id}/time_of_use_settings`
- **Auth**: `thirdpartytoken_authorization_code` OR `thirdpartytoken_client_credentials`
- **Signature**: `def update_time_of_use_tou_settings(energy_site_id: str, body: TimeOfUseSettingsRequest | TimeOfUseSettingsRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `energy_site_id`, `body`
- **Params**: `energy_site_id` — path · `body` — JSON body
- **Returns (parsed)**: `GenericUpdateResponse`
- **Returns (raw)**: `ApiResult[GenericUpdateResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `TimeOfUseSettingsRequest` | `tesla_fleet_management_api/models/time_of_use_settings_request.py` |
| `TimeOfUseSettingsRequestDict` | `tesla_fleet_management_api/models/time_of_use_settings_request.py` |
| `GenericUpdateResponse` | `tesla_fleet_management_api/models/generic_update_response.py` |


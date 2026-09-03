<!-- Generated file — do not edit; regenerated with the SDK. -->

# Vehicles — operations

Accessor: `client.vehicles` · Source: `tesla_fleet_management_api/apis/vehicles.py` · 21 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded, and an operation with no table mentions nothing but builtins and those.

### client.vehicles.configure_fleet_telemetry_using_signed_jws_token

- **Route**: `POST /api/1/vehicles/fleet_telemetry_config_jws`
- **Auth**: `thirdpartytoken_authorization_code` OR `thirdpartytoken_client_credentials`
- **Signature**: `def configure_fleet_telemetry_using_signed_jws_token(body: FleetTelemetryJwsRequest | FleetTelemetryJwsRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `Any`
- **Returns (raw)**: `ApiResult[Any, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `FleetTelemetryJwsRequest` | `tesla_fleet_management_api/models/fleet_telemetry_jws_request.py` |
| `FleetTelemetryJwsRequestDict` | `tesla_fleet_management_api/models/fleet_telemetry_jws_request.py` |

### client.vehicles.create_or_update_fleet_telemetry_configuration

- **Route**: `POST /api/1/vehicles/fleet_telemetry_config`
- **Auth**: `thirdpartytoken_authorization_code` OR `thirdpartytoken_client_credentials`
- **Signature**: `def create_or_update_fleet_telemetry_configuration(body: Any, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `Any`
- **Returns (raw)**: `ApiResult[Any, RawError]`
- **Error**: `RawError` — **Case B**

### client.vehicles.delete_fleet_telemetry_configuration

- **Route**: `DELETE /api/1/vehicles/{vehicle_tag}/fleet_telemetry_config`
- **Auth**: `thirdpartytoken_authorization_code` OR `thirdpartytoken_client_credentials`
- **Signature**: `def delete_fleet_telemetry_configuration(vehicle_tag: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `vehicle_tag`
- **Params**: `vehicle_tag` — path
- **Returns (parsed)**: `Any`
- **Returns (raw)**: `ApiResult[Any, RawError]`
- **Error**: `RawError` — **Case B**

### client.vehicles.get_allowed_drivers_for_a_vehicle

- **Route**: `GET /api/1/vehicles/{vehicle_tag}/drivers`
- **Auth**: `thirdpartytoken_authorization_code` OR `thirdpartytoken_client_credentials`
- **Signature**: `def get_allowed_drivers_for_a_vehicle(vehicle_tag: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `vehicle_tag`
- **Params**: `vehicle_tag` — path
- **Returns (parsed)**: `DriversResponse`
- **Returns (raw)**: `ApiResult[DriversResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `DriversResponse` | `tesla_fleet_management_api/models/drivers_response.py` |

### client.vehicles.get_eligible_vehicle_subscriptions

- **Route**: `GET /api/1/dx/vehicles/subscriptions/eligibility`
- **Auth**: `thirdpartytoken_authorization_code` OR `thirdpartytoken_client_credentials`
- **Signature**: `def get_eligible_vehicle_subscriptions(vin: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `vin`
- **Params**: `vin` — query
- **Returns (parsed)**: `SiteInfoResponse`
- **Returns (raw)**: `ApiResult[SiteInfoResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `SiteInfoResponse` | `tesla_fleet_management_api/models/site_info_response.py` |

### client.vehicles.get_eligible_vehicle_upgrades

- **Route**: `GET /api/1/dx/vehicles/upgrades/eligibility`
- **Auth**: `thirdpartytoken_authorization_code` OR `thirdpartytoken_client_credentials`
- **Signature**: `def get_eligible_vehicle_upgrades(vin: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `vin`
- **Params**: `vin` — query
- **Returns (parsed)**: `SiteInfoResponse`
- **Returns (raw)**: `ApiResult[SiteInfoResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `SiteInfoResponse` | `tesla_fleet_management_api/models/site_info_response.py` |

### client.vehicles.get_enterprise_roles_for_a_vehicle

- **Route**: `GET /api/1/dx/enterprise/v1/{vin}/roles`
- **Auth**: `thirdpartytoken_authorization_code` OR `thirdpartytoken_client_credentials`
- **Signature**: `def get_enterprise_roles_for_a_vehicle(vin: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `vin`
- **Params**: `vin` — path
- **Returns (parsed)**: `Any`
- **Returns (raw)**: `ApiResult[Any, RawError]`
- **Error**: `RawError` — **Case B**

### client.vehicles.get_fleet_status_for_vehicles

- **Route**: `POST /api/1/vehicles/fleet_status`
- **Auth**: `thirdpartytoken_authorization_code` OR `thirdpartytoken_client_credentials`
- **Signature**: `def get_fleet_status_for_vehicles(body: FleetStatusRequest | FleetStatusRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `Any`
- **Returns (raw)**: `ApiResult[Any, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `FleetStatusRequest` | `tesla_fleet_management_api/models/fleet_status_request.py` |
| `FleetStatusRequestDict` | `tesla_fleet_management_api/models/fleet_status_request.py` |

### client.vehicles.get_fleet_telemetry_configuration

- **Route**: `GET /api/1/vehicles/{vehicle_tag}/fleet_telemetry_config`
- **Auth**: `thirdpartytoken_authorization_code` OR `thirdpartytoken_client_credentials`
- **Signature**: `def get_fleet_telemetry_configuration(vehicle_tag: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `vehicle_tag`
- **Params**: `vehicle_tag` — path
- **Returns (parsed)**: `Any`
- **Returns (raw)**: `ApiResult[Any, RawError]`
- **Error**: `RawError` — **Case B**

### client.vehicles.get_fleet_telemetry_errors_for_a_vehicle

- **Route**: `GET /api/1/vehicles/{vehicle_tag}/fleet_telemetry_errors`
- **Auth**: `thirdpartytoken_authorization_code` OR `thirdpartytoken_client_credentials`
- **Signature**: `def get_fleet_telemetry_errors_for_a_vehicle(vehicle_tag: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `vehicle_tag`
- **Params**: `vehicle_tag` — path
- **Returns (parsed)**: `Any`
- **Returns (raw)**: `ApiResult[Any, RawError]`
- **Error**: `RawError` — **Case B**

### client.vehicles.get_vehicle

- **Route**: `GET /api/1/vehicles/{vehicle_tag}`
- **Auth**: `thirdpartytoken_authorization_code` OR `thirdpartytoken_client_credentials`
- **Signature**: `def get_vehicle(vehicle_tag: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `vehicle_tag`
- **Params**: `vehicle_tag` — path
- **Returns (parsed)**: `Api1VehiclesResponseResponse200`
- **Returns (raw)**: `ApiResult[Api1VehiclesResponseResponse200, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `Api1VehiclesResponseResponse200` | `tesla_fleet_management_api/models/api1_vehicles_response_response200.py` |

### client.vehicles.list_vehicles

- **Route**: `GET /api/1/vehicles`
- **Auth**: `thirdpartytoken_authorization_code` OR `thirdpartytoken_client_credentials`
- **Signature**: `def list_vehicles(*, request_options: RequestOptionsOrDict | None = None)`
- **Returns (parsed)**: `Api1VehiclesResponse`
- **Returns (raw)**: `ApiResult[Api1VehiclesResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `Api1VehiclesResponse` | `tesla_fleet_management_api/models/api1_vehicles_response.py` |

### client.vehicles.mobile_enabled

- **Route**: `GET /api/1/vehicles/{vehicle_tag}/mobile_enabled`
- **Auth**: `thirdpartytoken_authorization_code` OR `thirdpartytoken_client_credentials`
- **Signature**: `def mobile_enabled(vehicle_tag: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `vehicle_tag`
- **Params**: `vehicle_tag` — path
- **Returns (parsed)**: `Api1VehiclesMobileEnabledResponse`
- **Returns (raw)**: `ApiResult[Api1VehiclesMobileEnabledResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `Api1VehiclesMobileEnabledResponse` | `tesla_fleet_management_api/models/api1_vehicles_mobile_enabled_response.py` |

### client.vehicles.nearby_charging_sites

- **Route**: `GET /api/1/vehicles/{vehicle_tag}/nearby_charging_sites`
- **Auth**: `thirdpartytoken_authorization_code` OR `thirdpartytoken_client_credentials`
- **Signature**: `def nearby_charging_sites(vehicle_tag: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `vehicle_tag`
- **Params**: `vehicle_tag` — path
- **Returns (parsed)**: `Api1VehiclesNearbyChargingSitesResponse`
- **Returns (raw)**: `ApiResult[Api1VehiclesNearbyChargingSitesResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `Api1VehiclesNearbyChargingSitesResponse` | `tesla_fleet_management_api/models/api1_vehicles_nearby_charging_sites_response.py` |

### client.vehicles.remove_driver_access_from_a_vehicle

- **Route**: `DELETE /api/1/vehicles/{vehicle_tag}/drivers`
- **Auth**: `thirdpartytoken_authorization_code` OR `thirdpartytoken_client_credentials`
- **Signature**: `def remove_driver_access_from_a_vehicle(vehicle_tag: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `vehicle_tag`
- **Params**: `vehicle_tag` — path
- **Returns (parsed)**: `SimpleOkResponse`
- **Returns (raw)**: `ApiResult[SimpleOkResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `SimpleOkResponse` | `tesla_fleet_management_api/models/simple_ok_response.py` |

### client.vehicles.set_enterprise_payer_roles

- **Route**: `POST /api/1/dx/enterprise/v1/{vin}/payer`
- **Auth**: `thirdpartytoken_authorization_code` OR `thirdpartytoken_client_credentials`
- **Signature**: `def set_enterprise_payer_roles(vin: str, body: EnterprisePayerRequest | EnterprisePayerRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `vin`, `body`
- **Params**: `vin` — path · `body` — JSON body
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `EnterprisePayerRequest` | `tesla_fleet_management_api/models/enterprise_payer_request.py` |
| `EnterprisePayerRequestDict` | `tesla_fleet_management_api/models/enterprise_payer_request.py` |

### client.vehicles.vehicle_live_data

- **Route**: `GET /api/1/vehicles/{vehicle_tag}/vehicle_data`
- **Auth**: `thirdpartytoken_authorization_code` OR `thirdpartytoken_client_credentials`
- **Signature**: `def vehicle_live_data(vehicle_tag: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `vehicle_tag`
- **Params**: `vehicle_tag` — path
- **Returns (parsed)**: `SiteInfoResponse`
- **Returns (raw)**: `ApiResult[SiteInfoResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `SiteInfoResponse` | `tesla_fleet_management_api/models/site_info_response.py` |

### client.vehicles.vehicle_options

- **Route**: `GET /api/1/dx/vehicles/options`
- **Auth**: `thirdpartytoken_authorization_code` OR `thirdpartytoken_client_credentials`
- **Signature**: `def vehicle_options(vin: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `vin`
- **Params**: `vin` — query
- **Returns (parsed)**: `Api1DxVehiclesOptionsResponse`
- **Returns (raw)**: `ApiResult[Api1DxVehiclesOptionsResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `Api1DxVehiclesOptionsResponse` | `tesla_fleet_management_api/models/api1_dx_vehicles_options_response.py` |

### client.vehicles.vehicle_specs

- **Route**: `GET /api/1/vehicles/{vin}/specs`
- **Auth**: `thirdpartytoken_authorization_code` OR `thirdpartytoken_client_credentials`
- **Signature**: `def vehicle_specs(vin: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `vin`
- **Params**: `vin` — path
- **Returns (parsed)**: `SiteInfoResponse`
- **Returns (raw)**: `ApiResult[SiteInfoResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `SiteInfoResponse` | `tesla_fleet_management_api/models/site_info_response.py` |

### client.vehicles.wake_up_vehicle

- **Route**: `POST /api/1/vehicles/{vehicle_tag}/wake_up`
- **Auth**: `thirdpartytoken_authorization_code` OR `thirdpartytoken_client_credentials`
- **Signature**: `def wake_up_vehicle(vehicle_tag: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `vehicle_tag`
- **Params**: `vehicle_tag` — path
- **Returns (parsed)**: `Api1VehiclesWakeUpResponse`
- **Returns (raw)**: `ApiResult[Api1VehiclesWakeUpResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `Api1VehiclesWakeUpResponse` | `tesla_fleet_management_api/models/api1_vehicles_wake_up_response.py` |

### client.vehicles.warranty_details

- **Route**: `GET /api/1/dx/warranty/details`
- **Auth**: `thirdpartytoken_authorization_code` OR `thirdpartytoken_client_credentials`
- **Signature**: `def warranty_details(*, request_options: RequestOptionsOrDict | None = None)`
- **Returns (parsed)**: `Api1DxWarrantyDetailsResponse`
- **Returns (raw)**: `ApiResult[Api1DxWarrantyDetailsResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `Api1DxWarrantyDetailsResponse` | `tesla_fleet_management_api/models/api1_dx_warranty_details_response.py` |


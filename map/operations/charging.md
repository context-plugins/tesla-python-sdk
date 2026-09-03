<!-- Generated file — do not edit; regenerated with the SDK. -->

# Charging — operations

Accessor: `client.charging` · Source: `tesla_fleet_management_api/apis/charging.py` · 3 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded, and an operation with no table mentions nothing but builtins and those.

### client.charging.get_charging_history

- **Route**: `GET /api/1/dx/charging/history`
- **Auth**: `thirdpartytoken_authorization_code` OR `thirdpartytoken_client_credentials`
- **Signature**: `def get_charging_history(*, request_options: RequestOptionsOrDict | None = None)`
- **Returns (parsed)**: `ChargingHistoryResponse`
- **Returns (raw)**: `ApiResult[ChargingHistoryResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ChargingHistoryResponse` | `tesla_fleet_management_api/models/charging_history_response.py` |

### client.charging.get_charging_invoice

- **Route**: `GET /api/1/dx/charging/invoice/{id}`
- **Auth**: `thirdpartytoken_authorization_code` OR `thirdpartytoken_client_credentials`
- **Signature**: `def get_charging_invoice(id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `id`
- **Params**: `id` — path
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, RawError]`
- **Error**: `RawError` — **Case B**

### client.charging.get_charging_sessions

- **Route**: `GET /api/1/dx/charging/sessions`
- **Auth**: `thirdpartytoken_authorization_code` OR `thirdpartytoken_client_credentials`
- **Signature**: `def get_charging_sessions(*, request_options: RequestOptionsOrDict | None = None)`
- **Returns (parsed)**: `ChargingSessionsResponse`
- **Returns (raw)**: `ApiResult[ChargingSessionsResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ChargingSessionsResponse` | `tesla_fleet_management_api/models/charging_sessions_response.py` |


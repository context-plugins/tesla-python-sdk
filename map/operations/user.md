<!-- Generated file — do not edit; regenerated with the SDK. -->

# User — operations

Accessor: `client.user` · Source: `tesla_fleet_management_api/apis/user.py` · 4 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.user.get_active_orders_for_a_user

- **Route**: `GET /api/1/users/orders`
- **Auth**: `thirdpartytoken_authorization_code` OR `thirdpartytoken_client_credentials`
- **Signature**: `def get_active_orders_for_a_user(*, request_options: RequestOptionsOrDict | None = None)`
- **Returns (parsed)**: `OrdersResponse`
- **Returns (raw)**: `ApiResult[OrdersResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `OrdersResponse` | `tesla_fleet_management_api/models/orders_response.py` |

### client.user.get_custom_feature_flags_for_a_user

- **Route**: `GET /api/1/users/feature_config`
- **Auth**: `thirdpartytoken_authorization_code` OR `thirdpartytoken_client_credentials`
- **Signature**: `def get_custom_feature_flags_for_a_user(*, request_options: RequestOptionsOrDict | None = None)`
- **Returns (parsed)**: `BackupResponse`
- **Returns (raw)**: `ApiResult[BackupResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `BackupResponse` | `tesla_fleet_management_api/models/backup_response.py` |

### client.user.get_summary_of_a_user_s_account

- **Route**: `GET /api/1/users/me`
- **Auth**: `thirdpartytoken_authorization_code` OR `thirdpartytoken_client_credentials`
- **Signature**: `def get_summary_of_a_user_s_account(*, request_options: RequestOptionsOrDict | None = None)`
- **Returns (parsed)**: `MeResponse`
- **Returns (raw)**: `ApiResult[MeResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `MeResponse` | `tesla_fleet_management_api/models/me_response.py` |

### client.user.get_user_s_region_and_fleet_api_base_url

- **Route**: `GET /api/1/users/region`
- **Auth**: `thirdpartytoken_authorization_code` OR `thirdpartytoken_client_credentials`
- **Signature**: `def get_user_s_region_and_fleet_api_base_url(*, request_options: RequestOptionsOrDict | None = None)`
- **Returns (parsed)**: `RegionResponse`
- **Returns (raw)**: `ApiResult[RegionResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `RegionResponse` | `tesla_fleet_management_api/models/region_response.py` |


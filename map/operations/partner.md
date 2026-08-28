<!-- Generated file — do not edit; regenerated with the SDK. -->

# Partner — operations

Accessor: `client.partner` · Source: `tesla/apis/partner.py` · 4 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.partner.get_public_key_for_a_domain

- **Route**: `GET /api/1/partner_accounts/public_key`
- **Signature**: `def get_public_key_for_a_domain(domain: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `domain`
- **Params**: `domain` — query
- **Returns (parsed)**: `PublicKeyResponse`
- **Returns (raw)**: `ApiResult[PublicKeyResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `PublicKeyResponse` | `tesla/models/public_key_response.py` |

### client.partner.get_recent_fleet_telemetry_errors

- **Route**: `GET /api/1/partner_accounts/fleet_telemetry_errors`
- **Signature**: `def get_recent_fleet_telemetry_errors(*, request_options: RequestOptionsOrDict | None = None)`
- **Returns (parsed)**: `FleetTelemetryErrorsResponse`
- **Returns (raw)**: `ApiResult[FleetTelemetryErrorsResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `FleetTelemetryErrorsResponse` | `tesla/models/fleet_telemetry_errors_response.py` |

### client.partner.get_vins_with_fleet_telemetry_errors

- **Route**: `GET /api/1/partner_accounts/fleet_telemetry_error_vins`
- **Signature**: `def get_vins_with_fleet_telemetry_errors(*, request_options: RequestOptionsOrDict | None = None)`
- **Returns (parsed)**: `BackupResponse`
- **Returns (raw)**: `ApiResult[BackupResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `BackupResponse` | `tesla/models/backup_response.py` |

### client.partner.register_a_partner_account

- **Route**: `POST /api/1/partner_accounts`
- **Signature**: `def register_a_partner_account(body: RegisterPartnerRequest | RegisterPartnerRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `RegisterPartnerResponse`
- **Returns (raw)**: `ApiResult[RegisterPartnerResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `RegisterPartnerRequest` | `tesla/models/register_partner_request.py` |
| `RegisterPartnerRequestDict` | `tesla/models/register_partner_request.py` |
| `RegisterPartnerResponse` | `tesla/models/register_partner_response.py` |


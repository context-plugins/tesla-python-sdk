# Raw Reference

**Raw** endpoints, reached through `with_raw_response`, return `ApiResult[T, E]` and never raise for an API error. For the parsed endpoints, see [API Reference](api-reference.md).

> Source: [TeslaClient](tesla/client.py)

## Charging

> Source: [Charging](tesla/apis/charging.py)

<details>
<summary><code>def get_charging_history(*, request_options: RequestOptionsOrDict | None = None) -> ApiResult[ChargingHistoryResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Returns the paginated charging history for the authenticated account.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.charging.with_raw_response.get_charging_history()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ChargingHistoryResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.charging.with_raw_response.get_charging_history()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ChargingHistoryResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>request_options</code> | <code>[RequestOptionsOrDict](tesla/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](tesla/core/results.py)&#91;[ChargingHistoryResponse](tesla/models/charging_history_response.py), [RawError](tesla/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[ChargingHistoryResponse](tesla/models/charging_history_response.py)</code> -- Charging history retrieved successfully

**On `Failure`**: `error` is <code>[RawError](tesla/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_charging_invoice(id: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[None, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Returns a charging invoice PDF for a charging session.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.charging.with_raw_response.get_charging_invoice(id)
match result:
    case Success():
        ...  # 2xx, no content
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.charging.with_raw_response.get_charging_invoice(id)
match result:
    case Success():
        ...  # 2xx, no content
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>id</code> | <code>str</code> | Charging session invoice identifier |
| <code>request_options</code> | <code>[RequestOptionsOrDict](tesla/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](tesla/core/results.py)&#91;None, [RawError](tesla/core/results.py)&#93;</code>

**On `Success`**: the 2xx carries no content; `payload` is <code>None</code>

**On `Failure`**: `error` is <code>[RawError](tesla/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_charging_sessions(*, request_options: RequestOptionsOrDict | None = None) -> ApiResult[ChargingSessionsResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Returns charging session information. Only available for business fleet owners.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.charging.with_raw_response.get_charging_sessions()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ChargingSessionsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.charging.with_raw_response.get_charging_sessions()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ChargingSessionsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>request_options</code> | <code>[RequestOptionsOrDict](tesla/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](tesla/core/results.py)&#91;[ChargingSessionsResponse](tesla/models/charging_sessions_response.py), [RawError](tesla/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[ChargingSessionsResponse](tesla/models/charging_sessions_response.py)</code> -- Charging sessions retrieved successfully

**On `Failure`**: `error` is <code>[RawError](tesla/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

## Energy

> Source: [Energy](tesla/apis/energy.py)

<details>
<summary><code>def adjust_site_s_backup_reserve(energy_site_id: str, body: BackupRequest | BackupRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[BackupResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `POST` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.energy.with_raw_response.adjust_site_s_backup_reserve(energy_site_id, body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type BackupResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.energy.with_raw_response.adjust_site_s_backup_reserve(energy_site_id, body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type BackupResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>energy_site_id</code> | <code>str</code> | Value sent with the request. |
| <code>body</code> | <code>[BackupRequest](tesla/models/backup_request.py) \| [BackupRequestDict](tesla/models/backup_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](tesla/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](tesla/core/results.py)&#91;[BackupResponse](tesla/models/backup_response.py), [RawError](tesla/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[BackupResponse](tesla/models/backup_response.py)</code> -- Backup reserve updated

**On `Failure`**: `error` is <code>[RawError](tesla/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def adjust_site_s_off_grid_vehicle_charging_reserve(energy_site_id: str, body: OffGridVehicleChargingReserveRequest | OffGridVehicleChargingReserveRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[GenericUpdateResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `POST` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.energy.with_raw_response.adjust_site_s_off_grid_vehicle_charging_reserve(energy_site_id, body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type GenericUpdateResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.energy.with_raw_response.adjust_site_s_off_grid_vehicle_charging_reserve(
    energy_site_id, body
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type GenericUpdateResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>energy_site_id</code> | <code>str</code> | Value sent with the request. |
| <code>body</code> | <code>[OffGridVehicleChargingReserveRequest](tesla/models/off_grid_vehicle_charging_reserve_request.py) \| [OffGridVehicleChargingReserveRequestDict](tesla/models/off_grid_vehicle_charging_reserve_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](tesla/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](tesla/core/results.py)&#91;[GenericUpdateResponse](tesla/models/generic_update_response.py), [RawError](tesla/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[GenericUpdateResponse](tesla/models/generic_update_response.py)</code> -- Reserve updated

**On `Failure`**: `error` is <code>[RawError](tesla/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def allow_disallow_charging_from_the_grid_and_exporting_energy_to_the_grid(energy_site_id: str, *, body: Any | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[GenericUpdateResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `POST` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.energy.with_raw_response.allow_disallow_charging_from_the_grid_and_exporting_energy_to_the_grid(
    energy_site_id
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type GenericUpdateResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.energy.with_raw_response.allow_disallow_charging_from_the_grid_and_exporting_energy_to_the_grid(
    energy_site_id
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type GenericUpdateResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>energy_site_id</code> | <code>str</code> | Value sent with the request. |
| <code>body</code> | <code>Any \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](tesla/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](tesla/core/results.py)&#91;[GenericUpdateResponse](tesla/models/generic_update_response.py), [RawError](tesla/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[GenericUpdateResponse](tesla/models/generic_update_response.py)</code> -- Grid import/export updated

**On `Failure`**: `error` is <code>[RawError](tesla/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_backup_or_energy_history(energy_site_id: str, kind: KindOrStr, start_date: RFC3339DateTime, end_date: RFC3339DateTime, *, period: str | None = None, time_zone: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[CalendarHistoryResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `GET` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.energy.with_raw_response.get_backup_or_energy_history(energy_site_id, kind, start_date, end_date)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CalendarHistoryResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.energy.with_raw_response.get_backup_or_energy_history(
    energy_site_id, kind, start_date, end_date
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CalendarHistoryResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>energy_site_id</code> | <code>str</code> | Value sent with the request. |
| <code>kind</code> | <code>[KindOrStr](tesla/models/enums/kind.py)</code> | Value sent with the request. |
| <code>start_date</code> | <code>RFC3339DateTime</code> | Value sent with the request. |
| <code>end_date</code> | <code>RFC3339DateTime</code> | Value sent with the request. |
| <code>period</code> | <code>str \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>time_zone</code> | <code>str \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](tesla/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](tesla/core/results.py)&#91;[CalendarHistoryResponse](tesla/models/calendar_history_response.py), [RawError](tesla/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[CalendarHistoryResponse](tesla/models/calendar_history_response.py)</code> -- History retrieved

**On `Failure`**: `error` is <code>[RawError](tesla/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_live_site_status(energy_site_id: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[LiveStatusResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `GET` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.energy.with_raw_response.get_live_site_status(energy_site_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type LiveStatusResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.energy.with_raw_response.get_live_site_status(energy_site_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type LiveStatusResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>energy_site_id</code> | <code>str</code> | Value sent with the request. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](tesla/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](tesla/core/results.py)&#91;[LiveStatusResponse](tesla/models/live_status_response.py), [RawError](tesla/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[LiveStatusResponse](tesla/models/live_status_response.py)</code> -- Live status retrieved

**On `Failure`**: `error` is <code>[RawError](tesla/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_site_information_assets_settings_features(energy_site_id: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[SiteInfoResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `GET` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.energy.with_raw_response.get_site_information_assets_settings_features(energy_site_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type SiteInfoResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.energy.with_raw_response.get_site_information_assets_settings_features(energy_site_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type SiteInfoResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>energy_site_id</code> | <code>str</code> | Value sent with the request. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](tesla/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](tesla/core/results.py)&#91;[SiteInfoResponse](tesla/models/site_info_response.py), [RawError](tesla/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[SiteInfoResponse](tesla/models/site_info_response.py)</code> -- Site info retrieved

**On `Failure`**: `error` is <code>[RawError](tesla/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_user_products_vehicles_energy_sites(*, request_options: RequestOptionsOrDict | None = None) -> ApiResult[ProductsResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `GET` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.energy.with_raw_response.get_user_products_vehicles_energy_sites()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ProductsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.energy.with_raw_response.get_user_products_vehicles_energy_sites()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ProductsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>request_options</code> | <code>[RequestOptionsOrDict](tesla/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](tesla/core/results.py)&#91;[ProductsResponse](tesla/models/products_response.py), [RawError](tesla/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[ProductsResponse](tesla/models/products_response.py)</code> -- Products retrieved

**On `Failure`**: `error` is <code>[RawError](tesla/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_wall_connector_charging_history(energy_site_id: str, kind: KindGetWallConnectorChargingHistoryOrStr, start_date: RFC3339DateTime, end_date: RFC3339DateTime, *, time_zone: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[ChargeHistoryResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `GET` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.energy.with_raw_response.get_wall_connector_charging_history(energy_site_id, kind, start_date, end_date)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ChargeHistoryResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.energy.with_raw_response.get_wall_connector_charging_history(
    energy_site_id, kind, start_date, end_date
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ChargeHistoryResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>energy_site_id</code> | <code>str</code> | Value sent with the request. |
| <code>kind</code> | <code>[KindGetWallConnectorChargingHistoryOrStr](tesla/models/enums/kind_get_wall_connector_charging_history.py)</code> | Value sent with the request. |
| <code>start_date</code> | <code>RFC3339DateTime</code> | Value sent with the request. |
| <code>end_date</code> | <code>RFC3339DateTime</code> | Value sent with the request. |
| <code>time_zone</code> | <code>str \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](tesla/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](tesla/core/results.py)&#91;[ChargeHistoryResponse](tesla/models/charge_history_response.py), [RawError](tesla/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[ChargeHistoryResponse](tesla/models/charge_history_response.py)</code> -- Charging history retrieved

**On `Failure`**: `error` is <code>[RawError](tesla/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def set_site_mode_autonomous_or_self_consumption(energy_site_id: str, body: OperationRequest | OperationRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[GenericUpdateResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `POST` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.energy.with_raw_response.set_site_mode_autonomous_or_self_consumption(energy_site_id, body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type GenericUpdateResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.energy.with_raw_response.set_site_mode_autonomous_or_self_consumption(energy_site_id, body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type GenericUpdateResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>energy_site_id</code> | <code>str</code> | Value sent with the request. |
| <code>body</code> | <code>[OperationRequest](tesla/models/operation_request.py) \| [OperationRequestDict](tesla/models/operation_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](tesla/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](tesla/core/results.py)&#91;[GenericUpdateResponse](tesla/models/generic_update_response.py), [RawError](tesla/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[GenericUpdateResponse](tesla/models/generic_update_response.py)</code> -- Operation mode updated

**On `Failure`**: `error` is <code>[RawError](tesla/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def update_storm_watch_participation(energy_site_id: str, body: StormModeRequest | StormModeRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[GenericUpdateResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `POST` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.energy.with_raw_response.update_storm_watch_participation(energy_site_id, body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type GenericUpdateResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.energy.with_raw_response.update_storm_watch_participation(energy_site_id, body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type GenericUpdateResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>energy_site_id</code> | <code>str</code> | Value sent with the request. |
| <code>body</code> | <code>[StormModeRequest](tesla/models/storm_mode_request.py) \| [StormModeRequestDict](tesla/models/storm_mode_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](tesla/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](tesla/core/results.py)&#91;[GenericUpdateResponse](tesla/models/generic_update_response.py), [RawError](tesla/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[GenericUpdateResponse](tesla/models/generic_update_response.py)</code> -- Storm mode updated

**On `Failure`**: `error` is <code>[RawError](tesla/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def update_time_of_use_tou_settings(energy_site_id: str, body: TimeOfUseSettingsRequest | TimeOfUseSettingsRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[GenericUpdateResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `POST` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.energy.with_raw_response.update_time_of_use_tou_settings(energy_site_id, body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type GenericUpdateResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.energy.with_raw_response.update_time_of_use_tou_settings(energy_site_id, body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type GenericUpdateResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>energy_site_id</code> | <code>str</code> | Value sent with the request. |
| <code>body</code> | <code>[TimeOfUseSettingsRequest](tesla/models/time_of_use_settings_request.py) \| [TimeOfUseSettingsRequestDict](tesla/models/time_of_use_settings_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](tesla/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](tesla/core/results.py)&#91;[GenericUpdateResponse](tesla/models/generic_update_response.py), [RawError](tesla/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[GenericUpdateResponse](tesla/models/generic_update_response.py)</code> -- TOU settings updated

**On `Failure`**: `error` is <code>[RawError](tesla/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

## Partner

> Source: [Partner](tesla/apis/partner.py)

<details>
<summary><code>def get_public_key_for_a_domain(domain: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[PublicKeyResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `GET` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.partner.with_raw_response.get_public_key_for_a_domain(domain)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type PublicKeyResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.partner.with_raw_response.get_public_key_for_a_domain(domain)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type PublicKeyResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>domain</code> | <code>str</code> | Value sent with the request. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](tesla/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](tesla/core/results.py)&#91;[PublicKeyResponse](tesla/models/public_key_response.py), [RawError](tesla/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[PublicKeyResponse](tesla/models/public_key_response.py)</code> -- Public key retrieved

**On `Failure`**: `error` is <code>[RawError](tesla/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_recent_fleet_telemetry_errors(*, request_options: RequestOptionsOrDict | None = None) -> ApiResult[FleetTelemetryErrorsResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `GET` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.partner.with_raw_response.get_recent_fleet_telemetry_errors()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type FleetTelemetryErrorsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.partner.with_raw_response.get_recent_fleet_telemetry_errors()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type FleetTelemetryErrorsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>request_options</code> | <code>[RequestOptionsOrDict](tesla/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](tesla/core/results.py)&#91;[FleetTelemetryErrorsResponse](tesla/models/fleet_telemetry_errors_response.py), [RawError](tesla/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[FleetTelemetryErrorsResponse](tesla/models/fleet_telemetry_errors_response.py)</code> -- Fleet telemetry errors retrieved

**On `Failure`**: `error` is <code>[RawError](tesla/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_vins_with_fleet_telemetry_errors(*, request_options: RequestOptionsOrDict | None = None) -> ApiResult[BackupResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `GET` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.partner.with_raw_response.get_vins_with_fleet_telemetry_errors()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type BackupResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.partner.with_raw_response.get_vins_with_fleet_telemetry_errors()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type BackupResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>request_options</code> | <code>[RequestOptionsOrDict](tesla/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](tesla/core/results.py)&#91;[BackupResponse](tesla/models/backup_response.py), [RawError](tesla/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[BackupResponse](tesla/models/backup_response.py)</code> -- List of VINs with telemetry errors

**On `Failure`**: `error` is <code>[RawError](tesla/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def register_a_partner_account(body: RegisterPartnerRequest | RegisterPartnerRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[RegisterPartnerResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `POST` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.partner.with_raw_response.register_a_partner_account(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type RegisterPartnerResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.partner.with_raw_response.register_a_partner_account(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type RegisterPartnerResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[RegisterPartnerRequest](tesla/models/register_partner_request.py) \| [RegisterPartnerRequestDict](tesla/models/register_partner_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](tesla/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](tesla/core/results.py)&#91;[RegisterPartnerResponse](tesla/models/register_partner_response.py), [RawError](tesla/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[RegisterPartnerResponse](tesla/models/register_partner_response.py)</code> -- Partner account registered

**On `Failure`**: `error` is <code>[RawError](tesla/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

## User

> Source: [User](tesla/apis/user.py)

<details>
<summary><code>def get_active_orders_for_a_user(*, request_options: RequestOptionsOrDict | None = None) -> ApiResult[OrdersResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `GET` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.user.with_raw_response.get_active_orders_for_a_user()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type OrdersResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.user.with_raw_response.get_active_orders_for_a_user()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type OrdersResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>request_options</code> | <code>[RequestOptionsOrDict](tesla/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](tesla/core/results.py)&#91;[OrdersResponse](tesla/models/orders_response.py), [RawError](tesla/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[OrdersResponse](tesla/models/orders_response.py)</code> -- User orders retrieved

**On `Failure`**: `error` is <code>[RawError](tesla/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_custom_feature_flags_for_a_user(*, request_options: RequestOptionsOrDict | None = None) -> ApiResult[BackupResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `GET` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.user.with_raw_response.get_custom_feature_flags_for_a_user()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type BackupResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.user.with_raw_response.get_custom_feature_flags_for_a_user()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type BackupResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>request_options</code> | <code>[RequestOptionsOrDict](tesla/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](tesla/core/results.py)&#91;[BackupResponse](tesla/models/backup_response.py), [RawError](tesla/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[BackupResponse](tesla/models/backup_response.py)</code> -- Feature flags retrieved

**On `Failure`**: `error` is <code>[RawError](tesla/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_summary_of_a_user_s_account(*, request_options: RequestOptionsOrDict | None = None) -> ApiResult[MeResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `GET` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.user.with_raw_response.get_summary_of_a_user_s_account()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type MeResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.user.with_raw_response.get_summary_of_a_user_s_account()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type MeResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>request_options</code> | <code>[RequestOptionsOrDict](tesla/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](tesla/core/results.py)&#91;[MeResponse](tesla/models/me_response.py), [RawError](tesla/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[MeResponse](tesla/models/me_response.py)</code> -- User account retrieved

**On `Failure`**: `error` is <code>[RawError](tesla/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_user_s_region_and_fleet_api_base_url(*, request_options: RequestOptionsOrDict | None = None) -> ApiResult[RegionResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `GET` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.user.with_raw_response.get_user_s_region_and_fleet_api_base_url()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type RegionResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.user.with_raw_response.get_user_s_region_and_fleet_api_base_url()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type RegionResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>request_options</code> | <code>[RequestOptionsOrDict](tesla/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](tesla/core/results.py)&#91;[RegionResponse](tesla/models/region_response.py), [RawError](tesla/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[RegionResponse](tesla/models/region_response.py)</code> -- Region information retrieved

**On `Failure`**: `error` is <code>[RawError](tesla/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

## VehicleCommands

> Source: [VehicleCommands](tesla/apis/vehicle_commands.py)

<details>
<summary><code>def actuatetrunk(vehicle_tag: str, body: ActuateTrunkRequest | ActuateTrunkRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[CommandResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Controls the front or rear trunk

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.vehicle_commands.with_raw_response.actuatetrunk(vehicle_tag, body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CommandResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.vehicle_commands.with_raw_response.actuatetrunk(vehicle_tag, body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CommandResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>vehicle_tag</code> | <code>str</code> | Value sent with the request. |
| <code>body</code> | <code>[ActuateTrunkRequest](tesla/models/actuate_trunk_request.py) \| [ActuateTrunkRequestDict](tesla/models/actuate_trunk_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](tesla/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](tesla/core/results.py)&#91;[CommandResponse](tesla/models/command_response.py), [RawError](tesla/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[CommandResponse](tesla/models/command_response.py)</code> -- Vehicle command response

**On `Failure`**: `error` is <code>[RawError](tesla/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def addchargeschedule(vehicle_tag: str, body: AddChargeScheduleRequest | AddChargeScheduleRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[CommandResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `POST` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.vehicle_commands.with_raw_response.addchargeschedule(vehicle_tag, body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CommandResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.vehicle_commands.with_raw_response.addchargeschedule(vehicle_tag, body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CommandResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>vehicle_tag</code> | <code>str</code> | Value sent with the request. |
| <code>body</code> | <code>[AddChargeScheduleRequest](tesla/models/add_charge_schedule_request.py) \| [AddChargeScheduleRequestDict](tesla/models/add_charge_schedule_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](tesla/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](tesla/core/results.py)&#91;[CommandResponse](tesla/models/command_response.py), [RawError](tesla/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[CommandResponse](tesla/models/command_response.py)</code> -- Vehicle command response

**On `Failure`**: `error` is <code>[RawError](tesla/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def addpreconditionschedule(vehicle_tag: str, body: AddPreconditionScheduleRequest | AddPreconditionScheduleRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[CommandResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `POST` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.vehicle_commands.with_raw_response.addpreconditionschedule(vehicle_tag, body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CommandResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.vehicle_commands.with_raw_response.addpreconditionschedule(vehicle_tag, body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CommandResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>vehicle_tag</code> | <code>str</code> | Value sent with the request. |
| <code>body</code> | <code>[AddPreconditionScheduleRequest](tesla/models/add_precondition_schedule_request.py) \| [AddPreconditionScheduleRequestDict](tesla/models/add_precondition_schedule_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](tesla/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](tesla/core/results.py)&#91;[CommandResponse](tesla/models/command_response.py), [RawError](tesla/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[CommandResponse](tesla/models/command_response.py)</code> -- Vehicle command response

**On `Failure`**: `error` is <code>[RawError](tesla/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def adjustmediavolume(vehicle_tag: str, body: AdjustVolumeRequest | AdjustVolumeRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[CommandResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `POST` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.vehicle_commands.with_raw_response.adjustmediavolume(vehicle_tag, body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CommandResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.vehicle_commands.with_raw_response.adjustmediavolume(vehicle_tag, body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CommandResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>vehicle_tag</code> | <code>str</code> | Value sent with the request. |
| <code>body</code> | <code>[AdjustVolumeRequest](tesla/models/adjust_volume_request.py) \| [AdjustVolumeRequestDict](tesla/models/adjust_volume_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](tesla/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](tesla/core/results.py)&#91;[CommandResponse](tesla/models/command_response.py), [RawError](tesla/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[CommandResponse](tesla/models/command_response.py)</code> -- Vehicle command response

**On `Failure`**: `error` is <code>[RawError](tesla/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def cancelsoftwareupdate(vehicle_tag: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[CommandResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `POST` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.vehicle_commands.with_raw_response.cancelsoftwareupdate(vehicle_tag)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CommandResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.vehicle_commands.with_raw_response.cancelsoftwareupdate(vehicle_tag)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CommandResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>vehicle_tag</code> | <code>str</code> | Value sent with the request. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](tesla/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](tesla/core/results.py)&#91;[CommandResponse](tesla/models/command_response.py), [RawError](tesla/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[CommandResponse](tesla/models/command_response.py)</code> -- Vehicle command response

**On `Failure`**: `error` is <code>[RawError](tesla/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def chargemaxrange(vehicle_tag: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[CommandResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `POST` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.vehicle_commands.with_raw_response.chargemaxrange(vehicle_tag)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CommandResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.vehicle_commands.with_raw_response.chargemaxrange(vehicle_tag)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CommandResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>vehicle_tag</code> | <code>str</code> | Value sent with the request. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](tesla/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](tesla/core/results.py)&#91;[CommandResponse](tesla/models/command_response.py), [RawError](tesla/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[CommandResponse](tesla/models/command_response.py)</code> -- Vehicle command response

**On `Failure`**: `error` is <code>[RawError](tesla/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def chargestandard(vehicle_tag: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[CommandResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `POST` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.vehicle_commands.with_raw_response.chargestandard(vehicle_tag)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CommandResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.vehicle_commands.with_raw_response.chargestandard(vehicle_tag)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CommandResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>vehicle_tag</code> | <code>str</code> | Value sent with the request. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](tesla/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](tesla/core/results.py)&#91;[CommandResponse](tesla/models/command_response.py), [RawError](tesla/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[CommandResponse](tesla/models/command_response.py)</code> -- Vehicle command response

**On `Failure`**: `error` is <code>[RawError](tesla/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def clear_pi_nto_drive_admin(vehicle_tag: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[CommandResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Deactivates PIN to Drive and resets the associated PIN for supported firmware versions.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.vehicle_commands.with_raw_response.clear_pi_nto_drive_admin(vehicle_tag)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CommandResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.vehicle_commands.with_raw_response.clear_pi_nto_drive_admin(vehicle_tag)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CommandResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>vehicle_tag</code> | <code>str</code> | Value sent with the request. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](tesla/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](tesla/core/results.py)&#91;[CommandResponse](tesla/models/command_response.py), [RawError](tesla/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[CommandResponse](tesla/models/command_response.py)</code> -- Vehicle command response

**On `Failure`**: `error` is <code>[RawError](tesla/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def closechargeportdoor(vehicle_tag: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[CommandResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `POST` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.vehicle_commands.with_raw_response.closechargeportdoor(vehicle_tag)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CommandResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.vehicle_commands.with_raw_response.closechargeportdoor(vehicle_tag)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CommandResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>vehicle_tag</code> | <code>str</code> | Value sent with the request. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](tesla/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](tesla/core/results.py)&#91;[CommandResponse](tesla/models/command_response.py), [RawError](tesla/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[CommandResponse](tesla/models/command_response.py)</code> -- Vehicle command response

**On `Failure`**: `error` is <code>[RawError](tesla/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def enableordisable_guest_mode(vehicle_tag: str, body: GuestModeRequest | GuestModeRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[CommandResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `POST` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.vehicle_commands.with_raw_response.enableordisable_guest_mode(vehicle_tag, body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CommandResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.vehicle_commands.with_raw_response.enableordisable_guest_mode(vehicle_tag, body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CommandResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>vehicle_tag</code> | <code>str</code> | Value sent with the request. |
| <code>body</code> | <code>[GuestModeRequest](tesla/models/guest_mode_request.py) \| [GuestModeRequestDict](tesla/models/guest_mode_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](tesla/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](tesla/core/results.py)&#91;[CommandResponse](tesla/models/command_response.py), [RawError](tesla/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[CommandResponse](tesla/models/command_response.py)</code> -- Vehicle command response

**On `Failure`**: `error` is <code>[RawError](tesla/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def eraseuserdata(vehicle_tag: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[CommandResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Erases user data from the vehicle UI. Requires Guest Mode.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.vehicle_commands.with_raw_response.eraseuserdata(vehicle_tag)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CommandResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.vehicle_commands.with_raw_response.eraseuserdata(vehicle_tag)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CommandResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>vehicle_tag</code> | <code>str</code> | Value sent with the request. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](tesla/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](tesla/core/results.py)&#91;[CommandResponse](tesla/models/command_response.py), [RawError](tesla/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[CommandResponse](tesla/models/command_response.py)</code> -- Vehicle command response

**On `Failure`**: `error` is <code>[RawError](tesla/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def flashlights(vehicle_tag: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[CommandResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Briefly flashes vehicle headlights.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.vehicle_commands.with_raw_response.flashlights(vehicle_tag)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CommandResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.vehicle_commands.with_raw_response.flashlights(vehicle_tag)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CommandResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>vehicle_tag</code> | <code>str</code> | Value sent with the request. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](tesla/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](tesla/core/results.py)&#91;[CommandResponse](tesla/models/command_response.py), [RawError](tesla/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[CommandResponse](tesla/models/command_response.py)</code> -- Vehicle command response

**On `Failure`**: `error` is <code>[RawError](tesla/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def honkhorn(vehicle_tag: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[CommandResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `POST` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.vehicle_commands.with_raw_response.honkhorn(vehicle_tag)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CommandResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.vehicle_commands.with_raw_response.honkhorn(vehicle_tag)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CommandResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>vehicle_tag</code> | <code>str</code> | Value sent with the request. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](tesla/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](tesla/core/results.py)&#91;[CommandResponse](tesla/models/command_response.py), [RawError](tesla/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[CommandResponse](tesla/models/command_response.py)</code> -- Vehicle command response

**On `Failure`**: `error` is <code>[RawError](tesla/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def lockdoors(vehicle_tag: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[CommandResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `POST` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.vehicle_commands.with_raw_response.lockdoors(vehicle_tag)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CommandResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.vehicle_commands.with_raw_response.lockdoors(vehicle_tag)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CommandResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>vehicle_tag</code> | <code>str</code> | Value sent with the request. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](tesla/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](tesla/core/results.py)&#91;[CommandResponse](tesla/models/command_response.py), [RawError](tesla/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[CommandResponse](tesla/models/command_response.py)</code> -- Vehicle command response

**On `Failure`**: `error` is <code>[RawError](tesla/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def nextfavoritemediatrack(vehicle_tag: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[CommandResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `POST` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.vehicle_commands.with_raw_response.nextfavoritemediatrack(vehicle_tag)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CommandResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.vehicle_commands.with_raw_response.nextfavoritemediatrack(vehicle_tag)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CommandResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>vehicle_tag</code> | <code>str</code> | Value sent with the request. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](tesla/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](tesla/core/results.py)&#91;[CommandResponse](tesla/models/command_response.py), [RawError](tesla/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[CommandResponse](tesla/models/command_response.py)</code> -- Vehicle command response

**On `Failure`**: `error` is <code>[RawError](tesla/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def openchargeportdoor(vehicle_tag: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[CommandResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `POST` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.vehicle_commands.with_raw_response.openchargeportdoor(vehicle_tag)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CommandResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.vehicle_commands.with_raw_response.openchargeportdoor(vehicle_tag)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CommandResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>vehicle_tag</code> | <code>str</code> | Value sent with the request. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](tesla/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](tesla/core/results.py)&#91;[CommandResponse](tesla/models/command_response.py), [RawError](tesla/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[CommandResponse](tesla/models/command_response.py)</code> -- Vehicle command response

**On `Failure`**: `error` is <code>[RawError](tesla/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def startcharging(vehicle_tag: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[CommandResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `POST` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.vehicle_commands.with_raw_response.startcharging(vehicle_tag)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CommandResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.vehicle_commands.with_raw_response.startcharging(vehicle_tag)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CommandResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>vehicle_tag</code> | <code>str</code> | Value sent with the request. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](tesla/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](tesla/core/results.py)&#91;[CommandResponse](tesla/models/command_response.py), [RawError](tesla/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[CommandResponse](tesla/models/command_response.py)</code> -- Vehicle command response

**On `Failure`**: `error` is <code>[RawError](tesla/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def startclimatepreconditioning(vehicle_tag: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[CommandResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `POST` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.vehicle_commands.with_raw_response.startclimatepreconditioning(vehicle_tag)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CommandResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.vehicle_commands.with_raw_response.startclimatepreconditioning(vehicle_tag)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CommandResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>vehicle_tag</code> | <code>str</code> | Value sent with the request. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](tesla/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](tesla/core/results.py)&#91;[CommandResponse](tesla/models/command_response.py), [RawError](tesla/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[CommandResponse](tesla/models/command_response.py)</code> -- Vehicle command response

**On `Failure`**: `error` is <code>[RawError](tesla/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def stopcharging(vehicle_tag: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[CommandResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `POST` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.vehicle_commands.with_raw_response.stopcharging(vehicle_tag)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CommandResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.vehicle_commands.with_raw_response.stopcharging(vehicle_tag)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CommandResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>vehicle_tag</code> | <code>str</code> | Value sent with the request. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](tesla/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](tesla/core/results.py)&#91;[CommandResponse](tesla/models/command_response.py), [RawError](tesla/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[CommandResponse](tesla/models/command_response.py)</code> -- Vehicle command response

**On `Failure`**: `error` is <code>[RawError](tesla/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def stopclimatepreconditioning(vehicle_tag: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[CommandResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `POST` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.vehicle_commands.with_raw_response.stopclimatepreconditioning(vehicle_tag)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CommandResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.vehicle_commands.with_raw_response.stopclimatepreconditioning(vehicle_tag)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CommandResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>vehicle_tag</code> | <code>str</code> | Value sent with the request. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](tesla/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](tesla/core/results.py)&#91;[CommandResponse](tesla/models/command_response.py), [RawError](tesla/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[CommandResponse](tesla/models/command_response.py)</code> -- Vehicle command response

**On `Failure`**: `error` is <code>[RawError](tesla/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def unlockdoors(vehicle_tag: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[CommandResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `POST` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.vehicle_commands.with_raw_response.unlockdoors(vehicle_tag)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CommandResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.vehicle_commands.with_raw_response.unlockdoors(vehicle_tag)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CommandResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>vehicle_tag</code> | <code>str</code> | Value sent with the request. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](tesla/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](tesla/core/results.py)&#91;[CommandResponse](tesla/models/command_response.py), [RawError](tesla/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[CommandResponse](tesla/models/command_response.py)</code> -- Vehicle command response

**On `Failure`**: `error` is <code>[RawError](tesla/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

## Vehicles

> Source: [Vehicles](tesla/apis/vehicles.py)

<details>
<summary><code>def configure_fleet_telemetry_using_signed_jws_token(body: FleetTelemetryJwsRequest | FleetTelemetryJwsRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[Any, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `POST` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.vehicles.with_raw_response.configure_fleet_telemetry_using_signed_jws_token(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type Any
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.vehicles.with_raw_response.configure_fleet_telemetry_using_signed_jws_token(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type Any
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[FleetTelemetryJwsRequest](tesla/models/fleet_telemetry_jws_request.py) \| [FleetTelemetryJwsRequestDict](tesla/models/fleet_telemetry_jws_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](tesla/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](tesla/core/results.py)&#91;Any, [RawError](tesla/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>Any</code> -- Telemetry configuration result

**On `Failure`**: `error` is <code>[RawError](tesla/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def create_or_update_fleet_telemetry_configuration(body: Any, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[Any, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `POST` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.vehicles.with_raw_response.create_or_update_fleet_telemetry_configuration(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type Any
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.vehicles.with_raw_response.create_or_update_fleet_telemetry_configuration(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type Any
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>Any</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](tesla/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](tesla/core/results.py)&#91;Any, [RawError](tesla/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>Any</code> -- Telemetry configuration result

**On `Failure`**: `error` is <code>[RawError](tesla/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def delete_fleet_telemetry_configuration(vehicle_tag: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[Any, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `DELETE` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.vehicles.with_raw_response.delete_fleet_telemetry_configuration(vehicle_tag)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type Any
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.vehicles.with_raw_response.delete_fleet_telemetry_configuration(vehicle_tag)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type Any
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>vehicle_tag</code> | <code>str</code> | Value sent with the request. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](tesla/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](tesla/core/results.py)&#91;Any, [RawError](tesla/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>Any</code> -- Configuration deleted

**On `Failure`**: `error` is <code>[RawError](tesla/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_allowed_drivers_for_a_vehicle(vehicle_tag: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[DriversResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `GET` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.vehicles.with_raw_response.get_allowed_drivers_for_a_vehicle(vehicle_tag)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type DriversResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.vehicles.with_raw_response.get_allowed_drivers_for_a_vehicle(vehicle_tag)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type DriversResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>vehicle_tag</code> | <code>str</code> | Value sent with the request. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](tesla/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](tesla/core/results.py)&#91;[DriversResponse](tesla/models/drivers_response.py), [RawError](tesla/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[DriversResponse](tesla/models/drivers_response.py)</code> -- List of drivers

**On `Failure`**: `error` is <code>[RawError](tesla/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_eligible_vehicle_subscriptions(vin: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[SiteInfoResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `GET` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.vehicles.with_raw_response.get_eligible_vehicle_subscriptions(vin)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type SiteInfoResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.vehicles.with_raw_response.get_eligible_vehicle_subscriptions(vin)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type SiteInfoResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>vin</code> | <code>str</code> | Value sent with the request. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](tesla/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](tesla/core/results.py)&#91;[SiteInfoResponse](tesla/models/site_info_response.py), [RawError](tesla/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[SiteInfoResponse](tesla/models/site_info_response.py)</code> -- Eligible subscriptions

**On `Failure`**: `error` is <code>[RawError](tesla/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_eligible_vehicle_upgrades(vin: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[SiteInfoResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `GET` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.vehicles.with_raw_response.get_eligible_vehicle_upgrades(vin)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type SiteInfoResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.vehicles.with_raw_response.get_eligible_vehicle_upgrades(vin)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type SiteInfoResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>vin</code> | <code>str</code> | Value sent with the request. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](tesla/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](tesla/core/results.py)&#91;[SiteInfoResponse](tesla/models/site_info_response.py), [RawError](tesla/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[SiteInfoResponse](tesla/models/site_info_response.py)</code> -- Eligible upgrades

**On `Failure`**: `error` is <code>[RawError](tesla/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_enterprise_roles_for_a_vehicle(vin: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[Any, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `GET` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.vehicles.with_raw_response.get_enterprise_roles_for_a_vehicle(vin)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type Any
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.vehicles.with_raw_response.get_enterprise_roles_for_a_vehicle(vin)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type Any
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>vin</code> | <code>str</code> | Value sent with the request. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](tesla/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](tesla/core/results.py)&#91;Any, [RawError](tesla/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>Any</code> -- Enterprise roles

**On `Failure`**: `error` is <code>[RawError](tesla/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_fleet_status_for_vehicles(body: FleetStatusRequest | FleetStatusRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[Any, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `POST` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.vehicles.with_raw_response.get_fleet_status_for_vehicles(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type Any
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.vehicles.with_raw_response.get_fleet_status_for_vehicles(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type Any
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[FleetStatusRequest](tesla/models/fleet_status_request.py) \| [FleetStatusRequestDict](tesla/models/fleet_status_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](tesla/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](tesla/core/results.py)&#91;Any, [RawError](tesla/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>Any</code> -- Fleet status

**On `Failure`**: `error` is <code>[RawError](tesla/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_fleet_telemetry_configuration(vehicle_tag: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[Any, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `GET` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.vehicles.with_raw_response.get_fleet_telemetry_configuration(vehicle_tag)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type Any
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.vehicles.with_raw_response.get_fleet_telemetry_configuration(vehicle_tag)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type Any
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>vehicle_tag</code> | <code>str</code> | Value sent with the request. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](tesla/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](tesla/core/results.py)&#91;Any, [RawError](tesla/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>Any</code> -- Fleet telemetry configuration

**On `Failure`**: `error` is <code>[RawError](tesla/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_fleet_telemetry_errors_for_a_vehicle(vehicle_tag: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[Any, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `GET` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.vehicles.with_raw_response.get_fleet_telemetry_errors_for_a_vehicle(vehicle_tag)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type Any
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.vehicles.with_raw_response.get_fleet_telemetry_errors_for_a_vehicle(vehicle_tag)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type Any
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>vehicle_tag</code> | <code>str</code> | Value sent with the request. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](tesla/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](tesla/core/results.py)&#91;Any, [RawError](tesla/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>Any</code> -- Fleet telemetry errors

**On `Failure`**: `error` is <code>[RawError](tesla/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_vehicle(vehicle_tag: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[Api1VehiclesResponseResponse200, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `GET` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.vehicles.with_raw_response.get_vehicle(vehicle_tag)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type Api1VehiclesResponseResponse200
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.vehicles.with_raw_response.get_vehicle(vehicle_tag)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type Api1VehiclesResponseResponse200
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>vehicle_tag</code> | <code>str</code> | Value sent with the request. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](tesla/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](tesla/core/results.py)&#91;[Api1VehiclesResponseResponse200](tesla/models/api1_vehicles_response_response200.py), [RawError](tesla/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[Api1VehiclesResponseResponse200](tesla/models/api1_vehicles_response_response200.py)</code> -- Vehicle info

**On `Failure`**: `error` is <code>[RawError](tesla/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def list_vehicles(*, request_options: RequestOptionsOrDict | None = None) -> ApiResult[Api1VehiclesResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `GET` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.vehicles.with_raw_response.list_vehicles()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type Api1VehiclesResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.vehicles.with_raw_response.list_vehicles()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type Api1VehiclesResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>request_options</code> | <code>[RequestOptionsOrDict](tesla/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](tesla/core/results.py)&#91;[Api1VehiclesResponse](tesla/models/api1_vehicles_response.py), [RawError](tesla/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[Api1VehiclesResponse](tesla/models/api1_vehicles_response.py)</code> -- Vehicles list

**On `Failure`**: `error` is <code>[RawError](tesla/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def mobile_enabled(vehicle_tag: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[Api1VehiclesMobileEnabledResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `GET` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.vehicles.with_raw_response.mobile_enabled(vehicle_tag)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type Api1VehiclesMobileEnabledResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.vehicles.with_raw_response.mobile_enabled(vehicle_tag)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type Api1VehiclesMobileEnabledResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>vehicle_tag</code> | <code>str</code> | Value sent with the request. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](tesla/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](tesla/core/results.py)&#91;[Api1VehiclesMobileEnabledResponse](tesla/models/api1_vehicles_mobile_enabled_response.py), [RawError](tesla/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[Api1VehiclesMobileEnabledResponse](tesla/models/api1_vehicles_mobile_enabled_response.py)</code> -- Mobile access status

**On `Failure`**: `error` is <code>[RawError](tesla/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def nearby_charging_sites(vehicle_tag: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[Api1VehiclesNearbyChargingSitesResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `GET` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.vehicles.with_raw_response.nearby_charging_sites(vehicle_tag)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type Api1VehiclesNearbyChargingSitesResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.vehicles.with_raw_response.nearby_charging_sites(vehicle_tag)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type Api1VehiclesNearbyChargingSitesResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>vehicle_tag</code> | <code>str</code> | Value sent with the request. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](tesla/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](tesla/core/results.py)&#91;[Api1VehiclesNearbyChargingSitesResponse](tesla/models/api1_vehicles_nearby_charging_sites_response.py), [RawError](tesla/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[Api1VehiclesNearbyChargingSitesResponse](tesla/models/api1_vehicles_nearby_charging_sites_response.py)</code> -- Charging sites

**On `Failure`**: `error` is <code>[RawError](tesla/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def remove_driver_access_from_a_vehicle(vehicle_tag: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[SimpleOkResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `DELETE` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.vehicles.with_raw_response.remove_driver_access_from_a_vehicle(vehicle_tag)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type SimpleOkResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.vehicles.with_raw_response.remove_driver_access_from_a_vehicle(vehicle_tag)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type SimpleOkResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>vehicle_tag</code> | <code>str</code> | Value sent with the request. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](tesla/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](tesla/core/results.py)&#91;[SimpleOkResponse](tesla/models/simple_ok_response.py), [RawError](tesla/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[SimpleOkResponse](tesla/models/simple_ok_response.py)</code> -- Driver removed

**On `Failure`**: `error` is <code>[RawError](tesla/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def set_enterprise_payer_roles(vin: str, body: EnterprisePayerRequest | EnterprisePayerRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[None, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `POST` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.vehicles.with_raw_response.set_enterprise_payer_roles(vin, body)
match result:
    case Success():
        ...  # 2xx, no content
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.vehicles.with_raw_response.set_enterprise_payer_roles(vin, body)
match result:
    case Success():
        ...  # 2xx, no content
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>vin</code> | <code>str</code> | Value sent with the request. |
| <code>body</code> | <code>[EnterprisePayerRequest](tesla/models/enterprise_payer_request.py) \| [EnterprisePayerRequestDict](tesla/models/enterprise_payer_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](tesla/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](tesla/core/results.py)&#91;None, [RawError](tesla/core/results.py)&#93;</code>

**On `Success`**: the 2xx carries no content; `payload` is <code>None</code>

**On `Failure`**: `error` is <code>[RawError](tesla/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def vehicle_live_data(vehicle_tag: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[SiteInfoResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `GET` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.vehicles.with_raw_response.vehicle_live_data(vehicle_tag)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type SiteInfoResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.vehicles.with_raw_response.vehicle_live_data(vehicle_tag)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type SiteInfoResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>vehicle_tag</code> | <code>str</code> | Value sent with the request. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](tesla/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](tesla/core/results.py)&#91;[SiteInfoResponse](tesla/models/site_info_response.py), [RawError](tesla/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[SiteInfoResponse](tesla/models/site_info_response.py)</code> -- Realtime vehicle data

**On `Failure`**: `error` is <code>[RawError](tesla/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def vehicle_options(vin: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[Api1DxVehiclesOptionsResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `GET` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.vehicles.with_raw_response.vehicle_options(vin)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type Api1DxVehiclesOptionsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.vehicles.with_raw_response.vehicle_options(vin)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type Api1DxVehiclesOptionsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>vin</code> | <code>str</code> | Value sent with the request. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](tesla/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](tesla/core/results.py)&#91;[Api1DxVehiclesOptionsResponse](tesla/models/api1_dx_vehicles_options_response.py), [RawError](tesla/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[Api1DxVehiclesOptionsResponse](tesla/models/api1_dx_vehicles_options_response.py)</code> -- Vehicle options

**On `Failure`**: `error` is <code>[RawError](tesla/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def vehicle_specs(vin: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[SiteInfoResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `GET` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.vehicles.with_raw_response.vehicle_specs(vin)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type SiteInfoResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.vehicles.with_raw_response.vehicle_specs(vin)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type SiteInfoResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>vin</code> | <code>str</code> | Value sent with the request. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](tesla/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](tesla/core/results.py)&#91;[SiteInfoResponse](tesla/models/site_info_response.py), [RawError](tesla/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[SiteInfoResponse](tesla/models/site_info_response.py)</code> -- Vehicle specifications

**On `Failure`**: `error` is <code>[RawError](tesla/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def wake_up_vehicle(vehicle_tag: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[Api1VehiclesWakeUpResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `POST` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.vehicles.with_raw_response.wake_up_vehicle(vehicle_tag)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type Api1VehiclesWakeUpResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.vehicles.with_raw_response.wake_up_vehicle(vehicle_tag)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type Api1VehiclesWakeUpResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>vehicle_tag</code> | <code>str</code> | Value sent with the request. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](tesla/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](tesla/core/results.py)&#91;[Api1VehiclesWakeUpResponse](tesla/models/api1_vehicles_wake_up_response.py), [RawError](tesla/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[Api1VehiclesWakeUpResponse](tesla/models/api1_vehicles_wake_up_response.py)</code> -- Vehicle awakened

**On `Failure`**: `error` is <code>[RawError](tesla/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def warranty_details(*, request_options: RequestOptionsOrDict | None = None) -> ApiResult[Api1DxWarrantyDetailsResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `GET` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.vehicles.with_raw_response.warranty_details()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type Api1DxWarrantyDetailsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.vehicles.with_raw_response.warranty_details()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type Api1DxWarrantyDetailsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>request_options</code> | <code>[RequestOptionsOrDict](tesla/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](tesla/core/results.py)&#91;[Api1DxWarrantyDetailsResponse](tesla/models/api1_dx_warranty_details_response.py), [RawError](tesla/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[Api1DxWarrantyDetailsResponse](tesla/models/api1_dx_warranty_details_response.py)</code> -- Warranty information

**On `Failure`**: `error` is <code>[RawError](tesla/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>


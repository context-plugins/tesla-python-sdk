# Reference

**Parsed** endpoints return the typed payload and raise `ApiError` on a documented non-2xx. For the raw endpoints, see [Raw API Reference](raw-api-reference.md).

> Source: [TeslaFleetManagementApiClient](tesla_fleet_management_api/client.py)

## Charging

> Source: [Charging](tesla_fleet_management_api/apis/charging.py)

<details>
<summary><code>def get_charging_history(*, request_options: RequestOptionsOrDict | None = None) -> ChargingHistoryResponse</code></summary>

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
try:
    response = client.charging.get_charging_history()
    # TODO: Handle 'response' of type ChargingHistoryResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.charging.get_charging_history()
    # TODO: Handle 'response' of type ChargingHistoryResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>request_options</code> | <code>[RequestOptionsOrDict](tesla_fleet_management_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[ChargingHistoryResponse](tesla_fleet_management_api/models/charging_history_response.py)</code> -- Charging history retrieved successfully

**OnError**: <code>[ApiError](tesla_fleet_management_api/core/exceptions.py)&#91;[RawError](tesla_fleet_management_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_charging_invoice(id: str, *, request_options: RequestOptionsOrDict | None = None) -> None</code></summary>

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
try:
    client.charging.get_charging_invoice(id)
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    await async_client.charging.get_charging_invoice(id)
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>id</code> | <code>str</code> | Charging session invoice identifier |
| <code>request_options</code> | <code>[RequestOptionsOrDict](tesla_fleet_management_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: No content

**OnError**: <code>[ApiError](tesla_fleet_management_api/core/exceptions.py)&#91;[RawError](tesla_fleet_management_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_charging_sessions(*, request_options: RequestOptionsOrDict | None = None) -> ChargingSessionsResponse</code></summary>

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
try:
    response = client.charging.get_charging_sessions()
    # TODO: Handle 'response' of type ChargingSessionsResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.charging.get_charging_sessions()
    # TODO: Handle 'response' of type ChargingSessionsResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>request_options</code> | <code>[RequestOptionsOrDict](tesla_fleet_management_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[ChargingSessionsResponse](tesla_fleet_management_api/models/charging_sessions_response.py)</code> -- Charging sessions retrieved successfully

**OnError**: <code>[ApiError](tesla_fleet_management_api/core/exceptions.py)&#91;[RawError](tesla_fleet_management_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

## Energy

> Source: [Energy](tesla_fleet_management_api/apis/energy.py)

<details>
<summary><code>def adjust_site_s_backup_reserve(energy_site_id: str, body: BackupRequest | BackupRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> BackupResponse</code></summary>

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
try:
    response = client.energy.adjust_site_s_backup_reserve(energy_site_id, body)
    # TODO: Handle 'response' of type BackupResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.energy.adjust_site_s_backup_reserve(energy_site_id, body)
    # TODO: Handle 'response' of type BackupResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>energy_site_id</code> | <code>str</code> | Value sent with the request. |
| <code>body</code> | <code>[BackupRequest](tesla_fleet_management_api/models/backup_request.py) \| [BackupRequestDict](tesla_fleet_management_api/models/backup_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](tesla_fleet_management_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[BackupResponse](tesla_fleet_management_api/models/backup_response.py)</code> -- Backup reserve updated

**OnError**: <code>[ApiError](tesla_fleet_management_api/core/exceptions.py)&#91;[RawError](tesla_fleet_management_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def adjust_site_s_off_grid_vehicle_charging_reserve(energy_site_id: str, body: OffGridVehicleChargingReserveRequest | OffGridVehicleChargingReserveRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> GenericUpdateResponse</code></summary>

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
try:
    response = client.energy.adjust_site_s_off_grid_vehicle_charging_reserve(energy_site_id, body)
    # TODO: Handle 'response' of type GenericUpdateResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.energy.adjust_site_s_off_grid_vehicle_charging_reserve(energy_site_id, body)
    # TODO: Handle 'response' of type GenericUpdateResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>energy_site_id</code> | <code>str</code> | Value sent with the request. |
| <code>body</code> | <code>[OffGridVehicleChargingReserveRequest](tesla_fleet_management_api/models/off_grid_vehicle_charging_reserve_request.py) \| [OffGridVehicleChargingReserveRequestDict](tesla_fleet_management_api/models/off_grid_vehicle_charging_reserve_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](tesla_fleet_management_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[GenericUpdateResponse](tesla_fleet_management_api/models/generic_update_response.py)</code> -- Reserve updated

**OnError**: <code>[ApiError](tesla_fleet_management_api/core/exceptions.py)&#91;[RawError](tesla_fleet_management_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def allow_disallow_charging_from_the_grid_and_exporting_energy_to_the_grid(energy_site_id: str, *, body: Any | None = None, request_options: RequestOptionsOrDict | None = None) -> GenericUpdateResponse</code></summary>

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
try:
    response = client.energy.allow_disallow_charging_from_the_grid_and_exporting_energy_to_the_grid(energy_site_id)
    # TODO: Handle 'response' of type GenericUpdateResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.energy.allow_disallow_charging_from_the_grid_and_exporting_energy_to_the_grid(
        energy_site_id
    )
    # TODO: Handle 'response' of type GenericUpdateResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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
| <code>request_options</code> | <code>[RequestOptionsOrDict](tesla_fleet_management_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[GenericUpdateResponse](tesla_fleet_management_api/models/generic_update_response.py)</code> -- Grid import/export updated

**OnError**: <code>[ApiError](tesla_fleet_management_api/core/exceptions.py)&#91;[RawError](tesla_fleet_management_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_backup_or_energy_history(energy_site_id: str, kind: KindOrStr, start_date: RFC3339DateTime, end_date: RFC3339DateTime, *, period: str | None = None, time_zone: str | None = None, request_options: RequestOptionsOrDict | None = None) -> CalendarHistoryResponse</code></summary>

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
try:
    response = client.energy.get_backup_or_energy_history(energy_site_id, kind, start_date, end_date)
    # TODO: Handle 'response' of type CalendarHistoryResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.energy.get_backup_or_energy_history(energy_site_id, kind, start_date, end_date)
    # TODO: Handle 'response' of type CalendarHistoryResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>energy_site_id</code> | <code>str</code> | Value sent with the request. |
| <code>kind</code> | <code>[KindOrStr](tesla_fleet_management_api/models/enums/kind.py)</code> | Value sent with the request. |
| <code>start_date</code> | <code>RFC3339DateTime</code> | Value sent with the request. |
| <code>end_date</code> | <code>RFC3339DateTime</code> | Value sent with the request. |
| <code>period</code> | <code>str \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>time_zone</code> | <code>str \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](tesla_fleet_management_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[CalendarHistoryResponse](tesla_fleet_management_api/models/calendar_history_response.py)</code> -- History retrieved

**OnError**: <code>[ApiError](tesla_fleet_management_api/core/exceptions.py)&#91;[RawError](tesla_fleet_management_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_live_site_status(energy_site_id: str, *, request_options: RequestOptionsOrDict | None = None) -> LiveStatusResponse</code></summary>

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
try:
    response = client.energy.get_live_site_status(energy_site_id)
    # TODO: Handle 'response' of type LiveStatusResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.energy.get_live_site_status(energy_site_id)
    # TODO: Handle 'response' of type LiveStatusResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>energy_site_id</code> | <code>str</code> | Value sent with the request. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](tesla_fleet_management_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[LiveStatusResponse](tesla_fleet_management_api/models/live_status_response.py)</code> -- Live status retrieved

**OnError**: <code>[ApiError](tesla_fleet_management_api/core/exceptions.py)&#91;[RawError](tesla_fleet_management_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_site_information_assets_settings_features(energy_site_id: str, *, request_options: RequestOptionsOrDict | None = None) -> SiteInfoResponse</code></summary>

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
try:
    response = client.energy.get_site_information_assets_settings_features(energy_site_id)
    # TODO: Handle 'response' of type SiteInfoResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.energy.get_site_information_assets_settings_features(energy_site_id)
    # TODO: Handle 'response' of type SiteInfoResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>energy_site_id</code> | <code>str</code> | Value sent with the request. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](tesla_fleet_management_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SiteInfoResponse](tesla_fleet_management_api/models/site_info_response.py)</code> -- Site info retrieved

**OnError**: <code>[ApiError](tesla_fleet_management_api/core/exceptions.py)&#91;[RawError](tesla_fleet_management_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_user_products_vehicles_energy_sites(*, request_options: RequestOptionsOrDict | None = None) -> ProductsResponse</code></summary>

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
try:
    response = client.energy.get_user_products_vehicles_energy_sites()
    # TODO: Handle 'response' of type ProductsResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.energy.get_user_products_vehicles_energy_sites()
    # TODO: Handle 'response' of type ProductsResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>request_options</code> | <code>[RequestOptionsOrDict](tesla_fleet_management_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[ProductsResponse](tesla_fleet_management_api/models/products_response.py)</code> -- Products retrieved

**OnError**: <code>[ApiError](tesla_fleet_management_api/core/exceptions.py)&#91;[RawError](tesla_fleet_management_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_wall_connector_charging_history(energy_site_id: str, kind: KindGetWallConnectorChargingHistoryOrStr, start_date: RFC3339DateTime, end_date: RFC3339DateTime, *, time_zone: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ChargeHistoryResponse</code></summary>

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
try:
    response = client.energy.get_wall_connector_charging_history(energy_site_id, kind, start_date, end_date)
    # TODO: Handle 'response' of type ChargeHistoryResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.energy.get_wall_connector_charging_history(energy_site_id, kind, start_date, end_date)
    # TODO: Handle 'response' of type ChargeHistoryResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>energy_site_id</code> | <code>str</code> | Value sent with the request. |
| <code>kind</code> | <code>[KindGetWallConnectorChargingHistoryOrStr](tesla_fleet_management_api/models/enums/kind_get_wall_connector_charging_history.py)</code> | Value sent with the request. |
| <code>start_date</code> | <code>RFC3339DateTime</code> | Value sent with the request. |
| <code>end_date</code> | <code>RFC3339DateTime</code> | Value sent with the request. |
| <code>time_zone</code> | <code>str \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](tesla_fleet_management_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[ChargeHistoryResponse](tesla_fleet_management_api/models/charge_history_response.py)</code> -- Charging history retrieved

**OnError**: <code>[ApiError](tesla_fleet_management_api/core/exceptions.py)&#91;[RawError](tesla_fleet_management_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def set_site_mode_autonomous_or_self_consumption(energy_site_id: str, body: OperationRequest | OperationRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> GenericUpdateResponse</code></summary>

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
try:
    response = client.energy.set_site_mode_autonomous_or_self_consumption(energy_site_id, body)
    # TODO: Handle 'response' of type GenericUpdateResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.energy.set_site_mode_autonomous_or_self_consumption(energy_site_id, body)
    # TODO: Handle 'response' of type GenericUpdateResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>energy_site_id</code> | <code>str</code> | Value sent with the request. |
| <code>body</code> | <code>[OperationRequest](tesla_fleet_management_api/models/operation_request.py) \| [OperationRequestDict](tesla_fleet_management_api/models/operation_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](tesla_fleet_management_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[GenericUpdateResponse](tesla_fleet_management_api/models/generic_update_response.py)</code> -- Operation mode updated

**OnError**: <code>[ApiError](tesla_fleet_management_api/core/exceptions.py)&#91;[RawError](tesla_fleet_management_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def update_storm_watch_participation(energy_site_id: str, body: StormModeRequest | StormModeRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> GenericUpdateResponse</code></summary>

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
try:
    response = client.energy.update_storm_watch_participation(energy_site_id, body)
    # TODO: Handle 'response' of type GenericUpdateResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.energy.update_storm_watch_participation(energy_site_id, body)
    # TODO: Handle 'response' of type GenericUpdateResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>energy_site_id</code> | <code>str</code> | Value sent with the request. |
| <code>body</code> | <code>[StormModeRequest](tesla_fleet_management_api/models/storm_mode_request.py) \| [StormModeRequestDict](tesla_fleet_management_api/models/storm_mode_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](tesla_fleet_management_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[GenericUpdateResponse](tesla_fleet_management_api/models/generic_update_response.py)</code> -- Storm mode updated

**OnError**: <code>[ApiError](tesla_fleet_management_api/core/exceptions.py)&#91;[RawError](tesla_fleet_management_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def update_time_of_use_tou_settings(energy_site_id: str, body: TimeOfUseSettingsRequest | TimeOfUseSettingsRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> GenericUpdateResponse</code></summary>

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
try:
    response = client.energy.update_time_of_use_tou_settings(energy_site_id, body)
    # TODO: Handle 'response' of type GenericUpdateResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.energy.update_time_of_use_tou_settings(energy_site_id, body)
    # TODO: Handle 'response' of type GenericUpdateResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>energy_site_id</code> | <code>str</code> | Value sent with the request. |
| <code>body</code> | <code>[TimeOfUseSettingsRequest](tesla_fleet_management_api/models/time_of_use_settings_request.py) \| [TimeOfUseSettingsRequestDict](tesla_fleet_management_api/models/time_of_use_settings_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](tesla_fleet_management_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[GenericUpdateResponse](tesla_fleet_management_api/models/generic_update_response.py)</code> -- TOU settings updated

**OnError**: <code>[ApiError](tesla_fleet_management_api/core/exceptions.py)&#91;[RawError](tesla_fleet_management_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

## Partner

> Source: [Partner](tesla_fleet_management_api/apis/partner.py)

<details>
<summary><code>def get_public_key_for_a_domain(domain: str, *, request_options: RequestOptionsOrDict | None = None) -> PublicKeyResponse</code></summary>

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
try:
    response = client.partner.get_public_key_for_a_domain(domain)
    # TODO: Handle 'response' of type PublicKeyResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.partner.get_public_key_for_a_domain(domain)
    # TODO: Handle 'response' of type PublicKeyResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>domain</code> | <code>str</code> | Value sent with the request. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](tesla_fleet_management_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[PublicKeyResponse](tesla_fleet_management_api/models/public_key_response.py)</code> -- Public key retrieved

**OnError**: <code>[ApiError](tesla_fleet_management_api/core/exceptions.py)&#91;[RawError](tesla_fleet_management_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_recent_fleet_telemetry_errors(*, request_options: RequestOptionsOrDict | None = None) -> FleetTelemetryErrorsResponse</code></summary>

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
try:
    response = client.partner.get_recent_fleet_telemetry_errors()
    # TODO: Handle 'response' of type FleetTelemetryErrorsResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.partner.get_recent_fleet_telemetry_errors()
    # TODO: Handle 'response' of type FleetTelemetryErrorsResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>request_options</code> | <code>[RequestOptionsOrDict](tesla_fleet_management_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[FleetTelemetryErrorsResponse](tesla_fleet_management_api/models/fleet_telemetry_errors_response.py)</code> -- Fleet telemetry errors retrieved

**OnError**: <code>[ApiError](tesla_fleet_management_api/core/exceptions.py)&#91;[RawError](tesla_fleet_management_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_vins_with_fleet_telemetry_errors(*, request_options: RequestOptionsOrDict | None = None) -> BackupResponse</code></summary>

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
try:
    response = client.partner.get_vins_with_fleet_telemetry_errors()
    # TODO: Handle 'response' of type BackupResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.partner.get_vins_with_fleet_telemetry_errors()
    # TODO: Handle 'response' of type BackupResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>request_options</code> | <code>[RequestOptionsOrDict](tesla_fleet_management_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[BackupResponse](tesla_fleet_management_api/models/backup_response.py)</code> -- List of VINs with telemetry errors

**OnError**: <code>[ApiError](tesla_fleet_management_api/core/exceptions.py)&#91;[RawError](tesla_fleet_management_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def register_a_partner_account(body: RegisterPartnerRequest | RegisterPartnerRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> RegisterPartnerResponse</code></summary>

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
try:
    response = client.partner.register_a_partner_account(body)
    # TODO: Handle 'response' of type RegisterPartnerResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.partner.register_a_partner_account(body)
    # TODO: Handle 'response' of type RegisterPartnerResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[RegisterPartnerRequest](tesla_fleet_management_api/models/register_partner_request.py) \| [RegisterPartnerRequestDict](tesla_fleet_management_api/models/register_partner_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](tesla_fleet_management_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[RegisterPartnerResponse](tesla_fleet_management_api/models/register_partner_response.py)</code> -- Partner account registered

**OnError**: <code>[ApiError](tesla_fleet_management_api/core/exceptions.py)&#91;[RawError](tesla_fleet_management_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

## User

> Source: [User](tesla_fleet_management_api/apis/user.py)

<details>
<summary><code>def get_active_orders_for_a_user(*, request_options: RequestOptionsOrDict | None = None) -> OrdersResponse</code></summary>

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
try:
    response = client.user.get_active_orders_for_a_user()
    # TODO: Handle 'response' of type OrdersResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.user.get_active_orders_for_a_user()
    # TODO: Handle 'response' of type OrdersResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>request_options</code> | <code>[RequestOptionsOrDict](tesla_fleet_management_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[OrdersResponse](tesla_fleet_management_api/models/orders_response.py)</code> -- User orders retrieved

**OnError**: <code>[ApiError](tesla_fleet_management_api/core/exceptions.py)&#91;[RawError](tesla_fleet_management_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_custom_feature_flags_for_a_user(*, request_options: RequestOptionsOrDict | None = None) -> BackupResponse</code></summary>

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
try:
    response = client.user.get_custom_feature_flags_for_a_user()
    # TODO: Handle 'response' of type BackupResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.user.get_custom_feature_flags_for_a_user()
    # TODO: Handle 'response' of type BackupResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>request_options</code> | <code>[RequestOptionsOrDict](tesla_fleet_management_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[BackupResponse](tesla_fleet_management_api/models/backup_response.py)</code> -- Feature flags retrieved

**OnError**: <code>[ApiError](tesla_fleet_management_api/core/exceptions.py)&#91;[RawError](tesla_fleet_management_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_summary_of_a_user_s_account(*, request_options: RequestOptionsOrDict | None = None) -> MeResponse</code></summary>

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
try:
    response = client.user.get_summary_of_a_user_s_account()
    # TODO: Handle 'response' of type MeResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.user.get_summary_of_a_user_s_account()
    # TODO: Handle 'response' of type MeResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>request_options</code> | <code>[RequestOptionsOrDict](tesla_fleet_management_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[MeResponse](tesla_fleet_management_api/models/me_response.py)</code> -- User account retrieved

**OnError**: <code>[ApiError](tesla_fleet_management_api/core/exceptions.py)&#91;[RawError](tesla_fleet_management_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_user_s_region_and_fleet_api_base_url(*, request_options: RequestOptionsOrDict | None = None) -> RegionResponse</code></summary>

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
try:
    response = client.user.get_user_s_region_and_fleet_api_base_url()
    # TODO: Handle 'response' of type RegionResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.user.get_user_s_region_and_fleet_api_base_url()
    # TODO: Handle 'response' of type RegionResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>request_options</code> | <code>[RequestOptionsOrDict](tesla_fleet_management_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[RegionResponse](tesla_fleet_management_api/models/region_response.py)</code> -- Region information retrieved

**OnError**: <code>[ApiError](tesla_fleet_management_api/core/exceptions.py)&#91;[RawError](tesla_fleet_management_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

## VehicleCommands

> Source: [VehicleCommands](tesla_fleet_management_api/apis/vehicle_commands.py)

<details>
<summary><code>def actuatetrunk(vehicle_tag: str, body: ActuateTrunkRequest | ActuateTrunkRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> CommandResponse</code></summary>

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
try:
    response = client.vehicle_commands.actuatetrunk(vehicle_tag, body)
    # TODO: Handle 'response' of type CommandResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.vehicle_commands.actuatetrunk(vehicle_tag, body)
    # TODO: Handle 'response' of type CommandResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>vehicle_tag</code> | <code>str</code> | Value sent with the request. |
| <code>body</code> | <code>[ActuateTrunkRequest](tesla_fleet_management_api/models/actuate_trunk_request.py) \| [ActuateTrunkRequestDict](tesla_fleet_management_api/models/actuate_trunk_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](tesla_fleet_management_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[CommandResponse](tesla_fleet_management_api/models/command_response.py)</code> -- Vehicle command response

**OnError**: <code>[ApiError](tesla_fleet_management_api/core/exceptions.py)&#91;[RawError](tesla_fleet_management_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def addchargeschedule(vehicle_tag: str, body: AddChargeScheduleRequest | AddChargeScheduleRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> CommandResponse</code></summary>

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
try:
    response = client.vehicle_commands.addchargeschedule(vehicle_tag, body)
    # TODO: Handle 'response' of type CommandResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.vehicle_commands.addchargeschedule(vehicle_tag, body)
    # TODO: Handle 'response' of type CommandResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>vehicle_tag</code> | <code>str</code> | Value sent with the request. |
| <code>body</code> | <code>[AddChargeScheduleRequest](tesla_fleet_management_api/models/add_charge_schedule_request.py) \| [AddChargeScheduleRequestDict](tesla_fleet_management_api/models/add_charge_schedule_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](tesla_fleet_management_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[CommandResponse](tesla_fleet_management_api/models/command_response.py)</code> -- Vehicle command response

**OnError**: <code>[ApiError](tesla_fleet_management_api/core/exceptions.py)&#91;[RawError](tesla_fleet_management_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def addpreconditionschedule(vehicle_tag: str, body: AddPreconditionScheduleRequest | AddPreconditionScheduleRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> CommandResponse</code></summary>

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
try:
    response = client.vehicle_commands.addpreconditionschedule(vehicle_tag, body)
    # TODO: Handle 'response' of type CommandResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.vehicle_commands.addpreconditionschedule(vehicle_tag, body)
    # TODO: Handle 'response' of type CommandResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>vehicle_tag</code> | <code>str</code> | Value sent with the request. |
| <code>body</code> | <code>[AddPreconditionScheduleRequest](tesla_fleet_management_api/models/add_precondition_schedule_request.py) \| [AddPreconditionScheduleRequestDict](tesla_fleet_management_api/models/add_precondition_schedule_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](tesla_fleet_management_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[CommandResponse](tesla_fleet_management_api/models/command_response.py)</code> -- Vehicle command response

**OnError**: <code>[ApiError](tesla_fleet_management_api/core/exceptions.py)&#91;[RawError](tesla_fleet_management_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def adjustmediavolume(vehicle_tag: str, body: AdjustVolumeRequest | AdjustVolumeRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> CommandResponse</code></summary>

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
try:
    response = client.vehicle_commands.adjustmediavolume(vehicle_tag, body)
    # TODO: Handle 'response' of type CommandResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.vehicle_commands.adjustmediavolume(vehicle_tag, body)
    # TODO: Handle 'response' of type CommandResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>vehicle_tag</code> | <code>str</code> | Value sent with the request. |
| <code>body</code> | <code>[AdjustVolumeRequest](tesla_fleet_management_api/models/adjust_volume_request.py) \| [AdjustVolumeRequestDict](tesla_fleet_management_api/models/adjust_volume_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](tesla_fleet_management_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[CommandResponse](tesla_fleet_management_api/models/command_response.py)</code> -- Vehicle command response

**OnError**: <code>[ApiError](tesla_fleet_management_api/core/exceptions.py)&#91;[RawError](tesla_fleet_management_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def cancelsoftwareupdate(vehicle_tag: str, *, request_options: RequestOptionsOrDict | None = None) -> CommandResponse</code></summary>

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
try:
    response = client.vehicle_commands.cancelsoftwareupdate(vehicle_tag)
    # TODO: Handle 'response' of type CommandResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.vehicle_commands.cancelsoftwareupdate(vehicle_tag)
    # TODO: Handle 'response' of type CommandResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>vehicle_tag</code> | <code>str</code> | Value sent with the request. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](tesla_fleet_management_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[CommandResponse](tesla_fleet_management_api/models/command_response.py)</code> -- Vehicle command response

**OnError**: <code>[ApiError](tesla_fleet_management_api/core/exceptions.py)&#91;[RawError](tesla_fleet_management_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def chargemaxrange(vehicle_tag: str, *, request_options: RequestOptionsOrDict | None = None) -> CommandResponse</code></summary>

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
try:
    response = client.vehicle_commands.chargemaxrange(vehicle_tag)
    # TODO: Handle 'response' of type CommandResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.vehicle_commands.chargemaxrange(vehicle_tag)
    # TODO: Handle 'response' of type CommandResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>vehicle_tag</code> | <code>str</code> | Value sent with the request. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](tesla_fleet_management_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[CommandResponse](tesla_fleet_management_api/models/command_response.py)</code> -- Vehicle command response

**OnError**: <code>[ApiError](tesla_fleet_management_api/core/exceptions.py)&#91;[RawError](tesla_fleet_management_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def chargestandard(vehicle_tag: str, *, request_options: RequestOptionsOrDict | None = None) -> CommandResponse</code></summary>

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
try:
    response = client.vehicle_commands.chargestandard(vehicle_tag)
    # TODO: Handle 'response' of type CommandResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.vehicle_commands.chargestandard(vehicle_tag)
    # TODO: Handle 'response' of type CommandResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>vehicle_tag</code> | <code>str</code> | Value sent with the request. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](tesla_fleet_management_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[CommandResponse](tesla_fleet_management_api/models/command_response.py)</code> -- Vehicle command response

**OnError**: <code>[ApiError](tesla_fleet_management_api/core/exceptions.py)&#91;[RawError](tesla_fleet_management_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def clear_pi_nto_drive_admin(vehicle_tag: str, *, request_options: RequestOptionsOrDict | None = None) -> CommandResponse</code></summary>

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
try:
    response = client.vehicle_commands.clear_pi_nto_drive_admin(vehicle_tag)
    # TODO: Handle 'response' of type CommandResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.vehicle_commands.clear_pi_nto_drive_admin(vehicle_tag)
    # TODO: Handle 'response' of type CommandResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>vehicle_tag</code> | <code>str</code> | Value sent with the request. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](tesla_fleet_management_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[CommandResponse](tesla_fleet_management_api/models/command_response.py)</code> -- Vehicle command response

**OnError**: <code>[ApiError](tesla_fleet_management_api/core/exceptions.py)&#91;[RawError](tesla_fleet_management_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def closechargeportdoor(vehicle_tag: str, *, request_options: RequestOptionsOrDict | None = None) -> CommandResponse</code></summary>

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
try:
    response = client.vehicle_commands.closechargeportdoor(vehicle_tag)
    # TODO: Handle 'response' of type CommandResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.vehicle_commands.closechargeportdoor(vehicle_tag)
    # TODO: Handle 'response' of type CommandResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>vehicle_tag</code> | <code>str</code> | Value sent with the request. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](tesla_fleet_management_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[CommandResponse](tesla_fleet_management_api/models/command_response.py)</code> -- Vehicle command response

**OnError**: <code>[ApiError](tesla_fleet_management_api/core/exceptions.py)&#91;[RawError](tesla_fleet_management_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def enableordisable_guest_mode(vehicle_tag: str, body: GuestModeRequest | GuestModeRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> CommandResponse</code></summary>

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
try:
    response = client.vehicle_commands.enableordisable_guest_mode(vehicle_tag, body)
    # TODO: Handle 'response' of type CommandResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.vehicle_commands.enableordisable_guest_mode(vehicle_tag, body)
    # TODO: Handle 'response' of type CommandResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>vehicle_tag</code> | <code>str</code> | Value sent with the request. |
| <code>body</code> | <code>[GuestModeRequest](tesla_fleet_management_api/models/guest_mode_request.py) \| [GuestModeRequestDict](tesla_fleet_management_api/models/guest_mode_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](tesla_fleet_management_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[CommandResponse](tesla_fleet_management_api/models/command_response.py)</code> -- Vehicle command response

**OnError**: <code>[ApiError](tesla_fleet_management_api/core/exceptions.py)&#91;[RawError](tesla_fleet_management_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def eraseuserdata(vehicle_tag: str, *, request_options: RequestOptionsOrDict | None = None) -> CommandResponse</code></summary>

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
try:
    response = client.vehicle_commands.eraseuserdata(vehicle_tag)
    # TODO: Handle 'response' of type CommandResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.vehicle_commands.eraseuserdata(vehicle_tag)
    # TODO: Handle 'response' of type CommandResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>vehicle_tag</code> | <code>str</code> | Value sent with the request. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](tesla_fleet_management_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[CommandResponse](tesla_fleet_management_api/models/command_response.py)</code> -- Vehicle command response

**OnError**: <code>[ApiError](tesla_fleet_management_api/core/exceptions.py)&#91;[RawError](tesla_fleet_management_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def flashlights(vehicle_tag: str, *, request_options: RequestOptionsOrDict | None = None) -> CommandResponse</code></summary>

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
try:
    response = client.vehicle_commands.flashlights(vehicle_tag)
    # TODO: Handle 'response' of type CommandResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.vehicle_commands.flashlights(vehicle_tag)
    # TODO: Handle 'response' of type CommandResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>vehicle_tag</code> | <code>str</code> | Value sent with the request. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](tesla_fleet_management_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[CommandResponse](tesla_fleet_management_api/models/command_response.py)</code> -- Vehicle command response

**OnError**: <code>[ApiError](tesla_fleet_management_api/core/exceptions.py)&#91;[RawError](tesla_fleet_management_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def honkhorn(vehicle_tag: str, *, request_options: RequestOptionsOrDict | None = None) -> CommandResponse</code></summary>

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
try:
    response = client.vehicle_commands.honkhorn(vehicle_tag)
    # TODO: Handle 'response' of type CommandResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.vehicle_commands.honkhorn(vehicle_tag)
    # TODO: Handle 'response' of type CommandResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>vehicle_tag</code> | <code>str</code> | Value sent with the request. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](tesla_fleet_management_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[CommandResponse](tesla_fleet_management_api/models/command_response.py)</code> -- Vehicle command response

**OnError**: <code>[ApiError](tesla_fleet_management_api/core/exceptions.py)&#91;[RawError](tesla_fleet_management_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def lockdoors(vehicle_tag: str, *, request_options: RequestOptionsOrDict | None = None) -> CommandResponse</code></summary>

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
try:
    response = client.vehicle_commands.lockdoors(vehicle_tag)
    # TODO: Handle 'response' of type CommandResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.vehicle_commands.lockdoors(vehicle_tag)
    # TODO: Handle 'response' of type CommandResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>vehicle_tag</code> | <code>str</code> | Value sent with the request. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](tesla_fleet_management_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[CommandResponse](tesla_fleet_management_api/models/command_response.py)</code> -- Vehicle command response

**OnError**: <code>[ApiError](tesla_fleet_management_api/core/exceptions.py)&#91;[RawError](tesla_fleet_management_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def nextfavoritemediatrack(vehicle_tag: str, *, request_options: RequestOptionsOrDict | None = None) -> CommandResponse</code></summary>

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
try:
    response = client.vehicle_commands.nextfavoritemediatrack(vehicle_tag)
    # TODO: Handle 'response' of type CommandResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.vehicle_commands.nextfavoritemediatrack(vehicle_tag)
    # TODO: Handle 'response' of type CommandResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>vehicle_tag</code> | <code>str</code> | Value sent with the request. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](tesla_fleet_management_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[CommandResponse](tesla_fleet_management_api/models/command_response.py)</code> -- Vehicle command response

**OnError**: <code>[ApiError](tesla_fleet_management_api/core/exceptions.py)&#91;[RawError](tesla_fleet_management_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def openchargeportdoor(vehicle_tag: str, *, request_options: RequestOptionsOrDict | None = None) -> CommandResponse</code></summary>

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
try:
    response = client.vehicle_commands.openchargeportdoor(vehicle_tag)
    # TODO: Handle 'response' of type CommandResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.vehicle_commands.openchargeportdoor(vehicle_tag)
    # TODO: Handle 'response' of type CommandResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>vehicle_tag</code> | <code>str</code> | Value sent with the request. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](tesla_fleet_management_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[CommandResponse](tesla_fleet_management_api/models/command_response.py)</code> -- Vehicle command response

**OnError**: <code>[ApiError](tesla_fleet_management_api/core/exceptions.py)&#91;[RawError](tesla_fleet_management_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def startcharging(vehicle_tag: str, *, request_options: RequestOptionsOrDict | None = None) -> CommandResponse</code></summary>

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
try:
    response = client.vehicle_commands.startcharging(vehicle_tag)
    # TODO: Handle 'response' of type CommandResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.vehicle_commands.startcharging(vehicle_tag)
    # TODO: Handle 'response' of type CommandResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>vehicle_tag</code> | <code>str</code> | Value sent with the request. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](tesla_fleet_management_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[CommandResponse](tesla_fleet_management_api/models/command_response.py)</code> -- Vehicle command response

**OnError**: <code>[ApiError](tesla_fleet_management_api/core/exceptions.py)&#91;[RawError](tesla_fleet_management_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def startclimatepreconditioning(vehicle_tag: str, *, request_options: RequestOptionsOrDict | None = None) -> CommandResponse</code></summary>

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
try:
    response = client.vehicle_commands.startclimatepreconditioning(vehicle_tag)
    # TODO: Handle 'response' of type CommandResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.vehicle_commands.startclimatepreconditioning(vehicle_tag)
    # TODO: Handle 'response' of type CommandResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>vehicle_tag</code> | <code>str</code> | Value sent with the request. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](tesla_fleet_management_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[CommandResponse](tesla_fleet_management_api/models/command_response.py)</code> -- Vehicle command response

**OnError**: <code>[ApiError](tesla_fleet_management_api/core/exceptions.py)&#91;[RawError](tesla_fleet_management_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def stopcharging(vehicle_tag: str, *, request_options: RequestOptionsOrDict | None = None) -> CommandResponse</code></summary>

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
try:
    response = client.vehicle_commands.stopcharging(vehicle_tag)
    # TODO: Handle 'response' of type CommandResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.vehicle_commands.stopcharging(vehicle_tag)
    # TODO: Handle 'response' of type CommandResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>vehicle_tag</code> | <code>str</code> | Value sent with the request. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](tesla_fleet_management_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[CommandResponse](tesla_fleet_management_api/models/command_response.py)</code> -- Vehicle command response

**OnError**: <code>[ApiError](tesla_fleet_management_api/core/exceptions.py)&#91;[RawError](tesla_fleet_management_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def stopclimatepreconditioning(vehicle_tag: str, *, request_options: RequestOptionsOrDict | None = None) -> CommandResponse</code></summary>

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
try:
    response = client.vehicle_commands.stopclimatepreconditioning(vehicle_tag)
    # TODO: Handle 'response' of type CommandResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.vehicle_commands.stopclimatepreconditioning(vehicle_tag)
    # TODO: Handle 'response' of type CommandResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>vehicle_tag</code> | <code>str</code> | Value sent with the request. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](tesla_fleet_management_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[CommandResponse](tesla_fleet_management_api/models/command_response.py)</code> -- Vehicle command response

**OnError**: <code>[ApiError](tesla_fleet_management_api/core/exceptions.py)&#91;[RawError](tesla_fleet_management_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def unlockdoors(vehicle_tag: str, *, request_options: RequestOptionsOrDict | None = None) -> CommandResponse</code></summary>

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
try:
    response = client.vehicle_commands.unlockdoors(vehicle_tag)
    # TODO: Handle 'response' of type CommandResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.vehicle_commands.unlockdoors(vehicle_tag)
    # TODO: Handle 'response' of type CommandResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>vehicle_tag</code> | <code>str</code> | Value sent with the request. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](tesla_fleet_management_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[CommandResponse](tesla_fleet_management_api/models/command_response.py)</code> -- Vehicle command response

**OnError**: <code>[ApiError](tesla_fleet_management_api/core/exceptions.py)&#91;[RawError](tesla_fleet_management_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

## Vehicles

> Source: [Vehicles](tesla_fleet_management_api/apis/vehicles.py)

<details>
<summary><code>def configure_fleet_telemetry_using_signed_jws_token(body: FleetTelemetryJwsRequest | FleetTelemetryJwsRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> Any</code></summary>

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
try:
    response = client.vehicles.configure_fleet_telemetry_using_signed_jws_token(body)
    # TODO: Handle 'response' of type Any
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.vehicles.configure_fleet_telemetry_using_signed_jws_token(body)
    # TODO: Handle 'response' of type Any
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[FleetTelemetryJwsRequest](tesla_fleet_management_api/models/fleet_telemetry_jws_request.py) \| [FleetTelemetryJwsRequestDict](tesla_fleet_management_api/models/fleet_telemetry_jws_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](tesla_fleet_management_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>Any</code> -- Telemetry configuration result

**OnError**: <code>[ApiError](tesla_fleet_management_api/core/exceptions.py)&#91;[RawError](tesla_fleet_management_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def create_or_update_fleet_telemetry_configuration(body: Any, *, request_options: RequestOptionsOrDict | None = None) -> Any</code></summary>

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
try:
    response = client.vehicles.create_or_update_fleet_telemetry_configuration(body)
    # TODO: Handle 'response' of type Any
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.vehicles.create_or_update_fleet_telemetry_configuration(body)
    # TODO: Handle 'response' of type Any
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>Any</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](tesla_fleet_management_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>Any</code> -- Telemetry configuration result

**OnError**: <code>[ApiError](tesla_fleet_management_api/core/exceptions.py)&#91;[RawError](tesla_fleet_management_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def delete_fleet_telemetry_configuration(vehicle_tag: str, *, request_options: RequestOptionsOrDict | None = None) -> Any</code></summary>

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
try:
    response = client.vehicles.delete_fleet_telemetry_configuration(vehicle_tag)
    # TODO: Handle 'response' of type Any
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.vehicles.delete_fleet_telemetry_configuration(vehicle_tag)
    # TODO: Handle 'response' of type Any
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>vehicle_tag</code> | <code>str</code> | Value sent with the request. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](tesla_fleet_management_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>Any</code> -- Configuration deleted

**OnError**: <code>[ApiError](tesla_fleet_management_api/core/exceptions.py)&#91;[RawError](tesla_fleet_management_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_allowed_drivers_for_a_vehicle(vehicle_tag: str, *, request_options: RequestOptionsOrDict | None = None) -> DriversResponse</code></summary>

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
try:
    response = client.vehicles.get_allowed_drivers_for_a_vehicle(vehicle_tag)
    # TODO: Handle 'response' of type DriversResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.vehicles.get_allowed_drivers_for_a_vehicle(vehicle_tag)
    # TODO: Handle 'response' of type DriversResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>vehicle_tag</code> | <code>str</code> | Value sent with the request. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](tesla_fleet_management_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[DriversResponse](tesla_fleet_management_api/models/drivers_response.py)</code> -- List of drivers

**OnError**: <code>[ApiError](tesla_fleet_management_api/core/exceptions.py)&#91;[RawError](tesla_fleet_management_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_eligible_vehicle_subscriptions(vin: str, *, request_options: RequestOptionsOrDict | None = None) -> SiteInfoResponse</code></summary>

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
try:
    response = client.vehicles.get_eligible_vehicle_subscriptions(vin)
    # TODO: Handle 'response' of type SiteInfoResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.vehicles.get_eligible_vehicle_subscriptions(vin)
    # TODO: Handle 'response' of type SiteInfoResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>vin</code> | <code>str</code> | Value sent with the request. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](tesla_fleet_management_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SiteInfoResponse](tesla_fleet_management_api/models/site_info_response.py)</code> -- Eligible subscriptions

**OnError**: <code>[ApiError](tesla_fleet_management_api/core/exceptions.py)&#91;[RawError](tesla_fleet_management_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_eligible_vehicle_upgrades(vin: str, *, request_options: RequestOptionsOrDict | None = None) -> SiteInfoResponse</code></summary>

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
try:
    response = client.vehicles.get_eligible_vehicle_upgrades(vin)
    # TODO: Handle 'response' of type SiteInfoResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.vehicles.get_eligible_vehicle_upgrades(vin)
    # TODO: Handle 'response' of type SiteInfoResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>vin</code> | <code>str</code> | Value sent with the request. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](tesla_fleet_management_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SiteInfoResponse](tesla_fleet_management_api/models/site_info_response.py)</code> -- Eligible upgrades

**OnError**: <code>[ApiError](tesla_fleet_management_api/core/exceptions.py)&#91;[RawError](tesla_fleet_management_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_enterprise_roles_for_a_vehicle(vin: str, *, request_options: RequestOptionsOrDict | None = None) -> Any</code></summary>

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
try:
    response = client.vehicles.get_enterprise_roles_for_a_vehicle(vin)
    # TODO: Handle 'response' of type Any
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.vehicles.get_enterprise_roles_for_a_vehicle(vin)
    # TODO: Handle 'response' of type Any
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>vin</code> | <code>str</code> | Value sent with the request. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](tesla_fleet_management_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>Any</code> -- Enterprise roles

**OnError**: <code>[ApiError](tesla_fleet_management_api/core/exceptions.py)&#91;[RawError](tesla_fleet_management_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_fleet_status_for_vehicles(body: FleetStatusRequest | FleetStatusRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> Any</code></summary>

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
try:
    response = client.vehicles.get_fleet_status_for_vehicles(body)
    # TODO: Handle 'response' of type Any
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.vehicles.get_fleet_status_for_vehicles(body)
    # TODO: Handle 'response' of type Any
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[FleetStatusRequest](tesla_fleet_management_api/models/fleet_status_request.py) \| [FleetStatusRequestDict](tesla_fleet_management_api/models/fleet_status_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](tesla_fleet_management_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>Any</code> -- Fleet status

**OnError**: <code>[ApiError](tesla_fleet_management_api/core/exceptions.py)&#91;[RawError](tesla_fleet_management_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_fleet_telemetry_configuration(vehicle_tag: str, *, request_options: RequestOptionsOrDict | None = None) -> Any</code></summary>

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
try:
    response = client.vehicles.get_fleet_telemetry_configuration(vehicle_tag)
    # TODO: Handle 'response' of type Any
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.vehicles.get_fleet_telemetry_configuration(vehicle_tag)
    # TODO: Handle 'response' of type Any
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>vehicle_tag</code> | <code>str</code> | Value sent with the request. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](tesla_fleet_management_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>Any</code> -- Fleet telemetry configuration

**OnError**: <code>[ApiError](tesla_fleet_management_api/core/exceptions.py)&#91;[RawError](tesla_fleet_management_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_fleet_telemetry_errors_for_a_vehicle(vehicle_tag: str, *, request_options: RequestOptionsOrDict | None = None) -> Any</code></summary>

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
try:
    response = client.vehicles.get_fleet_telemetry_errors_for_a_vehicle(vehicle_tag)
    # TODO: Handle 'response' of type Any
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.vehicles.get_fleet_telemetry_errors_for_a_vehicle(vehicle_tag)
    # TODO: Handle 'response' of type Any
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>vehicle_tag</code> | <code>str</code> | Value sent with the request. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](tesla_fleet_management_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>Any</code> -- Fleet telemetry errors

**OnError**: <code>[ApiError](tesla_fleet_management_api/core/exceptions.py)&#91;[RawError](tesla_fleet_management_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_vehicle(vehicle_tag: str, *, request_options: RequestOptionsOrDict | None = None) -> Api1VehiclesResponseResponse200</code></summary>

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
try:
    response = client.vehicles.get_vehicle(vehicle_tag)
    # TODO: Handle 'response' of type Api1VehiclesResponseResponse200
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.vehicles.get_vehicle(vehicle_tag)
    # TODO: Handle 'response' of type Api1VehiclesResponseResponse200
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>vehicle_tag</code> | <code>str</code> | Value sent with the request. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](tesla_fleet_management_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[Api1VehiclesResponseResponse200](tesla_fleet_management_api/models/api1_vehicles_response_response200.py)</code> -- Vehicle info

**OnError**: <code>[ApiError](tesla_fleet_management_api/core/exceptions.py)&#91;[RawError](tesla_fleet_management_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def list_vehicles(*, request_options: RequestOptionsOrDict | None = None) -> Api1VehiclesResponse</code></summary>

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
try:
    response = client.vehicles.list_vehicles()
    # TODO: Handle 'response' of type Api1VehiclesResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.vehicles.list_vehicles()
    # TODO: Handle 'response' of type Api1VehiclesResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>request_options</code> | <code>[RequestOptionsOrDict](tesla_fleet_management_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[Api1VehiclesResponse](tesla_fleet_management_api/models/api1_vehicles_response.py)</code> -- Vehicles list

**OnError**: <code>[ApiError](tesla_fleet_management_api/core/exceptions.py)&#91;[RawError](tesla_fleet_management_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def mobile_enabled(vehicle_tag: str, *, request_options: RequestOptionsOrDict | None = None) -> Api1VehiclesMobileEnabledResponse</code></summary>

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
try:
    response = client.vehicles.mobile_enabled(vehicle_tag)
    # TODO: Handle 'response' of type Api1VehiclesMobileEnabledResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.vehicles.mobile_enabled(vehicle_tag)
    # TODO: Handle 'response' of type Api1VehiclesMobileEnabledResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>vehicle_tag</code> | <code>str</code> | Value sent with the request. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](tesla_fleet_management_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[Api1VehiclesMobileEnabledResponse](tesla_fleet_management_api/models/api1_vehicles_mobile_enabled_response.py)</code> -- Mobile access status

**OnError**: <code>[ApiError](tesla_fleet_management_api/core/exceptions.py)&#91;[RawError](tesla_fleet_management_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def nearby_charging_sites(vehicle_tag: str, *, request_options: RequestOptionsOrDict | None = None) -> Api1VehiclesNearbyChargingSitesResponse</code></summary>

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
try:
    response = client.vehicles.nearby_charging_sites(vehicle_tag)
    # TODO: Handle 'response' of type Api1VehiclesNearbyChargingSitesResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.vehicles.nearby_charging_sites(vehicle_tag)
    # TODO: Handle 'response' of type Api1VehiclesNearbyChargingSitesResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>vehicle_tag</code> | <code>str</code> | Value sent with the request. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](tesla_fleet_management_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[Api1VehiclesNearbyChargingSitesResponse](tesla_fleet_management_api/models/api1_vehicles_nearby_charging_sites_response.py)</code> -- Charging sites

**OnError**: <code>[ApiError](tesla_fleet_management_api/core/exceptions.py)&#91;[RawError](tesla_fleet_management_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def remove_driver_access_from_a_vehicle(vehicle_tag: str, *, request_options: RequestOptionsOrDict | None = None) -> SimpleOkResponse</code></summary>

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
try:
    response = client.vehicles.remove_driver_access_from_a_vehicle(vehicle_tag)
    # TODO: Handle 'response' of type SimpleOkResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.vehicles.remove_driver_access_from_a_vehicle(vehicle_tag)
    # TODO: Handle 'response' of type SimpleOkResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>vehicle_tag</code> | <code>str</code> | Value sent with the request. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](tesla_fleet_management_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SimpleOkResponse](tesla_fleet_management_api/models/simple_ok_response.py)</code> -- Driver removed

**OnError**: <code>[ApiError](tesla_fleet_management_api/core/exceptions.py)&#91;[RawError](tesla_fleet_management_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def set_enterprise_payer_roles(vin: str, body: EnterprisePayerRequest | EnterprisePayerRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> None</code></summary>

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
try:
    client.vehicles.set_enterprise_payer_roles(vin, body)
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    await async_client.vehicles.set_enterprise_payer_roles(vin, body)
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>vin</code> | <code>str</code> | Value sent with the request. |
| <code>body</code> | <code>[EnterprisePayerRequest](tesla_fleet_management_api/models/enterprise_payer_request.py) \| [EnterprisePayerRequestDict](tesla_fleet_management_api/models/enterprise_payer_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](tesla_fleet_management_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: No content

**OnError**: <code>[ApiError](tesla_fleet_management_api/core/exceptions.py)&#91;[RawError](tesla_fleet_management_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def vehicle_live_data(vehicle_tag: str, *, request_options: RequestOptionsOrDict | None = None) -> SiteInfoResponse</code></summary>

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
try:
    response = client.vehicles.vehicle_live_data(vehicle_tag)
    # TODO: Handle 'response' of type SiteInfoResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.vehicles.vehicle_live_data(vehicle_tag)
    # TODO: Handle 'response' of type SiteInfoResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>vehicle_tag</code> | <code>str</code> | Value sent with the request. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](tesla_fleet_management_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SiteInfoResponse](tesla_fleet_management_api/models/site_info_response.py)</code> -- Realtime vehicle data

**OnError**: <code>[ApiError](tesla_fleet_management_api/core/exceptions.py)&#91;[RawError](tesla_fleet_management_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def vehicle_options(vin: str, *, request_options: RequestOptionsOrDict | None = None) -> Api1DxVehiclesOptionsResponse</code></summary>

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
try:
    response = client.vehicles.vehicle_options(vin)
    # TODO: Handle 'response' of type Api1DxVehiclesOptionsResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.vehicles.vehicle_options(vin)
    # TODO: Handle 'response' of type Api1DxVehiclesOptionsResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>vin</code> | <code>str</code> | Value sent with the request. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](tesla_fleet_management_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[Api1DxVehiclesOptionsResponse](tesla_fleet_management_api/models/api1_dx_vehicles_options_response.py)</code> -- Vehicle options

**OnError**: <code>[ApiError](tesla_fleet_management_api/core/exceptions.py)&#91;[RawError](tesla_fleet_management_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def vehicle_specs(vin: str, *, request_options: RequestOptionsOrDict | None = None) -> SiteInfoResponse</code></summary>

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
try:
    response = client.vehicles.vehicle_specs(vin)
    # TODO: Handle 'response' of type SiteInfoResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.vehicles.vehicle_specs(vin)
    # TODO: Handle 'response' of type SiteInfoResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>vin</code> | <code>str</code> | Value sent with the request. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](tesla_fleet_management_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SiteInfoResponse](tesla_fleet_management_api/models/site_info_response.py)</code> -- Vehicle specifications

**OnError**: <code>[ApiError](tesla_fleet_management_api/core/exceptions.py)&#91;[RawError](tesla_fleet_management_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def wake_up_vehicle(vehicle_tag: str, *, request_options: RequestOptionsOrDict | None = None) -> Api1VehiclesWakeUpResponse</code></summary>

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
try:
    response = client.vehicles.wake_up_vehicle(vehicle_tag)
    # TODO: Handle 'response' of type Api1VehiclesWakeUpResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.vehicles.wake_up_vehicle(vehicle_tag)
    # TODO: Handle 'response' of type Api1VehiclesWakeUpResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>vehicle_tag</code> | <code>str</code> | Value sent with the request. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](tesla_fleet_management_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[Api1VehiclesWakeUpResponse](tesla_fleet_management_api/models/api1_vehicles_wake_up_response.py)</code> -- Vehicle awakened

**OnError**: <code>[ApiError](tesla_fleet_management_api/core/exceptions.py)&#91;[RawError](tesla_fleet_management_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def warranty_details(*, request_options: RequestOptionsOrDict | None = None) -> Api1DxWarrantyDetailsResponse</code></summary>

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
try:
    response = client.vehicles.warranty_details()
    # TODO: Handle 'response' of type Api1DxWarrantyDetailsResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.vehicles.warranty_details()
    # TODO: Handle 'response' of type Api1DxWarrantyDetailsResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>request_options</code> | <code>[RequestOptionsOrDict](tesla_fleet_management_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[Api1DxWarrantyDetailsResponse](tesla_fleet_management_api/models/api1_dx_warranty_details_response.py)</code> -- Warranty information

**OnError**: <code>[ApiError](tesla_fleet_management_api/core/exceptions.py)&#91;[RawError](tesla_fleet_management_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>


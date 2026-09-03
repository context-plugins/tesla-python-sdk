from __future__ import annotations

from typing import Any
from uuid import UUID, uuid4

from ..auth import AsyncAuthSchemes, AuthSchemes
from ..core import (
    AnySchemes,
    ApiResult,
    AsyncAnySchemes,
    AsyncRawClient,
    RawClient,
    RawError,
    RequestOptionsOrDict,
    RFC3339DateTime,
    SecuredRawResponse,
    json_body,
    json_decoder,
    param,
    raw_error_response,
)
from ..models.backup_request import BackupRequest, BackupRequestDict
from ..models.backup_response import BackupResponse
from ..models.calendar_history_response import CalendarHistoryResponse
from ..models.charge_history_response import ChargeHistoryResponse
from ..models.enums.kind import KindOrStr
from ..models.enums.kind_get_wall_connector_charging_history import KindGetWallConnectorChargingHistoryOrStr
from ..models.generic_update_response import GenericUpdateResponse
from ..models.live_status_response import LiveStatusResponse
from ..models.off_grid_vehicle_charging_reserve_request import (
    OffGridVehicleChargingReserveRequest,
    OffGridVehicleChargingReserveRequestDict,
)
from ..models.operation_request import OperationRequest, OperationRequestDict
from ..models.products_response import ProductsResponse
from ..models.site_info_response import SiteInfoResponse
from ..models.storm_mode_request import StormModeRequest, StormModeRequestDict
from ..models.time_of_use_settings_request import TimeOfUseSettingsRequest, TimeOfUseSettingsRequestDict
from ..server.server import Server


class Energy:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = EnergyWithRawResponse(client, server, auth)

    def adjust_site_s_backup_reserve(
        self,
        energy_site_id: str,
        body: BackupRequest | BackupRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> BackupResponse:
        """Send a ``POST`` request.

        Args:
            energy_site_id: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Backup reserve updated

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.adjust_site_s_backup_reserve(
            energy_site_id, body, request_options=request_options
        ).unwrap()

    def adjust_site_s_off_grid_vehicle_charging_reserve(
        self,
        energy_site_id: str,
        body: OffGridVehicleChargingReserveRequest | OffGridVehicleChargingReserveRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> GenericUpdateResponse:
        """Send a ``POST`` request.

        Args:
            energy_site_id: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Reserve updated

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.adjust_site_s_off_grid_vehicle_charging_reserve(
            energy_site_id, body, request_options=request_options
        ).unwrap()

    def allow_disallow_charging_from_the_grid_and_exporting_energy_to_the_grid(
        self, energy_site_id: str, *, body: Any | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> GenericUpdateResponse:
        """Send a ``POST`` request.

        Args:
            energy_site_id: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Grid import/export updated

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.allow_disallow_charging_from_the_grid_and_exporting_energy_to_the_grid(
            energy_site_id, body=body, request_options=request_options
        ).unwrap()

    def get_backup_or_energy_history(
        self,
        energy_site_id: str,
        kind: KindOrStr,
        start_date: RFC3339DateTime,
        end_date: RFC3339DateTime,
        *,
        period: str | None = None,
        time_zone: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CalendarHistoryResponse:
        """Send a ``GET`` request.

        Args:
            energy_site_id: Value sent with the request.
            kind: Value sent with the request.
            start_date: Value sent with the request.
            end_date: Value sent with the request.
            period: Value sent with the request.
            time_zone: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            History retrieved

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.get_backup_or_energy_history(
            energy_site_id,
            kind,
            start_date,
            end_date,
            period=period,
            time_zone=time_zone,
            request_options=request_options,
        ).unwrap()

    def get_live_site_status(
        self, energy_site_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> LiveStatusResponse:
        """Send a ``GET`` request.

        Args:
            energy_site_id: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Live status retrieved

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.get_live_site_status(energy_site_id, request_options=request_options).unwrap()

    def get_site_information_assets_settings_features(
        self, energy_site_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> SiteInfoResponse:
        """Send a ``GET`` request.

        Args:
            energy_site_id: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Site info retrieved

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.get_site_information_assets_settings_features(
            energy_site_id, request_options=request_options
        ).unwrap()

    def get_user_products_vehicles_energy_sites(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> ProductsResponse:
        """Send a ``GET`` request.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Products retrieved

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.get_user_products_vehicles_energy_sites(request_options=request_options).unwrap()

    def get_wall_connector_charging_history(
        self,
        energy_site_id: str,
        kind: KindGetWallConnectorChargingHistoryOrStr,
        start_date: RFC3339DateTime,
        end_date: RFC3339DateTime,
        *,
        time_zone: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ChargeHistoryResponse:
        """Send a ``GET`` request.

        Args:
            energy_site_id: Value sent with the request.
            kind: Value sent with the request.
            start_date: Value sent with the request.
            end_date: Value sent with the request.
            time_zone: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Charging history retrieved

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.get_wall_connector_charging_history(
            energy_site_id, kind, start_date, end_date, time_zone=time_zone, request_options=request_options
        ).unwrap()

    def set_site_mode_autonomous_or_self_consumption(
        self,
        energy_site_id: str,
        body: OperationRequest | OperationRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> GenericUpdateResponse:
        """Send a ``POST`` request.

        Args:
            energy_site_id: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Operation mode updated

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.set_site_mode_autonomous_or_self_consumption(
            energy_site_id, body, request_options=request_options
        ).unwrap()

    def update_storm_watch_participation(
        self,
        energy_site_id: str,
        body: StormModeRequest | StormModeRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> GenericUpdateResponse:
        """Send a ``POST`` request.

        Args:
            energy_site_id: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Storm mode updated

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.update_storm_watch_participation(
            energy_site_id, body, request_options=request_options
        ).unwrap()

    def update_time_of_use_tou_settings(
        self,
        energy_site_id: str,
        body: TimeOfUseSettingsRequest | TimeOfUseSettingsRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> GenericUpdateResponse:
        """Send a ``POST`` request.

        Args:
            energy_site_id: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            TOU settings updated

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.update_time_of_use_tou_settings(
            energy_site_id, body, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> EnergyWithRawResponse:
        return self._with_raw_response


class AsyncEnergy:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncEnergyWithRawResponse(client, server, auth)

    async def adjust_site_s_backup_reserve(
        self,
        energy_site_id: str,
        body: BackupRequest | BackupRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> BackupResponse:
        """Send a ``POST`` request.

        Args:
            energy_site_id: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Backup reserve updated

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.adjust_site_s_backup_reserve(
                energy_site_id, body, request_options=request_options
            )
        ).unwrap()

    async def adjust_site_s_off_grid_vehicle_charging_reserve(
        self,
        energy_site_id: str,
        body: OffGridVehicleChargingReserveRequest | OffGridVehicleChargingReserveRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> GenericUpdateResponse:
        """Send a ``POST`` request.

        Args:
            energy_site_id: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Reserve updated

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.adjust_site_s_off_grid_vehicle_charging_reserve(
                energy_site_id, body, request_options=request_options
            )
        ).unwrap()

    async def allow_disallow_charging_from_the_grid_and_exporting_energy_to_the_grid(
        self, energy_site_id: str, *, body: Any | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> GenericUpdateResponse:
        """Send a ``POST`` request.

        Args:
            energy_site_id: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Grid import/export updated

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.allow_disallow_charging_from_the_grid_and_exporting_energy_to_the_grid(
                energy_site_id, body=body, request_options=request_options
            )
        ).unwrap()

    async def get_backup_or_energy_history(
        self,
        energy_site_id: str,
        kind: KindOrStr,
        start_date: RFC3339DateTime,
        end_date: RFC3339DateTime,
        *,
        period: str | None = None,
        time_zone: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CalendarHistoryResponse:
        """Send a ``GET`` request.

        Args:
            energy_site_id: Value sent with the request.
            kind: Value sent with the request.
            start_date: Value sent with the request.
            end_date: Value sent with the request.
            period: Value sent with the request.
            time_zone: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            History retrieved

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.get_backup_or_energy_history(
                energy_site_id,
                kind,
                start_date,
                end_date,
                period=period,
                time_zone=time_zone,
                request_options=request_options,
            )
        ).unwrap()

    async def get_live_site_status(
        self, energy_site_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> LiveStatusResponse:
        """Send a ``GET`` request.

        Args:
            energy_site_id: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Live status retrieved

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.get_live_site_status(energy_site_id, request_options=request_options)
        ).unwrap()

    async def get_site_information_assets_settings_features(
        self, energy_site_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> SiteInfoResponse:
        """Send a ``GET`` request.

        Args:
            energy_site_id: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Site info retrieved

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.get_site_information_assets_settings_features(
                energy_site_id, request_options=request_options
            )
        ).unwrap()

    async def get_user_products_vehicles_energy_sites(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> ProductsResponse:
        """Send a ``GET`` request.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Products retrieved

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.get_user_products_vehicles_energy_sites(request_options=request_options)
        ).unwrap()

    async def get_wall_connector_charging_history(
        self,
        energy_site_id: str,
        kind: KindGetWallConnectorChargingHistoryOrStr,
        start_date: RFC3339DateTime,
        end_date: RFC3339DateTime,
        *,
        time_zone: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ChargeHistoryResponse:
        """Send a ``GET`` request.

        Args:
            energy_site_id: Value sent with the request.
            kind: Value sent with the request.
            start_date: Value sent with the request.
            end_date: Value sent with the request.
            time_zone: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Charging history retrieved

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.get_wall_connector_charging_history(
                energy_site_id, kind, start_date, end_date, time_zone=time_zone, request_options=request_options
            )
        ).unwrap()

    async def set_site_mode_autonomous_or_self_consumption(
        self,
        energy_site_id: str,
        body: OperationRequest | OperationRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> GenericUpdateResponse:
        """Send a ``POST`` request.

        Args:
            energy_site_id: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Operation mode updated

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.set_site_mode_autonomous_or_self_consumption(
                energy_site_id, body, request_options=request_options
            )
        ).unwrap()

    async def update_storm_watch_participation(
        self,
        energy_site_id: str,
        body: StormModeRequest | StormModeRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> GenericUpdateResponse:
        """Send a ``POST`` request.

        Args:
            energy_site_id: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Storm mode updated

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.update_storm_watch_participation(
                energy_site_id, body, request_options=request_options
            )
        ).unwrap()

    async def update_time_of_use_tou_settings(
        self,
        energy_site_id: str,
        body: TimeOfUseSettingsRequest | TimeOfUseSettingsRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> GenericUpdateResponse:
        """Send a ``POST`` request.

        Args:
            energy_site_id: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            TOU settings updated

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.update_time_of_use_tou_settings(
                energy_site_id, body, request_options=request_options
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncEnergyWithRawResponse:
        return self._with_raw_response


class EnergyWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def adjust_site_s_backup_reserve(
        self,
        energy_site_id: str,
        body: BackupRequest | BackupRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[BackupResponse, RawError]:
        """Send a ``POST`` request.

        Args:
            energy_site_id: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/api/1/energy_sites/{energy_site_id}/backup"),
            path_params=[param[str]("energy_site_id", energy_site_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[BackupRequest | BackupRequestDict](body),
            auth_scheme=AnySchemes(
                self._auth.thirdpartytoken_authorization_code, self._auth.thirdpartytoken_client_credentials
            ),
            decoder=json_decoder[BackupResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def adjust_site_s_off_grid_vehicle_charging_reserve(
        self,
        energy_site_id: str,
        body: OffGridVehicleChargingReserveRequest | OffGridVehicleChargingReserveRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[GenericUpdateResponse, RawError]:
        """Send a ``POST`` request.

        Args:
            energy_site_id: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/api/1/energy_sites/{energy_site_id}/off_grid_vehicle_charging_reserve"),
            path_params=[param[str]("energy_site_id", energy_site_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[OffGridVehicleChargingReserveRequest | OffGridVehicleChargingReserveRequestDict](body),
            auth_scheme=AnySchemes(
                self._auth.thirdpartytoken_authorization_code, self._auth.thirdpartytoken_client_credentials
            ),
            decoder=json_decoder[GenericUpdateResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def allow_disallow_charging_from_the_grid_and_exporting_energy_to_the_grid(
        self, energy_site_id: str, *, body: Any | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[GenericUpdateResponse, RawError]:
        """Send a ``POST`` request.

        Args:
            energy_site_id: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/api/1/energy_sites/{energy_site_id}/grid_import_export"),
            path_params=[param[str]("energy_site_id", energy_site_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[Any | None](body),
            auth_scheme=AnySchemes(
                self._auth.thirdpartytoken_authorization_code, self._auth.thirdpartytoken_client_credentials
            ),
            decoder=json_decoder[GenericUpdateResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def get_backup_or_energy_history(
        self,
        energy_site_id: str,
        kind: KindOrStr,
        start_date: RFC3339DateTime,
        end_date: RFC3339DateTime,
        *,
        period: str | None = None,
        time_zone: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CalendarHistoryResponse, RawError]:
        """Send a ``GET`` request.

        Args:
            energy_site_id: Value sent with the request.
            kind: Value sent with the request.
            start_date: Value sent with the request.
            end_date: Value sent with the request.
            period: Value sent with the request.
            time_zone: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/api/1/energy_sites/{energy_site_id}/calendar_history"),
            path_params=[param[str]("energy_site_id", energy_site_id)],
            query_params=[
                param[KindOrStr]("kind", kind),
                param[RFC3339DateTime]("start_date", start_date),
                param[RFC3339DateTime]("end_date", end_date),
                param[str | None]("period", period),
                param[str | None]("time_zone", time_zone),
            ],
            auth_scheme=AnySchemes(
                self._auth.thirdpartytoken_authorization_code, self._auth.thirdpartytoken_client_credentials
            ),
            decoder=json_decoder[CalendarHistoryResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def get_live_site_status(
        self, energy_site_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[LiveStatusResponse, RawError]:
        """Send a ``GET`` request.

        Args:
            energy_site_id: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/api/1/energy_sites/{energy_site_id}/live_status"),
            path_params=[param[str]("energy_site_id", energy_site_id)],
            auth_scheme=AnySchemes(
                self._auth.thirdpartytoken_authorization_code, self._auth.thirdpartytoken_client_credentials
            ),
            decoder=json_decoder[LiveStatusResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def get_site_information_assets_settings_features(
        self, energy_site_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[SiteInfoResponse, RawError]:
        """Send a ``GET`` request.

        Args:
            energy_site_id: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/api/1/energy_sites/{energy_site_id}/site_info"),
            path_params=[param[str]("energy_site_id", energy_site_id)],
            auth_scheme=AnySchemes(
                self._auth.thirdpartytoken_authorization_code, self._auth.thirdpartytoken_client_credentials
            ),
            decoder=json_decoder[SiteInfoResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def get_user_products_vehicles_energy_sites(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ProductsResponse, RawError]:
        """Send a ``GET`` request.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/api/1/products"),
            auth_scheme=AnySchemes(
                self._auth.thirdpartytoken_authorization_code, self._auth.thirdpartytoken_client_credentials
            ),
            decoder=json_decoder[ProductsResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def get_wall_connector_charging_history(
        self,
        energy_site_id: str,
        kind: KindGetWallConnectorChargingHistoryOrStr,
        start_date: RFC3339DateTime,
        end_date: RFC3339DateTime,
        *,
        time_zone: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ChargeHistoryResponse, RawError]:
        """Send a ``GET`` request.

        Args:
            energy_site_id: Value sent with the request.
            kind: Value sent with the request.
            start_date: Value sent with the request.
            end_date: Value sent with the request.
            time_zone: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/api/1/energy_sites/{energy_site_id}/telemetry_history"),
            path_params=[param[str]("energy_site_id", energy_site_id)],
            query_params=[
                param[KindGetWallConnectorChargingHistoryOrStr]("kind", kind),
                param[RFC3339DateTime]("start_date", start_date),
                param[RFC3339DateTime]("end_date", end_date),
                param[str | None]("time_zone", time_zone),
            ],
            auth_scheme=AnySchemes(
                self._auth.thirdpartytoken_authorization_code, self._auth.thirdpartytoken_client_credentials
            ),
            decoder=json_decoder[ChargeHistoryResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def set_site_mode_autonomous_or_self_consumption(
        self,
        energy_site_id: str,
        body: OperationRequest | OperationRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[GenericUpdateResponse, RawError]:
        """Send a ``POST`` request.

        Args:
            energy_site_id: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/api/1/energy_sites/{energy_site_id}/operation"),
            path_params=[param[str]("energy_site_id", energy_site_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[OperationRequest | OperationRequestDict](body),
            auth_scheme=AnySchemes(
                self._auth.thirdpartytoken_authorization_code, self._auth.thirdpartytoken_client_credentials
            ),
            decoder=json_decoder[GenericUpdateResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def update_storm_watch_participation(
        self,
        energy_site_id: str,
        body: StormModeRequest | StormModeRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[GenericUpdateResponse, RawError]:
        """Send a ``POST`` request.

        Args:
            energy_site_id: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/api/1/energy_sites/{energy_site_id}/storm_mode"),
            path_params=[param[str]("energy_site_id", energy_site_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[StormModeRequest | StormModeRequestDict](body),
            auth_scheme=AnySchemes(
                self._auth.thirdpartytoken_authorization_code, self._auth.thirdpartytoken_client_credentials
            ),
            decoder=json_decoder[GenericUpdateResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def update_time_of_use_tou_settings(
        self,
        energy_site_id: str,
        body: TimeOfUseSettingsRequest | TimeOfUseSettingsRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[GenericUpdateResponse, RawError]:
        """Send a ``POST`` request.

        Args:
            energy_site_id: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/api/1/energy_sites/{energy_site_id}/time_of_use_settings"),
            path_params=[param[str]("energy_site_id", energy_site_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[TimeOfUseSettingsRequest | TimeOfUseSettingsRequestDict](body),
            auth_scheme=AnySchemes(
                self._auth.thirdpartytoken_authorization_code, self._auth.thirdpartytoken_client_credentials
            ),
            decoder=json_decoder[GenericUpdateResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncEnergyWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def adjust_site_s_backup_reserve(
        self,
        energy_site_id: str,
        body: BackupRequest | BackupRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[BackupResponse, RawError]:
        """Send a ``POST`` request.

        Args:
            energy_site_id: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/api/1/energy_sites/{energy_site_id}/backup"),
            path_params=[param[str]("energy_site_id", energy_site_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[BackupRequest | BackupRequestDict](body),
            auth_scheme=AsyncAnySchemes(
                self._auth.thirdpartytoken_authorization_code, self._auth.thirdpartytoken_client_credentials
            ),
            decoder=json_decoder[BackupResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def adjust_site_s_off_grid_vehicle_charging_reserve(
        self,
        energy_site_id: str,
        body: OffGridVehicleChargingReserveRequest | OffGridVehicleChargingReserveRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[GenericUpdateResponse, RawError]:
        """Send a ``POST`` request.

        Args:
            energy_site_id: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/api/1/energy_sites/{energy_site_id}/off_grid_vehicle_charging_reserve"),
            path_params=[param[str]("energy_site_id", energy_site_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[OffGridVehicleChargingReserveRequest | OffGridVehicleChargingReserveRequestDict](body),
            auth_scheme=AsyncAnySchemes(
                self._auth.thirdpartytoken_authorization_code, self._auth.thirdpartytoken_client_credentials
            ),
            decoder=json_decoder[GenericUpdateResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def allow_disallow_charging_from_the_grid_and_exporting_energy_to_the_grid(
        self, energy_site_id: str, *, body: Any | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[GenericUpdateResponse, RawError]:
        """Send a ``POST`` request.

        Args:
            energy_site_id: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/api/1/energy_sites/{energy_site_id}/grid_import_export"),
            path_params=[param[str]("energy_site_id", energy_site_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[Any | None](body),
            auth_scheme=AsyncAnySchemes(
                self._auth.thirdpartytoken_authorization_code, self._auth.thirdpartytoken_client_credentials
            ),
            decoder=json_decoder[GenericUpdateResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def get_backup_or_energy_history(
        self,
        energy_site_id: str,
        kind: KindOrStr,
        start_date: RFC3339DateTime,
        end_date: RFC3339DateTime,
        *,
        period: str | None = None,
        time_zone: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CalendarHistoryResponse, RawError]:
        """Send a ``GET`` request.

        Args:
            energy_site_id: Value sent with the request.
            kind: Value sent with the request.
            start_date: Value sent with the request.
            end_date: Value sent with the request.
            period: Value sent with the request.
            time_zone: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/api/1/energy_sites/{energy_site_id}/calendar_history"),
            path_params=[param[str]("energy_site_id", energy_site_id)],
            query_params=[
                param[KindOrStr]("kind", kind),
                param[RFC3339DateTime]("start_date", start_date),
                param[RFC3339DateTime]("end_date", end_date),
                param[str | None]("period", period),
                param[str | None]("time_zone", time_zone),
            ],
            auth_scheme=AsyncAnySchemes(
                self._auth.thirdpartytoken_authorization_code, self._auth.thirdpartytoken_client_credentials
            ),
            decoder=json_decoder[CalendarHistoryResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def get_live_site_status(
        self, energy_site_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[LiveStatusResponse, RawError]:
        """Send a ``GET`` request.

        Args:
            energy_site_id: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/api/1/energy_sites/{energy_site_id}/live_status"),
            path_params=[param[str]("energy_site_id", energy_site_id)],
            auth_scheme=AsyncAnySchemes(
                self._auth.thirdpartytoken_authorization_code, self._auth.thirdpartytoken_client_credentials
            ),
            decoder=json_decoder[LiveStatusResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def get_site_information_assets_settings_features(
        self, energy_site_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[SiteInfoResponse, RawError]:
        """Send a ``GET`` request.

        Args:
            energy_site_id: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/api/1/energy_sites/{energy_site_id}/site_info"),
            path_params=[param[str]("energy_site_id", energy_site_id)],
            auth_scheme=AsyncAnySchemes(
                self._auth.thirdpartytoken_authorization_code, self._auth.thirdpartytoken_client_credentials
            ),
            decoder=json_decoder[SiteInfoResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def get_user_products_vehicles_energy_sites(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ProductsResponse, RawError]:
        """Send a ``GET`` request.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/api/1/products"),
            auth_scheme=AsyncAnySchemes(
                self._auth.thirdpartytoken_authorization_code, self._auth.thirdpartytoken_client_credentials
            ),
            decoder=json_decoder[ProductsResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def get_wall_connector_charging_history(
        self,
        energy_site_id: str,
        kind: KindGetWallConnectorChargingHistoryOrStr,
        start_date: RFC3339DateTime,
        end_date: RFC3339DateTime,
        *,
        time_zone: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ChargeHistoryResponse, RawError]:
        """Send a ``GET`` request.

        Args:
            energy_site_id: Value sent with the request.
            kind: Value sent with the request.
            start_date: Value sent with the request.
            end_date: Value sent with the request.
            time_zone: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/api/1/energy_sites/{energy_site_id}/telemetry_history"),
            path_params=[param[str]("energy_site_id", energy_site_id)],
            query_params=[
                param[KindGetWallConnectorChargingHistoryOrStr]("kind", kind),
                param[RFC3339DateTime]("start_date", start_date),
                param[RFC3339DateTime]("end_date", end_date),
                param[str | None]("time_zone", time_zone),
            ],
            auth_scheme=AsyncAnySchemes(
                self._auth.thirdpartytoken_authorization_code, self._auth.thirdpartytoken_client_credentials
            ),
            decoder=json_decoder[ChargeHistoryResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def set_site_mode_autonomous_or_self_consumption(
        self,
        energy_site_id: str,
        body: OperationRequest | OperationRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[GenericUpdateResponse, RawError]:
        """Send a ``POST`` request.

        Args:
            energy_site_id: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/api/1/energy_sites/{energy_site_id}/operation"),
            path_params=[param[str]("energy_site_id", energy_site_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[OperationRequest | OperationRequestDict](body),
            auth_scheme=AsyncAnySchemes(
                self._auth.thirdpartytoken_authorization_code, self._auth.thirdpartytoken_client_credentials
            ),
            decoder=json_decoder[GenericUpdateResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def update_storm_watch_participation(
        self,
        energy_site_id: str,
        body: StormModeRequest | StormModeRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[GenericUpdateResponse, RawError]:
        """Send a ``POST`` request.

        Args:
            energy_site_id: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/api/1/energy_sites/{energy_site_id}/storm_mode"),
            path_params=[param[str]("energy_site_id", energy_site_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[StormModeRequest | StormModeRequestDict](body),
            auth_scheme=AsyncAnySchemes(
                self._auth.thirdpartytoken_authorization_code, self._auth.thirdpartytoken_client_credentials
            ),
            decoder=json_decoder[GenericUpdateResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def update_time_of_use_tou_settings(
        self,
        energy_site_id: str,
        body: TimeOfUseSettingsRequest | TimeOfUseSettingsRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[GenericUpdateResponse, RawError]:
        """Send a ``POST`` request.

        Args:
            energy_site_id: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/api/1/energy_sites/{energy_site_id}/time_of_use_settings"),
            path_params=[param[str]("energy_site_id", energy_site_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[TimeOfUseSettingsRequest | TimeOfUseSettingsRequestDict](body),
            auth_scheme=AsyncAnySchemes(
                self._auth.thirdpartytoken_authorization_code, self._auth.thirdpartytoken_client_credentials
            ),
            decoder=json_decoder[GenericUpdateResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

from __future__ import annotations

from ..auth import AsyncAuthSchemes, AuthSchemes
from ..core import (
    AnySchemes,
    ApiResult,
    AsyncAnySchemes,
    AsyncRawClient,
    RawClient,
    RawError,
    RequestOptionsOrDict,
    SecuredRawResponse,
    empty_response,
    json_decoder,
    param,
    raw_error_response,
)
from ..models.charging_history_response import ChargingHistoryResponse
from ..models.charging_sessions_response import ChargingSessionsResponse
from ..server.server import Server


class Charging:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = ChargingWithRawResponse(client, server, auth)

    def get_charging_history(self, *, request_options: RequestOptionsOrDict | None = None) -> ChargingHistoryResponse:
        """Returns the paginated charging history for the authenticated account.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Charging history retrieved successfully

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.get_charging_history(request_options=request_options).unwrap()

    def get_charging_invoice(self, id: str, *, request_options: RequestOptionsOrDict | None = None) -> None:
        """Returns a charging invoice PDF for a charging session.

        Args:
            id: Charging session invoice identifier
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Invoice PDF document

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.get_charging_invoice(id, request_options=request_options).unwrap()

    def get_charging_sessions(self, *, request_options: RequestOptionsOrDict | None = None) -> ChargingSessionsResponse:
        """Returns charging session information. Only available for business fleet owners.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Charging sessions retrieved successfully

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.get_charging_sessions(request_options=request_options).unwrap()

    @property
    def with_raw_response(self) -> ChargingWithRawResponse:
        return self._with_raw_response


class AsyncCharging:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncChargingWithRawResponse(client, server, auth)

    async def get_charging_history(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> ChargingHistoryResponse:
        """Returns the paginated charging history for the authenticated account.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Charging history retrieved successfully

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.get_charging_history(request_options=request_options)).unwrap()

    async def get_charging_invoice(self, id: str, *, request_options: RequestOptionsOrDict | None = None) -> None:
        """Returns a charging invoice PDF for a charging session.

        Args:
            id: Charging session invoice identifier
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Invoice PDF document

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.get_charging_invoice(id, request_options=request_options)).unwrap()

    async def get_charging_sessions(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> ChargingSessionsResponse:
        """Returns charging session information. Only available for business fleet owners.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Charging sessions retrieved successfully

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.get_charging_sessions(request_options=request_options)).unwrap()

    @property
    def with_raw_response(self) -> AsyncChargingWithRawResponse:
        return self._with_raw_response


class ChargingWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def get_charging_history(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ChargingHistoryResponse, RawError]:
        """Returns the paginated charging history for the authenticated account.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/api/1/dx/charging/history"),
            auth_scheme=AnySchemes(
                self._auth.thirdpartytoken_authorization_code, self._auth.thirdpartytoken_client_credentials
            ),
            decoder=json_decoder[ChargingHistoryResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def get_charging_invoice(
        self, id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, RawError]:
        """Returns a charging invoice PDF for a charging session.

        Args:
            id: Charging session invoice identifier
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/api/1/dx/charging/invoice/{id}"),
            path_params=[param[str]("id", id)],
            auth_scheme=AnySchemes(
                self._auth.thirdpartytoken_authorization_code, self._auth.thirdpartytoken_client_credentials
            ),
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def get_charging_sessions(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ChargingSessionsResponse, RawError]:
        """Returns charging session information. Only available for business fleet owners.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/api/1/dx/charging/sessions"),
            auth_scheme=AnySchemes(
                self._auth.thirdpartytoken_authorization_code, self._auth.thirdpartytoken_client_credentials
            ),
            decoder=json_decoder[ChargingSessionsResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncChargingWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def get_charging_history(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ChargingHistoryResponse, RawError]:
        """Returns the paginated charging history for the authenticated account.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/api/1/dx/charging/history"),
            auth_scheme=AsyncAnySchemes(
                self._auth.thirdpartytoken_authorization_code, self._auth.thirdpartytoken_client_credentials
            ),
            decoder=json_decoder[ChargingHistoryResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def get_charging_invoice(
        self, id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, RawError]:
        """Returns a charging invoice PDF for a charging session.

        Args:
            id: Charging session invoice identifier
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/api/1/dx/charging/invoice/{id}"),
            path_params=[param[str]("id", id)],
            auth_scheme=AsyncAnySchemes(
                self._auth.thirdpartytoken_authorization_code, self._auth.thirdpartytoken_client_credentials
            ),
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def get_charging_sessions(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ChargingSessionsResponse, RawError]:
        """Returns charging session information. Only available for business fleet owners.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/api/1/dx/charging/sessions"),
            auth_scheme=AsyncAnySchemes(
                self._auth.thirdpartytoken_authorization_code, self._auth.thirdpartytoken_client_credentials
            ),
            decoder=json_decoder[ChargingSessionsResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

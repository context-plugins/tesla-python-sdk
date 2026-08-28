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
    json_decoder,
    raw_error_response,
)
from ..models.backup_response import BackupResponse
from ..models.me_response import MeResponse
from ..models.orders_response import OrdersResponse
from ..models.region_response import RegionResponse
from ..server.server import Server


class User:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = UserWithRawResponse(client, server, auth)

    def get_active_orders_for_a_user(self, *, request_options: RequestOptionsOrDict | None = None) -> OrdersResponse:
        """Send a ``GET`` request.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            User orders retrieved

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.get_active_orders_for_a_user(request_options=request_options).unwrap()

    def get_custom_feature_flags_for_a_user(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> BackupResponse:
        """Send a ``GET`` request.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Feature flags retrieved

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.get_custom_feature_flags_for_a_user(request_options=request_options).unwrap()

    def get_summary_of_a_user_s_account(self, *, request_options: RequestOptionsOrDict | None = None) -> MeResponse:
        """Send a ``GET`` request.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            User account retrieved

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.get_summary_of_a_user_s_account(request_options=request_options).unwrap()

    def get_user_s_region_and_fleet_api_base_url(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> RegionResponse:
        """Send a ``GET`` request.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Region information retrieved

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.get_user_s_region_and_fleet_api_base_url(
            request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> UserWithRawResponse:
        return self._with_raw_response


class AsyncUser:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncUserWithRawResponse(client, server, auth)

    async def get_active_orders_for_a_user(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> OrdersResponse:
        """Send a ``GET`` request.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            User orders retrieved

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.get_active_orders_for_a_user(request_options=request_options)).unwrap()

    async def get_custom_feature_flags_for_a_user(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> BackupResponse:
        """Send a ``GET`` request.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Feature flags retrieved

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.get_custom_feature_flags_for_a_user(request_options=request_options)
        ).unwrap()

    async def get_summary_of_a_user_s_account(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> MeResponse:
        """Send a ``GET`` request.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            User account retrieved

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.get_summary_of_a_user_s_account(request_options=request_options)).unwrap()

    async def get_user_s_region_and_fleet_api_base_url(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> RegionResponse:
        """Send a ``GET`` request.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Region information retrieved

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.get_user_s_region_and_fleet_api_base_url(request_options=request_options)
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncUserWithRawResponse:
        return self._with_raw_response


class UserWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def get_active_orders_for_a_user(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[OrdersResponse, RawError]:
        """Send a ``GET`` request.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/api/1/users/orders"),
            auth_scheme=AnySchemes(
                self._auth.thirdpartytoken_authorization_code, self._auth.thirdpartytoken_client_credentials
            ),
            decoder=json_decoder[OrdersResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def get_custom_feature_flags_for_a_user(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[BackupResponse, RawError]:
        """Send a ``GET`` request.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/api/1/users/feature_config"),
            auth_scheme=AnySchemes(
                self._auth.thirdpartytoken_authorization_code, self._auth.thirdpartytoken_client_credentials
            ),
            decoder=json_decoder[BackupResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def get_summary_of_a_user_s_account(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[MeResponse, RawError]:
        """Send a ``GET`` request.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/api/1/users/me"),
            auth_scheme=AnySchemes(
                self._auth.thirdpartytoken_authorization_code, self._auth.thirdpartytoken_client_credentials
            ),
            decoder=json_decoder[MeResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def get_user_s_region_and_fleet_api_base_url(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[RegionResponse, RawError]:
        """Send a ``GET`` request.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/api/1/users/region"),
            auth_scheme=AnySchemes(
                self._auth.thirdpartytoken_authorization_code, self._auth.thirdpartytoken_client_credentials
            ),
            decoder=json_decoder[RegionResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncUserWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def get_active_orders_for_a_user(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[OrdersResponse, RawError]:
        """Send a ``GET`` request.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/api/1/users/orders"),
            auth_scheme=AsyncAnySchemes(
                self._auth.thirdpartytoken_authorization_code, self._auth.thirdpartytoken_client_credentials
            ),
            decoder=json_decoder[OrdersResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def get_custom_feature_flags_for_a_user(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[BackupResponse, RawError]:
        """Send a ``GET`` request.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/api/1/users/feature_config"),
            auth_scheme=AsyncAnySchemes(
                self._auth.thirdpartytoken_authorization_code, self._auth.thirdpartytoken_client_credentials
            ),
            decoder=json_decoder[BackupResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def get_summary_of_a_user_s_account(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[MeResponse, RawError]:
        """Send a ``GET`` request.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/api/1/users/me"),
            auth_scheme=AsyncAnySchemes(
                self._auth.thirdpartytoken_authorization_code, self._auth.thirdpartytoken_client_credentials
            ),
            decoder=json_decoder[MeResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def get_user_s_region_and_fleet_api_base_url(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[RegionResponse, RawError]:
        """Send a ``GET`` request.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/api/1/users/region"),
            auth_scheme=AsyncAnySchemes(
                self._auth.thirdpartytoken_authorization_code, self._auth.thirdpartytoken_client_credentials
            ),
            decoder=json_decoder[RegionResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

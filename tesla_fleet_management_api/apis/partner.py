from __future__ import annotations

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
    SecuredRawResponse,
    json_body,
    json_decoder,
    param,
    raw_error_response,
)
from ..models.backup_response import BackupResponse
from ..models.fleet_telemetry_errors_response import FleetTelemetryErrorsResponse
from ..models.public_key_response import PublicKeyResponse
from ..models.register_partner_request import RegisterPartnerRequest, RegisterPartnerRequestDict
from ..models.register_partner_response import RegisterPartnerResponse
from ..server.server import Server


class Partner:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = PartnerWithRawResponse(client, server, auth)

    def get_public_key_for_a_domain(
        self, domain: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> PublicKeyResponse:
        """Send a ``GET`` request.

        Args:
            domain: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Public key retrieved

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.get_public_key_for_a_domain(domain, request_options=request_options).unwrap()

    def get_recent_fleet_telemetry_errors(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> FleetTelemetryErrorsResponse:
        """Send a ``GET`` request.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Fleet telemetry errors retrieved

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.get_recent_fleet_telemetry_errors(request_options=request_options).unwrap()

    def get_vins_with_fleet_telemetry_errors(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> BackupResponse:
        """Send a ``GET`` request.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            List of VINs with telemetry errors

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.get_vins_with_fleet_telemetry_errors(request_options=request_options).unwrap()

    def register_a_partner_account(
        self,
        body: RegisterPartnerRequest | RegisterPartnerRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> RegisterPartnerResponse:
        """Send a ``POST`` request.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Partner account registered

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.register_a_partner_account(body, request_options=request_options).unwrap()

    @property
    def with_raw_response(self) -> PartnerWithRawResponse:
        return self._with_raw_response


class AsyncPartner:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncPartnerWithRawResponse(client, server, auth)

    async def get_public_key_for_a_domain(
        self, domain: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> PublicKeyResponse:
        """Send a ``GET`` request.

        Args:
            domain: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Public key retrieved

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.get_public_key_for_a_domain(domain, request_options=request_options)
        ).unwrap()

    async def get_recent_fleet_telemetry_errors(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> FleetTelemetryErrorsResponse:
        """Send a ``GET`` request.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Fleet telemetry errors retrieved

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.get_recent_fleet_telemetry_errors(request_options=request_options)
        ).unwrap()

    async def get_vins_with_fleet_telemetry_errors(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> BackupResponse:
        """Send a ``GET`` request.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            List of VINs with telemetry errors

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.get_vins_with_fleet_telemetry_errors(request_options=request_options)
        ).unwrap()

    async def register_a_partner_account(
        self,
        body: RegisterPartnerRequest | RegisterPartnerRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> RegisterPartnerResponse:
        """Send a ``POST`` request.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Partner account registered

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.register_a_partner_account(body, request_options=request_options)
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncPartnerWithRawResponse:
        return self._with_raw_response


class PartnerWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def get_public_key_for_a_domain(
        self, domain: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[PublicKeyResponse, RawError]:
        """Send a ``GET`` request.

        Args:
            domain: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/api/1/partner_accounts/public_key"),
            query_params=[param[str]("domain", domain)],
            auth_scheme=AnySchemes(
                self._auth.thirdpartytoken_authorization_code, self._auth.thirdpartytoken_client_credentials
            ),
            decoder=json_decoder[PublicKeyResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def get_recent_fleet_telemetry_errors(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[FleetTelemetryErrorsResponse, RawError]:
        """Send a ``GET`` request.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/api/1/partner_accounts/fleet_telemetry_errors"),
            auth_scheme=AnySchemes(
                self._auth.thirdpartytoken_authorization_code, self._auth.thirdpartytoken_client_credentials
            ),
            decoder=json_decoder[FleetTelemetryErrorsResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def get_vins_with_fleet_telemetry_errors(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[BackupResponse, RawError]:
        """Send a ``GET`` request.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/api/1/partner_accounts/fleet_telemetry_error_vins"),
            auth_scheme=AnySchemes(
                self._auth.thirdpartytoken_authorization_code, self._auth.thirdpartytoken_client_credentials
            ),
            decoder=json_decoder[BackupResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def register_a_partner_account(
        self,
        body: RegisterPartnerRequest | RegisterPartnerRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[RegisterPartnerResponse, RawError]:
        """Send a ``POST`` request.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/api/1/partner_accounts"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[RegisterPartnerRequest | RegisterPartnerRequestDict](body),
            auth_scheme=AnySchemes(
                self._auth.thirdpartytoken_authorization_code, self._auth.thirdpartytoken_client_credentials
            ),
            decoder=json_decoder[RegisterPartnerResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncPartnerWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def get_public_key_for_a_domain(
        self, domain: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[PublicKeyResponse, RawError]:
        """Send a ``GET`` request.

        Args:
            domain: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/api/1/partner_accounts/public_key"),
            query_params=[param[str]("domain", domain)],
            auth_scheme=AsyncAnySchemes(
                self._auth.thirdpartytoken_authorization_code, self._auth.thirdpartytoken_client_credentials
            ),
            decoder=json_decoder[PublicKeyResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def get_recent_fleet_telemetry_errors(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[FleetTelemetryErrorsResponse, RawError]:
        """Send a ``GET`` request.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/api/1/partner_accounts/fleet_telemetry_errors"),
            auth_scheme=AsyncAnySchemes(
                self._auth.thirdpartytoken_authorization_code, self._auth.thirdpartytoken_client_credentials
            ),
            decoder=json_decoder[FleetTelemetryErrorsResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def get_vins_with_fleet_telemetry_errors(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[BackupResponse, RawError]:
        """Send a ``GET`` request.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/api/1/partner_accounts/fleet_telemetry_error_vins"),
            auth_scheme=AsyncAnySchemes(
                self._auth.thirdpartytoken_authorization_code, self._auth.thirdpartytoken_client_credentials
            ),
            decoder=json_decoder[BackupResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def register_a_partner_account(
        self,
        body: RegisterPartnerRequest | RegisterPartnerRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[RegisterPartnerResponse, RawError]:
        """Send a ``POST`` request.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/api/1/partner_accounts"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[RegisterPartnerRequest | RegisterPartnerRequestDict](body),
            auth_scheme=AsyncAnySchemes(
                self._auth.thirdpartytoken_authorization_code, self._auth.thirdpartytoken_client_credentials
            ),
            decoder=json_decoder[RegisterPartnerResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

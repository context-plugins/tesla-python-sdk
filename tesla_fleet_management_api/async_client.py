from __future__ import annotations

from functools import cached_property
from types import TracebackType

from typing_extensions import Self

from .apis.charging import AsyncCharging
from .apis.energy import AsyncEnergy
from .apis.partner import AsyncPartner
from .apis.user import AsyncUser
from .apis.vehicle_commands import AsyncVehicleCommands
from .apis.vehicles import AsyncVehicles
from .auth import AsyncAuthSchemes, ThirdpartytokenAuthorizationCodeScope, ThirdpartytokenClientCredentialsScope
from .base_client import DEFAULT_TIMEOUT, BaseTeslaFleetManagementApiClient
from .core import (
    OPERATING_SYSTEM,
    PYTHON_RUNTIME,
    AsyncAuthorizationCodeCredentials,
    AsyncAuthorizationCodeCredentialsOrDict,
    AsyncAuthorizationCodeTokenSource,
    AsyncClientCredentialsTokenSource,
    AsyncHttpClient,
    AsyncHttpxClient,
    AsyncOAuth2RefreshableScheme,
    AsyncOAuth2Scheme,
    AsyncRawClient,
    AsyncRefreshableTokenSource,
    AsyncTokenSource,
    BearerAuthScheme,
    ClientCredentials,
    ClientCredentialsOrDict,
    client_secret_post,
    no_auth,
    param,
)
from .server.environment import Environment


class AsyncTeslaFleetManagementApiClient(BaseTeslaFleetManagementApiClient[AsyncRawClient]):
    def __init__(
        self,
        *,
        environment: Environment = "production",
        base_url: str | None = None,
        timeout: float = DEFAULT_TIMEOUT,
        custom_async_http_client: AsyncHttpClient | None = None,
        bearer_auth: str | None = None,
        thirdpartytoken_authorization_code: (
            AsyncAuthorizationCodeCredentialsOrDict[ThirdpartytokenAuthorizationCodeScope] | None
        ) = None,
        thirdpartytoken_authorization_code_token_source: (
            AsyncRefreshableTokenSource[AsyncAuthorizationCodeCredentials[ThirdpartytokenAuthorizationCodeScope]] | None
        ) = None,
        thirdpartytoken_client_credentials: (
            ClientCredentialsOrDict[ThirdpartytokenClientCredentialsScope] | None
        ) = None,
        thirdpartytoken_client_credentials_token_source: (
            AsyncTokenSource[ClientCredentials[ThirdpartytokenClientCredentialsScope]] | None
        ) = None,
    ) -> None:
        super().__init__(environment=environment, base_url=base_url, timeout=timeout)
        self._raw_client = AsyncRawClient(
            http_client=(
                custom_async_http_client if custom_async_http_client is not None else AsyncHttpxClient(timeout=timeout)
            ),
            global_headers=[
                param[str]("User-Agent", "TeslaFleetManagementApiClient/1.0.0 Python"),
                param[str]("X-APIMatic-Lang", "Python"),
                param[str]("X-APIMatic-Package-Version", "1.0.0"),
                param[str]("X-APIMatic-Gen-Version", "4.0.0"),
                param[str]("X-APIMatic-OS", OPERATING_SYSTEM),
                param[str]("X-APIMatic-Runtime", PYTHON_RUNTIME),
            ],
        )
        self._auth = AsyncAuthSchemes(
            bearer_auth=BearerAuthScheme(bearer_auth) if bearer_auth is not None else no_auth,
            thirdpartytoken_authorization_code=(
                AsyncOAuth2RefreshableScheme(
                    credentials=AsyncAuthorizationCodeCredentials[ThirdpartytokenAuthorizationCodeScope].coerce(
                        thirdpartytoken_authorization_code
                    ),
                    source=(
                        thirdpartytoken_authorization_code_token_source
                        if thirdpartytoken_authorization_code_token_source is not None
                        else AsyncAuthorizationCodeTokenSource[ThirdpartytokenAuthorizationCodeScope](
                            client=self._raw_client,
                            authorization_url=self._server.default("/authorize"),
                            token_url=self._server.default("/token"),
                            refresh_url=self._server.default("/token"),
                            placement=client_secret_post,
                        )
                    ),
                )
                if thirdpartytoken_authorization_code is not None
                else no_auth
            ),
            thirdpartytoken_client_credentials=(
                AsyncOAuth2Scheme(
                    credentials=ClientCredentials[ThirdpartytokenClientCredentialsScope].coerce(
                        thirdpartytoken_client_credentials
                    ),
                    source=(
                        thirdpartytoken_client_credentials_token_source
                        if thirdpartytoken_client_credentials_token_source is not None
                        else AsyncClientCredentialsTokenSource[ThirdpartytokenClientCredentialsScope](
                            client=self._raw_client,
                            token_url=self._server.default("/token"),
                            placement=client_secret_post,
                        )
                    ),
                )
                if thirdpartytoken_client_credentials is not None
                else no_auth
            ),
        )

    @cached_property
    def charging(self) -> AsyncCharging:
        return AsyncCharging(self._raw_client, self._server, self._auth)

    @cached_property
    def energy(self) -> AsyncEnergy:
        return AsyncEnergy(self._raw_client, self._server, self._auth)

    @cached_property
    def partner(self) -> AsyncPartner:
        return AsyncPartner(self._raw_client, self._server, self._auth)

    @cached_property
    def user(self) -> AsyncUser:
        return AsyncUser(self._raw_client, self._server, self._auth)

    @cached_property
    def vehicle_commands(self) -> AsyncVehicleCommands:
        return AsyncVehicleCommands(self._raw_client, self._server, self._auth)

    @cached_property
    def vehicles(self) -> AsyncVehicles:
        return AsyncVehicles(self._raw_client, self._server, self._auth)

    async def aclose(self) -> None:
        await self._raw_client.http_client.aclose()

    async def __aenter__(self) -> Self:
        return self

    async def __aexit__(
        self, exc_type: type[BaseException] | None, exc: BaseException | None, exc_tb: TracebackType | None
    ) -> None:
        await self.aclose()


AsyncClient = AsyncTeslaFleetManagementApiClient

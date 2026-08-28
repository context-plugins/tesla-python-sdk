from __future__ import annotations

from functools import cached_property
from types import TracebackType

from typing_extensions import Self

from .apis.charging import Charging
from .apis.energy import Energy
from .apis.partner import Partner
from .apis.user import User
from .apis.vehicle_commands import VehicleCommands
from .apis.vehicles import Vehicles
from .auth import AuthSchemes, ThirdpartytokenAuthorizationCodeScope, ThirdpartytokenClientCredentialsScope
from .base_client import DEFAULT_TIMEOUT, BaseTeslaClient
from .core import (
    AuthorizationCodeCredentials,
    AuthorizationCodeCredentialsOrDict,
    AuthorizationCodeTokenSource,
    BearerAuthScheme,
    ClientCredentials,
    ClientCredentialsOrDict,
    ClientCredentialsTokenSource,
    HttpClient,
    HttpxClient,
    OAuth2RefreshableScheme,
    OAuth2Scheme,
    RawClient,
    RefreshableTokenSource,
    TokenSource,
    client_secret_post,
    no_auth,
)
from .server.environment import Environment


class TeslaClient(BaseTeslaClient[RawClient]):
    def __init__(
        self,
        *,
        environment: Environment = "production",
        base_url: str | None = None,
        timeout: float = DEFAULT_TIMEOUT,
        custom_http_client: HttpClient | None = None,
        bearer_auth: str | None = None,
        thirdpartytoken_authorization_code: (
            AuthorizationCodeCredentialsOrDict[ThirdpartytokenAuthorizationCodeScope] | None
        ) = None,
        thirdpartytoken_authorization_code_token_source: (
            RefreshableTokenSource[AuthorizationCodeCredentials[ThirdpartytokenAuthorizationCodeScope]] | None
        ) = None,
        thirdpartytoken_client_credentials: (
            ClientCredentialsOrDict[ThirdpartytokenClientCredentialsScope] | None
        ) = None,
        thirdpartytoken_client_credentials_token_source: (
            TokenSource[ClientCredentials[ThirdpartytokenClientCredentialsScope]] | None
        ) = None,
    ) -> None:
        super().__init__(environment=environment, base_url=base_url, timeout=timeout)
        self._raw_client = RawClient(
            http_client=custom_http_client if custom_http_client is not None else HttpxClient(timeout=timeout)
        )
        self._auth = AuthSchemes(
            bearer_auth=BearerAuthScheme(bearer_auth) if bearer_auth is not None else no_auth,
            thirdpartytoken_authorization_code=(
                OAuth2RefreshableScheme(
                    credentials=AuthorizationCodeCredentials[ThirdpartytokenAuthorizationCodeScope].coerce(
                        thirdpartytoken_authorization_code
                    ),
                    source=(
                        thirdpartytoken_authorization_code_token_source
                        if thirdpartytoken_authorization_code_token_source is not None
                        else AuthorizationCodeTokenSource[ThirdpartytokenAuthorizationCodeScope](
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
                OAuth2Scheme(
                    credentials=ClientCredentials[ThirdpartytokenClientCredentialsScope].coerce(
                        thirdpartytoken_client_credentials
                    ),
                    source=(
                        thirdpartytoken_client_credentials_token_source
                        if thirdpartytoken_client_credentials_token_source is not None
                        else ClientCredentialsTokenSource[ThirdpartytokenClientCredentialsScope](
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
    def charging(self) -> Charging:
        return Charging(self._raw_client, self._server, self._auth)

    @cached_property
    def energy(self) -> Energy:
        return Energy(self._raw_client, self._server, self._auth)

    @cached_property
    def partner(self) -> Partner:
        return Partner(self._raw_client, self._server, self._auth)

    @cached_property
    def user(self) -> User:
        return User(self._raw_client, self._server, self._auth)

    @cached_property
    def vehicle_commands(self) -> VehicleCommands:
        return VehicleCommands(self._raw_client, self._server, self._auth)

    @cached_property
    def vehicles(self) -> Vehicles:
        return Vehicles(self._raw_client, self._server, self._auth)

    def close(self) -> None:
        self._raw_client.http_client.close()

    def __enter__(self) -> Self:
        return self

    def __exit__(
        self, exc_type: type[BaseException] | None, exc: BaseException | None, exc_tb: TracebackType | None
    ) -> None:
        self.close()


Client = TeslaClient

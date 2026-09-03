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
    SecuredRawResponse,
    empty_response,
    json_body,
    json_decoder,
    param,
    raw_error_response,
)
from ..models.api1_dx_vehicles_options_response import Api1DxVehiclesOptionsResponse
from ..models.api1_dx_warranty_details_response import Api1DxWarrantyDetailsResponse
from ..models.api1_vehicles_mobile_enabled_response import Api1VehiclesMobileEnabledResponse
from ..models.api1_vehicles_nearby_charging_sites_response import Api1VehiclesNearbyChargingSitesResponse
from ..models.api1_vehicles_response import Api1VehiclesResponse
from ..models.api1_vehicles_response_response200 import Api1VehiclesResponseResponse200
from ..models.api1_vehicles_wake_up_response import Api1VehiclesWakeUpResponse
from ..models.drivers_response import DriversResponse
from ..models.enterprise_payer_request import EnterprisePayerRequest, EnterprisePayerRequestDict
from ..models.fleet_status_request import FleetStatusRequest, FleetStatusRequestDict
from ..models.fleet_telemetry_jws_request import FleetTelemetryJwsRequest, FleetTelemetryJwsRequestDict
from ..models.simple_ok_response import SimpleOkResponse
from ..models.site_info_response import SiteInfoResponse
from ..server.server import Server


class Vehicles:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = VehiclesWithRawResponse(client, server, auth)

    def configure_fleet_telemetry_using_signed_jws_token(
        self,
        body: FleetTelemetryJwsRequest | FleetTelemetryJwsRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Any:
        """Send a ``POST`` request.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Telemetry configuration result

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.configure_fleet_telemetry_using_signed_jws_token(
            body, request_options=request_options
        ).unwrap()

    def create_or_update_fleet_telemetry_configuration(
        self, body: Any, *, request_options: RequestOptionsOrDict | None = None
    ) -> Any:
        """Send a ``POST`` request.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Telemetry configuration result

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.create_or_update_fleet_telemetry_configuration(
            body, request_options=request_options
        ).unwrap()

    def delete_fleet_telemetry_configuration(
        self, vehicle_tag: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> Any:
        """Send a ``DELETE`` request.

        Args:
            vehicle_tag: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Configuration deleted

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.delete_fleet_telemetry_configuration(
            vehicle_tag, request_options=request_options
        ).unwrap()

    def get_allowed_drivers_for_a_vehicle(
        self, vehicle_tag: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> DriversResponse:
        """Send a ``GET`` request.

        Args:
            vehicle_tag: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            List of drivers

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.get_allowed_drivers_for_a_vehicle(
            vehicle_tag, request_options=request_options
        ).unwrap()

    def get_eligible_vehicle_subscriptions(
        self, vin: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> SiteInfoResponse:
        """Send a ``GET`` request.

        Args:
            vin: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Eligible subscriptions

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.get_eligible_vehicle_subscriptions(vin, request_options=request_options).unwrap()

    def get_eligible_vehicle_upgrades(
        self, vin: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> SiteInfoResponse:
        """Send a ``GET`` request.

        Args:
            vin: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Eligible upgrades

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.get_eligible_vehicle_upgrades(vin, request_options=request_options).unwrap()

    def get_enterprise_roles_for_a_vehicle(
        self, vin: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> Any:
        """Send a ``GET`` request.

        Args:
            vin: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Enterprise roles

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.get_enterprise_roles_for_a_vehicle(vin, request_options=request_options).unwrap()

    def get_fleet_status_for_vehicles(
        self, body: FleetStatusRequest | FleetStatusRequestDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> Any:
        """Send a ``POST`` request.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Fleet status

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.get_fleet_status_for_vehicles(body, request_options=request_options).unwrap()

    def get_fleet_telemetry_configuration(
        self, vehicle_tag: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> Any:
        """Send a ``GET`` request.

        Args:
            vehicle_tag: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Fleet telemetry configuration

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.get_fleet_telemetry_configuration(
            vehicle_tag, request_options=request_options
        ).unwrap()

    def get_fleet_telemetry_errors_for_a_vehicle(
        self, vehicle_tag: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> Any:
        """Send a ``GET`` request.

        Args:
            vehicle_tag: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Fleet telemetry errors

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.get_fleet_telemetry_errors_for_a_vehicle(
            vehicle_tag, request_options=request_options
        ).unwrap()

    def get_vehicle(
        self, vehicle_tag: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> Api1VehiclesResponseResponse200:
        """Send a ``GET`` request.

        Args:
            vehicle_tag: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Vehicle info

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.get_vehicle(vehicle_tag, request_options=request_options).unwrap()

    def list_vehicles(self, *, request_options: RequestOptionsOrDict | None = None) -> Api1VehiclesResponse:
        """Send a ``GET`` request.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Vehicles list

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.list_vehicles(request_options=request_options).unwrap()

    def mobile_enabled(
        self, vehicle_tag: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> Api1VehiclesMobileEnabledResponse:
        """Send a ``GET`` request.

        Args:
            vehicle_tag: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Mobile access status

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.mobile_enabled(vehicle_tag, request_options=request_options).unwrap()

    def nearby_charging_sites(
        self, vehicle_tag: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> Api1VehiclesNearbyChargingSitesResponse:
        """Send a ``GET`` request.

        Args:
            vehicle_tag: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Charging sites

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.nearby_charging_sites(vehicle_tag, request_options=request_options).unwrap()

    def remove_driver_access_from_a_vehicle(
        self, vehicle_tag: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> SimpleOkResponse:
        """Send a ``DELETE`` request.

        Args:
            vehicle_tag: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Driver removed

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.remove_driver_access_from_a_vehicle(
            vehicle_tag, request_options=request_options
        ).unwrap()

    def set_enterprise_payer_roles(
        self,
        vin: str,
        body: EnterprisePayerRequest | EnterprisePayerRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """Send a ``POST`` request.

        Args:
            vin: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.set_enterprise_payer_roles(vin, body, request_options=request_options).unwrap()

    def vehicle_live_data(
        self, vehicle_tag: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> SiteInfoResponse:
        """Send a ``GET`` request.

        Args:
            vehicle_tag: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Realtime vehicle data

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.vehicle_live_data(vehicle_tag, request_options=request_options).unwrap()

    def vehicle_options(
        self, vin: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> Api1DxVehiclesOptionsResponse:
        """Send a ``GET`` request.

        Args:
            vin: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Vehicle options

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.vehicle_options(vin, request_options=request_options).unwrap()

    def vehicle_specs(self, vin: str, *, request_options: RequestOptionsOrDict | None = None) -> SiteInfoResponse:
        """Send a ``GET`` request.

        Args:
            vin: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Vehicle specifications

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.vehicle_specs(vin, request_options=request_options).unwrap()

    def wake_up_vehicle(
        self, vehicle_tag: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> Api1VehiclesWakeUpResponse:
        """Send a ``POST`` request.

        Args:
            vehicle_tag: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Vehicle awakened

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.wake_up_vehicle(vehicle_tag, request_options=request_options).unwrap()

    def warranty_details(self, *, request_options: RequestOptionsOrDict | None = None) -> Api1DxWarrantyDetailsResponse:
        """Send a ``GET`` request.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Warranty information

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.warranty_details(request_options=request_options).unwrap()

    @property
    def with_raw_response(self) -> VehiclesWithRawResponse:
        return self._with_raw_response


class AsyncVehicles:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncVehiclesWithRawResponse(client, server, auth)

    async def configure_fleet_telemetry_using_signed_jws_token(
        self,
        body: FleetTelemetryJwsRequest | FleetTelemetryJwsRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Any:
        """Send a ``POST`` request.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Telemetry configuration result

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.configure_fleet_telemetry_using_signed_jws_token(
                body, request_options=request_options
            )
        ).unwrap()

    async def create_or_update_fleet_telemetry_configuration(
        self, body: Any, *, request_options: RequestOptionsOrDict | None = None
    ) -> Any:
        """Send a ``POST`` request.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Telemetry configuration result

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.create_or_update_fleet_telemetry_configuration(
                body, request_options=request_options
            )
        ).unwrap()

    async def delete_fleet_telemetry_configuration(
        self, vehicle_tag: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> Any:
        """Send a ``DELETE`` request.

        Args:
            vehicle_tag: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Configuration deleted

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.delete_fleet_telemetry_configuration(
                vehicle_tag, request_options=request_options
            )
        ).unwrap()

    async def get_allowed_drivers_for_a_vehicle(
        self, vehicle_tag: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> DriversResponse:
        """Send a ``GET`` request.

        Args:
            vehicle_tag: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            List of drivers

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.get_allowed_drivers_for_a_vehicle(
                vehicle_tag, request_options=request_options
            )
        ).unwrap()

    async def get_eligible_vehicle_subscriptions(
        self, vin: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> SiteInfoResponse:
        """Send a ``GET`` request.

        Args:
            vin: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Eligible subscriptions

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.get_eligible_vehicle_subscriptions(vin, request_options=request_options)
        ).unwrap()

    async def get_eligible_vehicle_upgrades(
        self, vin: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> SiteInfoResponse:
        """Send a ``GET`` request.

        Args:
            vin: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Eligible upgrades

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.get_eligible_vehicle_upgrades(vin, request_options=request_options)
        ).unwrap()

    async def get_enterprise_roles_for_a_vehicle(
        self, vin: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> Any:
        """Send a ``GET`` request.

        Args:
            vin: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Enterprise roles

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.get_enterprise_roles_for_a_vehicle(vin, request_options=request_options)
        ).unwrap()

    async def get_fleet_status_for_vehicles(
        self, body: FleetStatusRequest | FleetStatusRequestDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> Any:
        """Send a ``POST`` request.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Fleet status

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.get_fleet_status_for_vehicles(body, request_options=request_options)
        ).unwrap()

    async def get_fleet_telemetry_configuration(
        self, vehicle_tag: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> Any:
        """Send a ``GET`` request.

        Args:
            vehicle_tag: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Fleet telemetry configuration

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.get_fleet_telemetry_configuration(
                vehicle_tag, request_options=request_options
            )
        ).unwrap()

    async def get_fleet_telemetry_errors_for_a_vehicle(
        self, vehicle_tag: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> Any:
        """Send a ``GET`` request.

        Args:
            vehicle_tag: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Fleet telemetry errors

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.get_fleet_telemetry_errors_for_a_vehicle(
                vehicle_tag, request_options=request_options
            )
        ).unwrap()

    async def get_vehicle(
        self, vehicle_tag: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> Api1VehiclesResponseResponse200:
        """Send a ``GET`` request.

        Args:
            vehicle_tag: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Vehicle info

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.get_vehicle(vehicle_tag, request_options=request_options)).unwrap()

    async def list_vehicles(self, *, request_options: RequestOptionsOrDict | None = None) -> Api1VehiclesResponse:
        """Send a ``GET`` request.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Vehicles list

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.list_vehicles(request_options=request_options)).unwrap()

    async def mobile_enabled(
        self, vehicle_tag: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> Api1VehiclesMobileEnabledResponse:
        """Send a ``GET`` request.

        Args:
            vehicle_tag: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Mobile access status

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.mobile_enabled(vehicle_tag, request_options=request_options)).unwrap()

    async def nearby_charging_sites(
        self, vehicle_tag: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> Api1VehiclesNearbyChargingSitesResponse:
        """Send a ``GET`` request.

        Args:
            vehicle_tag: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Charging sites

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.nearby_charging_sites(vehicle_tag, request_options=request_options)
        ).unwrap()

    async def remove_driver_access_from_a_vehicle(
        self, vehicle_tag: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> SimpleOkResponse:
        """Send a ``DELETE`` request.

        Args:
            vehicle_tag: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Driver removed

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.remove_driver_access_from_a_vehicle(
                vehicle_tag, request_options=request_options
            )
        ).unwrap()

    async def set_enterprise_payer_roles(
        self,
        vin: str,
        body: EnterprisePayerRequest | EnterprisePayerRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """Send a ``POST`` request.

        Args:
            vin: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.set_enterprise_payer_roles(vin, body, request_options=request_options)
        ).unwrap()

    async def vehicle_live_data(
        self, vehicle_tag: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> SiteInfoResponse:
        """Send a ``GET`` request.

        Args:
            vehicle_tag: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Realtime vehicle data

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.vehicle_live_data(vehicle_tag, request_options=request_options)).unwrap()

    async def vehicle_options(
        self, vin: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> Api1DxVehiclesOptionsResponse:
        """Send a ``GET`` request.

        Args:
            vin: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Vehicle options

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.vehicle_options(vin, request_options=request_options)).unwrap()

    async def vehicle_specs(self, vin: str, *, request_options: RequestOptionsOrDict | None = None) -> SiteInfoResponse:
        """Send a ``GET`` request.

        Args:
            vin: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Vehicle specifications

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.vehicle_specs(vin, request_options=request_options)).unwrap()

    async def wake_up_vehicle(
        self, vehicle_tag: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> Api1VehiclesWakeUpResponse:
        """Send a ``POST`` request.

        Args:
            vehicle_tag: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Vehicle awakened

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.wake_up_vehicle(vehicle_tag, request_options=request_options)).unwrap()

    async def warranty_details(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> Api1DxWarrantyDetailsResponse:
        """Send a ``GET`` request.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Warranty information

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.warranty_details(request_options=request_options)).unwrap()

    @property
    def with_raw_response(self) -> AsyncVehiclesWithRawResponse:
        return self._with_raw_response


class VehiclesWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def configure_fleet_telemetry_using_signed_jws_token(
        self,
        body: FleetTelemetryJwsRequest | FleetTelemetryJwsRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Any, RawError]:
        """Send a ``POST`` request.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/api/1/vehicles/fleet_telemetry_config_jws"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[FleetTelemetryJwsRequest | FleetTelemetryJwsRequestDict](body),
            auth_scheme=AnySchemes(
                self._auth.thirdpartytoken_authorization_code, self._auth.thirdpartytoken_client_credentials
            ),
            decoder=json_decoder[Any],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def create_or_update_fleet_telemetry_configuration(
        self, body: Any, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Any, RawError]:
        """Send a ``POST`` request.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/api/1/vehicles/fleet_telemetry_config"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[Any](body),
            auth_scheme=AnySchemes(
                self._auth.thirdpartytoken_authorization_code, self._auth.thirdpartytoken_client_credentials
            ),
            decoder=json_decoder[Any],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def delete_fleet_telemetry_configuration(
        self, vehicle_tag: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Any, RawError]:
        """Send a ``DELETE`` request.

        Args:
            vehicle_tag: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/api/1/vehicles/{vehicle_tag}/fleet_telemetry_config"),
            path_params=[param[str]("vehicle_tag", vehicle_tag)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AnySchemes(
                self._auth.thirdpartytoken_authorization_code, self._auth.thirdpartytoken_client_credentials
            ),
            decoder=json_decoder[Any],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def get_allowed_drivers_for_a_vehicle(
        self, vehicle_tag: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[DriversResponse, RawError]:
        """Send a ``GET`` request.

        Args:
            vehicle_tag: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/api/1/vehicles/{vehicle_tag}/drivers"),
            path_params=[param[str]("vehicle_tag", vehicle_tag)],
            auth_scheme=AnySchemes(
                self._auth.thirdpartytoken_authorization_code, self._auth.thirdpartytoken_client_credentials
            ),
            decoder=json_decoder[DriversResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def get_eligible_vehicle_subscriptions(
        self, vin: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[SiteInfoResponse, RawError]:
        """Send a ``GET`` request.

        Args:
            vin: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/api/1/dx/vehicles/subscriptions/eligibility"),
            query_params=[param[str]("vin", vin)],
            auth_scheme=AnySchemes(
                self._auth.thirdpartytoken_authorization_code, self._auth.thirdpartytoken_client_credentials
            ),
            decoder=json_decoder[SiteInfoResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def get_eligible_vehicle_upgrades(
        self, vin: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[SiteInfoResponse, RawError]:
        """Send a ``GET`` request.

        Args:
            vin: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/api/1/dx/vehicles/upgrades/eligibility"),
            query_params=[param[str]("vin", vin)],
            auth_scheme=AnySchemes(
                self._auth.thirdpartytoken_authorization_code, self._auth.thirdpartytoken_client_credentials
            ),
            decoder=json_decoder[SiteInfoResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def get_enterprise_roles_for_a_vehicle(
        self, vin: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Any, RawError]:
        """Send a ``GET`` request.

        Args:
            vin: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/api/1/dx/enterprise/v1/{vin}/roles"),
            path_params=[param[str]("vin", vin)],
            auth_scheme=AnySchemes(
                self._auth.thirdpartytoken_authorization_code, self._auth.thirdpartytoken_client_credentials
            ),
            decoder=json_decoder[Any],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def get_fleet_status_for_vehicles(
        self, body: FleetStatusRequest | FleetStatusRequestDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Any, RawError]:
        """Send a ``POST`` request.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/api/1/vehicles/fleet_status"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[FleetStatusRequest | FleetStatusRequestDict](body),
            auth_scheme=AnySchemes(
                self._auth.thirdpartytoken_authorization_code, self._auth.thirdpartytoken_client_credentials
            ),
            decoder=json_decoder[Any],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def get_fleet_telemetry_configuration(
        self, vehicle_tag: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Any, RawError]:
        """Send a ``GET`` request.

        Args:
            vehicle_tag: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/api/1/vehicles/{vehicle_tag}/fleet_telemetry_config"),
            path_params=[param[str]("vehicle_tag", vehicle_tag)],
            auth_scheme=AnySchemes(
                self._auth.thirdpartytoken_authorization_code, self._auth.thirdpartytoken_client_credentials
            ),
            decoder=json_decoder[Any],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def get_fleet_telemetry_errors_for_a_vehicle(
        self, vehicle_tag: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Any, RawError]:
        """Send a ``GET`` request.

        Args:
            vehicle_tag: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/api/1/vehicles/{vehicle_tag}/fleet_telemetry_errors"),
            path_params=[param[str]("vehicle_tag", vehicle_tag)],
            auth_scheme=AnySchemes(
                self._auth.thirdpartytoken_authorization_code, self._auth.thirdpartytoken_client_credentials
            ),
            decoder=json_decoder[Any],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def get_vehicle(
        self, vehicle_tag: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Api1VehiclesResponseResponse200, RawError]:
        """Send a ``GET`` request.

        Args:
            vehicle_tag: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/api/1/vehicles/{vehicle_tag}"),
            path_params=[param[str]("vehicle_tag", vehicle_tag)],
            auth_scheme=AnySchemes(
                self._auth.thirdpartytoken_authorization_code, self._auth.thirdpartytoken_client_credentials
            ),
            decoder=json_decoder[Api1VehiclesResponseResponse200],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def list_vehicles(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Api1VehiclesResponse, RawError]:
        """Send a ``GET`` request.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/api/1/vehicles"),
            auth_scheme=AnySchemes(
                self._auth.thirdpartytoken_authorization_code, self._auth.thirdpartytoken_client_credentials
            ),
            decoder=json_decoder[Api1VehiclesResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def mobile_enabled(
        self, vehicle_tag: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Api1VehiclesMobileEnabledResponse, RawError]:
        """Send a ``GET`` request.

        Args:
            vehicle_tag: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/api/1/vehicles/{vehicle_tag}/mobile_enabled"),
            path_params=[param[str]("vehicle_tag", vehicle_tag)],
            auth_scheme=AnySchemes(
                self._auth.thirdpartytoken_authorization_code, self._auth.thirdpartytoken_client_credentials
            ),
            decoder=json_decoder[Api1VehiclesMobileEnabledResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def nearby_charging_sites(
        self, vehicle_tag: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Api1VehiclesNearbyChargingSitesResponse, RawError]:
        """Send a ``GET`` request.

        Args:
            vehicle_tag: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/api/1/vehicles/{vehicle_tag}/nearby_charging_sites"),
            path_params=[param[str]("vehicle_tag", vehicle_tag)],
            auth_scheme=AnySchemes(
                self._auth.thirdpartytoken_authorization_code, self._auth.thirdpartytoken_client_credentials
            ),
            decoder=json_decoder[Api1VehiclesNearbyChargingSitesResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def remove_driver_access_from_a_vehicle(
        self, vehicle_tag: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[SimpleOkResponse, RawError]:
        """Send a ``DELETE`` request.

        Args:
            vehicle_tag: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/api/1/vehicles/{vehicle_tag}/drivers"),
            path_params=[param[str]("vehicle_tag", vehicle_tag)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AnySchemes(
                self._auth.thirdpartytoken_authorization_code, self._auth.thirdpartytoken_client_credentials
            ),
            decoder=json_decoder[SimpleOkResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def set_enterprise_payer_roles(
        self,
        vin: str,
        body: EnterprisePayerRequest | EnterprisePayerRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, RawError]:
        """Send a ``POST`` request.

        Args:
            vin: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/api/1/dx/enterprise/v1/{vin}/payer"),
            path_params=[param[str]("vin", vin)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[EnterprisePayerRequest | EnterprisePayerRequestDict](body),
            auth_scheme=AnySchemes(
                self._auth.thirdpartytoken_authorization_code, self._auth.thirdpartytoken_client_credentials
            ),
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def vehicle_live_data(
        self, vehicle_tag: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[SiteInfoResponse, RawError]:
        """Send a ``GET`` request.

        Args:
            vehicle_tag: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/api/1/vehicles/{vehicle_tag}/vehicle_data"),
            path_params=[param[str]("vehicle_tag", vehicle_tag)],
            auth_scheme=AnySchemes(
                self._auth.thirdpartytoken_authorization_code, self._auth.thirdpartytoken_client_credentials
            ),
            decoder=json_decoder[SiteInfoResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def vehicle_options(
        self, vin: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Api1DxVehiclesOptionsResponse, RawError]:
        """Send a ``GET`` request.

        Args:
            vin: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/api/1/dx/vehicles/options"),
            query_params=[param[str]("vin", vin)],
            auth_scheme=AnySchemes(
                self._auth.thirdpartytoken_authorization_code, self._auth.thirdpartytoken_client_credentials
            ),
            decoder=json_decoder[Api1DxVehiclesOptionsResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def vehicle_specs(
        self, vin: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[SiteInfoResponse, RawError]:
        """Send a ``GET`` request.

        Args:
            vin: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/api/1/vehicles/{vin}/specs"),
            path_params=[param[str]("vin", vin)],
            auth_scheme=AnySchemes(
                self._auth.thirdpartytoken_authorization_code, self._auth.thirdpartytoken_client_credentials
            ),
            decoder=json_decoder[SiteInfoResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def wake_up_vehicle(
        self, vehicle_tag: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Api1VehiclesWakeUpResponse, RawError]:
        """Send a ``POST`` request.

        Args:
            vehicle_tag: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/api/1/vehicles/{vehicle_tag}/wake_up"),
            path_params=[param[str]("vehicle_tag", vehicle_tag)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AnySchemes(
                self._auth.thirdpartytoken_authorization_code, self._auth.thirdpartytoken_client_credentials
            ),
            decoder=json_decoder[Api1VehiclesWakeUpResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def warranty_details(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Api1DxWarrantyDetailsResponse, RawError]:
        """Send a ``GET`` request.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/api/1/dx/warranty/details"),
            auth_scheme=AnySchemes(
                self._auth.thirdpartytoken_authorization_code, self._auth.thirdpartytoken_client_credentials
            ),
            decoder=json_decoder[Api1DxWarrantyDetailsResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncVehiclesWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def configure_fleet_telemetry_using_signed_jws_token(
        self,
        body: FleetTelemetryJwsRequest | FleetTelemetryJwsRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Any, RawError]:
        """Send a ``POST`` request.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/api/1/vehicles/fleet_telemetry_config_jws"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[FleetTelemetryJwsRequest | FleetTelemetryJwsRequestDict](body),
            auth_scheme=AsyncAnySchemes(
                self._auth.thirdpartytoken_authorization_code, self._auth.thirdpartytoken_client_credentials
            ),
            decoder=json_decoder[Any],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def create_or_update_fleet_telemetry_configuration(
        self, body: Any, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Any, RawError]:
        """Send a ``POST`` request.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/api/1/vehicles/fleet_telemetry_config"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[Any](body),
            auth_scheme=AsyncAnySchemes(
                self._auth.thirdpartytoken_authorization_code, self._auth.thirdpartytoken_client_credentials
            ),
            decoder=json_decoder[Any],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def delete_fleet_telemetry_configuration(
        self, vehicle_tag: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Any, RawError]:
        """Send a ``DELETE`` request.

        Args:
            vehicle_tag: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/api/1/vehicles/{vehicle_tag}/fleet_telemetry_config"),
            path_params=[param[str]("vehicle_tag", vehicle_tag)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AsyncAnySchemes(
                self._auth.thirdpartytoken_authorization_code, self._auth.thirdpartytoken_client_credentials
            ),
            decoder=json_decoder[Any],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def get_allowed_drivers_for_a_vehicle(
        self, vehicle_tag: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[DriversResponse, RawError]:
        """Send a ``GET`` request.

        Args:
            vehicle_tag: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/api/1/vehicles/{vehicle_tag}/drivers"),
            path_params=[param[str]("vehicle_tag", vehicle_tag)],
            auth_scheme=AsyncAnySchemes(
                self._auth.thirdpartytoken_authorization_code, self._auth.thirdpartytoken_client_credentials
            ),
            decoder=json_decoder[DriversResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def get_eligible_vehicle_subscriptions(
        self, vin: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[SiteInfoResponse, RawError]:
        """Send a ``GET`` request.

        Args:
            vin: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/api/1/dx/vehicles/subscriptions/eligibility"),
            query_params=[param[str]("vin", vin)],
            auth_scheme=AsyncAnySchemes(
                self._auth.thirdpartytoken_authorization_code, self._auth.thirdpartytoken_client_credentials
            ),
            decoder=json_decoder[SiteInfoResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def get_eligible_vehicle_upgrades(
        self, vin: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[SiteInfoResponse, RawError]:
        """Send a ``GET`` request.

        Args:
            vin: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/api/1/dx/vehicles/upgrades/eligibility"),
            query_params=[param[str]("vin", vin)],
            auth_scheme=AsyncAnySchemes(
                self._auth.thirdpartytoken_authorization_code, self._auth.thirdpartytoken_client_credentials
            ),
            decoder=json_decoder[SiteInfoResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def get_enterprise_roles_for_a_vehicle(
        self, vin: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Any, RawError]:
        """Send a ``GET`` request.

        Args:
            vin: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/api/1/dx/enterprise/v1/{vin}/roles"),
            path_params=[param[str]("vin", vin)],
            auth_scheme=AsyncAnySchemes(
                self._auth.thirdpartytoken_authorization_code, self._auth.thirdpartytoken_client_credentials
            ),
            decoder=json_decoder[Any],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def get_fleet_status_for_vehicles(
        self, body: FleetStatusRequest | FleetStatusRequestDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Any, RawError]:
        """Send a ``POST`` request.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/api/1/vehicles/fleet_status"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[FleetStatusRequest | FleetStatusRequestDict](body),
            auth_scheme=AsyncAnySchemes(
                self._auth.thirdpartytoken_authorization_code, self._auth.thirdpartytoken_client_credentials
            ),
            decoder=json_decoder[Any],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def get_fleet_telemetry_configuration(
        self, vehicle_tag: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Any, RawError]:
        """Send a ``GET`` request.

        Args:
            vehicle_tag: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/api/1/vehicles/{vehicle_tag}/fleet_telemetry_config"),
            path_params=[param[str]("vehicle_tag", vehicle_tag)],
            auth_scheme=AsyncAnySchemes(
                self._auth.thirdpartytoken_authorization_code, self._auth.thirdpartytoken_client_credentials
            ),
            decoder=json_decoder[Any],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def get_fleet_telemetry_errors_for_a_vehicle(
        self, vehicle_tag: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Any, RawError]:
        """Send a ``GET`` request.

        Args:
            vehicle_tag: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/api/1/vehicles/{vehicle_tag}/fleet_telemetry_errors"),
            path_params=[param[str]("vehicle_tag", vehicle_tag)],
            auth_scheme=AsyncAnySchemes(
                self._auth.thirdpartytoken_authorization_code, self._auth.thirdpartytoken_client_credentials
            ),
            decoder=json_decoder[Any],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def get_vehicle(
        self, vehicle_tag: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Api1VehiclesResponseResponse200, RawError]:
        """Send a ``GET`` request.

        Args:
            vehicle_tag: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/api/1/vehicles/{vehicle_tag}"),
            path_params=[param[str]("vehicle_tag", vehicle_tag)],
            auth_scheme=AsyncAnySchemes(
                self._auth.thirdpartytoken_authorization_code, self._auth.thirdpartytoken_client_credentials
            ),
            decoder=json_decoder[Api1VehiclesResponseResponse200],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def list_vehicles(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Api1VehiclesResponse, RawError]:
        """Send a ``GET`` request.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/api/1/vehicles"),
            auth_scheme=AsyncAnySchemes(
                self._auth.thirdpartytoken_authorization_code, self._auth.thirdpartytoken_client_credentials
            ),
            decoder=json_decoder[Api1VehiclesResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def mobile_enabled(
        self, vehicle_tag: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Api1VehiclesMobileEnabledResponse, RawError]:
        """Send a ``GET`` request.

        Args:
            vehicle_tag: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/api/1/vehicles/{vehicle_tag}/mobile_enabled"),
            path_params=[param[str]("vehicle_tag", vehicle_tag)],
            auth_scheme=AsyncAnySchemes(
                self._auth.thirdpartytoken_authorization_code, self._auth.thirdpartytoken_client_credentials
            ),
            decoder=json_decoder[Api1VehiclesMobileEnabledResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def nearby_charging_sites(
        self, vehicle_tag: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Api1VehiclesNearbyChargingSitesResponse, RawError]:
        """Send a ``GET`` request.

        Args:
            vehicle_tag: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/api/1/vehicles/{vehicle_tag}/nearby_charging_sites"),
            path_params=[param[str]("vehicle_tag", vehicle_tag)],
            auth_scheme=AsyncAnySchemes(
                self._auth.thirdpartytoken_authorization_code, self._auth.thirdpartytoken_client_credentials
            ),
            decoder=json_decoder[Api1VehiclesNearbyChargingSitesResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def remove_driver_access_from_a_vehicle(
        self, vehicle_tag: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[SimpleOkResponse, RawError]:
        """Send a ``DELETE`` request.

        Args:
            vehicle_tag: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/api/1/vehicles/{vehicle_tag}/drivers"),
            path_params=[param[str]("vehicle_tag", vehicle_tag)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AsyncAnySchemes(
                self._auth.thirdpartytoken_authorization_code, self._auth.thirdpartytoken_client_credentials
            ),
            decoder=json_decoder[SimpleOkResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def set_enterprise_payer_roles(
        self,
        vin: str,
        body: EnterprisePayerRequest | EnterprisePayerRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, RawError]:
        """Send a ``POST`` request.

        Args:
            vin: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/api/1/dx/enterprise/v1/{vin}/payer"),
            path_params=[param[str]("vin", vin)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[EnterprisePayerRequest | EnterprisePayerRequestDict](body),
            auth_scheme=AsyncAnySchemes(
                self._auth.thirdpartytoken_authorization_code, self._auth.thirdpartytoken_client_credentials
            ),
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def vehicle_live_data(
        self, vehicle_tag: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[SiteInfoResponse, RawError]:
        """Send a ``GET`` request.

        Args:
            vehicle_tag: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/api/1/vehicles/{vehicle_tag}/vehicle_data"),
            path_params=[param[str]("vehicle_tag", vehicle_tag)],
            auth_scheme=AsyncAnySchemes(
                self._auth.thirdpartytoken_authorization_code, self._auth.thirdpartytoken_client_credentials
            ),
            decoder=json_decoder[SiteInfoResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def vehicle_options(
        self, vin: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Api1DxVehiclesOptionsResponse, RawError]:
        """Send a ``GET`` request.

        Args:
            vin: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/api/1/dx/vehicles/options"),
            query_params=[param[str]("vin", vin)],
            auth_scheme=AsyncAnySchemes(
                self._auth.thirdpartytoken_authorization_code, self._auth.thirdpartytoken_client_credentials
            ),
            decoder=json_decoder[Api1DxVehiclesOptionsResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def vehicle_specs(
        self, vin: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[SiteInfoResponse, RawError]:
        """Send a ``GET`` request.

        Args:
            vin: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/api/1/vehicles/{vin}/specs"),
            path_params=[param[str]("vin", vin)],
            auth_scheme=AsyncAnySchemes(
                self._auth.thirdpartytoken_authorization_code, self._auth.thirdpartytoken_client_credentials
            ),
            decoder=json_decoder[SiteInfoResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def wake_up_vehicle(
        self, vehicle_tag: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Api1VehiclesWakeUpResponse, RawError]:
        """Send a ``POST`` request.

        Args:
            vehicle_tag: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/api/1/vehicles/{vehicle_tag}/wake_up"),
            path_params=[param[str]("vehicle_tag", vehicle_tag)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AsyncAnySchemes(
                self._auth.thirdpartytoken_authorization_code, self._auth.thirdpartytoken_client_credentials
            ),
            decoder=json_decoder[Api1VehiclesWakeUpResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def warranty_details(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Api1DxWarrantyDetailsResponse, RawError]:
        """Send a ``GET`` request.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/api/1/dx/warranty/details"),
            auth_scheme=AsyncAnySchemes(
                self._auth.thirdpartytoken_authorization_code, self._auth.thirdpartytoken_client_credentials
            ),
            decoder=json_decoder[Api1DxWarrantyDetailsResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

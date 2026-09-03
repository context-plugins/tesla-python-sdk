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
from ..models.actuate_trunk_request import ActuateTrunkRequest, ActuateTrunkRequestDict
from ..models.add_charge_schedule_request import AddChargeScheduleRequest, AddChargeScheduleRequestDict
from ..models.add_precondition_schedule_request import (
    AddPreconditionScheduleRequest,
    AddPreconditionScheduleRequestDict,
)
from ..models.adjust_volume_request import AdjustVolumeRequest, AdjustVolumeRequestDict
from ..models.command_response import CommandResponse
from ..models.guest_mode_request import GuestModeRequest, GuestModeRequestDict
from ..server.server import Server


class VehicleCommands:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = VehicleCommandsWithRawResponse(client, server, auth)

    def actuatetrunk(
        self,
        vehicle_tag: str,
        body: ActuateTrunkRequest | ActuateTrunkRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CommandResponse:
        """Controls the front or rear trunk

        Args:
            vehicle_tag: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Vehicle command response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.actuatetrunk(vehicle_tag, body, request_options=request_options).unwrap()

    def addchargeschedule(
        self,
        vehicle_tag: str,
        body: AddChargeScheduleRequest | AddChargeScheduleRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CommandResponse:
        """Send a ``POST`` request.

        Args:
            vehicle_tag: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Vehicle command response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.addchargeschedule(vehicle_tag, body, request_options=request_options).unwrap()

    def addpreconditionschedule(
        self,
        vehicle_tag: str,
        body: AddPreconditionScheduleRequest | AddPreconditionScheduleRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CommandResponse:
        """Send a ``POST`` request.

        Args:
            vehicle_tag: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Vehicle command response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.addpreconditionschedule(
            vehicle_tag, body, request_options=request_options
        ).unwrap()

    def adjustmediavolume(
        self,
        vehicle_tag: str,
        body: AdjustVolumeRequest | AdjustVolumeRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CommandResponse:
        """Send a ``POST`` request.

        Args:
            vehicle_tag: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Vehicle command response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.adjustmediavolume(vehicle_tag, body, request_options=request_options).unwrap()

    def cancelsoftwareupdate(
        self, vehicle_tag: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> CommandResponse:
        """Send a ``POST`` request.

        Args:
            vehicle_tag: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Vehicle command response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.cancelsoftwareupdate(vehicle_tag, request_options=request_options).unwrap()

    def chargemaxrange(
        self, vehicle_tag: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> CommandResponse:
        """Send a ``POST`` request.

        Args:
            vehicle_tag: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Vehicle command response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.chargemaxrange(vehicle_tag, request_options=request_options).unwrap()

    def chargestandard(
        self, vehicle_tag: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> CommandResponse:
        """Send a ``POST`` request.

        Args:
            vehicle_tag: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Vehicle command response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.chargestandard(vehicle_tag, request_options=request_options).unwrap()

    def clear_pi_nto_drive_admin(
        self, vehicle_tag: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> CommandResponse:
        """Deactivates PIN to Drive and resets the associated PIN for supported firmware versions.

        Args:
            vehicle_tag: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Vehicle command response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.clear_pi_nto_drive_admin(vehicle_tag, request_options=request_options).unwrap()

    def closechargeportdoor(
        self, vehicle_tag: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> CommandResponse:
        """Send a ``POST`` request.

        Args:
            vehicle_tag: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Vehicle command response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.closechargeportdoor(vehicle_tag, request_options=request_options).unwrap()

    def enableordisable_guest_mode(
        self,
        vehicle_tag: str,
        body: GuestModeRequest | GuestModeRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CommandResponse:
        """Send a ``POST`` request.

        Args:
            vehicle_tag: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Vehicle command response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.enableordisable_guest_mode(
            vehicle_tag, body, request_options=request_options
        ).unwrap()

    def eraseuserdata(
        self, vehicle_tag: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> CommandResponse:
        """Erases user data from the vehicle UI. Requires Guest Mode.

        Args:
            vehicle_tag: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Vehicle command response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.eraseuserdata(vehicle_tag, request_options=request_options).unwrap()

    def flashlights(self, vehicle_tag: str, *, request_options: RequestOptionsOrDict | None = None) -> CommandResponse:
        """Briefly flashes vehicle headlights.

        Args:
            vehicle_tag: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Vehicle command response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.flashlights(vehicle_tag, request_options=request_options).unwrap()

    def honkhorn(self, vehicle_tag: str, *, request_options: RequestOptionsOrDict | None = None) -> CommandResponse:
        """Send a ``POST`` request.

        Args:
            vehicle_tag: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Vehicle command response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.honkhorn(vehicle_tag, request_options=request_options).unwrap()

    def lockdoors(self, vehicle_tag: str, *, request_options: RequestOptionsOrDict | None = None) -> CommandResponse:
        """Send a ``POST`` request.

        Args:
            vehicle_tag: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Vehicle command response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.lockdoors(vehicle_tag, request_options=request_options).unwrap()

    def nextfavoritemediatrack(
        self, vehicle_tag: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> CommandResponse:
        """Send a ``POST`` request.

        Args:
            vehicle_tag: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Vehicle command response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.nextfavoritemediatrack(vehicle_tag, request_options=request_options).unwrap()

    def openchargeportdoor(
        self, vehicle_tag: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> CommandResponse:
        """Send a ``POST`` request.

        Args:
            vehicle_tag: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Vehicle command response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.openchargeportdoor(vehicle_tag, request_options=request_options).unwrap()

    def startcharging(
        self, vehicle_tag: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> CommandResponse:
        """Send a ``POST`` request.

        Args:
            vehicle_tag: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Vehicle command response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.startcharging(vehicle_tag, request_options=request_options).unwrap()

    def startclimatepreconditioning(
        self, vehicle_tag: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> CommandResponse:
        """Send a ``POST`` request.

        Args:
            vehicle_tag: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Vehicle command response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.startclimatepreconditioning(
            vehicle_tag, request_options=request_options
        ).unwrap()

    def stopcharging(self, vehicle_tag: str, *, request_options: RequestOptionsOrDict | None = None) -> CommandResponse:
        """Send a ``POST`` request.

        Args:
            vehicle_tag: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Vehicle command response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.stopcharging(vehicle_tag, request_options=request_options).unwrap()

    def stopclimatepreconditioning(
        self, vehicle_tag: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> CommandResponse:
        """Send a ``POST`` request.

        Args:
            vehicle_tag: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Vehicle command response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.stopclimatepreconditioning(vehicle_tag, request_options=request_options).unwrap()

    def unlockdoors(self, vehicle_tag: str, *, request_options: RequestOptionsOrDict | None = None) -> CommandResponse:
        """Send a ``POST`` request.

        Args:
            vehicle_tag: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Vehicle command response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.unlockdoors(vehicle_tag, request_options=request_options).unwrap()

    @property
    def with_raw_response(self) -> VehicleCommandsWithRawResponse:
        return self._with_raw_response


class AsyncVehicleCommands:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncVehicleCommandsWithRawResponse(client, server, auth)

    async def actuatetrunk(
        self,
        vehicle_tag: str,
        body: ActuateTrunkRequest | ActuateTrunkRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CommandResponse:
        """Controls the front or rear trunk

        Args:
            vehicle_tag: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Vehicle command response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.actuatetrunk(vehicle_tag, body, request_options=request_options)).unwrap()

    async def addchargeschedule(
        self,
        vehicle_tag: str,
        body: AddChargeScheduleRequest | AddChargeScheduleRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CommandResponse:
        """Send a ``POST`` request.

        Args:
            vehicle_tag: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Vehicle command response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.addchargeschedule(vehicle_tag, body, request_options=request_options)
        ).unwrap()

    async def addpreconditionschedule(
        self,
        vehicle_tag: str,
        body: AddPreconditionScheduleRequest | AddPreconditionScheduleRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CommandResponse:
        """Send a ``POST`` request.

        Args:
            vehicle_tag: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Vehicle command response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.addpreconditionschedule(vehicle_tag, body, request_options=request_options)
        ).unwrap()

    async def adjustmediavolume(
        self,
        vehicle_tag: str,
        body: AdjustVolumeRequest | AdjustVolumeRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CommandResponse:
        """Send a ``POST`` request.

        Args:
            vehicle_tag: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Vehicle command response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.adjustmediavolume(vehicle_tag, body, request_options=request_options)
        ).unwrap()

    async def cancelsoftwareupdate(
        self, vehicle_tag: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> CommandResponse:
        """Send a ``POST`` request.

        Args:
            vehicle_tag: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Vehicle command response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.cancelsoftwareupdate(vehicle_tag, request_options=request_options)
        ).unwrap()

    async def chargemaxrange(
        self, vehicle_tag: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> CommandResponse:
        """Send a ``POST`` request.

        Args:
            vehicle_tag: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Vehicle command response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.chargemaxrange(vehicle_tag, request_options=request_options)).unwrap()

    async def chargestandard(
        self, vehicle_tag: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> CommandResponse:
        """Send a ``POST`` request.

        Args:
            vehicle_tag: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Vehicle command response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.chargestandard(vehicle_tag, request_options=request_options)).unwrap()

    async def clear_pi_nto_drive_admin(
        self, vehicle_tag: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> CommandResponse:
        """Deactivates PIN to Drive and resets the associated PIN for supported firmware versions.

        Args:
            vehicle_tag: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Vehicle command response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.clear_pi_nto_drive_admin(vehicle_tag, request_options=request_options)
        ).unwrap()

    async def closechargeportdoor(
        self, vehicle_tag: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> CommandResponse:
        """Send a ``POST`` request.

        Args:
            vehicle_tag: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Vehicle command response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.closechargeportdoor(vehicle_tag, request_options=request_options)
        ).unwrap()

    async def enableordisable_guest_mode(
        self,
        vehicle_tag: str,
        body: GuestModeRequest | GuestModeRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CommandResponse:
        """Send a ``POST`` request.

        Args:
            vehicle_tag: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Vehicle command response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.enableordisable_guest_mode(vehicle_tag, body, request_options=request_options)
        ).unwrap()

    async def eraseuserdata(
        self, vehicle_tag: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> CommandResponse:
        """Erases user data from the vehicle UI. Requires Guest Mode.

        Args:
            vehicle_tag: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Vehicle command response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.eraseuserdata(vehicle_tag, request_options=request_options)).unwrap()

    async def flashlights(
        self, vehicle_tag: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> CommandResponse:
        """Briefly flashes vehicle headlights.

        Args:
            vehicle_tag: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Vehicle command response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.flashlights(vehicle_tag, request_options=request_options)).unwrap()

    async def honkhorn(
        self, vehicle_tag: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> CommandResponse:
        """Send a ``POST`` request.

        Args:
            vehicle_tag: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Vehicle command response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.honkhorn(vehicle_tag, request_options=request_options)).unwrap()

    async def lockdoors(
        self, vehicle_tag: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> CommandResponse:
        """Send a ``POST`` request.

        Args:
            vehicle_tag: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Vehicle command response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.lockdoors(vehicle_tag, request_options=request_options)).unwrap()

    async def nextfavoritemediatrack(
        self, vehicle_tag: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> CommandResponse:
        """Send a ``POST`` request.

        Args:
            vehicle_tag: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Vehicle command response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.nextfavoritemediatrack(vehicle_tag, request_options=request_options)
        ).unwrap()

    async def openchargeportdoor(
        self, vehicle_tag: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> CommandResponse:
        """Send a ``POST`` request.

        Args:
            vehicle_tag: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Vehicle command response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.openchargeportdoor(vehicle_tag, request_options=request_options)).unwrap()

    async def startcharging(
        self, vehicle_tag: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> CommandResponse:
        """Send a ``POST`` request.

        Args:
            vehicle_tag: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Vehicle command response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.startcharging(vehicle_tag, request_options=request_options)).unwrap()

    async def startclimatepreconditioning(
        self, vehicle_tag: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> CommandResponse:
        """Send a ``POST`` request.

        Args:
            vehicle_tag: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Vehicle command response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.startclimatepreconditioning(vehicle_tag, request_options=request_options)
        ).unwrap()

    async def stopcharging(
        self, vehicle_tag: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> CommandResponse:
        """Send a ``POST`` request.

        Args:
            vehicle_tag: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Vehicle command response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.stopcharging(vehicle_tag, request_options=request_options)).unwrap()

    async def stopclimatepreconditioning(
        self, vehicle_tag: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> CommandResponse:
        """Send a ``POST`` request.

        Args:
            vehicle_tag: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Vehicle command response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.stopclimatepreconditioning(vehicle_tag, request_options=request_options)
        ).unwrap()

    async def unlockdoors(
        self, vehicle_tag: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> CommandResponse:
        """Send a ``POST`` request.

        Args:
            vehicle_tag: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Vehicle command response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.unlockdoors(vehicle_tag, request_options=request_options)).unwrap()

    @property
    def with_raw_response(self) -> AsyncVehicleCommandsWithRawResponse:
        return self._with_raw_response


class VehicleCommandsWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def actuatetrunk(
        self,
        vehicle_tag: str,
        body: ActuateTrunkRequest | ActuateTrunkRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CommandResponse, RawError]:
        """Controls the front or rear trunk

        Args:
            vehicle_tag: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/api/1/vehicles/{vehicle_tag}/command/actuate_trunk"),
            path_params=[param[str]("vehicle_tag", vehicle_tag)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[ActuateTrunkRequest | ActuateTrunkRequestDict](body),
            auth_scheme=AnySchemes(
                self._auth.thirdpartytoken_authorization_code, self._auth.thirdpartytoken_client_credentials
            ),
            decoder=json_decoder[CommandResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def addchargeschedule(
        self,
        vehicle_tag: str,
        body: AddChargeScheduleRequest | AddChargeScheduleRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CommandResponse, RawError]:
        """Send a ``POST`` request.

        Args:
            vehicle_tag: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/api/1/vehicles/{vehicle_tag}/command/add_charge_schedule"),
            path_params=[param[str]("vehicle_tag", vehicle_tag)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[AddChargeScheduleRequest | AddChargeScheduleRequestDict](body),
            auth_scheme=AnySchemes(
                self._auth.thirdpartytoken_authorization_code, self._auth.thirdpartytoken_client_credentials
            ),
            decoder=json_decoder[CommandResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def addpreconditionschedule(
        self,
        vehicle_tag: str,
        body: AddPreconditionScheduleRequest | AddPreconditionScheduleRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CommandResponse, RawError]:
        """Send a ``POST`` request.

        Args:
            vehicle_tag: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/api/1/vehicles/{vehicle_tag}/command/add_precondition_schedule"),
            path_params=[param[str]("vehicle_tag", vehicle_tag)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[AddPreconditionScheduleRequest | AddPreconditionScheduleRequestDict](body),
            auth_scheme=AnySchemes(
                self._auth.thirdpartytoken_authorization_code, self._auth.thirdpartytoken_client_credentials
            ),
            decoder=json_decoder[CommandResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def adjustmediavolume(
        self,
        vehicle_tag: str,
        body: AdjustVolumeRequest | AdjustVolumeRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CommandResponse, RawError]:
        """Send a ``POST`` request.

        Args:
            vehicle_tag: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/api/1/vehicles/{vehicle_tag}/command/adjust_volume"),
            path_params=[param[str]("vehicle_tag", vehicle_tag)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[AdjustVolumeRequest | AdjustVolumeRequestDict](body),
            auth_scheme=AnySchemes(
                self._auth.thirdpartytoken_authorization_code, self._auth.thirdpartytoken_client_credentials
            ),
            decoder=json_decoder[CommandResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def cancelsoftwareupdate(
        self, vehicle_tag: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[CommandResponse, RawError]:
        """Send a ``POST`` request.

        Args:
            vehicle_tag: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/api/1/vehicles/{vehicle_tag}/command/cancel_software_update"),
            path_params=[param[str]("vehicle_tag", vehicle_tag)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AnySchemes(
                self._auth.thirdpartytoken_authorization_code, self._auth.thirdpartytoken_client_credentials
            ),
            decoder=json_decoder[CommandResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def chargemaxrange(
        self, vehicle_tag: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[CommandResponse, RawError]:
        """Send a ``POST`` request.

        Args:
            vehicle_tag: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/api/1/vehicles/{vehicle_tag}/command/charge_max_range"),
            path_params=[param[str]("vehicle_tag", vehicle_tag)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AnySchemes(
                self._auth.thirdpartytoken_authorization_code, self._auth.thirdpartytoken_client_credentials
            ),
            decoder=json_decoder[CommandResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def chargestandard(
        self, vehicle_tag: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[CommandResponse, RawError]:
        """Send a ``POST`` request.

        Args:
            vehicle_tag: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/api/1/vehicles/{vehicle_tag}/command/charge_standard"),
            path_params=[param[str]("vehicle_tag", vehicle_tag)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AnySchemes(
                self._auth.thirdpartytoken_authorization_code, self._auth.thirdpartytoken_client_credentials
            ),
            decoder=json_decoder[CommandResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def clear_pi_nto_drive_admin(
        self, vehicle_tag: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[CommandResponse, RawError]:
        """Deactivates PIN to Drive and resets the associated PIN for supported firmware versions.

        Args:
            vehicle_tag: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/api/1/vehicles/{vehicle_tag}/command/clear_pin_to_drive_admin"),
            path_params=[param[str]("vehicle_tag", vehicle_tag)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AnySchemes(
                self._auth.thirdpartytoken_authorization_code, self._auth.thirdpartytoken_client_credentials
            ),
            decoder=json_decoder[CommandResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def closechargeportdoor(
        self, vehicle_tag: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[CommandResponse, RawError]:
        """Send a ``POST`` request.

        Args:
            vehicle_tag: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/api/1/vehicles/{vehicle_tag}/command/charge_port_door_close"),
            path_params=[param[str]("vehicle_tag", vehicle_tag)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AnySchemes(
                self._auth.thirdpartytoken_authorization_code, self._auth.thirdpartytoken_client_credentials
            ),
            decoder=json_decoder[CommandResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def enableordisable_guest_mode(
        self,
        vehicle_tag: str,
        body: GuestModeRequest | GuestModeRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CommandResponse, RawError]:
        """Send a ``POST`` request.

        Args:
            vehicle_tag: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/api/1/vehicles/{vehicle_tag}/command/guest_mode"),
            path_params=[param[str]("vehicle_tag", vehicle_tag)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[GuestModeRequest | GuestModeRequestDict](body),
            auth_scheme=AnySchemes(
                self._auth.thirdpartytoken_authorization_code, self._auth.thirdpartytoken_client_credentials
            ),
            decoder=json_decoder[CommandResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def eraseuserdata(
        self, vehicle_tag: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[CommandResponse, RawError]:
        """Erases user data from the vehicle UI. Requires Guest Mode.

        Args:
            vehicle_tag: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/api/1/vehicles/{vehicle_tag}/command/erase_user_data"),
            path_params=[param[str]("vehicle_tag", vehicle_tag)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AnySchemes(
                self._auth.thirdpartytoken_authorization_code, self._auth.thirdpartytoken_client_credentials
            ),
            decoder=json_decoder[CommandResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def flashlights(
        self, vehicle_tag: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[CommandResponse, RawError]:
        """Briefly flashes vehicle headlights.

        Args:
            vehicle_tag: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/api/1/vehicles/{vehicle_tag}/command/flash_lights"),
            path_params=[param[str]("vehicle_tag", vehicle_tag)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AnySchemes(
                self._auth.thirdpartytoken_authorization_code, self._auth.thirdpartytoken_client_credentials
            ),
            decoder=json_decoder[CommandResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def honkhorn(
        self, vehicle_tag: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[CommandResponse, RawError]:
        """Send a ``POST`` request.

        Args:
            vehicle_tag: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/api/1/vehicles/{vehicle_tag}/command/honk_horn"),
            path_params=[param[str]("vehicle_tag", vehicle_tag)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AnySchemes(
                self._auth.thirdpartytoken_authorization_code, self._auth.thirdpartytoken_client_credentials
            ),
            decoder=json_decoder[CommandResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def lockdoors(
        self, vehicle_tag: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[CommandResponse, RawError]:
        """Send a ``POST`` request.

        Args:
            vehicle_tag: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/api/1/vehicles/{vehicle_tag}/command/door_lock"),
            path_params=[param[str]("vehicle_tag", vehicle_tag)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AnySchemes(
                self._auth.thirdpartytoken_authorization_code, self._auth.thirdpartytoken_client_credentials
            ),
            decoder=json_decoder[CommandResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def nextfavoritemediatrack(
        self, vehicle_tag: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[CommandResponse, RawError]:
        """Send a ``POST`` request.

        Args:
            vehicle_tag: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/api/1/vehicles/{vehicle_tag}/command/media_next_fav"),
            path_params=[param[str]("vehicle_tag", vehicle_tag)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AnySchemes(
                self._auth.thirdpartytoken_authorization_code, self._auth.thirdpartytoken_client_credentials
            ),
            decoder=json_decoder[CommandResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def openchargeportdoor(
        self, vehicle_tag: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[CommandResponse, RawError]:
        """Send a ``POST`` request.

        Args:
            vehicle_tag: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/api/1/vehicles/{vehicle_tag}/command/charge_port_door_open"),
            path_params=[param[str]("vehicle_tag", vehicle_tag)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AnySchemes(
                self._auth.thirdpartytoken_authorization_code, self._auth.thirdpartytoken_client_credentials
            ),
            decoder=json_decoder[CommandResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def startcharging(
        self, vehicle_tag: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[CommandResponse, RawError]:
        """Send a ``POST`` request.

        Args:
            vehicle_tag: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/api/1/vehicles/{vehicle_tag}/command/charge_start"),
            path_params=[param[str]("vehicle_tag", vehicle_tag)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AnySchemes(
                self._auth.thirdpartytoken_authorization_code, self._auth.thirdpartytoken_client_credentials
            ),
            decoder=json_decoder[CommandResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def startclimatepreconditioning(
        self, vehicle_tag: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[CommandResponse, RawError]:
        """Send a ``POST`` request.

        Args:
            vehicle_tag: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/api/1/vehicles/{vehicle_tag}/command/auto_conditioning_start"),
            path_params=[param[str]("vehicle_tag", vehicle_tag)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AnySchemes(
                self._auth.thirdpartytoken_authorization_code, self._auth.thirdpartytoken_client_credentials
            ),
            decoder=json_decoder[CommandResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def stopcharging(
        self, vehicle_tag: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[CommandResponse, RawError]:
        """Send a ``POST`` request.

        Args:
            vehicle_tag: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/api/1/vehicles/{vehicle_tag}/command/charge_stop"),
            path_params=[param[str]("vehicle_tag", vehicle_tag)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AnySchemes(
                self._auth.thirdpartytoken_authorization_code, self._auth.thirdpartytoken_client_credentials
            ),
            decoder=json_decoder[CommandResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def stopclimatepreconditioning(
        self, vehicle_tag: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[CommandResponse, RawError]:
        """Send a ``POST`` request.

        Args:
            vehicle_tag: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/api/1/vehicles/{vehicle_tag}/command/auto_conditioning_stop"),
            path_params=[param[str]("vehicle_tag", vehicle_tag)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AnySchemes(
                self._auth.thirdpartytoken_authorization_code, self._auth.thirdpartytoken_client_credentials
            ),
            decoder=json_decoder[CommandResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def unlockdoors(
        self, vehicle_tag: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[CommandResponse, RawError]:
        """Send a ``POST`` request.

        Args:
            vehicle_tag: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/api/1/vehicles/{vehicle_tag}/command/door_unlock"),
            path_params=[param[str]("vehicle_tag", vehicle_tag)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AnySchemes(
                self._auth.thirdpartytoken_authorization_code, self._auth.thirdpartytoken_client_credentials
            ),
            decoder=json_decoder[CommandResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncVehicleCommandsWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def actuatetrunk(
        self,
        vehicle_tag: str,
        body: ActuateTrunkRequest | ActuateTrunkRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CommandResponse, RawError]:
        """Controls the front or rear trunk

        Args:
            vehicle_tag: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/api/1/vehicles/{vehicle_tag}/command/actuate_trunk"),
            path_params=[param[str]("vehicle_tag", vehicle_tag)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[ActuateTrunkRequest | ActuateTrunkRequestDict](body),
            auth_scheme=AsyncAnySchemes(
                self._auth.thirdpartytoken_authorization_code, self._auth.thirdpartytoken_client_credentials
            ),
            decoder=json_decoder[CommandResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def addchargeschedule(
        self,
        vehicle_tag: str,
        body: AddChargeScheduleRequest | AddChargeScheduleRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CommandResponse, RawError]:
        """Send a ``POST`` request.

        Args:
            vehicle_tag: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/api/1/vehicles/{vehicle_tag}/command/add_charge_schedule"),
            path_params=[param[str]("vehicle_tag", vehicle_tag)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[AddChargeScheduleRequest | AddChargeScheduleRequestDict](body),
            auth_scheme=AsyncAnySchemes(
                self._auth.thirdpartytoken_authorization_code, self._auth.thirdpartytoken_client_credentials
            ),
            decoder=json_decoder[CommandResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def addpreconditionschedule(
        self,
        vehicle_tag: str,
        body: AddPreconditionScheduleRequest | AddPreconditionScheduleRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CommandResponse, RawError]:
        """Send a ``POST`` request.

        Args:
            vehicle_tag: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/api/1/vehicles/{vehicle_tag}/command/add_precondition_schedule"),
            path_params=[param[str]("vehicle_tag", vehicle_tag)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[AddPreconditionScheduleRequest | AddPreconditionScheduleRequestDict](body),
            auth_scheme=AsyncAnySchemes(
                self._auth.thirdpartytoken_authorization_code, self._auth.thirdpartytoken_client_credentials
            ),
            decoder=json_decoder[CommandResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def adjustmediavolume(
        self,
        vehicle_tag: str,
        body: AdjustVolumeRequest | AdjustVolumeRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CommandResponse, RawError]:
        """Send a ``POST`` request.

        Args:
            vehicle_tag: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/api/1/vehicles/{vehicle_tag}/command/adjust_volume"),
            path_params=[param[str]("vehicle_tag", vehicle_tag)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[AdjustVolumeRequest | AdjustVolumeRequestDict](body),
            auth_scheme=AsyncAnySchemes(
                self._auth.thirdpartytoken_authorization_code, self._auth.thirdpartytoken_client_credentials
            ),
            decoder=json_decoder[CommandResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def cancelsoftwareupdate(
        self, vehicle_tag: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[CommandResponse, RawError]:
        """Send a ``POST`` request.

        Args:
            vehicle_tag: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/api/1/vehicles/{vehicle_tag}/command/cancel_software_update"),
            path_params=[param[str]("vehicle_tag", vehicle_tag)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AsyncAnySchemes(
                self._auth.thirdpartytoken_authorization_code, self._auth.thirdpartytoken_client_credentials
            ),
            decoder=json_decoder[CommandResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def chargemaxrange(
        self, vehicle_tag: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[CommandResponse, RawError]:
        """Send a ``POST`` request.

        Args:
            vehicle_tag: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/api/1/vehicles/{vehicle_tag}/command/charge_max_range"),
            path_params=[param[str]("vehicle_tag", vehicle_tag)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AsyncAnySchemes(
                self._auth.thirdpartytoken_authorization_code, self._auth.thirdpartytoken_client_credentials
            ),
            decoder=json_decoder[CommandResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def chargestandard(
        self, vehicle_tag: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[CommandResponse, RawError]:
        """Send a ``POST`` request.

        Args:
            vehicle_tag: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/api/1/vehicles/{vehicle_tag}/command/charge_standard"),
            path_params=[param[str]("vehicle_tag", vehicle_tag)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AsyncAnySchemes(
                self._auth.thirdpartytoken_authorization_code, self._auth.thirdpartytoken_client_credentials
            ),
            decoder=json_decoder[CommandResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def clear_pi_nto_drive_admin(
        self, vehicle_tag: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[CommandResponse, RawError]:
        """Deactivates PIN to Drive and resets the associated PIN for supported firmware versions.

        Args:
            vehicle_tag: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/api/1/vehicles/{vehicle_tag}/command/clear_pin_to_drive_admin"),
            path_params=[param[str]("vehicle_tag", vehicle_tag)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AsyncAnySchemes(
                self._auth.thirdpartytoken_authorization_code, self._auth.thirdpartytoken_client_credentials
            ),
            decoder=json_decoder[CommandResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def closechargeportdoor(
        self, vehicle_tag: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[CommandResponse, RawError]:
        """Send a ``POST`` request.

        Args:
            vehicle_tag: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/api/1/vehicles/{vehicle_tag}/command/charge_port_door_close"),
            path_params=[param[str]("vehicle_tag", vehicle_tag)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AsyncAnySchemes(
                self._auth.thirdpartytoken_authorization_code, self._auth.thirdpartytoken_client_credentials
            ),
            decoder=json_decoder[CommandResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def enableordisable_guest_mode(
        self,
        vehicle_tag: str,
        body: GuestModeRequest | GuestModeRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CommandResponse, RawError]:
        """Send a ``POST`` request.

        Args:
            vehicle_tag: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/api/1/vehicles/{vehicle_tag}/command/guest_mode"),
            path_params=[param[str]("vehicle_tag", vehicle_tag)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[GuestModeRequest | GuestModeRequestDict](body),
            auth_scheme=AsyncAnySchemes(
                self._auth.thirdpartytoken_authorization_code, self._auth.thirdpartytoken_client_credentials
            ),
            decoder=json_decoder[CommandResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def eraseuserdata(
        self, vehicle_tag: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[CommandResponse, RawError]:
        """Erases user data from the vehicle UI. Requires Guest Mode.

        Args:
            vehicle_tag: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/api/1/vehicles/{vehicle_tag}/command/erase_user_data"),
            path_params=[param[str]("vehicle_tag", vehicle_tag)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AsyncAnySchemes(
                self._auth.thirdpartytoken_authorization_code, self._auth.thirdpartytoken_client_credentials
            ),
            decoder=json_decoder[CommandResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def flashlights(
        self, vehicle_tag: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[CommandResponse, RawError]:
        """Briefly flashes vehicle headlights.

        Args:
            vehicle_tag: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/api/1/vehicles/{vehicle_tag}/command/flash_lights"),
            path_params=[param[str]("vehicle_tag", vehicle_tag)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AsyncAnySchemes(
                self._auth.thirdpartytoken_authorization_code, self._auth.thirdpartytoken_client_credentials
            ),
            decoder=json_decoder[CommandResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def honkhorn(
        self, vehicle_tag: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[CommandResponse, RawError]:
        """Send a ``POST`` request.

        Args:
            vehicle_tag: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/api/1/vehicles/{vehicle_tag}/command/honk_horn"),
            path_params=[param[str]("vehicle_tag", vehicle_tag)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AsyncAnySchemes(
                self._auth.thirdpartytoken_authorization_code, self._auth.thirdpartytoken_client_credentials
            ),
            decoder=json_decoder[CommandResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def lockdoors(
        self, vehicle_tag: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[CommandResponse, RawError]:
        """Send a ``POST`` request.

        Args:
            vehicle_tag: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/api/1/vehicles/{vehicle_tag}/command/door_lock"),
            path_params=[param[str]("vehicle_tag", vehicle_tag)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AsyncAnySchemes(
                self._auth.thirdpartytoken_authorization_code, self._auth.thirdpartytoken_client_credentials
            ),
            decoder=json_decoder[CommandResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def nextfavoritemediatrack(
        self, vehicle_tag: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[CommandResponse, RawError]:
        """Send a ``POST`` request.

        Args:
            vehicle_tag: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/api/1/vehicles/{vehicle_tag}/command/media_next_fav"),
            path_params=[param[str]("vehicle_tag", vehicle_tag)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AsyncAnySchemes(
                self._auth.thirdpartytoken_authorization_code, self._auth.thirdpartytoken_client_credentials
            ),
            decoder=json_decoder[CommandResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def openchargeportdoor(
        self, vehicle_tag: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[CommandResponse, RawError]:
        """Send a ``POST`` request.

        Args:
            vehicle_tag: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/api/1/vehicles/{vehicle_tag}/command/charge_port_door_open"),
            path_params=[param[str]("vehicle_tag", vehicle_tag)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AsyncAnySchemes(
                self._auth.thirdpartytoken_authorization_code, self._auth.thirdpartytoken_client_credentials
            ),
            decoder=json_decoder[CommandResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def startcharging(
        self, vehicle_tag: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[CommandResponse, RawError]:
        """Send a ``POST`` request.

        Args:
            vehicle_tag: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/api/1/vehicles/{vehicle_tag}/command/charge_start"),
            path_params=[param[str]("vehicle_tag", vehicle_tag)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AsyncAnySchemes(
                self._auth.thirdpartytoken_authorization_code, self._auth.thirdpartytoken_client_credentials
            ),
            decoder=json_decoder[CommandResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def startclimatepreconditioning(
        self, vehicle_tag: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[CommandResponse, RawError]:
        """Send a ``POST`` request.

        Args:
            vehicle_tag: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/api/1/vehicles/{vehicle_tag}/command/auto_conditioning_start"),
            path_params=[param[str]("vehicle_tag", vehicle_tag)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AsyncAnySchemes(
                self._auth.thirdpartytoken_authorization_code, self._auth.thirdpartytoken_client_credentials
            ),
            decoder=json_decoder[CommandResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def stopcharging(
        self, vehicle_tag: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[CommandResponse, RawError]:
        """Send a ``POST`` request.

        Args:
            vehicle_tag: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/api/1/vehicles/{vehicle_tag}/command/charge_stop"),
            path_params=[param[str]("vehicle_tag", vehicle_tag)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AsyncAnySchemes(
                self._auth.thirdpartytoken_authorization_code, self._auth.thirdpartytoken_client_credentials
            ),
            decoder=json_decoder[CommandResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def stopclimatepreconditioning(
        self, vehicle_tag: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[CommandResponse, RawError]:
        """Send a ``POST`` request.

        Args:
            vehicle_tag: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/api/1/vehicles/{vehicle_tag}/command/auto_conditioning_stop"),
            path_params=[param[str]("vehicle_tag", vehicle_tag)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AsyncAnySchemes(
                self._auth.thirdpartytoken_authorization_code, self._auth.thirdpartytoken_client_credentials
            ),
            decoder=json_decoder[CommandResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def unlockdoors(
        self, vehicle_tag: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[CommandResponse, RawError]:
        """Send a ``POST`` request.

        Args:
            vehicle_tag: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/api/1/vehicles/{vehicle_tag}/command/door_unlock"),
            path_params=[param[str]("vehicle_tag", vehicle_tag)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AsyncAnySchemes(
                self._auth.thirdpartytoken_authorization_code, self._auth.thirdpartytoken_client_credentials
            ),
            decoder=json_decoder[CommandResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

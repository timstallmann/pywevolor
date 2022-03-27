from typing import Union, List, Dict

import aiohttp


class Wevolor:
    """Python wrapper for Wevolor local API.

    Requires Wevolor device version 5.4 or greater.
    """

    def __init__(self, host: str) -> None:
        """Initialize host IP address."""
        self.host = host

    async def get_status(self) -> Union[None, Dict[str, any]]:
        """Test if we can authenticate with the host."""
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(f'http://{self.host}/_status') as response:
                    return await response.json()

        except aiohttp.ClientError:
            return None

    async def _send_command(self, command: str, channels: List[int]) -> bool:
        # Group is a bitwise flag for the channels to be controlled.
        group = sum([2**(i-1) for i in channels])
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(f'http://{self.host}/_command?action={command}&groups={group}') as response:
                    return response.status == 200

        except aiohttp.ClientError:
            return False

    async def open_blind(self, channel: int) -> bool:
        """Send command to open blind on specified channel."""
        return await self.open_blinds([channel, ])

    async def close_blind(self, channel: int) -> bool:
        """Send command to close blind on specified channel."""
        return await self.close_blinds([channel, ])

    async def favorite_blind(self, channel: int) -> bool:
        """Send command to set blind on specified channel to favorite position."""
        return await self.favorite_blinds([channel, ])

    async def stop_blind(self, channel: int) -> bool:
        """Send command to stop blind on specified channel."""
        return await self.stop_blinds([channel, ])

    async def open_blind_tilt(self, channel: int) -> bool:
        """Send command to open blind tilt on specified channel."""
        return await self.open_blinds_tilt([channel, ])

    async def close_blind_tilt(self, channel: int) -> bool:
        """Send command to close blind tilt on specified channel."""
        return await self.close_blinds_tilt([channel, ])

    async def stop_blind_tilt(self, channel: int) -> bool:
        """Send command to stop blind tilt on specified channel."""
        return await self.stop_blinds_tilt(channel)
    
    async def open_blinds(self, channels: list[int]) -> bool:
        """Send command to open blinds on specified channels."""
        return await self._send_command('open', channels)

    async def close_blinds(self, channels) -> bool:
        """Send command to close blinds on specified channels."""
        return await self._send_command('close', channels)

    async def favorite_blinds(self, channels: list[int]) -> bool:
        """Send command to set blinds on specified channels to favorite position."""
        return await self._send_command('favorite', channels)

    async def stop_blinds(self, channels: list[int]) -> bool:
        """Send command to stop blinds on specified channels."""
        return await self._send_command('stop', channels)

    async def open_blinds_tilt(self, channels: list[int]) -> bool:
        """Send command to open blinds tilt on specified channels."""
        return await self._send_command('tiltopen', channels)

    async def close_blinds_tilt(self, channels: list[int]) -> bool:
        """Send command to close blinds tilt on specified channels."""
        return await self._send_command('tiltclose', channels)

    async def stop_blinds_tilt(self, channels: list[int]) -> bool:
        """Send command to stop blinds tilt on specified channels."""
        return await self.stop_blinds(channels)

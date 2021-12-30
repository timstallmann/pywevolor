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
        return await self._send_command('open', [channel, ])

    async def close_blind(self, channel: int) -> bool:
        """Send command to close blind on specified channel."""
        return await self._send_command('close', [channel, ])

    async def favorite_blind(self, channel: int) -> bool:
        """Send command to set blind on specified channel to favorite position."""
        return await self._send_command('favorite', [channel, ])

    async def stop_blind(self, channel: int) -> bool:
        """Send command to stop blind on specified channel."""
        return await self._send_command('stop', [channel, ])

    async def open_blind_tilt(self, channel: int) -> bool:
        """Send command to open blind tilt on specified channel."""
        return await self._send_command('tiltopen', [channel, ])

    async def close_blind_tilt(self, channel: int) -> bool:
        """Send command to close blind tilt on specified channel."""
        return await self._send_command('tiltclose', [channel, ])

    async def stop_blind_tilt(self, channel: int) -> bool:
        """Send command to stop blind tilt on specified channel."""
        return await self.stop_blind(channel)

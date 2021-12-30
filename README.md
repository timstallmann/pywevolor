# PyWevolor

This package is a lightweight wrapper around the local API for the [Wevolor](https://wevolor.com/) device.

Wevolor is a WiFi to bluetooth bridge device for controlling Levolor motorized blinds via the Levolor 6-channel bluetooth remote.

## Requirements

Wevolor device with firmware 5.4 or higher, accessible on the local network.

## Usage

Instantiate a `Wevolor` object with the host IP address.

Commands are triggered with methods on the `Wevolor` object, e.g.:

```python
from pywevolor import Wevolor

wevolor = Wevolor(host='192.168.1.1')

# Send open command to channel 3 on the remote.
wevolor.open_blind(3)

# Send close command to channel 3 on the remote.
wevolor.close_blind(3)

# Get status info from Wevolor API
wevolor.get_status()
```

## Limitations

The public API currently does not support sending commands
to multiple channels at once.


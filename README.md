# Pinch Cafe

A dashboard-style page to be displayed on a public 42" TV screen in the lobby of Pinch Cafe, Tooting Works, Tooting, London.

Includes the cafe's menu, times for various nearby public transport, and whatever else we feel might be handy.

This is a community project - we meet up in Pinch Cafe every other Thursday evening (6:30pm). See [Meetup](https://www.meetup.com/sw-london-design-code-coffee-eve/) for more details.

## Installation

If you want a local development version installed on your local machine you will need Node.js installed.

You can view the [hosted version](https://dev.sansay.co.uk/pinch-cafe) used by the kiosk machine in the cafe.

The screen in Pinch Cafe is driven by a Raspberry Pi 3 running as a simple web kiosk, configured using the following ["configKiosk"](https://github.com/dhicks6345789/device-config) command:

```
curl -s https://www.sansay.co.uk/device-config/configKiosk.py > config.py; sudo python3 config.py --URL https://dev.sansay.co.uk/pinch-cafe; rm config.py
```

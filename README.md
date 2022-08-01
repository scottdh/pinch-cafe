# Pinch Cafe

A dashboard-style page to be displayed on a public 42" TV screen in the lobby of Pinch Cafe, Tooting Works, Tooting, London.

Includes the cafe's menu, times for various nearby public transport, and whatever else we feel might be handy.

This is a community project - we meet up in Pinch Cafe every other Thursday evening (6:30pm). See [Meetup](https://www.meetup.com/sw-london-design-code-coffee-eve/) for more details.

## Installation

If you want a local development version installed on your local machine you will need [Node.js](https://nodejs.org/en/) and [Eleventy](https://www.11ty.dev/) installed.

You can view the [hosted version](https://dev.sansay.co.uk/pinch-cafe) used by the kiosk machine in the cafe.

The screen in Pinch Cafe is driven by a Raspberry Pi 3 running as a simple web kiosk, configured using the following ["configKiosk"](https://github.com/dhicks6345789/device-config) command:

```
curl -s https://www.sansay.co.uk/device-config/configKiosk.py > config.py; sudo python3 config.py --URL https://dev.sansay.co.uk/pinch-cafe; rm config.py
```

## Development

If you want access to the Github project, contact Scott, the project owner. There is also a shared Google Drive folder where some content is placed.

The hosted version used in the cafe is hosted on a server running [Web Console](https://github.com/dhicks6345789/web-console).

Hosted version of the display screen: [https://dev.sansay.co.uk/pinch-cafe](https://dev.sansay.co.uk/pinch-cafe).

URL of Web Console task to build the Github project: [https://dev.sansay.co.uk/view?taskID=pinch-cafe](https://dev.sansay.co.uk/view?taskID=pinch-cafe).

Shared Google Drive folder for display content: [https://drive.google.com/drive/folders/1JYy3Vd2T3y7-sOH_7hZktn-4Ax8KW_RJ?usp=sharing](https://drive.google.com/drive/folders/1JYy3Vd2T3y7-sOH_7hZktn-4Ax8KW_RJ?usp=sharing).

Web Console task to fetch data from the TFL API: (https://dev.sansay.co.uk/view?taskID=lv04p52ns6fqnbzi)[https://dev.sansay.co.uk/view?taskID=lv04p52ns6fqnbzi].

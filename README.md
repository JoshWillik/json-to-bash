# JSON to BASH

Converts your JSON configs into bash exports

## Installation

```
$ git clone https://github.com/joshwillik/json-to-bash.git
$ chmod +x json-to-bash/json-to-bash.py
$ mv json-to-bash/json-to-bash.py ~/my-scripts/json-to-bash
# Assuming ~/my-scripts is in $PATH
```

## Usage

```js
// config.json
{
  "remoteHost": "api.app.biz",
  "authenticationOff": true,
  "useTestServer": true
}
```
```shell
$ json-to-bash < config.json
# Generated exports
export REMOTE_HOST=api.app.biz
export USE_TEST_SERVER=true
export AUTHENTICATION_OFF=true
$ eval $( json-to-bash < config.json )
# JSON config exported
```
## Note
As of right now, json-to-bash makes no attempt to preserve json key order, as python scrambles dictionary order. If you need this, please open an issue and say why.

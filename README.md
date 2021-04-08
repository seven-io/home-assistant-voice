![Sms77.io Logo](https://www.sms77.io/wp-content/uploads/2019/07/sms77-Logo-400x79.png "Sms77.io Logo")

# Official Home Assistant Voice Component

## Installation

Add to `configuration.yaml` usually in `~/.homeassistant/`:

```yaml
sms77_voice:

notify:
  - platform: sms77_voice
    sender: +491771783130 # Must be a verified virtual inbound number or a shared virtual number
    name: sms77_voice
    api_key: ThisIsWhereYouInsertYourSms77ApiKey
    recipient: +4943160049853
```

### Example

[Configure service call on automation](./screenshots/automation_action_call_service.png)

#### Support

Need help? Feel free to [contact us](https://www.sms77.io/en/company/contact/).

[![MIT](https://img.shields.io/badge/License-MIT-teal.svg)](./LICENSE)
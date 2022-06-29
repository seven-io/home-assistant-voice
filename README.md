![sms77.io Logo](https://www.sms77.io/wp-content/uploads/2019/07/sms77-Logo-400x79.png "sms77.io Logo")

# Official Home Assistant Voice Component

This integration adds the possibility of making text-to-speech calls via [sms77](https://www.sms77.io).

## Installation

### Manually

Clone the repository to a folder called "custom_components" in your Home
Assistant root directory, e.g. `git clone https://github.com/seven-io/home-assistant-voice ~/.homeassistant/custom_components/sms77_voice`

### Via [HACS](https://hacs.xyz/)
- Navigate to HACS -> Integrations -> Custom repositories -> Add
- Set *Repository* to **https://github.com/seven-io/home-assistant-voice**
- Set *Type* to **Integration**
- Confirm form submission and the repository should be appended to the list

## Configuration

Add to `configuration.yaml` usually in `~/.homeassistant/`:

```yaml
sms77_voice:

notify:
  - platform: sms77_voice
    sender: +491771783130 # Must be a verified virtual inbound number or a shared virtual number 
    name: sms77_voice
    api_key: ThisIsWhereYouInsertYourSms77ApiKey # see https://help.sms77.io/en/api-key-access
    recipient: +4943130149270
```

Check out the [example](./screenshots/automation_action_call_service.png) on how to
configure a service call on automation.

## Support

Need help? Feel free to [contact us](https://www.sms77.io/en/company/contact/).

[![MIT](https://img.shields.io/badge/License-MIT-teal.svg)](LICENSE)
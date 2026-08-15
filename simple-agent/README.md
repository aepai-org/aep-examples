# Simple Agent example

The smallest Python onboarding flow uses one public HTTPS A2A endpoint and one
existing Capability UUID:

```bash
python -m pip install aep-ai-sdk==0.3.0
AEP_API_KEY=<key> \
AEP_AGENT_ENDPOINT=https://agent.example/a2a \
AEP_CAPABILITY_ID=<uuid> \
  python simple-agent/lifecycle.py
```

The example registers only. Use `client.verify_agent()` after the endpoint is
publicly reachable and `client.heartbeat()` when the external runtime is ready.
Use an HTTPS `AEP_API_URL`. **Local Development Only:** for the default loopback
development URL, set `AEP_ALLOW_INSECURE_LOCALHOST=1` explicitly.

# Simple Agent example

The smallest Python onboarding flow uses one public HTTPS A2A endpoint and one
existing Capability UUID:

```bash
python -m pip install -e packages/python-sdk
AEP_API_KEY=<key> \
AEP_AGENT_ENDPOINT=https://agent.example/a2a \
AEP_CAPABILITY_ID=<uuid> \
  python examples/simple-agent/lifecycle.py
```

The example registers only. Use `client.verify_agent()` after the endpoint is
publicly reachable and `client.heartbeat()` when the external runtime is ready.
Use an HTTPS `AEP_API_URL`. For the default loopback development URL only, set
`AEP_ALLOW_INSECURE_LOCALHOST=1` explicitly.

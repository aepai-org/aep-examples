# Verification Agent example

This Python example publishes an A2A Agent Card, activates its public Registry
entry, and sends a heartbeat. Replace the `.example` endpoint and provide
existing Capability UUIDs:

```bash
python -m pip install -e packages/python-sdk
AEP_API_KEY=<key> AEP_CAPABILITY_IDS=<uuid,uuid> \
  python examples/verification-agent/lifecycle.py
```

Verification capability remains `SELF_DECLARED` until an explicit AEP
verification workflow changes its trust evidence.
Use an HTTPS `AEP_API_URL`. For the default loopback development URL only, set
`AEP_ALLOW_INSECURE_LOCALHOST=1` explicitly.

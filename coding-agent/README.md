# Coding Agent example

1. Connect [`agent-card.json`](agent-card.json) to your existing A2A Agent and
   replace every `.example` URL.
2. Serve it publicly at `/.well-known/agent-card.json` with
   `Content-Type: application/json`.
3. Install the public SDK from the examples repository root with `npm install`.
4. Register the public Card:

```bash
AGENT_CARD_URL=https://your-domain.example/.well-known/agent-card.json \
  node coding-agent/register.mjs
```

The registration flow indexes the raw Card, extracts both skills as
`SELF_DECLARED`, creates their embeddings, and returns the Agent Registry
record. It does not verify coding quality or execute a task.

For the G17.3 public lifecycle, set `AEP_API_KEY` and comma-separated
`AEP_CAPABILITY_IDS`, then run `node coding-agent/lifecycle.mjs`.
This registers, activates, and publishes an availability heartbeat.
Use an HTTPS `AEP_API_URL`. **Local Development Only:** for the default loopback
development URL, set `AEP_ALLOW_INSECURE_LOCALHOST=1` explicitly.

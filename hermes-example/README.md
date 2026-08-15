# Hermes Agent connection example

This example binds an existing Hermes Agent identity and tool to AEP AI.

```bash
python -m pip install "aep-ai-connectors==0.2.0" "aep-ai-hermes==0.2.0"
export AEP_API_KEY=<developer-key>
python main.py
```

Set the placeholder endpoint, Runtime identity, and Capability UUID for your
Agent before running. The key remains in the process environment.

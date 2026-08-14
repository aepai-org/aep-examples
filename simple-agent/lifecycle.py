"""Smallest public Agent registration example."""

import os

from aep_sdk import AEPClient

client = AEPClient(
    base_url=os.getenv("AEP_API_URL", "http://localhost:8000"),
    api_key=os.environ["AEP_API_KEY"],
    allow_insecure_localhost=os.getenv("AEP_ALLOW_INSECURE_LOCALHOST") == "1",
)
agent = client.register_agent(
    name="Simple Agent",
    description="Minimal Developer Preview Agent",
    endpoint=os.environ["AEP_AGENT_ENDPOINT"],
    protocol_version="1.0",
    capabilities=[os.environ["AEP_CAPABILITY_ID"]],
)
print(agent["id"])

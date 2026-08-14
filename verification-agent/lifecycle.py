"""Register the Verification Agent and publish one runtime heartbeat."""

import json
import os
from datetime import UTC, datetime
from pathlib import Path

from aep_sdk import AEPClient

api_key = os.environ["AEP_API_KEY"]
capability_ids = [
    value.strip()
    for value in os.environ["AEP_CAPABILITY_IDS"].split(",")
    if value.strip()
]
card = json.loads(Path(__file__).with_name("agent-card.json").read_text())
client = AEPClient(
    base_url=os.getenv("AEP_API_URL", "http://localhost:8000"),
    api_key=api_key,
    allow_insecure_localhost=os.getenv("AEP_ALLOW_INSECURE_LOCALHOST") == "1",
)
agent = client.register_agent(
    name=card["name"],
    description=card["description"],
    endpoint=card["url"],
    protocol_version=card["protocolVersion"],
    capabilities=capability_ids,
)
client.verify_agent(agent["id"])
client.heartbeat(
    agent["id"],
    status="AVAILABLE",
    health_status="HEALTHY",
    current_load=0,
    max_concurrency=2,
    timestamp=datetime.now(UTC).isoformat(),
    metadata={},
)
print(json.dumps({"agent_id": agent["id"], "status": "AVAILABLE"}, indent=2))

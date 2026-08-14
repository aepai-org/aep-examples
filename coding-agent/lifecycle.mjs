import { readFile } from "node:fs/promises";

import { AEPClient } from "../../packages/sdk/dist/index.js";

const apiKey = process.env.AEP_API_KEY;
const capabilityIds = (process.env.AEP_CAPABILITY_IDS ?? "")
  .split(",")
  .map((value) => value.trim())
  .filter(Boolean);
if (!apiKey || capabilityIds.length === 0) {
  throw new Error("Set AEP_API_KEY and AEP_CAPABILITY_IDS before running");
}

const card = JSON.parse(
  await readFile(new URL("./agent-card.json", import.meta.url), "utf8"),
);
const client = new AEPClient({
  baseUrl: process.env.AEP_API_URL ?? "http://localhost:8000",
  apiKey,
  allowInsecureLocalhost: process.env.AEP_ALLOW_INSECURE_LOCALHOST === "1",
});
const agent = await client.registerPublicAgent({
  name: card.name,
  description: card.description,
  endpoint: card.url,
  protocolVersion: card.protocolVersion,
  capabilities: capabilityIds,
});
await client.verifyPublicAgent(agent.id);
await client.heartbeat(agent.id, {
  status: "AVAILABLE",
  health_status: "HEALTHY",
  current_load: 0,
  max_concurrency: 4,
  timestamp: new Date().toISOString(),
});
console.log(JSON.stringify({ agent_id: agent.id, status: "AVAILABLE" }, null, 2));

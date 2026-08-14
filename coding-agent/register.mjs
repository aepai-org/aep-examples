import { RegistryClient } from "../../packages/sdk/dist/index.js";

const apiBaseUrl = process.env.AEP_API_URL ?? "http://localhost:8000";
const agentCardUrl = process.env.AGENT_CARD_URL;

if (!agentCardUrl) {
  throw new Error(
    "Set AGENT_CARD_URL to the public Coding Agent Card URL before registering.",
  );
}

const client = new RegistryClient({
  baseUrl: apiBaseUrl,
  allowInsecureLocalhost: process.env.AEP_ALLOW_INSECURE_LOCALHOST === "1",
});
const result = await client.registerAgent(agentCardUrl);

console.log(
  JSON.stringify(
    {
      agent_id: result.agent.id,
      name: result.agent.name,
      capabilities: result.capabilities.items.map((item) => ({
        id: item.capability_id,
        name: item.capability.name,
        source: item.source,
      })),
      embedding_count: result.embeddings.length,
    },
    null,
    2,
  ),
);

import os

from aep_hermes_plugin import (
    HermesAEPPlugin,
    HermesCapabilityBinding,
    HermesPluginConfig,
)


def connect() -> None:
    plugin = HermesAEPPlugin(
        HermesPluginConfig(
            base_url="https://api.aepai.org",
            api_key=os.environ["AEP_API_KEY"],
            endpoint="https://hermes.example/aep",
            runtime_agent_id="hermes-research",
            display_name="Hermes Research Agent",
        )
    )
    binding = plugin.bind_identity(
        (HermesCapabilityBinding("research", "<capability-uuid>"),),
        max_concurrency=2,
    )
    print(binding.connector_session_id)


if __name__ == "__main__":
    connect()

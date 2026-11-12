# AGENTS.md

This folder connects MCP clients to Ironflow's hosted Hyperliquid MCP server at `https://mcp.ironflow.sh/mcp` (Streamable HTTP, stateless, no key needed).

## Setting it up for a user

- Claude Code: `claude mcp add --transport http ironflow https://mcp.ironflow.sh/mcp`. In this folder, `.mcp.json` already has it.
- Other clients: the config files here (`.cursor/mcp.json`, `.vscode/mcp.json`, `.codex/config.toml`, `.gemini/settings.json`) and the list in README.md. Copy the right one to the client's user config for use outside this folder.
- Check the server answers: `python check.py` (Python 3.9+, standard library only). It runs initialize, tools/list and one tools/call.
- A key is optional: header `Authorization: Bearer if_...`, or `?key=if_...` on the URL. Never write a user's key into a file that gets committed; use the client's environment variable support or user-level config.

## Using the tools

- Markets take display symbols (BTC-PERP, xyz:NVDA-PERP, HYPE/USDC) or Hyperliquid names (BTC, xyz:NVDA, @107). `list_markets` with `q` finds a name.
- Times take Unix ms, Unix seconds, ISO 8601 or relative times (-7d, -24h, now).
- Start with `get_liquidations` or `get_liquidation_summary` for liquidations, `get_liquidation_map` for where open positions would be liquidated, `get_user_state` for a wallet, `get_markets_snapshot` and `get_candles` for market moves.
- For anything else: `describe_data`, then `run_query` with one ClickHouse SELECT over the `hl.*` tables.
- A result can start with a `notice`, for example that a window was cut to the key's history. Pass it on to the user.
- Keyless: 30 requests a minute, 300 a day, 24 hours of history. A free key (https://ironflow.sh/key) gives 60 a minute and 14 days.
- No tool places a Hyperliquid order. `create_ironbox` makes a paper box, a simulated account for testing a bot.

## Reference

- Setup for every client: https://docs.ironflow.sh/guides/ai-agents
- Server source and tool list: https://github.com/ironflowsh/mcp
- REST API behind the tools: https://api.ironflow.sh/openapi.yaml

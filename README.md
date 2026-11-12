# Hyperliquid MCP quickstart

Connect Claude Code, Cursor, VS Code, Codex, Gemini CLI, ChatGPT and other MCP clients to Hyperliquid data. The server is hosted at `https://mcp.ironflow.sh/mcp`. Nothing to install and no key needed.

Its tools cover trades, candles, funding, open interest, liquidations, the liquidation map, wallet positions and PnL, top traders and read-only SQL. They work across native perps, HIP-3 markets, HIP-4 outcomes and spot.

## Check

```bash
python check.py
```

```text
Connected to Ironflow Hyperliquid 0.18.0 at https://mcp.ironflow.sh/mcp
54 tools, e.g. describe_data, run_query, get_wallet_behavior, get_price, get_recent_trades, get_candles, get_funding_rates, get_open_interest
Liquidations in the last 1h: 199 (longs $14,463, shorts $968,038)
```

## Open this folder

The server is already set up for these clients in this folder:

| Client | File |
|---|---|
| Claude Code | `.mcp.json` (approve it when Claude Code asks) |
| Cursor | `.cursor/mcp.json` |
| VS Code | `.vscode/mcp.json` |
| Codex | `.codex/config.toml` (trusted projects) |
| Gemini CLI | `.gemini/settings.json` |

## Add it everywhere

- **Claude Code:** `claude mcp add --transport http ironflow https://mcp.ironflow.sh/mcp`
- **Claude desktop and claude.ai:** Settings, Connectors, Add custom connector. Name it Ironflow, paste `https://mcp.ironflow.sh/mcp`, no sign-in.
- **Cursor:** [one-click install](https://cursor.com/install-mcp?name=ironflow&config=eyJ1cmwiOiJodHRwczovL21jcC5pcm9uZmxvdy5zaC9tY3AifQ%3D%3D), or copy `.cursor/mcp.json` to `~/.cursor/mcp.json`.
- **VS Code:** [one-click install](https://insiders.vscode.dev/redirect?url=vscode%3Amcp%2Finstall%3F%257B%2522name%2522%253A%2522ironflow%2522%252C%2522type%2522%253A%2522http%2522%252C%2522url%2522%253A%2522https%253A%252F%252Fmcp.ironflow.sh%252Fmcp%2522%257D), or copy `.vscode/mcp.json`.
- **Codex:** add `.codex/config.toml`'s two lines to `~/.codex/config.toml`.
- **Gemini CLI:** `gemini mcp add --transport http -s user ironflow https://mcp.ironflow.sh/mcp`
- **ChatGPT:** [chatgpt.com/plugins](https://chatgpt.com/plugins), +, Add custom MCP server. Paste the URL and choose no authentication.
- **Windsurf:** in `~/.codeium/windsurf/mcp_config.json`, `{"mcpServers": {"ironflow": {"serverUrl": "https://mcp.ironflow.sh/mcp"}}}`
- **Cline:** in `cline_mcp_settings.json`, `{"mcpServers": {"ironflow": {"type": "streamableHttp", "url": "https://mcp.ironflow.sh/mcp"}}}`
- **Zed:** in `settings.json`, `"context_servers": {"ironflow": {"url": "https://mcp.ironflow.sh/mcp"}}`
- **Local (stdio):** `npx -y @ironflowsh/mcp` ([npm](https://www.npmjs.com/package/@ironflowsh/mcp), [source](https://github.com/ironflowsh/mcp)).

## Ask

- "Who got liquidated on Hyperliquid in the last hour?"
- "Where would BTC longs get liquidated if price fell 5%?"
- "Show this wallet's open positions and 30-day PnL: 0x..."
- "Which perps had the biggest open interest jump today?"
- "Write SQL for hourly ETH taker buy and sell volume over the last day."

## Limits and keys

Without a key: 30 requests a minute, 300 a day and 24 hours of history. A free key from [ironflow.sh/key](https://ironflow.sh/key) gives 60 a minute and 14 days. Send it as the header `Authorization: Bearer if_your_key`:

```bash
claude mcp add --transport http ironflow https://mcp.ironflow.sh/mcp --header "Authorization: Bearer if_your_key"
```

For clients that cannot set headers, use `https://mcp.ironflow.sh/mcp?key=if_your_key`. For the local package, set `IRONFLOW_API_KEY`.

For a read-only set of data tools, use `https://mcp.ironflow.sh/mcp?toolset=data`.

## Links

- [Setup guide for every client](https://docs.ironflow.sh/guides/ai-agents)
- [Tool list and source](https://github.com/ironflowsh/mcp)
- [Ironflow API docs](https://docs.ironflow.sh)

## License

MIT

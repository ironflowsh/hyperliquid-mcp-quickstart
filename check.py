"""Check the connection to Ironflow's hosted Hyperliquid MCP server.

    python check.py

Connects the way an MCP client does (Streamable HTTP), lists the tools and
calls one. Python 3.9+, standard library only, no key needed.
"""
from __future__ import annotations

import json
import os
import urllib.request

URL = os.environ.get("IRONFLOW_MCP_URL", "https://mcp.ironflow.sh/mcp")
CLIENT = os.environ.get("IRONFLOW_USER_AGENT", "hyperliquid-mcp-quickstart")
KEY = os.environ.get("IRONFLOW_KEY", "")  # optional, from https://ironflow.sh/key


def rpc(method: str, params: dict | None = None, id: int | None = 1) -> dict:
    body = {"jsonrpc": "2.0", "method": method, "params": params or {}}
    if id is not None:
        body["id"] = id
    headers = {"Content-Type": "application/json", "Accept": "application/json, text/event-stream",
               "User-Agent": CLIENT}
    if KEY:
        headers["Authorization"] = f"Bearer {KEY}"
    req = urllib.request.Request(URL, data=json.dumps(body).encode(), headers=headers)
    with urllib.request.urlopen(req, timeout=60) as r:
        text = r.read().decode()
    if not text:
        return {}
    if text.startswith("event:") or text.startswith("data:"):  # an SSE reply
        text = next(line[5:] for line in text.splitlines() if line.startswith("data:"))
    reply = json.loads(text)
    if "error" in reply:
        raise SystemExit(f"{method}: {reply['error']}")
    return reply["result"]


def main() -> None:
    init = rpc("initialize", {"protocolVersion": "2025-06-18", "capabilities": {},
                              "clientInfo": {"name": CLIENT, "version": "0.1"}})
    server = init["serverInfo"]
    print(f"Connected to {server.get('title', server['name'])} {server['version']} at {URL}")
    rpc("notifications/initialized", id=None)

    tools = rpc("tools/list", id=2)["tools"]
    print(f"{len(tools)} tools, e.g. " + ", ".join(t["name"] for t in tools[:8]))

    result = rpc("tools/call", {"name": "get_liquidation_summary", "arguments": {"window": "1h"}}, id=3)
    s = json.loads(result["content"][0]["text"])
    print(f"Liquidations in the last {s['window']}: {s['count']:,} (longs ${s['longs_liquidated_usd']:,.0f}, "
          f"shorts ${s['shorts_liquidated_usd']:,.0f})")
    print("Ready. Add the server to your client: see README.md.")


if __name__ == "__main__":
    main()

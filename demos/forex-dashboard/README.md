# RathodX FX dashboard — freelance portfolio sample

**Status:** Original client-facing visual demo only. No live feed or trading functionality.

Open `index.html` in a modern browser. It uses eight illustrative FX pairs and a browser-local simulation, with a responsive chart, pair search, simulated bid/ask/spread, session high/low and pause/update interval controls. It needs no dependencies or account.

## Demo limitations
- Quote values and charts are **synthetic**, and must not be represented as market data.
- No API key, live provider, broker integration, orders or historical candles are included.
- The forex client in the Nov 26 Freelancer email requires a real external market-data provider; implementing it depends on the client's **licensed API**, API docs, quotas, available quote fields and approved backend hosting.

## Client delivery plan
**Milestone A — data contract and UI**: Confirm symbols, quote precision, timestamps, refresh frequency, chart history, sorting/search requirements, device breakpoints and backend hosting. Provide responsive views and keyboard-accessible controls.

**Milestone B — authorized provider adapter**: Server-side credential storage; a bounded upstream HTTP/WebSocket client; normalisation to a documented JSON schema with fields `symbol`, `bid`, `ask`, `timestamp`, `source`; provider-specific authentication, retries/backoff and clear stale/error state. Never disclose provider tokens in browser code.

**Milestone C — verification and handoff**: Representative fixtures and contract tests; latency, stale-data, reconnection, failure and rate-limit cases; simple deployment guide and code handover.

## Proposed commercial guardrails
- Scope, permitted market-data provider, accepted features, milestone payments and support terms must be agreed **before production work**.
- Demonstration is not a promise of a completed live system.
- Price and timeline are indicative until the client's full brief and API limitations have been reviewed.

Created as an original proof of UI capability for a specific freelance opportunity.
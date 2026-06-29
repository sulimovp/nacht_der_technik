# Leaderboard backend

A tiny shared leaderboard for the games (currently used by **Quanten-Elfmeter**). Pick **one** of
the two options below. Both expose the same API and both enable CORS, so the static games can call
them from any origin.

## API

```
GET  /scores?board=penalty&top=10   ->  [{ "name": "...", "score": 7, "ts": 1720000000000 }, ...]   (highest first)
POST /scores   body { "board":"penalty", "name":"Mia", "score":7 }   ->  { "ok": true }
```

Names are trimmed to 12 chars and sanitised; scores are clamped to 0–1000.

## Option A — Cloudflare Worker (recommended: free, global, zero maintenance)

```bash
npm i -g wrangler
wrangler login
wrangler kv namespace create LB      # copy the printed id into wrangler.toml
wrangler deploy                       # prints https://htq-leaderboard.<you>.workers.dev
```

Then open `quantum-penalty.html` and set:

```js
const LB_API_BASE = "https://htq-leaderboard.<you>.workers.dev";
```

(or append `?api=https://...workers.dev` to the URL for quick testing).

## Option B — plain Node (self-host)

```bash
node server.js          # listens on :8787, writes scores.json
```

Put it behind HTTPS (the games are served over HTTPS, and browsers block calling an http API from
an https page). Then set `LB_API_BASE` to that public https URL.

## How robust is this at the stand?

- The **games themselves are 100% client-side** — each phone runs its own copy, so the number of
  kids playing at once does **not** load any server of ours.
- The leaderboard is the **only** shared component. A Cloudflare Worker handles thousands of
  requests/second; a kids' stand will do maybe a few hundred score posts the whole evening. Load is
  a non-issue.
- If the leaderboard URL is **unreachable** (no Wi-Fi, backend down), every game **falls back to a
  local leaderboard** stored in the browser — so a phone always shows *a* board and nothing breaks.
- Practical caveat: a *shared* board needs the phones to reach the internet. If you want one combined
  ranking for the prize, the cleanest is to run the competition on **one or two stand tablets** that
  you know are online, and read the live board there. Kids' own phones still play fine for fun.

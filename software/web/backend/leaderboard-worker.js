/*
 * Hack the Quantum — leaderboard (Cloudflare Worker)
 * Free, global, scales far beyond a kids' stand. Stores top scores per "board" in KV.
 *
 * Deploy (one time):
 *   npm i -g wrangler && wrangler login
 *   wrangler kv namespace create LB           # note the id it prints
 *   # put that id in wrangler.toml (see backend/wrangler.toml)
 *   wrangler deploy
 * Then set LB_API_BASE in the game HTML to the printed https://....workers.dev URL.
 *
 * API:
 *   GET  /scores?board=penalty&top=10  -> [{name,score,ts}, ...] (desc)
 *   POST /scores  {board,name,score}   -> {ok:true}
 */
const CORS = {
  "Access-Control-Allow-Origin": "*",
  "Access-Control-Allow-Methods": "GET,POST,OPTIONS",
  "Access-Control-Allow-Headers": "Content-Type",
};
const MAX_KEEP = 100;
const json = (obj, status = 200) =>
  new Response(JSON.stringify(obj), { status, headers: { "Content-Type": "application/json", ...CORS } });

function cleanBoard(b) { return (typeof b === "string" && /^[a-z0-9_-]{1,24}$/i.test(b)) ? b : "default"; }
function cleanName(n) { return String(n || "Anonym").replace(/[<>&"]/g, "").trim().slice(0, 12) || "Anonym"; }
function cleanScore(s) { s = Math.floor(Number(s)); return (Number.isFinite(s) && s >= 0 && s <= 1000) ? s : 0; }

export default {
  async fetch(req, env) {
    if (req.method === "OPTIONS") return new Response(null, { headers: CORS });
    const url = new URL(req.url);
    if (!url.pathname.endsWith("/scores")) return json({ error: "not found" }, 404);

    if (req.method === "GET") {
      const board = cleanBoard(url.searchParams.get("board"));
      const top = Math.min(50, Math.max(1, parseInt(url.searchParams.get("top") || "10", 10)));
      const list = JSON.parse((await env.LB.get("board:" + board)) || "[]");
      return json(list.slice(0, top));
    }

    if (req.method === "POST") {
      let body;
      try { body = await req.json(); } catch { return json({ error: "bad json" }, 400); }
      const board = cleanBoard(body.board);
      const entry = { name: cleanName(body.name), score: cleanScore(body.score), ts: Date.now() };
      const key = "board:" + board;
      const list = JSON.parse((await env.LB.get(key)) || "[]");
      list.push(entry);
      list.sort((a, b) => b.score - a.score || a.ts - b.ts);
      await env.LB.put(key, JSON.stringify(list.slice(0, MAX_KEEP)));
      return json({ ok: true });
    }
    return json({ error: "method" }, 405);
  },
};

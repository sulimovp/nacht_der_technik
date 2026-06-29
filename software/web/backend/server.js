/*
 * Hack the Quantum — leaderboard (plain Node, no dependencies).
 * Use this instead of the Cloudflare Worker if you'd rather self-host
 * (e.g. on a small VPS or anywhere that runs Node and is reachable over HTTPS).
 *
 * Run:   node server.js            # listens on :8787, stores scores in scores.json
 * API is identical to the Worker:
 *   GET  /scores?board=penalty&top=10
 *   POST /scores  {board,name,score}
 *
 * NOTE: for phones on cellular data the host must be reachable over the public
 * internet (and HTTPS if the games are served over HTTPS — browsers block mixed content).
 */
const http = require("http");
const fs = require("fs");
const FILE = "./scores.json";
const MAX_KEEP = 100;
const cors = {
  "Access-Control-Allow-Origin": "*",
  "Access-Control-Allow-Methods": "GET,POST,OPTIONS",
  "Access-Control-Allow-Headers": "Content-Type",
};
const load = () => { try { return JSON.parse(fs.readFileSync(FILE)); } catch { return {}; } };
const save = (d) => fs.writeFileSync(FILE, JSON.stringify(d));
const cleanBoard = (b) => (/^[a-z0-9_-]{1,24}$/i.test(b || "") ? b : "default");
const cleanName = (n) => String(n || "Anonym").replace(/[<>&"]/g, "").trim().slice(0, 12) || "Anonym";
const cleanScore = (s) => { s = Math.floor(Number(s)); return Number.isFinite(s) && s >= 0 && s <= 1000 ? s : 0; };
const send = (res, obj, status = 200) =>
  res.writeHead(status, { "Content-Type": "application/json", ...cors }).end(JSON.stringify(obj));

http.createServer((req, res) => {
  if (req.method === "OPTIONS") return res.writeHead(204, cors).end();
  const url = new URL(req.url, "http://x");
  if (!url.pathname.endsWith("/scores")) return send(res, { error: "not found" }, 404);

  if (req.method === "GET") {
    const board = cleanBoard(url.searchParams.get("board"));
    const top = Math.min(50, Math.max(1, parseInt(url.searchParams.get("top") || "10", 10)));
    const list = load()["board:" + board] || [];
    return send(res, list.slice(0, top));
  }
  if (req.method === "POST") {
    let raw = "";
    req.on("data", (c) => (raw += c));
    req.on("end", () => {
      let b; try { b = JSON.parse(raw); } catch { return send(res, { error: "bad json" }, 400); }
      const db = load();
      const key = "board:" + cleanBoard(b.board);
      const list = db[key] || [];
      list.push({ name: cleanName(b.name), score: cleanScore(b.score), ts: Date.now() });
      list.sort((a, z) => z.score - a.score || a.ts - z.ts);
      db[key] = list.slice(0, MAX_KEEP);
      save(db);
      send(res, { ok: true });
    });
    return;
  }
  send(res, { error: "method" }, 405);
}).listen(8787, () => console.log("Leaderboard on http://localhost:8787"));

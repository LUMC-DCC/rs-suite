import { readFile } from "node:fs/promises";
import { instance } from "@viz-js/viz";

const dotPath = process.argv[2];
if (!dotPath) {
  throw new Error("usage: node scripts/render-diagram.mjs <diagram.dot>");
}

const dot = await readFile(dotPath, "utf8");
const viz = await instance();
let svg = viz.renderString(dot, { engine: "dot", format: "svg" });

svg = svg.replace(
  /<svg ([^>]+)>/,
  '<svg $1 role="img" aria-labelledby="suite-title suite-description">\n' +
    '  <title id="suite-title">RS suite map</title>\n' +
    '  <desc id="suite-description">Projects grouped by lifecycle category with labelled relationships.</desc>',
);

process.stdout.write(svg);

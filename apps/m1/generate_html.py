#!/usr/bin/env python3
"""Generate large synthetic HTML files for stress-testing a BeautifulSoup 4 program.

Examples:
    python generate_html.py                        # 10 files x 100 MB = ~1 GB in ./sample_html
    python generate_html.py --size-mb 500          # 10 files x 500 MB = ~5 GB
    python generate_html.py --files 3 --size-mb 1  # quick smoke test

Files are streamed to disk in chunks, so memory use stays small no matter how big they get.
Content mixes headings, paragraphs, links, images, lists, tables, nested divs, scripts,
comments, unicode, HTML entities, and (optionally) slightly malformed markup.
"""
import argparse
import os
import random

WORDS = ("lorem ipsum dolor sit amet consectetur adipiscing elit sed do eiusmod tempor "
         "incididunt ut labore et dolore magna aliqua data parser soup tag attribute "
         "scrape crawl index node tree element select find class title café naïve "
         "日本語 データ résumé").split()
TAGS_INLINE = ["b", "i", "em", "strong", "span", "code"]


def words(rng, n):
    return " ".join(rng.choice(WORDS) for _ in range(n))


def paragraph(rng, i):
    inner = words(rng, rng.randint(10, 40))
    if rng.random() < 0.3:
        t = rng.choice(TAGS_INLINE)
        inner += f" <{t}>{words(rng, 3)}</{t}> {words(rng, 5)}"
    if rng.random() < 0.1:
        inner += " &amp; &lt;escaped&gt; &copy; &nbsp;"
    return f'<p class="para c{i % 7}" id="p{i}">{inner}</p>\n'


def link(rng, i):
    return (f'<a href="https://example.com/page/{i}?q={rng.randint(0, 9999)}" '
            f'class="link" data-id="{i}">{words(rng, 3)}</a>\n')


def image(rng, i):
    return f'<img src="/img/{i}.png" alt="{words(rng, 2)}" width="{rng.randint(50, 800)}">\n'


def ul(rng, i):
    items = "".join(f'<li class="item">{words(rng, 4)}</li>' for _ in range(rng.randint(3, 10)))
    return f'<ul id="list{i}">{items}</ul>\n'


def table(rng, i):
    rows = "".join(
        "<tr>" + "".join(f"<td>{rng.randint(0, 99999)}</td>" for _ in range(4)) + "</tr>"
        for _ in range(rng.randint(3, 8)))
    return (f'<table class="data" id="t{i}"><thead><tr><th>A</th><th>B</th><th>C</th><th>D</th>'
            f"</tr></thead><tbody>{rows}</tbody></table>\n")


def nested(rng, i, depth=0):
    if depth > 4:
        return f"<span>{words(rng, 3)}</span>"
    return (f'<div class="level{depth}">' + nested(rng, i, depth + 1)
            + f"<p>{words(rng, 4)}</p></div>")


def misc(rng, i):
    r = rng.random()
    if r < 0.33:
        return f"<!-- comment {i}: {words(rng, 5)} -->\n"
    if r < 0.66:
        return f"<script>var x{i} = {rng.randint(0, 1000)}; // {words(rng, 3)}</script>\n"
    return f'<h{rng.randint(2, 4)} class="heading">{words(rng, 5)}</h{rng.randint(2, 4)}>\n'


def malformed(rng, i):
    # Unclosed tags / bad nesting, which parsers like lxml and html.parser handle differently
    return f"<p>unclosed paragraph {i} <b>bold <i>both</b> italic</i>\n<br>\n"


def make_block(rng, i, malformed_rate):
    parts = [paragraph(rng, i), link(rng, i), image(rng, i), ul(rng, i),
             table(rng, i), nested(rng, i) + "\n", misc(rng, i)]
    out = "".join(rng.sample(parts, k=rng.randint(3, len(parts))))
    if rng.random() < malformed_rate:
        out += malformed(rng, i)
    return f'<section class="block" data-n="{i}">\n{out}</section>\n'


def write_file(path, target_bytes, seed, malformed_rate):
    rng = random.Random(seed)
    written = 0
    i = 0
    head = (f'<!DOCTYPE html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n'
            f"<title>Sample document {seed}</title>\n</head>\n<body>\n")
    tail = "</body>\n</html>\n"
    with open(path, "w", encoding="utf-8", buffering=1 << 20) as f:
        f.write(head)
        written += len(head.encode())
        while written < target_bytes:
            block = make_block(rng, i, malformed_rate)
            f.write(block)
            written += len(block.encode())
            i += 1
        f.write(tail)
    return i


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--files", type=int, default=10)
    ap.add_argument("--size-mb", type=float, default=100, help="size of EACH file in MB")
    ap.add_argument("--out", default="sample_html")
    ap.add_argument("--malformed-rate", type=float, default=0.02,
                    help="fraction of blocks with broken markup (0 to disable)")
    args = ap.parse_args()

    os.makedirs(args.out, exist_ok=True)
    target = int(args.size_mb * 1024 * 1024)
    print(f"Writing {args.files} files x {args.size_mb} MB "
          f"(~{args.files * args.size_mb / 1024:.2f} GB) to {args.out}/")
    for n in range(1, args.files + 1):
        path = os.path.join(args.out, f"sample_{n:02d}.html")
        blocks = write_file(path, target, seed=n, malformed_rate=args.malformed_rate)
        print(f"  {path}: {os.path.getsize(path) / 1024 / 1024:.1f} MB, {blocks} blocks")


if __name__ == "__main__":
    main()

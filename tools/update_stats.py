"""
Update GitHub Profile Stats SVGs
================================
Fetches fresh SVG cards from reliable unthrottled endpoints and saves them
directly into assets/ to ensure 100% uptime without GitHub API rate limits.
"""

import urllib.request
from pathlib import Path


def update_stats():
    assets_dir = Path(__file__).resolve().parent.parent / "assets"
    assets_dir.mkdir(exist_ok=True)

    # 1. Streak Stats
    url_streak = (
        "https://streak-stats.demolab.com?user=HiteshdropNan&theme=tokyonight"
        "&hide_border=true&background=0b0f19&ring=38bdf8&fire=38bdf8&currStreakLabel=38bdf8"
    )
    try:
        req1 = urllib.request.Request(url_streak, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req1) as r1:
            content = r1.read()
            if b"Something went wrong" not in content and len(content) > 1000:
                with open(assets_dir / "streak-stats.svg", "wb") as f:
                    f.write(content)
                print("Successfully updated streak-stats.svg")
    except Exception as e:
        print(f"Error fetching streak stats: {e}")

    # 2. GitHub Stats Card
    url_stats = (
        "https://github-stats-alpha.vercel.app/api?username=HiteshdropNan"
        "&show_icons=true&theme=tokyonight&hide_border=true&bg_color=0b0f19"
        "&title_color=38bdf8&icon_color=22c55e&text_color=94a3b8"
    )
    try:
        req2 = urllib.request.Request(url_stats, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req2) as r2:
            content = r2.read()
            if b"Something went wrong" not in content and len(content) > 1000:
                with open(assets_dir / "github-stats.svg", "wb") as f:
                    f.write(content)
                print("Successfully updated github-stats.svg")
    except Exception as e:
        print(f"Error fetching github stats: {e}")


if __name__ == "__main__":
    update_stats()

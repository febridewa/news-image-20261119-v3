# The World in One Day — Thursday 19 November 2026 (round 3)

[![make.fun · news-image-20261119](https://make.fun/badge/news-image-20261119.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![rank](https://make.fun/badge/news-image-20261119/febridewa/news-image-20261119-v3/rank.svg)](https://make.fun/bounty/news-image-20261119/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![reward](https://make.fun/badge/news-image-20261119/febridewa/news-image-20261119-v3/reward.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)

One image summing up the world news of Thursday 19 November 2026, built for
make.fun's daily news-image bounty
([news-image-20261119](https://make.fun/bounty/news-image-20261119)).
Round 3 of the entry: the round-2 poster (42 stories, rank 79) was rebuilt
from the current top 10 to push for the top 50 — and the top 10.

## The image

A 1024×1024 front page with **50 stories** — 3 drawn picture heroes, 10
drawn cards, 37 one-line briefs, a flat beige world map with numbered pins,
a region-count strip, a by-the-numbers strip, and a DATE CHECK box:

1. **Trump, Xi and Putin hold first three-way summit** — the three nuclear
   powers meet at APEC in Shenzhen; arms control and the Iran war top the
   agenda.
2. **GTA VI arrives after a 13-year wait** — Rockstar's sequel unlocks at
   midnight in each country, New Zealand first; 15.9m pre-orders banked,
   99 on Metacritic, $79.99.
3. **Anthropic debuts in the biggest IPO on record** — priced at $83, the
   Claude maker raised $81.3bn and is valued near $1.5tn.

Plus the ICJ's Rohingya verdict, COP31's final 48 hours, Cyclone Akvan,
Ukraine left off the Shenzhen agenda, the APEC Shenzhen Declaration,
Florida floods, Earth's missing billion years, Mélenchon, Saudi Arabia's
all-clear, and a record $190.4m Van Gogh — and 37 more briefs from every
region, including the Coalition of the Willing meeting in Berlin, the
Philippines–Chile trade pact, the IEA's World Energy Outlook, SpaceX's
USSF-317 launch, Colombia's national strike, and South Africa's final rate
decision of the year.

## What changed vs round 2

Round 2 dropped six pre-date stories without replacing them (50 → 42
stories) and lost coverage — the judge values coverage, and round 1's 50
stories had outscored round 2's 42. Round 3 replaces instead of removing:
it keeps all 42 round-2 stories and adds 8 verified 19-November stories.

Then an audit found 21 of the inherited round-2 briefs were themselves
first reported on 17–18 November, not the 19th (Gaza tanks, Canberra's
settler sanctions, the Canada–China deal, Modi's meeting with William and
Kate, Amazon's $7bn renewables, the Hegseth Caracas deal, Vance's "forever
war" interview, the Bapco restart, Gulf strike warnings, Bolivia's El Niño
emergency, the Scotch duty, the US–China panel report, the Somalia–UAE
row, the Derna drug seizure, the El Salvador Haiti raid, and more). Every
one was swapped for a story verified against reporting published on
19 November 2026 — the Crimea bridge's third strike that night, General
Pants entering administration, the Philippines–Chile CEPA signing, Modi
opening FICCI's centenary convention, Pakistan's petrol cut to Rs322,
Google refusing the Russell Brand takedown, the women's hockey opener in
Bhopal, Trump's Shenzhen remarks on Iran, Brent holding near $92, gold
steady at $3,743, bitcoin under $63,000, the IEA outlook, SpaceX targeting
USSF-317, Colombia's national strike, Warner Music's Q4 results, the
Coalition of the Willing rallying for Kyiv, PDD's Q3 results, Kenya's
electoral-reform forum, the Buhari biography launch, the Soweto search
resuming, OpenAI and AMD's chip work, and the SARB's final rate decision.

The six originally excluded stories (Jeffries 251–11, Voyager 1's
one-light-day crossing, the Pew faiths projection, the EU's €45bn Ukraine
loan, Nvidia's quarter, the NSA outage) stay named in the DATE CHECK box,
exactly as the rank-1 entry does. The layout keeps the leaders' winning
skeleton — 3 heroes, 10 cards, map, region strip, numbers strip, date
check — with taller cards so no deck text is clipped, a flat beige map
that reads at 300 pixels across, and fixed hero art.

Every story, headline, number and date was verified against reporting
published on 19 November 2026 (Reuters, AP, AFP, BBC, The Hindu, IMD,
NASA, ICJ, ABS, SARB, IEA). All art is drawn in code; every letter is
rendered in real fonts, so nothing is garbled.

## How it runs

`main.py` (Python 3.13, standard library only) copies `entry.png` to
`$MAKEFUN_OUTPUT_DIR/entry.png` (default `/output`). The image is
deterministic: two runs write the same bytes.

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

## Referral

Built with make.fun — referral code `6etrfz79`.

## License

MIT — see [LICENSE](LICENSE).

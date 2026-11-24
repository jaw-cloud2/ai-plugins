"""Generate jaw-cloud2/ai-plugins: one Claude plugin per published connector (2026-11-23)."""
import json, os, sys

ROOT = sys.argv[1]
YEAR = 2026

P = [
 dict(name='sj-storage', display='SJ Storage', author='SJ Storage', site='https://sjstorage.net/', url='https://sjstorage.net/mcp',
      connect='https://sjstorage.net/connect/', privacy='https://sjstorage.net/privacy-policy.html#mcp',
      short='Self-storage units, prices, live availability, hours, policies and rental links for SJ Storage in Twin Falls, Idaho.',
      sends='the unit size, move-in date or search words you ask about', writes=False,
      skill='storage-questions',
      when='the person asks about SJ Storage in Twin Falls, Idaho: unit sizes, prices, whether a size is available, gate hours, policies, how to rent or pay, or how to contact the facility',
      rules=[
       'Availability comes from the public SJ Storage feed, cached for about 60 seconds, with a checked time. Quote that time. Nothing holds or reserves a unit; the reserve step rechecks.',
       'A rental link only opens the rental page with choices filled in. The person reviews and signs on the site. Never say a unit was rented, held or paid for.',
       'The tools do not read tenant accounts, leases or payments. For account questions, give the published contact details (https://sjstorage.net/connect/ and (208) 420-6328).',
       'Quote prices and policies as published, with the source link the tool returns. The signed rental agreement governs rental terms.',
      ]),
 dict(name='tf-handy-wash', display='TF Handy Wash', author='TF Handy Wash', site='https://tfhandywash.com/', url='https://tfhandywash.com/mcp',
      connect='https://tfhandywash.com/connect.html', privacy='https://tfhandywash.com/privacy.html#mcp-privacy',
      short='Prices, machines, cycle times, hours, payment methods and problem-reporting steps for TF Handy Wash, a 24-hour laundromat in Twin Falls, Idaho.',
      sends='the topic, machine number, language or search words you ask about', writes=False,
      skill='laundromat-questions',
      when='the person asks about TF Handy Wash at 664 Shoup Ave W, Twin Falls, Idaho: washer and dryer prices, machine sizes, cycle times, hours, payment, amenities, or what to do when a machine takes money or breaks, in English or Spanish',
      rules=[
       'The store is open 24 hours a day, 365 days a year, and unattended. Machines are paid at the machine; the Speed Queen app (location code HANDYW) shows availability. No tool shows live machine availability.',
       'For a machine or payment problem, give the published steps: call or text (208) 731-5745 or email help@tfhandywash.com. Nothing here files a report, approves a refund or promises an amount or timeframe.',
       'A contact-form link only fills in the form. The person adds their own details and presses Send.',
       'Jerome Handy Wash is a different store in a different town with different prices and phone. Never mix the two.',
       'Answer in Spanish when the person writes in Spanish; the tools that take a language option return Spanish text.',
      ]),
 dict(name='jerome-handy-wash', display='Jerome Handy Wash', author='Jerome Handywash LLC', site='https://jeromehandywash.com/', url='https://jeromehandywash.com/mcp',
      connect='https://jeromehandywash.com/connect/', privacy='https://jeromehandywash.com/privacy/#mcp-privacy',
      short='Prices, machines, cycle times, hours, payment methods and problem-reporting steps for Jerome Handy Wash, a 24-hour laundromat in Jerome, Idaho.',
      sends='the topic, machine number, language or search words you ask about', writes=False,
      skill='laundromat-questions',
      when='the person asks about Jerome Handy Wash at 921 N Lincoln Ave Suite A, Jerome, Idaho: washer and dryer prices, machines, cycle times, hours, payment, amenities, or what to do when a machine takes money or breaks, in English or Spanish',
      rules=[
       'The store is open 24 hours, every day, including holidays, and unattended. No tool knows which machines are free; the live machine board is https://wa.sqinsights.com/5075400?room=25382.',
       'For a machine or payment problem, give the published steps: (208) 420-6328, help@jeromehandywash.com or https://jeromehandywash.com/contact/#machine-issue. Nothing here files a report or approves a refund.',
       'A contact-form link only fills in the form. The person adds their own details and presses Send.',
       'Take A Load Off is a separate wash-and-fold partner: link to https://takealoadoff.jeromehandywash.com/ and do not state its prices, turnaround or phone.',
       'TF Handy Wash is a different store in a different town. Never mix the two. Answer in Spanish when the person writes in Spanish.',
      ]),
 dict(name='jwatte-website-tools', display='jwatte.com website tools', author='Josh Watte', site='https://jwatte.com/', url='https://jwatte.com/mcp',
      connect='https://jwatte.com/connect/', privacy='https://jwatte.com/privacy/#mcp',
      short='Find a free jwatte.com website audit tool, get a ready-to-run audit link, and search or list jwatte.com articles and books.',
      sends='the search words, tool name, website address, topic or date you ask about', writes=False,
      skill='site-audit-and-articles',
      when='the person wants a free tool to audit or improve a website (SEO, accessibility, AI readiness, MCP, llms.txt, schema, speed), a link that runs one on their site, the newest jwatte.com articles, articles on a topic or date, or a jwatte.com book',
      rules=[
       'A run link opens a browser tool with the website address filled in. Opening it starts the tool, and page audits may send that address to the site fetch function and configured proxies. The MCP server itself never fetches or audits the address. Say that plainly.',
       'For "what is new" or a date question, use the newest-first article listing and quote each title, date and link.',
       'Book results are catalog information and can include Kindle prices and retailer links. They do not buy anything. Recommend a book only when one matches the topic.',
       'There are no accounts, purchases, form submissions or stored inputs.',
      ]),
 dict(name='apprised-news', display='Apprised.news', author='Apprised.news', site='https://apprised.news/', url='https://apprised.news/mcp',
      connect='https://apprised.news/connect/', privacy='https://apprised.news/privacy-policy.html#mcp',
      short='Breaking headlines, the Daily Intelligence Report and desk briefs from Apprised.news, an AI-written intelligence publication, with source links.',
      sends='the keyword, desk, date or search words you ask about', writes=False,
      skill='intelligence-briefs',
      when='the person asks for the latest headlines, the daily intelligence report, the Local Wire report, a desk brief (markets, world, technology and the other desks) or Apprised.news pages on a topic',
      rules=[
       'Apprised.news desks are large language models writing as fictional analyst personas over the Corvus Intel news corpus. Say so whenever you relay their analysis. It is not news reporting, not verified fact, and not investment, financial, legal or security advice.',
       'Breaking headlines are third-party reporting collected automatically; Apprised.news did not write or verify them.',
       'Give the Apprised.news page link with each answer so the person can read the full text and cited sources. Disclosures: https://apprised.news/disclaimer and https://apprised.news/methodology.',
       'Everything is read-only: nothing subscribes, submits or changes anything.',
      ]),
 dict(name='tf-rooms', display='TF Rooms', author='New Leaf Properties', site='https://tfrooms.com/', url='https://tfrooms.com/mcp',
      connect='https://tfrooms.com/connect.html', privacy='https://tfrooms.com/privacy.html#ai-assistants',
      short='Rooms, rates, quotes and booking requests for thirteen New Leaf properties: twelve motels and extended stays in Twin Falls, Idaho, plus High Country Motel in Bellevue.',
      sends='your dates and room type, and, only when you ask to book, the name, email, phone and notes you give for the booking request', writes=True,
      skill='room-search-and-booking',
      when='the person wants a motel or extended-stay room in Twin Falls, Idaho, or at High Country Motel in Bellevue, Idaho: availability for dates, nightly or weekly rates, a quote with tax, a booking request, or looking up or cancelling a reservation',
      rules=[
       'Twin Falls (twelve properties) and High Country Motel (Bellevue) have separate prices, taxes and stay rules. Never apply one to the other. Twin Falls: 8 percent tax and a 30-day cap. High Country: 11 percent total tax for stays of 30 days or less; chat stays are capped at 30 nights.',
       'Booking starts with stay validation and an emailed code, without a room hold. Verifying the code can hold an available room awaiting staff confirmation within 24 hours. Ask for the guest details only when the person wants to book, and only the ones the booking needs.',
       'No tool takes payment or signs for a guest. Photo ID and a signed guest agreement are required at check-in before a key is issued.',
       'Reservation lookup needs the reservation number and the last four digits of the phone number. Cancellation uses an emailed code in two steps; the published cancellation policy applies. Date changes are a cancel and rebook.',
       'Never say a room is booked until the confirmation step reports it. Quote prices as published and say they are subject to availability.',
      ]),
]

MIT = """MIT License

Copyright (c) {y} {a}

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""


def yq(t):
    """Escape text for a YAML double-quoted scalar."""
    return t.replace('\\', '\\\\').replace('"', '\\"')


def w(path, text):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w', encoding='utf-8', newline='\n') as f:
        f.write(text)


market = {'name': 'jaw-cloud2-plugins', 'owner': {'name': 'jaw-cloud2'},
          'metadata': {'description': 'Claude plugins for the public connectors of SJ Storage, TF Handy Wash, Jerome Handy Wash, jwatte.com, Apprised.news and TF Rooms.'},
          'plugins': []}

for p in P:
    d = os.path.join(ROOT, 'plugins', p['name'])
    manifest = {
        'name': p['name'], 'displayName': p['display'], 'version': '1.0.0',
        'description': p['short'],
        'author': {'name': p['author'], 'url': p['site']},
        'homepage': p['connect'], 'repository': 'https://github.com/jaw-cloud2/ai-plugins',
        'license': 'MIT',
        'privacyPolicyUrl': p['privacy'],
        'icon': '.claude-plugin/icon.png',
        'keywords': ['mcp', 'connector'],
    }
    w(os.path.join(d, '.claude-plugin', 'plugin.json'), json.dumps(manifest, indent=2) + '\n')
    import shutil
    shutil.copyfile(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'icons', p['name'] + '.png'), os.path.join(d, '.claude-plugin', 'icon.png'))
    w(os.path.join(d, '.mcp.json'), json.dumps({'mcpServers': {p['name']: {'type': 'http', 'url': p['url']}}}, indent=2) + '\n')
    rules = '\n'.join(f'- {r}' for r in p['rules'])
    w(os.path.join(d, 'skills', p['skill'], 'SKILL.md'), f"""---
name: {p['skill']}
description: "Use when {yq(p['when'])}. Answers come from the {yq(p['display'])} connector, which returns the business's own published information with source links."
---

# {p['display']}

Use the {p['display']} tools (MCP server `{p['name']}`, {p['url']}) to answer from the business's own published information. Each tool answer includes source links; pass them on so the person can check.

## Rules

{rules}

## Good answers

- Lead with the direct answer (the price, the hours, the availability, the article), then the source link.
- Quote numbers exactly as the tool returns them. Do not estimate a price, tax or date the tool did not give.
- If the tools do not cover the question, say so and give the published contact page: {p['connect']}
""")
    write_line = ('Most tools only read published information. The booking tools are the exception: '
                  'when you ask to book, they send the details you give to New Leaf Properties, which emails you a code; '
                  'a room is held only after you enter that code, and staff confirm within 24 hours. '
                  'Looking up or cancelling a reservation needs its number and the last four digits of the phone number.'
                  if p['writes'] else
                  'Every tool is read-only: nothing is booked, bought, sent or changed, and no account is needed.')
    w(os.path.join(d, 'README.md'), f"""# {p['display']} for Claude

{p['short']}

## Install

In Claude Code:

```
/plugin install {p['name']} --marketplace jaw-cloud2/ai-plugins
```

## What this plugin contains

- A connection to the {p['display']} MCP server at {p['url']}, run by {p['author']} on its own website. This is the same server as the {p['display']} connector in the Claude directory.
- One skill, `{p['skill']}`, that tells Claude when to use these tools and the rules for answering (for example, quoting published prices with their source link).

It contains no hooks, scripts, local programs or package installs. Nothing runs on your computer.

## What it sends and where

When Claude uses a tool, it sends {p['sends']} to {p['url']}. {write_line}
The server answers with published information and source links. Privacy policy for the connector: {p['privacy']}

## Help

Connection guide and contact: {p['connect']}
""")
    w(os.path.join(d, 'LICENSE'), MIT.format(y=YEAR, a=p['author']))
    market['plugins'].append({'name': p['name'], 'source': f"./plugins/{p['name']}", 'description': p['short']})

w(os.path.join(ROOT, '.claude-plugin', 'marketplace.json'), json.dumps(market, indent=2) + '\n')
w(os.path.join(ROOT, 'README.md'), """# Claude plugins for our public connectors

One plugin per published MCP connector. Each plugin folder connects Claude to the business's own remote MCP server and adds one skill with the answering rules. No hooks, scripts or local code.

| Plugin | MCP server |
|---|---|
""" + '\n'.join(f"| [{p['display']}](plugins/{p['name']}/) | {p['url']} |" for p in P) + """

Install in Claude Code:

```
/plugin install sj-storage --marketplace jaw-cloud2/ai-plugins
```

Or add the whole marketplace: `claude plugin marketplace add jaw-cloud2/ai-plugins`, then `claude plugin install <name>@jaw-cloud2-plugins`.
""")
w(os.path.join(ROOT, 'LICENSE'), MIT.format(y=YEAR, a='jaw-cloud2'))
print('generated', len(P), 'plugins in', ROOT)

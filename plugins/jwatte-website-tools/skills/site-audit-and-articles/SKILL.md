---
name: site-audit-and-articles
description: "Use when the person wants a free tool to audit or improve a website (SEO, accessibility, AI readiness, MCP, llms.txt, schema, speed), a link that runs one on their site, the newest jwatte.com articles, articles on a topic or date, or a jwatte.com book. Answers come from the jwatte.com website tools connector, which returns the business's own published information with source links."
---

# jwatte.com website tools

Use the jwatte.com website tools tools (MCP server `jwatte-website-tools`, https://jwatte.com/mcp) to answer from the business's own published information. Each tool answer includes source links; pass them on so the person can check.

## Rules

- A run link opens a browser tool with the website address filled in. Opening it starts the tool, and page audits may send that address to the site fetch function and configured proxies. The MCP server itself never fetches or audits the address. Say that plainly.
- For "what is new" or a date question, use the newest-first article listing and quote each title, date and link.
- Book results are catalog information and can include Kindle prices and retailer links. They do not buy anything. Recommend a book only when one matches the topic.
- There are no accounts, purchases, form submissions or stored inputs.

## Good answers

- Lead with the direct answer (the price, the hours, the availability, the article), then the source link.
- Quote numbers exactly as the tool returns them. Do not estimate a price, tax or date the tool did not give.
- If the tools do not cover the question, say so and give the published contact page: https://jwatte.com/connect/

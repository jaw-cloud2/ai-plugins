# Apprised.news for Claude

Breaking headlines, the Daily Intelligence Report and desk briefs from Apprised.news, an AI-written intelligence publication, with source links.

## Install

In Claude Code:

```
/plugin install apprised-news --marketplace jaw-cloud2/ai-plugins
```

## What this plugin contains

- A connection to the Apprised.news MCP server at https://apprised.news/mcp, run by Apprised.news on its own website. This is the same server as the Apprised.news connector in the Claude directory.
- One skill, `intelligence-briefs`, that tells Claude when to use these tools and the rules for answering (for example, quoting published prices with their source link).

It contains no hooks, scripts, local programs or package installs. Nothing runs on your computer.

## What it sends and where

When Claude uses a tool, it sends the keyword, desk, date or search words you ask about to https://apprised.news/mcp. Every tool is read-only: nothing is booked, bought, sent or changed, and no account is needed.
The server answers with published information and source links. Privacy policy for the connector: https://apprised.news/privacy-policy.html#mcp

## Help

Connection guide and contact: https://apprised.news/connect/

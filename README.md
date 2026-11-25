# Claude plugins for our public connectors

One plugin per published MCP connector. Each plugin folder connects Claude to the business's own remote MCP server and adds one skill with the answering rules. No hooks, scripts or local code.

| Plugin | MCP server |
|---|---|
| [SJ Storage](plugins/sj-storage/) | https://sjstorage.net/mcp |
| [TF Handy Wash](plugins/tf-handy-wash/) | https://tfhandywash.com/mcp |
| [Jerome Handy Wash](plugins/jerome-handy-wash/) | https://jeromehandywash.com/mcp |
| [jwatte.com website tools](plugins/jwatte-website-tools/) | https://jwatte.com/mcp |
| [Apprised.news](plugins/apprised-news/) | https://apprised.news/mcp |
| [TF Rooms](plugins/tf-rooms/) | https://tfrooms.com/mcp |
| [High Country Motel](plugins/high-country-motel/) | https://highcountrymotelid.com/mcp |

Install in Claude Code:

```
/plugin install sj-storage --marketplace jaw-cloud2/ai-plugins
```

Or add the whole marketplace: `claude plugin marketplace add jaw-cloud2/ai-plugins`, then `claude plugin install <name>@jaw-cloud2-plugins`.

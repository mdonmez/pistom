# Pistom - MCP for Piston

*Piston API MCP server to enable LLMs to run Python code.*


![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) 
[![Licence](https://img.shields.io/github/license/Ileriayo/markdown-badges?style=for-the-badge)](./LICENSE)
## Features

* Instant code execution capability for any LLM
* No API key required
* Safe and sandboxed environment for running code
* Remote code execution to eliminate safety risks

> [!WARNING]
> *"The Piston API is rate limited to 5 requests per second..."*  
> — [Piston's documentation](https://github.com/engineer-man/piston)

## Installation

### Requirements
[uv]("https://docs.astral.sh/uv/")

#### (Testing) Run directly with `uvx`:

```bash
uvx --from git+https://github.com/mdonmez/pistom.git@master pistom
```

This command is expected to run without any errors.

#### You can add this server as MCP server to any compitable client:

```json
"pistom":{
  "command":"uvx",
  "args":[
    "--from",
    "git+https://github.com/mdonmez/pistom.git@master",
    "pistom"
  ]
}
```

That's it! You don't need to install or update anything; this implementation will always fetch the latest stable, up-to-date server from GitHub.

## Acknowledgements

Thanks to;
 - [Piston](https://github.com/engineer-man/piston) for free code execution engine.
 - [MCP](https://github.com/modelcontextprotocol) for SDK and protocol.
 
## License

This project is licensed under [MIT](/LICENSE) license.


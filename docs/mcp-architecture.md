# MCP 架構

## Participants

MCP follows a client-server architecture where an MCP host — an AI application like Claude Code or Claude Desktop — establishes connections to one or more MCP servers. The MCP host accomplishes this by creating one MCP client for each MCP server. Each MCP client maintains a dedicated one-to-one connection with its corresponding MCP server.
The key participants in the MCP architecture are:

+ MCP Host: The AI application that coordinates and manages one or multiple MCP clients
+ MCP Client: A component that maintains a connection to an MCP server and obtains context from an MCP server for the MCP host to use
+ MCP Server: A program that provides context to MCP clients

For example: Visual Studio Code acts as an MCP host. When Visual Studio Code establishes a connection to an MCP server, such as the Sentry MCP server, the Visual Studio Code runtime instantiates an MCP client object that maintains the connection to the Sentry MCP server.

## Layers

MCP consists of two layers:

+ Data layer: Defines the JSON-RPC 2.0 based protocol for client-server communication, including lifecycle management, and core primitives, such as tools, resources, prompts and notifications.
+ Transport layer: Defines the communication mechanisms and channels that enable data exchange between clients and servers, including transport-specific connection establishment, message framing, and authorization.
    - MCP supports two transport mechanisms: Stdio transport、Streamable HTTP transport
    - 在 [Base Protocol - Transports](https://modelcontextprotocol.io/specification/2025-06-18/basic/transports) 中提到可設定為 [Server-Sent Events (SSE)](https://en.wikipedia.org/wiki/Server-sent_events) 來傳送複數訊息。
        + [SSE](https://blackbing.medium.com/%E6%B7%BA%E8%AB%87-server-sent-events-9c81ef21ca8e) 是一個單向通訊的技術，其設計之初是在 WebSocket 未完成前，需提供長連線來高速傳遞內容之用；但在瀏覽器已經能提供 Socket 與 Fetch 運用的現況，SSE 技術並非最優解。

## Server

以下依據伺服器的核心區塊說明：

### 工具 ( tools )

[Tools - AI Actions](https://modelcontextprotocol.io/docs/learn/server-concepts#tools-ai-actions)

Tools enable AI models to perform actions through server-implemented functions. Each tool defines a specific operation with typed inputs and outputs. The model requests tool execution based on context.

### 資源 ( Resources )

[Resources - Context Data](https://modelcontextprotocol.io/docs/learn/server-concepts#resources-context-data)

Resources provide structured access to information that the host application can retrieve and provide to AI models as context.

### 提示 ( Prompts )

[Prompts - Interaction Templates](https://modelcontextprotocol.io/docs/learn/server-concepts#prompts-interaction-templates)

Prompts provide reusable templates. They allow MCP server authors to provide parameterized prompts for a domain, or showcase how to best use the MCP server.

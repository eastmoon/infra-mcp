# infra-mcp

MCP is an open protocol that standardizes how applications provide context to large language models (LLMs). Think of MCP like a USB-C port for AI applications.

MCP 是一個開源協定，其標準化應用程式提供給大語言模型 ( LLMs、Large Language Models ) 內容的方式。想像 MCP 就如同 USB-C 般，僅要掛接即可讓 AI 應用程式中提供多樣的內容。

MCP provides:
+ **A growing list of pre-built integrations** that your LLM can directly plug into
+ **A standardized way** to build custom integrations for AI applications
+ **An open protocol** that everyone is free to implement and use
+ **The flexibility to change** between different apps and take your context with you

經過實際建立與討論運用方式，MCP 嚴苛來說就如同微服務，啟動服務後即可讓任意 AI 應用程式**動態掛接並整合**，並基於其**標準介面**的操作流程來建立提供給大語言模型的內容。

此外，MCP 提供多樣語言的實作，**開發者可根據協定擴展需要產品與系統的介面**，從而讓**不同的 AI 應用程式能靈活的掛載開發者提供的內容與服務**。

對於 Model Context Protocol 是一個架構概念與定義，詳細文獻整理參閱 [Model Context Protocol 架構](./docs/mcp-architecture.md)。

## DevOps command

本專案提供以下開發運維指令：

+ 啟動

使用 CLI 呼叫 docker-compose 來啟動相關服務

```
mcp up
```

+ 關閉

使用 CLI 呼叫 docker-compose 來關閉相關服務

```
mcp down
```

+ 進入

使用 CLI 進入目標容器內來操作相關服務的命令

```
mcp into --tag=[service-name]
```

本專案啟動包括下列三個服務

### Inspector

[Inspector](https://modelcontextprotocol.io/legacy/tools/inspector) 是 MCP 提拱的伺服器開發服務，其操作介面可以明確看到其協定中規範的內容與操作步驟。

在本專案中，使用 ```mcp up``` 最後會自動擷取 Inspector 認證憑證並自動開啟網站；倘若自動開啟失敗，可以使用下列步驟開啟：

+ 使用 ```docker exec -ti docker-inspector_infra-mcp cat /var/local/mcp.inspector.token``` 憑證
+ 開啟網頁，使用網址 ```http://localhost:6274?MCP_PROXY_AUTH_TOKEN=[憑證]```

### Server

[MCP Server](https://modelcontextprotocol.io/docs/learn/server-concepts) 是透過標準化介面向 AI 應用程式開放特定功能的伺服器程式，因其開放功能可依據開發需求各自建立，進而讓沒個伺服器成為提供特定領域功能的微服務。

常見的例子包括用於文件管理的文件系統伺服器、用於訊息處理的電子郵件伺服器、用於行程規劃的旅行伺服器以及用於資料查詢的資料庫伺服器；每台伺服器都為 AI 應用程式帶來特定領域的功能。

MCP Server 的核心建構區塊：

+ Tools - AI Actions
    - 提供 AI 應用程式對服務的控制，在此分類下做到如搜尋資訊、發送訊息、建立表格等事件
+ Resources - Context Data
    - 提供 AI 應用程式可提取的資源，在此分類下做到如提取文件、信件、經整理的數據表格等內容資源
+ Prompts - Interaction Templates
    - 提供 AI 應用程式樣板化的提示詞 ( Prompts )，在此分類下提供便於操作工具、資源的提示詞樣板

基於 MCP 架構‧本專案將上述內容區分至項應目錄：

```
src\
  └ server \
    └ tools
    └ resources
    └ prompts
```

在其結構目錄中的 Python 檔案皆會集成為 Python 套件 ( Packags ) 模塊引入，因此僅需在目錄添加需要內容並重啟服務即可增加 MCP 功能，並可經由 Inspector 進行檢查。

### Client

MCP clients are instantiated by host applications to communicate with particular MCP servers. The host application, like Claude.ai or an IDE, manages the overall user experience and coordinates multiple clients. Each client handles one direct communication with one server.

Understanding the distinction is important: the host is the application users interact with, while clients are the protocol-level components that enable server connections.

[MCP Client](https://modelcontextprotocol.io/docs/learn/server-concepts)

```
# 進入 mcp 用戶端服務
mcp into --tag=client

# 啟動用戶端
python ./[client-name].py
```

## 文獻

+ [Model Context Protocol](https://modelcontextprotocol.io/docs/getting-started/intro/)
    - [Architecture](https://modelcontextprotocol.io/docs/learn/architecture)
    - [Server](https://modelcontextprotocol.io/docs/learn/server-concepts)
    - [Client](https://modelcontextprotocol.io/docs/learn/client-concepts)
+ [Model Context Protocol - Github](https://github.com/modelcontextprotocol)
    - [Python SDK](https://github.com/modelcontextprotocol/python-sdk)
        + [FastMCP](https://github.com/jlowin/fastmcp)
    - [Inspector](https://github.com/modelcontextprotocol/inspector)
+ 文獻
    - [How To Build RAG Applications Using Model Context Protocol](https://thenewstack.io/how-to-build-rag-applications-using-model-context-protocol/)

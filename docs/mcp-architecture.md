# MCP 架構

## Participants

MCP 是根據 Client-Server 架構，其中 MCP 主機 ( MCP Host )，會經由 MCP 用戶端 ( MCP Client ) 對 MCP 伺服器 ( MCP Server ) 建立連線，且每個 MCP 用戶端與其對應的 MCP 伺服器保持一對一的專用連線。

MCP 架構中的關鍵參與者：

+ MCP Host: 負責協調與管理複數 MCP 用戶端的 AI 應用程式
+ MCP Client: 維護 MCP 伺服器的連線，並從伺服器取得內容以供 MCP 主機使用的元件
+ MCP Server: 為 MCP 用戶端提供內容的伺服器

舉例來說，若 Visual Studio Code 充當 MCP 主機。當 Visual Studio Code 與 MCP 伺服器建立連線時，Visual Studio Code 運行時會建立一個 MCP 用戶端物件，用於維護與 MCP 伺服器的連線。

## Layers

MCP 由兩個層所組成：

+ Data layer: 定義基於 JSON-RPC 2.0 的 Client-Server 通訊協議，包括生命週期管理和基礎核心，例如工具、資源、提示和通知。
+ Transport layer: 定義實現客戶端和伺服器之間資料交換的通訊機制，包括傳輸的連線建立、訊息框架和授權。
    - MCP 支援兩種傳輸機制：Stdio transport、Streamable HTTP transport
    - 在 [Base Protocol - Transports](https://modelcontextprotocol.io/specification/2025-06-18/basic/transports) 中提到可設定為 [Server-Sent Events (SSE)](https://en.wikipedia.org/wiki/Server-sent_events) 來傳送複數訊息。
        + [SSE](https://blackbing.medium.com/%E6%B7%BA%E8%AB%87-server-sent-events-9c81ef21ca8e) 是一個單向通訊的技術，其設計之初是在 WebSocket 未完成前，需提供長連線來高速傳遞內容之用；但在瀏覽器已經能提供 Socket 與 Fetch 運用的現況，SSE 技術並非最優解。

## Server

以下依據伺服器的核心區塊說明：

### 工具 ( tools )

[Tools - AI Actions](https://modelcontextprotocol.io/docs/learn/server-concepts#tools-ai-actions)

工具 ( Tools ) 提供 AI 模型能夠透過伺服器實現的函數執行操作，每個工具都定義了一個根據輸入、輸出型別的操作邏輯，而 AI 模型會根據內容請求工具執行。

### 資源 ( Resources )

[Resources - Context Data](https://modelcontextprotocol.io/docs/learn/server-concepts#resources-context-data)

資源 ( Resources ) 提供對資訊的結構化訪問，主機應用程式可以檢索這些資訊並將其作為內容提供給 AI 模型。

### 提示 ( Prompts )

[Prompts - Interaction Templates](https://modelcontextprotocol.io/docs/learn/server-concepts#prompts-interaction-templates)

提示 ( Prompts ) 提供可複用的範本，它們允許 MCP 伺服器開發者，可基於其服務的領域知識提供參數化的提示產生。

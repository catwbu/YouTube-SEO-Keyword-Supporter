# YouTube SEO 關鍵字支援工具

## 概述
`YouTube-SEO-Keyword-Supporter` 是一個基於 Python 和 wxPython 的圖形化工具，旨在幫助 YouTube 創作者生成 SEO（搜尋引擎優化）關鍵字組合。使用者可以輸入三組關鍵字（以逗號分隔），點擊按鈕後，工具會將這些關鍵字進行排列組合，並將結果顯示在輸出區域中，方便用於影片標題、描述或標籤的關鍵字策略。

## 功能
- **多組關鍵字輸入**：支援三組獨立的關鍵字輸入欄，每組關鍵字以逗號分隔。
- **自動組合生成**：根據輸入的關鍵字，生成所有可能的組合（例如單詞、雙詞或三詞組合）。
- **直觀輸出**：將生成的關鍵字組合顯示在唯讀文字區域中，每行一個組合。
- **簡單介面**：使用 wxPython 提供圖形化操作，包含輸入框、按鈕和輸出區。

## 前置條件
- **Python 環境**：需要安裝 Python 3.x。
- **依賴庫**：
  - `wxPython`：用於構建圖形化使用者介面。
- **作業系統**：支援 Windows、macOS 和 Linux（需安裝 wxPython）。

## 安裝
1. 克隆此儲存庫（或下載腳本）：
   ```bash
   git clone https://github.com/<你的用戶名>/YouTube-SEO-Keyword-Supporter.git
   ```

2. 進入專案目錄
  ```bash
  cd YouTube-SEO-Keyword-Supporter
```

3. 安裝所需依賴
  ```bash
  pip install wxPython
```

4.運行腳本
  ```bash
    python "YouTube Keyword Supporter.py"
```

## 示例輸入與輸出

### 輸入：
第一欄：YouTube, video
第二欄：SEO, tips
第三欄：2023
### 輸出：
```bash
YouTubeSEO2023,
YouTubetips2023,
videoSEO2023,
videotips2023,
```


# [程式實作]自動化Google短連結點擊搜集程序

------

線上行銷時不可避免的使用大量Google短連結數據
但為了隨時決策行銷投入，必須同時追蹤大量Google短連結數據及整理成報告
所需時間與步驟繁瑣。
此程序將自動搜集提供的短連結點擊資料，並生成CSV檔案。

## 必要套件

> * python3.6
> * requests
> * Google token

可以透過以下方式準備
### python3.6.3
> https://www.python.org/downloads/
### requests
> pip install requests
### Google API token
>https://console.developers.google.com/apis/credentials

------

## 使用方式

1.使用前請上Google開發者論壇申請Google Developer Key
https://console.developers.google.com/apis/credentials

2.輸入與輸出格式統一為CSV，逗點型態檔案
可以先在Excel(or Number)調整完格式後，再透過Excel(or Number)表格進行輸出

### 表格建議格式：
|序號|項目|Google連結|開始日期|最後計入日期|期間總點擊數|備註
| :------: | :------: | :------: | :------: | :------: | :------: | :------: |
|1 |T1|http://goo.gl/eZml0W| | | | |
|2|T2|http://goo.gl/uDblK1| | | | |
|3|T3|http://goo.gl/5hjyCe| | | | |
|4|T4|http://goo.gl/g2JWzl| | | | |

3.執行TraceGoogleurl.py
Mac/Linux
> python3 TraceGoogleurl.py 

Windos
> python TraceGoogleurl.py

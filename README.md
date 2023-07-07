# xmlExcelParser

用于合并安卓多语言xml以及处理excel表格转换为多语言xml的小工具

# 如何运行

- 安装python 3.6.5
- 执行安装库

```python
# 简易窗口gui
pip install tkinter
# 用于处理表格
pip install openpyxl
# 用于打包exe
pip install pyinstaller
```

- 运行此目录中的main.py

# 如何打包exe

请在确保执行安装了pyinstaller之后使用

执行命令

```python
pyinstaller --windowed main.py
```

会在目录里生成压缩包。
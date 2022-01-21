# Linux的简单翻译软件
1. 仅支持linux
2. 可翻译单词和句子
3. 显示的发音为英式发音
4. 可以收藏单词和句子，导入到欧陆词典等单词软件中学习，默认收藏路径为`~/Documents/`路径下的`words.txt`和`sentences.txt`文件
5. 代码仅150余行，简洁易懂，方便扩展

![使用示意](https://raw.githubusercontent.com/xuestrange/picGoUploader/main/img/Peek%202022-01-21%2016-46.gif)
## 依赖
```shell
sudo pacman -S translate-shell # for arch linux
sudo apt install translate-sehll # for ubuntu
```
## 技术路线
+ 通过`xclip -o`监控鼠标选择
+ 句子翻译使用[translate-shell](https://github.com/soimort/translate-shell)
+ 单词翻译通过`有道词典网页版`
+ 使用`PyQt5`进行UI设计

## 安装
1. 下载`release`页面的可执行文件
2. 手动编译成可执行文件
    + 编译前需要安装`python3`及`bs4, requests, fake_useragent, PyQt5, pyinstaller`库
    + 然后进入到文件路径下，执行`pyinstaller --onefile --windowed ui.py`
    + 生成的可执行文件在`dist`路径下

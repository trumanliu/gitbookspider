# gitbookspider
[ gitbook](https://www.gitbook.com/) 是我最近发现的一个神奇的网站。更新非常及时，去年我读完了上面的git Pro,最近在读docker practice内容棒棒哒`  
我想搞一个爬虫,把上面的书籍都爬下来。当然我也在看Android的东西,目前的设想是把爬到的数据存到网站上然后搞一个app下载或者直接提供阅读功能。  
本项目是这个设想的第一步,用爬虫把书籍信息爬下来。为了使用强大而且便捷的Xpath选择器,此处选用比较成熟的爬虫框架scrapy。  
##项目的实现过程
###1.系统选择
  听我一句劝吧，如果你不是mac用户就安装一个ubuntu吧。我曾经在win上安装过一次scrapy,并且特意写了一篇[blog](http://www.trumanliu.com/windows-scrapy-install/)来记录整个安装过程中遇到的问题。写那篇blog的时候我还在嘲笑ubuntu太简便了，想想那时候很二。本项目的实现是在ubuntu 14.04LTS 下进行的。如果你没有安装ubuntu而在其它系统下使用，请仔细
查看官方的帮助文档。

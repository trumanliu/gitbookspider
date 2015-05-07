# gitbookspider
[ gitbook](https://www.gitbook.com/) 是我最近发现的一个神奇的网站。更新非常及时，去年我读完了上面的git Pro,最近在读docker practice内容棒棒哒`  
我想搞一个爬虫,把上面的书籍都爬下来。当然我也在看Android的东西,目前的设想是把爬到的数据存到网站上然后搞一个app下载或者直接提供阅读功能。  
本项目是这个设想的第一步,用爬虫把书籍信息爬下来。为了使用强大而且便捷的Xpath选择器,此处选用比较成熟的爬虫框架scrapy。  
##项目的实现过程
###1.系统选择
  听我一句劝吧，如果你不是mac用户就安装一个ubuntu吧。我曾经在win上安装过一次scrapy,并且特意写了一篇[blog](http://www.trumanliu.com/windows-scrapy-install/)来记录整个安装过程中遇到的问题。写那篇blog的时候我还在嘲笑ubuntu太简便了，想想那时候很二。本项目的实现是在ubuntu 14.04LTS 下进行的。如果你没有安装ubuntu而在其它系统下使用，请仔细
查看官方的帮助文档。  
###2.整个项目的技术选择
  **1**.爬虫---python scrapy：scrapy是一个成熟的爬虫，xpath选择器真的很强大，文档齐全。当然顺道把快要丢下的python拾起来。    
  **2**.DB ---mysql:本来真的想要使用mongo的，但我在公网只有屌丝的php+mysql虚拟主机。等我有钱上vps了应该就可以了。  
  **3**.后台---php:参见第一条  
  **4**.app---android:暂时先考虑android。  
  **5**.文档编写---markdown 虽然我认为使用非vim的人都应该被烧死,但我还是使用了retext在写你看到的这些文字。并经是要给别人看的东西，我希望不要太丑。
###3.安装scrapy
  请参考[scrapy文档](http://doc.scrapy.org/en/0.24/)，如果看英文有问题请查看[中文文档](http://scrapy-chs.readthedocs.org/zh_CN/0.24/).
   
###4.编写items.py
  可以参照文档中的例子进行.     
  目前定义了以下几个属性:  
  
    rbookName=scrapy.Field();//书籍名称,书籍路径
    rabookName=scrapy.Field();//书籍可读的书名
    inDate=scrapy.Field();//收录日期
    updDate=scrapy.Field();//更新日期
    lincense=scrapy.Field();//书籍的license信息
    language=scrapy.Field();//书籍的语言
    chapters=scrapy.Field();//书籍的章节数目
    rate=scrapy.Field();//书籍的评分
    readCount=scrapy.Field();//书籍已经被查看的次数
    coverAddress=scrapy.Field();//书籍封面地址
     

 
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
  **3**.后台---php:参见第2条  
  **4**.app---android:暂时先考虑android。  
  **5**.文档编写---markdown 虽然我认为使用非vim的人都应该被烧死,但我还是使用了retext在写你看到的这些文字。毕竟是要给别人看的东西，我希望不要太丑。
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
###5.使用选择器查找书籍信息
还是直接看gitbook_spider.py提示以下几点:  
**1**.在选出上级元素以后使用相对选择器选择下级元素。即在选择器下使用 **"."**
    book['rbookName']=link.xpath('.//div[@class="book-cover"]//a/@href').extract()  
    
**2**.在递归爬取多级页面时使用Request(url, callback=self.parse_item)

###6.编写pipelines.py
在pipeline.py中将书籍信息存入mysql,在这里使用了[MySQLdb](http://sourceforge.net/projects/mysql-python/),详细的安装过程请大家参照文档进行。顺便提醒一下，在安装之前查看软件的README是一个life-saving的习惯。  
在mysql数据库的管理方面推荐使用phpMyadmin。
存入数据库的代码没有什么技术含量,大家看一下就好了。   
当然在使用前需要设计一下数据库,根据我们前面对book信息的分析我们的间表sql为:  
    CREATE TABLE `books` (
 `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '书籍id',
 `rbookname` varchar(256) COLLATE utf8_bin DEFAULT NULL COMMENT '原始书籍名称带有作者信息',
 `rabookname` varchar(128) COLLATE utf8_bin DEFAULT NULL COMMENT '可读书籍名称',
 `indate` date DEFAULT NULL COMMENT '收录时间',
 `upddate` date DEFAULT NULL COMMENT '更新时间',
 `lincense` varchar(64) COLLATE utf8_bin DEFAULT NULL COMMENT 'lincense类别',
 `language` varchar(64) COLLATE utf8_bin DEFAULT NULL COMMENT '语言类型',
 `chapters` int(11) DEFAULT NULL COMMENT '章节数量',
 `rate` double NOT NULL COMMENT '评分状况',
 `readcount` int(11) NOT NULL COMMENT '阅读量',
 `coveraddress` varchar(300) COLLATE utf8_bin NOT NULL COMMENT '封面图片地址',
 PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5905 DEFAULT CHARSET=utf8 COLLATE=utf8_bin COMMENT='书籍表'  

编写完pipelines.py要在settings.py配置一下。
###7.运行爬虫
    scrapy crawl gitbook (-o book.json )  运行完成后数据库中应该就有书籍的信息了。
###8.下载所有书籍
好了有了书籍信息让我们干点丧心病狂的事情吧！把所有书籍都下载下来！首先在gitbook上可以分析出下载链接的格式。通过我们爬取的信息已经可以轻松组装出书籍的下载地址。为了简便，下载过程中使用了系统的wget命令，当然urllib提供了丰富的支持。由于每本书都可能提供三种格式(epub,mobi,pdf)，所以5k多本书下来会有近1个文件。如果单线程顺序下载可能会很蛋疼，在下载过程中使用了队列并用5个进程去下载。当然这个可以更大。下载所有的书籍用了差不多8个小时。希望后期能对此处做点优化。  
   well,到此处书籍信息就爬出来了。下面应该就要开始做app了。服务端先不大着急，现在不打算写一个web的gitbook，因为gitbook已经很赞了。后台端可能不提供页面展示，到时候只会提供一些返回json格式数据的东西。
     

 
# wechat_paper
把微信公众号的临时链接转换为永久链接
## 前言
本文中如有错误请指正。
## 我说
前一阵子由于需要，要把从搜狗微信上爬下来的微信公众号文章的临时链接转变为永久链接。一直在网上百度，但天公不做美，一直找不到比较满意的方法。
![在这里插入图片描述](https://img-blog.csdnimg.cn/20181215112033922.png)
通过百度我找到几种方法：
- 使用微信客户端打开要转换的链接（通过聊天窗口把链接发出去），点击右上角的三点，弹框中的复制链接 即为永久链接。
![在这里插入图片描述](https://img-blog.csdnimg.cn/20181215112800481.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3h1ZTYwNTgyNjE1Mw==,size_16,color_FFFFFF,t_70)
- 通过[微信公众平台](https://mp.weixin.qq.com)，登录后点击素材管理，点击超链接。搜索要找的文章，点击进入，浏览器上方的链接就是永久链接。
![在这里插入图片描述](https://img-blog.csdnimg.cn/20181215113658191.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3h1ZTYwNTgyNjE1Mw==,size_16,color_FFFFFF,t_70)
![在这里插入图片描述](https://img-blog.csdnimg.cn/20181215113710347.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3h1ZTYwNTgyNjE1Mw==,size_16,color_FFFFFF,t_70)
![在这里插入图片描述](https://img-blog.csdnimg.cn/20181215113804386.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3h1ZTYwNTgyNjE1Mw==,size_16,color_FFFFFF,t_70)
- 如第一条所在，在微信客户端打开临时链接的时候，通过软件抓包实现。（此处不再给出，大家可以自行百度。）
- 上面的方法转十条八条的数据虽然不是问题，但是如果转换的数量过大，则会浪费很长的时候，也很麻烦，所以想通过写程序实现。下面为具体的实现过程。
## 分析
在上面提到的第二种方法中，通过查询微信号可以一次性查到该公众号的多篇文章。打开谷歌浏览器的开发者工具可以看到返回的数据 ，都是微信公众号文章的相关信息。所以我们可以模拟发送请求，批量得到链接，其中就是永久链接。
![在这里插入图片描述](https://img-blog.csdnimg.cn/20181215115018476.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3h1ZTYwNTgyNjE1Mw==,size_16,color_FFFFFF,t_70)
通过查看头部信息，最关键的两个关键字就是token和fakeid。其中，token是我们登录后的，每次登录都有一个唯一token；fakeid则是我们要查询的微信公众号的标识。token我们可以在登录后手动得到，登录我们的微信公众号后它是不变的，所以当前的关键就是获得每个被查询公众号的fakeid。
![在这里插入图片描述](https://img-blog.csdnimg.cn/20181215115641764.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3h1ZTYwNTgyNjE1Mw==,size_16,color_FFFFFF,t_70)
仔细查看Network可以找到某一网页，通过发送请求，会返回要查询公众号的fakeid。
![在这里插入图片描述](https://img-blog.csdnimg.cn/20181215120253182.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3h1ZTYwNTgyNjE1Mw==,size_16,color_FFFFFF,t_70)
![在这里插入图片描述](https://img-blog.csdnimg.cn/20181215120308227.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3h1ZTYwNTgyNjE1Mw==,size_16,color_FFFFFF,t_70)
代码如下：
```
import requests
import random
link = 'https://mp.weixin.qq.com/cgi-bin/searchbiz?'
query_id = {'action': 'search_biz','token': '（登录后和cookie一块获取）','lang': 'zh_CN','f': 'json','ajax': '1','random': random.random(),'query': '(微信公众号)','begin:' 0','count': '5'}
header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}
cookie = {自己放一个吧，哈哈}
response = requests.get(url,headers=header,params=query_id,cookies=cookie)
print(response.text)
```
![在这里插入图片描述](https://img-blog.csdnimg.cn/20181215123127546.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3h1ZTYwNTgyNjE1Mw==,size_16,color_FFFFFF,t_70)
这次得到了fakeid ，哈哈，我们可以去获取公众号链接了。
接下来我们模拟  “分析”这个小标题下的第一张图片，发送链接。
![在这里插入图片描述](https://img-blog.csdnimg.cn/20181215124249541.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3h1ZTYwNTgyNjE1Mw==,size_16,color_FFFFFF,t_70)
我把程序输出的结果入到notepad++中，可以看到得到了多篇文章信息，当然包括微信公众号文章的永久链接。
![在这里插入图片描述](https://img-blog.csdnimg.cn/20181215124318225.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3h1ZTYwNTgyNjE1Mw==,size_16,color_FFFFFF,t_70)
## 结束语
查找资料时看到了一些说法，token信息是和微信公众号相关的，但是过于频繁的访问是有可能封号的，所以谨慎啊。

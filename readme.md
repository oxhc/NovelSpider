### 支持网站
1. 笔趣阁:
    1. www.xbiquge6.com
    2. www.biquge.com.cn
2. www.daocaorenshuwu.com
3. www.88dush.com (推荐)
4. www.qisuu.la
5. www.tianyashuku.com
6. www.x83zw.com

### 使用方法
1. 安装依赖
```shell script
pip install -r requirements.txt
```
2. 使用
```shell script
python manage.py download http[s]://xxx.xxx.xxx/xx/xx
```
> 网址为支持网站的小说目录页网址

### 配置文件
在configs/目录下

- example.json: 模板配置

- url_mapping.json: 网址配置映射

- xxx_config.json: xxx配置模式

```json
{
  "book_name": "书名位置, css选择器",

  "chapter_urls": "目录页的每章链接位置, css选择器",

  "chapter_name": "每章的标题, css选择器",

  "body": "每章正文",

  "inter_lines": "正文每行间的填充, 默认为\n",

  "has_more_pages": "章节是否分页, 默认为False",

  "chapter_url_prefix": "目录中链接形式",

  "encoding": "页面编码, 默认utf8"
}
```
#### chapter_url_prefix 字段详解:
示例链接 | 配置
-- | --
`34554080.html` | relative
`/book/404389.html` | absolute
`//www.xxx.com/book/101.html` | without_protocol



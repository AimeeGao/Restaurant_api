# wind


## 生产环境

项目目前已经[上线](http://w.yushu.im)，请在服务器下测试。
为了与以前开发的配置区分开，删除掉`secure.py`文件。
大家在开发时，要注意配置文件的改变。

> w.yushu.im -> 网站域名  
> ips.yushu.im -> watcher 域名  
> api.yushu.im -> 网站 api 域名

## InfluxDB

### 结构

| name     |     说明      |  类型  | 作用               |
| -------- | :-----------: | :----: | ------------------ |
| devkey   |   标识项目    |  tags  | 那个项目的流量大   |
| puid     |   标识用户    |  tags  | 用户的请求使用情况 |
| ip       |    标识 ip    |  tags  | 某 ip 的请求情况   |
| api_sign | 标识 api 类型 |  tags  | 那个 api 调用最多  |
| country  |     国家      | fields | \*\*\*\*           |
| region   |     省份      | fields | \*\*\*\*           |
| city     |     城市      | fields | \*\*\*\*           |
| isp      |    运营商     | fields | \*\*\*\*           |

### 结构要点

> 1.  把你经常查询的字段作为 tag
> 2.  如果你要对其使用`GROUP BY()`，也要放在 tag 中
> 3.  如果你要对其使用 InfluxQL 函数，则将其放到 field 中
> 4.  如果你需要存储的值不是字符串，则需要放到 field 中，因为 tag value 只能是字符串

### 查询使用

参考[官方文档](https://docs.influxdata.com/influxdb/v1.5/query_language/data_exploration/)

### 简单的一个查询语句

```sql
select count("country") from ip_flow where time >= now() - 12h group by "puid"
```

查出过去 12 小时每个用户（puid 标识用户）的请求数目。

### 数据 mock

目前使用 js 脚本`mock`

```js
const ipInfos = [
  {
    puid: 1,
    devkey: 'ku7hax',
    ip: '113.57.168.162',
    api_sign: 'dev'
  },
  {
    puid: 3,
    devkey: '8uy6da',
    ip: '178.62.53.205',
    api_sign: 'user'
  },
  {
    puid: 2,
    devkey: 'ku7hax',
    ip: '14.118.252.202',
    api_sign: 'token'
  },
  {
    puid: 1,
    devkey: '8uy6da',
    ip: '121.230.208.92',
    api_sign: 'user'
  },
  {
    puid: 4,
    devkey: 'ku7hax',
    ip: '42.203.193.169',
    api_sign: 'course'
  },
  {
    puid: 1,
    devkey: '8uy6da',
    ip: '125.118.76.118',
    api_sign: 'user'
  },
  {
    puid: 2,
    devkey: 'ku7hax',
    ip: '125.120.205.166',
    api_sign: 'course'
  }
];

function post(data) {
  axios.post('http://api.77.art:5000/developer/ip', data, {
    headers: {
      'Content-Type': 'application/json'
    }
  });
}

function sleep(time = 0) {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      resolve();
    }, time);
  });
}

async function main() {
  for (let i = 0; i < 5000; i++) {
    const index = await Math.round(Math.random() * 7);
    console.log(`post : ${i} time, data is : ${index}`);
    await post(ipInfos[index]);
    await sleep(2000);
  }
}

main();
```

### grafana

grafana 提供的可视化非常棒！但是并不能直接根据项目情况定制，因此还需多多参考 influxdb 的 DSL 查询语言。

## 前端 BasicAuth 认证

在请求头（headers）里面添加键值对

> key = Authorization  
> value = 'Basic ' + base64(user:password)  
> 例如 'Basic ' + base64(pedro:123456)

本项目中，`user` 为请求而来的 `token` 值，password 则不填，如：

> 'Basic ' + base64(token:)

流程：
前端使用`js-base64`生成，首先添加 js-base64

```bash
npm install --save js-base64
```

然后在代码中生成字段：

```js
import { Base64 } from 'js-base64';

const token =
  'eyJhbGciOiJIUzI1NiIsImlhdCI6MTUyODU1NzI1NSwiZXhwIjoxNTMxMTQ5MjU1fQ.eyJ1aWQiOjEsInR5cGUiOjEwMCwic2NvcGUiOiJVc2VyU2NvcGUifQ.VeXpSfTbk-Spv9cPnOn-AX5Y2alVogRwWIpCtyS5LeM';

const value = 'Basic ' + Base64.encode(`${token}:`);

console.log(value);
```

例如：

```bash
POST /persona/v1/dev/verify HTTP/1.1
Host: api.77.art:5000
Content-Type: application/json
Authorization: Basic ZXlKaGJHY2lPaUpJVXpJMU5pSXNJbWxoZENJNk1UVXlPRFUxTnpJMU5Td2laWGh3SWpveE5UTXhNVFE1TWpVMWZRLmV5SjFhV1FpT2pFc0luUjVjR1VpT2pFd01Dd2ljMk52Y0dVaU9pSlZjMlZ5VTJOdmNHVWlmUS5WZVhwU2ZUYmstU3B2OWNQbk9uLUFYNVkyYWxWb2dSd1dJcEN0eVM1TGVNOg==
Cache-Control: no-cache
Postman-Token: 7d7184ef-501a-421a-8e15-21bd9d64706c

{
    "account": "1456787",
    "type": 300,
    "cid": 1
}
```

## User 模型

::: warning 注意
User 模型增加了`muid`字段，代表慕课网的用户 id
:::

## API 文档

API 文档现在使用[apizza](https://apizza.net)，请前端同学联系我获得权限。

> 请大家多多测试自己的视图函数，将测试结果通过注释的方式或者文档的方式记录下来。

## Json Serializer

> 因数据库模型（models）与普通模型（view_model）在 json 序列化的冲突  
> 现将`MixinJSONSerializer`改为`MixinModelJSONSerializer`  
> 普通模型（view_model 下的）使用`keys`方法序列化

## fake 数据

请运行主目录下的`fake.py`文件，生成课程测试数据

```bash
python fake.py
```

使用`sql`导入`course`数据

```sql
SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for course
-- ----------------------------
DROP TABLE IF EXISTS `course`;
CREATE TABLE `course` (
  `create_time` int(11) DEFAULT NULL,
  `status` smallint(6) DEFAULT NULL,
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `platform` int(11) NOT NULL,
  `slogan` varchar(120) DEFAULT NULL,
  `thumbnail` varchar(32) DEFAULT NULL,
  `name` varchar(64) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of course
-- ----------------------------
INSERT INTO `course` VALUES ('1528884166', '1', '75', '300', '学会微信小程序开发，一个集阅读与电影于一体的小程序实战', 'img/one.jpg', '微信小程序入门与实战  常用组件API开发技巧项目实战');
INSERT INTO `course` VALUES ('1528884166', '1', '97', '300', '前后端分离+ RESTFul API标准接口+微信支付，手把手带你打通全栈！', 'img/two.jpg', '微信小程序商城构建全栈应用');
INSERT INTO `course` VALUES ('1528884166', '1', '136', '300', '【面试必备】入门就是最新版本，让你快速掌握Python3', 'img/three.jpg', '全网最热Python3入门+进阶 更快上手实际开发');
INSERT INTO `course` VALUES ('1528884166', '1', '194', '300', '7月老师深入浅出剖析Flask核心机制，和你一起探讨Python高级编程', 'img/four.jpg', 'Python Flask高级编程');
INSERT INTO `course` VALUES ('1528884166', '1', '220', '300', '构建一套适配 微信小程序/App/单页面 等前端的优秀RESTful API框架。', 'img/five.jpg', 'Python Flask构建可扩展的RESTful API');
```

> 新增的图片在`web/static/img`下，运行后通过`http://77.art:5000/static/img/one.jpg`访问（暂时）

## 返回码

参考[code](./code.md)，大家若定义了自己的返回码，请添加到该文件中。

## secure

```python
"""
 Created by 七月 on 2018/5/7.
"""

__author__ = '七月'

SQLALCHEMY_BINDS = {
    'persona': 'mysql+cymysql://root:123456@localhost/persona',
    'watcher': 'mysql+cymysql://root:123456@localhost/watcher'
}

SQLALCHEMY_TRACK_MODIFICATIONS = True

SERVER_NAME = '77.art:5000'
BASE_API_URL = 'api.77.art:5000'

# SQLALCHEMY_DATABASE_URI = \
#     'mysql+cymysql://root:123456@localhost/persona'

SECRET_KEY = '\x88D\xf09\x91\x07\x98\x89\x87\x96\xa0A\xc68\xf9\xecJ:U\x17\xc5V\xbe\x8b\xef\xd7\xd8\xd3\xe6\x98*4'


EMAIL_USERNAME = 'jiandan@soo9s.com'
EMAIL_PASSWORD = 'JIANdan147'
EMAIL_HOST = 'smtpdm.aliyun.com'

# InfluxDB config
INFLUX_HOST = 'localhost'
INFLUX_PORT = 8086
INFLUX_USERNAME = 'root'
INFLUX_PASSWORD = 'root'
INFLUX_DATABASE = 'watcher'
```

## TODO LIST

- [x] 用户登录、注册
- [x] 密码修改，重置
- [x] 邮件发送
- [x] 开发者验证，appkey 发送
- [x] 课程获取
- [ ] ip 监控，限流
- [ ] and so on....
# restaurant_api
# restaurant_api
# Restaurant_api

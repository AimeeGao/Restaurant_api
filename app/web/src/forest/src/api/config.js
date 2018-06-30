export const baseUrl = 'api.art.77.com:500'

// 用户信息
export let userData = {
  token: '', // 令牌
  secret: {} // 令牌信息
}

// 状态码
export const stateCode = {
  20001: '用户不存在',
  30001: '课程不存在',
  10029: '用户没有购买该课程',
  20002: '不是慕课网课程购买者',
  10028: '已经生成过 appkey',
  10027: '发送邮件错误',
  10004: '超权',
  10005: '认证错误',
  10001: '资源未找到',
  10000: '参数错误',
  10006: '客户端类型错误',
  999: '服务器未知错误',
  0: '操作成功',
  10008: '操作失败',
  20004: '您输入uid号已被其他用户绑定',
  20003: '密码校验失败',
  1: '删除数据成功'
}

export const xcxLink = 'https://coding.imooc.com/class/75.html' // 慕课网《微信小程序入门与实战》链接。 设置在Vue.prototype.xcxLink

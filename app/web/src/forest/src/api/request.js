/**
 * 统一处理ajax请求
 * **/

import axios from 'axios'
import { Base64 } from 'js-base64'
import { userData } from './config'

// const www = 'http://api.77.art:5000'
const www = 'http://api.yushu.im'

let axiosAjax = function (method, url, data) {
  return axios({
    method: method,
    url: url,
    data: data
  }).then(res => {
    return Promise.resolve(res.data)
  }).catch(err => {
    // console.log(err.response)
    return Promise.reject(err.response.data)
  })
}

// 获得令牌
export function getToken (param) {
  const url = `${www}/persona/v1/token`
  const data = Object.assign({}, param)

  return axiosAjax('post', url, data)
  // return axios.post(url, data).then((res) => {
  //   return Promise.resolve(res.data)
  // }).catch(err => {
  //   console.log(err.response.status)
  // })
}

// 获得令牌信息
export function getTokenInfo () {
  const url = `${www}/persona/v1/token/secret`
  const data = {token: userData.token}

  return axios.post(url, data).then((res) => {
    return Promise.resolve(res.data)
  }).catch(err => {
    return Promise.reject(err.response.data)
  })
}

// 客户端注册
export function register (param) {
  const url = `${www}/persona/v1/client/register`
  const data = Object.assign({}, param)

  return axios.post(url, data).then((res) => {
    return Promise.resolve(res.data)
  }).catch((err) => {
    return Promise.reject(err.response.data)
  })
}

// 找回密码
export function forgetPassword (param) {
  const url = `${www}/persona/v1/user/reset/password`
  const data = Object.assign({}, param)

  return axios.post(url, data).then((res) => {
    return Promise.resolve(res.data)
  }).catch((err) => {
    return Promise.reject(err.response.data)
  })
}

// 重置密码
export function resetPassword (param, token) {
  const url = `${www}/persona/v1/user/reset/password/${token}`
  const data = Object.assign({}, param)

  return axios.post(url, data).then((res) => {
    return Promise.resolve(res.data)
  }).catch((err) => {
    return Promise.reject(err.response.data)
  })
}

// 获得课程列表（需授权）
export function getCourseList () {
  const url = `${www}/persona/v1/course`

  return axios.get(url, {
    headers: {
      Authorization: 'Basic ' + Base64.encode(`${userData.token}:`)
    }
  }).then((res) => {
    return Promise.resolve(res.data)
  }).catch((err) => {
    return Promise.reject(err.response.data)
  })
}
// 获取用户信息/
export function getUserInfo() {
  const url = `${www}/persona/v1/user`
  return axios.get(url, {
    headers: {
      Authorization: 'Basic ' + Base64.encode(`${userData.token}:`)
    }
  }).then((res) => {
    return Promise.resolve(res.data)
  }).catch((err) => {
    return Promise.reject(err.response.data)
  })
}
// 获取开发者appkey
export function getAppKey (param) {
  const url = `${www}/persona/v1/dev/appkey`
  let data = param

  return axios.post(url, data, {
    headers: {
      Authorization: 'Basic ' + Base64.encode(`${userData.token}:`)
    }
  }).then((res) => {
    return Promise.resolve(res.data)
  }).catch((err) => {
    return Promise.reject(err.response.data)
  })
}
// 课程验证
export function courseVerify (param) {
  const url = `${www}/persona/v1/dev/verify`
  let data = param

  return axios.post(url, data, {
    headers: {
      Authorization: 'Basic ' + Base64.encode(`${userData.token}:`)
    }
  }).then((res) => {
    return Promise.resolve(res.data)
  }).catch((err) => {
    return Promise.reject(err.response.data)
  })
}

// 修改密码
export function changePassword (param) {
  const url = `${www}/persona/v1/user/change/password`
  let data = param

  return axios.post(url, data, {
    headers: {
      Authorization: 'Basic ' + Base64.encode(`${userData.token}:`)
    }
  }).then((res) => {
    return Promise.resolve(res.data)
  }).catch((err) => {
    return Promise.reject(err.response.data)
  })
}

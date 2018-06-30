import axios from 'axios'
import {baseUrl} from './config'

export default function request(url, params) {
  if (!params.type) {
    params.type = 'Get'
  }
  axios({
    url: params.url,
    method: params.type, // 默认是 get
    baseURL: baseUrl,
    headers: {'content-type': 'application/json'},
    data: params.data
  }).then(function (res) {
    params.wCallBack && params.wCallBack(res.data)
  }).catch(function (res) {

  }).finally(function (res) {

  })
}

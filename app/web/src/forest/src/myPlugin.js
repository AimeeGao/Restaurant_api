
import ripple from './directives/ripple/ripple'
import { mapMutations, mapState } from 'vuex'
import { xcxLink } from './api/config'

export default {
  install (Vue, options) {
    // 1. 添加全局方法或属性
    Vue.tests = () => 'test'
    // 2. 添加全局指令
    Vue.directive('ripple', ripple)
    // 3. 注入组件
    Vue.mixin({
      computed: mapState([
        'isLogin'
      ]),
      methods: {
        ...mapMutations([
          'showMessage',
          'hideMessage'
        ])
      }
    })
    // 添加在vue的原型上
    Vue.prototype.xcxLink = xcxLink // 慕课网《微信小程序入门与实战》链接
  }
}

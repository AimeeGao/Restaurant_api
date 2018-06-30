import 'babel-polyfill'
import Vue from 'vue'
import App from './App'
import router from './router'
import fastclick from 'fastclick'
import VueLazyload from 'vue-lazyload'

import 'assets/stylus/index.styl'
import message from 'components/message/message'
import store from './store/index'
import myPlugin from './myPlugin'

fastclick.attach(document.body)

Vue.config.productionTip = false

Vue.use(VueLazyload, {
  preLoad: 1.3,
  attempt: 2
})

Vue.use(myPlugin)

router.beforeEach((to, from, next) => {
  /* 路由发生变化修改页面title */
  if (to.meta.title) {
    document.title = to.meta.title
  }
  next()
})

/* eslint-disable no-new */
new Vue({
  el: '#app',
  store,
  router,
  render: h => h(App),
  components: {
    message
  }
}).$mount('#app')

Vue.component('app-message', message)

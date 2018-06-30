<template>
  <div id="app">
    <app-message v-if="message.display" :text="message.text" :type="message.type" :time="message.time"></app-message>
    <!--<transition name="page">-->
      <router-view/>
    <!--</transition>-->
  </div>
</template>

<script>
import { userData } from './api/config'

export default {
  name: 'App',
  computed: {
    message () {
      return this.$store.state.message
    }
  },
  data () {
    return {
    }
  },
  created () {
    let data = window.localStorage.getItem('wind')
    if (data) {
      data = JSON.parse(data)
      userData.token = data.token
      userData.secret = data.secret
      this.isLogin = true // 用户已登录
    }
  },
  methods: {
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  /*margin-top: 60px;*/

}

.pass{
  width: 62px;
  height: 17px;
  font-family: HanziPenSC-W3;
  font-size: 12px;
  font-weight: normal;
  font-stretch: normal;
  line-height: 0px;
  letter-spacing: 0px;
  color: #898888;
  background-color: white;
}

html, body, #app{
  width: 100%;
  height: 100%;
}
div{
  box-sizing: border-box;
}
</style>

<template>
  <div id="login" class="login login-public">
    <!--<h3 style="margin-bottom: 12px"><router-link to="/home" style="color: white; font-size: 30px">Go 首页</router-link></h3>-->
    <div class="login-box">
      <h1 class="logo">
        <img src="../../assets/img/login/logo.png" alt="七月有风" title="七月有风">
      </h1>
      <div class="form-box">
        <div class="form-wrap" v-if="!$store.state.isLogin">
          <form autocomplete="off" @submit.prevent="_login()">
            <div class="item mailbox" >
              <input :class="{email: !account}" type="text" autocomplete="off" v-model="account">
            </div>
            <div class="item password">
              <input :class="{password: !secret}" type="password" autocomplete="off" v-model="secret">
              <a @click="_goForget()">
                <img src="../../assets/img/login/forget_text.png" alt="">
              </a>
            </div>
            <button type="submit" value="" class="submit submit-login" v-ripple></button>
            <a class="info" @click="_goRegister()" >
              <span class="info-img"></span>
            </a>
          </form>
        </div>
        <div class="form-wrap" v-if="$store.state.isLogin">
          <router-link class="submit goLogin" to="/home" v-ripple ></router-link>
        </div>
      </div>
      <a class="links" :href="xcxLink" target="_blank">
        <span class="xcx-link"></span>
      </a>
    </div>
  </div>
</template>

<script type="text/ecmascript-6">
import { getToken, getTokenInfo } from '../../api/request'
import { stateCode, userData } from '../../api/config'

export default {
  name: 'Login',
  data () {
    return {
      account: '', // 用户名
      secret: '' // 密码
    }
  },
  created () {
    console.log(this.isLogin)
  },
  methods: {
    _login: function () {
      let emailReg = new RegExp(/^([a-zA-Z0-9._-])+@([a-zA-Z0-9_-])+(\.[a-zA-Z0-9_-])+/)
      if (!this.account) {
        this.showMessage({text: '邮箱不能为空', type: 'warn'})
        return
      } else if (!this.secret) {
        this.showMessage({text: '密码不能为空', type: 'warn'})
        return
      } else if (!emailReg.test(this.account)) {
        this.showMessage({text: '邮箱格式错误', type: 'warn'})
        return
      } else if (!emailReg.test(this.account)) {
        this.showMessage({text: '请输入有效的邮箱', type: 'warn'})
        return
      }

      let param = {
        'account': this.account,
        'secret': this.secret,
        'type': 100
      }
      // 拿到令牌和令牌信息
      this.showMessage({ text: '登录中...', time: 0 })
      getToken(param).then((data) => {
        userData.token = data.token
        return getTokenInfo()
      }).then((data) => {
        this.hideMessage()
        userData.secret = data
        window.localStorage.setItem('wind', JSON.stringify(userData))
        this.isLogin = true // 用户已登录
        this.$router.push('home')
      }).catch(err => {
        if (err['error_code'] === 10000) {
          let msg = Object.keys(err['msg'])[0] && err['msg'][Object.keys(err['msg'])[0]][0] // 该邮箱已经注册过
          this.showMessage({text: msg, type: 'warn'})
        } else {
          this.showMessage({text: stateCode[err['error_code'] + ''], type: 'warn'})
        }
      })
    },
    _goRegister () {
      this.$router.push('register')
    },
    _goForget () {
      this.$router.push('forget')
    }
  },
  components: {}
}
</script>

<style scoped lang="stylus" type="text/stylus" rel="stylesheet/stylus">
  @import "~assets/stylus/variable";
  @import "~assets/stylus/mixin";
  @import "~assets/stylus/login/public";
  .login
    .goLogin
      background-image url("../../assets/img/login/go_home.png")
      background-size 99px 18px
      background-position center
      background-repeat no-repeat
    .goLogin:hover
      background-image url("../../assets/img/login/go_home_hover.png")
    .info-img
      background-image url("../../assets/img/login/register_text.png")
      background-size cover
      background-position center
      &:hover
        background-image url("../../assets/img/login/register_text_hover.png")

</style>

<template>
  <div id="register" class="register login-public">
    <!--<h3 style="margin-bottom: 12px"><router-link to="/home" style="color: white; font-size: 30px">Go 首页</router-link></h3>-->
    <div class="register-box">
      <h1 class="logo">
        <img src="../../assets/img/login/logo.png" alt="">
      </h1>
      <div class="form-box">
        <div class="form-wrap">
          <form autocomplete="off" @submit.prevent="_register()">
            <div class="item mailbox" >
              <input type="text" :class="{nickname: !nickname}" v-model="nickname">
            </div>
            <div class="item mailbox" >
              <input type="text" :class="{email: !account}" v-model="account">
            </div>
            <div class="item mailbox" >
              <input type="password" autocomplete="off" :class="{password: !secret}" v-model="secret">
            </div>
            <button type="submit" value="" v-ripple class="submit submit-register"></button>
            <a class="info" @click="_goLogin()">
              <span class="info-img"></span>
              <!--<img src="../../assets/img/login/login_text.png" alt="">-->
            </a>
          </form>
        </div>
      </div>
      <a class="links" :href="xcxLink" target="_blank">
        <span class="xcx-link"></span>
      </a>
    </div>
  </div>
</template>

<script type="text/ecmascript-6">
import { register, getTokenInfo } from '../../api/request'
import { stateCode, userData } from '../../api/config'

export default {
  data () {
    return {
      account: '', // 邮箱
      secret: '', // 密码
      type: 100,
      nickname: '', // 昵称
      isFocus: false // input是否获得焦点
    }
  },
  created () {

  },
  methods: {
    _register() {
      let emailReg = new RegExp(/^([a-zA-Z0-9._-])+@([a-zA-Z0-9_-])+(\.[a-zA-Z0-9_-])+/)
      let nickName = new RegExp(/^.{2,10}$/)
      if (!this.nickname) {
        this.showMessage({ text: '昵称不能为空', type: 'warn' })
        return
      } else if (!this.account) {
        this.showMessage({ text: '邮箱不能为空', type: 'warn' })
        return
      } else if (!this.secret) {
        this.showMessage({ text: '密码不能为空', type: 'warn' })
        return
      } else if (!nickName.test(this.nickname)) {
        this.showMessage({ text: '昵称为2-10个字符，请检查重新输入', type: 'warn' })
        return
      } else if (!emailReg.test(this.account)) {
        this.showMessage({ text: '您输入的不是有效的邮箱，请重新输入', type: 'warn' })
        return
      }
      let param = {
        account: this.account, // 邮箱
        secret: this.secret, // 密码
        type: this.type,
        nickname: this.nickname // 昵称
      }
      this.showMessage({ text: '注册中...', time: 0 })
      register(param).then((data) => {
        this.hideMessage()
        this.showMessage({ text: '注册成功', time: 0 })
        userData.token = data.token
        return getTokenInfo()
      }).then((data) => {
        userData.secret = data
        window.localStorage.setItem('wind', JSON.stringify(userData))
        this.isLogin = true // 用户已登录
        setTimeout(() => {
          this.$router.push('login')
          this.hideMessage()
        }, 1000)
      }).catch(err => {
        if (err['error_code'] === 10000) {
          let msg = Object.keys(err['msg'])[0] && err['msg'][Object.keys(err['msg'])[0]][0] // 该邮箱已经注册过
          this.showMessage({ text: msg, type: 'warn' })
        } else {
          this.showMessage({ text: stateCode[err['error_code'] + ''], type: 'warn' })
        }
      })
    }, // 注册
    _goLogin() {
      this.$router.push('/login')
    }
  }
}
</script>

<style scoped lang="stylus" type="text/stylus" rel="stylesheet/stylus">
  @import "~assets/stylus/variable";
  @import "~assets/stylus/mixin";
  @import "~assets/stylus/login/public";

  #register
    .submit-register
      background-image url("../../assets/img/register/register.png")
      background-repeat no-repeat
      background-size 33px 17px
      background-position center center
    .submit-register:hover
      background-image url("../../assets/img/register/register_hover.png")
    .info-img
      background-image url("../../assets/img/login/login_text.png")
      background-size cover
      background-position center
      &:hover
        background-image url("../../assets/img/login/login_text_hover.png")

</style>

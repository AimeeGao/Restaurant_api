<template>
  <div id="forget" class="forget login-public">
    <!--<h3 style="margin-bottom: 12px"><router-link to="/home" style="color: white; font-size: 30px">Go 首页</router-link></h3>-->
    <div class="forget-box">
      <h1 class="logo">
        <img src="../../assets/img/login/logo.png" alt="">
      </h1>
      <div class="form-box">
        <div class="form-wrap">
          <form autocomplete="off" v-if="!step" @submit.prevent="_forget()">
            <div class="item mailbox" >
              <input type="text" :class="{forget: !email}" v-model="email">
            </div>
            <button type="submit" v-ripple value="" class="submit submit-submit" ></button>
            <a class="info" @click="_backLogin()">
              <span class="info-img"></span>
              <!--<img class="back_login" src="../../assets/img/login/back_login.png" alt="返回登录" title="返回登录">-->
            </a>
          </form>
          <form autocomplete="off" v-if="step">
            <div class="step-text1">
              <img src="../../assets/img/forget/step_text1.png" alt="已发送邮箱至" title="已发送邮箱至">
            </div>
            <p class="step-text" style="text-decoration: underline">{{email}}</p>
            <div class="step-text2">
              <img src="../../assets/img/forget/step_text2.png" alt="请注意查收" title="请注意查收">
            </div>
          </form>
        </div>
      </div>
      <a class="links" :href="xcxLink" target="_blank" >
        <span class="xcx-link"></span>
      </a>
    </div>
  </div>
</template>

<script type="text/ecmascript-6">
import { forgetPassword } from '../../api/request'
import { stateCode } from '../../api/config'

export default {
  data () {
    return {
      step: false, // 步骤   未发送邮件为false 已发送为true
      email: '' // 用户名
    }
  },
  created () {
  },
  methods: {
    _forget () {
      let emailReg = new RegExp(/^([a-zA-Z0-9._-])+@([a-zA-Z0-9_-])+(\.[a-zA-Z0-9_-])+/)
      if (!this.email) {
        this.showMessage({text: '邮箱不能为空', type: 'warn'})
        return
      } else if (!emailReg.test(this.email)) {
        this.showMessage({text: '请输入有效的邮箱', type: 'warn'})
        return
      }

      let param = {
        email: this.email
      }
      // resetPassword
      forgetPassword(param).then(res => {
        // this.showMessage({text: stateCode[res['error_code']+''], time: 5000})
        this.step = true
      }).catch(err => {
        if (err['error_code'] === 10000) {
          let msg = Object.keys(err['msg'])[0] && err['msg'][Object.keys(err['msg'])[0]][0] // 该邮箱已经注册过
          this.showMessage({text: msg, type: 'warn'})
        } else if (err['error_code'] === 10001) {
          this.showMessage({text: '该邮箱未注册', type: 'warn'})
        } else {
          this.showMessage({text: stateCode[err['error_code'] + ''], type: 'warn'})
        }
      })
    },
    _backLogin() {
      this.$router.push('login')
    }
  }
}
</script>

<style scoped lang="stylus" type="text/stylus" rel="stylesheet/stylus">
  @import "~assets/stylus/variable";
  @import "~assets/stylus/mixin";
  @import "~assets/stylus/login/public";

  #forget
    .step-text1
      img
        width 84px
        height 15px
    .step-text2
      img
        width 72px
        height 15px
    .info-img
      width 49px
      height 13px
      background-image url("../../assets/img/login/back_login.png")
      background-size cover
      background-position center
      &:hover
        background-image url("../../assets/img/login/back_login_hover.png")

</style>

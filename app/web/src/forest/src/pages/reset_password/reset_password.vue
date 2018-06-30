<template>
  <div id="reset_password" class="reset_password login-public">
    <!--<h3 style="margin-bottom: 12px"><router-link to="/home" style="color: white; font-size: 30px">Go 首页</router-link></h3>-->
    <div class="reset_password-box">
      <h1 class="logo">
        <img src="../../assets/img/login/logo.png" alt="">
      </h1>
      <div class="form-box">
        <div class="form-wrap">
          <form autocomplete="off" v-if="!step"  @submit.prevent="_reset_password()" >
            <div class="item mailbox" >
              <input type="password" :class="{new_password: !new_password}" autocomplete="off" v-model="new_password">
            </div>
            <div class="item mailbox" >
              <input type="password" :class="{confirm_password: !confirm_password}" autocomplete="off"  v-model="confirm_password">
            </div>
            <button type="submit" value="" v-ripple class="submit submit-submit"></button>
            <a class="info" @click="_goLogin()">
              <span class="info-img"></span>
              <!--<img class="back_login" src="../../assets/img/login/back_login.png" alt="返回登录" title="返回登录">-->
            </a>
          </form>
          <form autocomplete="off" v-if="step">
            <p class="step-text">已发送邮箱至</p>
            <p class="step-text" style="text-decoration: underline">{{email}}</p>
            <p class="step-text">请注意查收</p>
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
import { resetPassword } from '../../api/request'
import { stateCode } from '../../api/config'

export default {
  data () {
    return {
      token: null,
      step: false, // 步骤   未发送邮件为false 已发送为true
      new_password: '', // 新密码
      confirm_password: '' // 确认密码
    }
  },
  created () {
    document.title = '修改密码'
    this.token = this.$route.query.token
  },
  methods: {
    _reset_password() {
      if (!this.new_password) {
        this.showMessage({text: '新密码不能为空', type: 'warn'})
        return
      } else if (!this.confirm_password) {
        this.showMessage({text: '确认密码不能为空', type: 'warn'})
        return
      } else if (this.new_password !== this.confirm_password) {
        this.showMessage({text: '密码不一致', type: 'warn'})
        return
      } else if (String(this.new_password).length < 6) {
        this.showMessage({text: '密码长度不能小于6', type: 'warn'})
        return
      }

      let param = {
        new_password: this.new_password,
        confirm_password: this.confirm_password
      }
      // resetPassword
      resetPassword(param, this.token).then(() => {
        this.showMessage({text: '重置成功，请登陆'})
        this.$router.push('login')
      }).catch(err => {
        this.showMessage({text: stateCode[err['error_code'] + ''], type: 'warn'})
      })
    },
    _goLogin() {
      this.$router.push('login')
    }
  }
}
</script>

<style scoped lang="stylus" type="text/stylus" rel="stylesheet/stylus">
  @import "~assets/stylus/variable";
  @import "~assets/stylus/mixin";
  @import "~assets/stylus/login/public";
  #reset_password
    .info-img
      width 49px
      height 13px
      background-image url("../../assets/img/login/back_login.png")
      background-size cover
      background-position center
      &:hover
        background-image url("../../assets/img/login/back_login_hover.png")
</style>

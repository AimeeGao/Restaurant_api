<template>
  <div class="home">
    <v-header></v-header>
    <a class="group-btn" @click="switchMask()" v-ripple ></a>
    <div class="rectangle" id="rec">
        <template v-if="course.length">
          <courseCard @action="lisentCourse" v-for="(item, index) in course" :item="item" :key="item.value"
                      :index="index">
            <p class="text">开发者KEY：{{item.appkey}}</p>
          </courseCard>
        </template>
        <template v-else>
          <app-outline></app-outline>
        </template>
    </div>

    <!--Model-->
    <transition name="fade">
      <div class="show-model" @click.self="consoleModel" v-if="showModel">
        <div class="show-model-main">
          <div class="course-verify" v-if="modelType === 'courseVerify'">
            <div class="model-main-name">
              课程验证
            </div>
            <form autocomplete="off" style="margin-top: 39px;">
              <div class="item imooc-uid">
                <input type="text" placeholder="慕课网用户ID号" v-model="account">
              </div>
            </form>
            <div class="course-verify-note" style="margin-top: 11px;">
              * 请输入慕课网用户ID号
            </div>
            <div v-ripple="" @click="verifyCourse()" class="course-verify-do" style="margin-top: 39px;">
              提交
            </div>
          </div>
          <div class="get-key" v-if="modelType === 'getKey'">
            <div class="get-app-key" style="margin-top: 78px;">
              开发者KEY：{{appKey}}
            </div>
          </div>
          <div class="change-password" v-if="modelType === 'changePassword'">
            <div class="model-main-name">
              修改密码
            </div>
            <form autocomplete="off" style="margin-top: 16px;">
              <div class="item imooc-uid">
                <input type="password" placeholder="原密码" v-model="yPassword" autocomplete="off">
              </div>
              <div class="item imooc-uid">
                <input type="password" placeholder="新密码" v-model="xPassword" autocomplete="off">
              </div>
              <div class="item imooc-uid">
                <input type="password" placeholder="确认密码" v-model="rPassword" autocomplete="off">
              </div>
            </form>
            <div v-ripple="" @click="changepwd()" class="course-verify-do" style="margin-top: 21px;">
              提交
            </div>
          </div>
        </div>
      </div>
    </transition>

    <!--Mask-->
    <transition name="fade">
      <div class="my-mask" v-if="viewMask" @click.self="viewMask=false">
        <div class="menu">
          <p class="name">{{userInfo.nickname}}</p>
          <p>{{userInfo.email}}</p>
          <p v-ripple="" class="p-hover" @click="lisentCourse(changePasswordAction)" style="cursor: pointer;">修改密码</p>
          <p v-ripple="" class="p-hover" @click="outLogin()" style="border-bottom: none; cursor: pointer;">退出登录</p>
        </div>
      </div>
    </transition>
  </div>
</template>

<script type="text/ecmascript-6">
import courseCard from '../../components/courseCard/courseCard'
import vHeader from '../../components/header/header'
import appOutline from '../../components/outline/outline'
import {courseVerify, getCourseList, changePassword, getUserInfo, getAppKey} from '../../api/request'
import { stateCode } from '../../api/config'

export default {
  name: 'Home',
  data() {
    return {
      course: [],
      showModel: false,
      modelType: '',
      cId: null,
      userInfo: {
        nickname: null,
        email: null
      },
      account: null,
      viewMask: false,
      appKey: null,
      changePasswordAction: {
        'do': 'show',
        'type': 'changePassword'
      },
      yPassword: null,
      xPassword: null,
      rPassword: null
    }
  },
  created() {
    if (!this.isLogin) {
      this.showMessage({text: '未登录，请重新登录', type: 'warn'})
      this.$router.push('login')
      return
    }

    getCourseList().then((res) => {
      if (res['error_code'] === 1003) { // 假如令牌过期
        this.showMessage({text: '令牌过期，请重新登录', type: 'warn'})
        this.$router.push('login')
        return
      }
      this.course = res
    }).catch(err => {
      this.showMessage({text: stateCode[err['error_code'] + ''], type: 'warn'})
    })

    getUserInfo().then((res) => {
      this.userInfo = res
    }).catch(err => {
      this.showMessage({text: stateCode[err['error_code'] + ''], type: 'warn'})
    })
  },
  methods: {
    switchMask() {
      this.viewMask = !this.viewMask
    },
    _myMask() {
      this.viewMask = true
    },
    lisentCourse: function (action) {
      if (action.do === 'show') {
        this.cId = action.cId
        if (action.type === 'getKey') {
          let param = {
            account: this.userInfo.muid,
            type: 300,
            cid: action.cId
          }
          getAppKey(param).then((res) => {
            this.showModel = true
            this.appKey = res.appkey
            this.course[action.index]['appkey'] = res.appkey
            this.modelType = action.type
          }).catch(() => {
            this.showMessage({text: '获取失败', type: 'warn'})
          })
        }
        if (action.type === 'changePassword') {
          this.showModel = true
          this.viewMask = false
          this.modelType = action.type
        }
        if (action.type === 'courseVerify') {
          this.showModel = true
          this.modelType = action.type
        }
      } else {
        this.showModel = false
      }
    },
    consoleModel: function () {
      this.showModel = false
      this.modelType = ''
      this.account = null
    },
    changepwd: function () {
      if (!this.yPassword) {
        this.showMessage({text: '请输入原密码', type: 'warn'})
        return
      } else if (!this.xPassword) {
        this.showMessage({text: '请输密码', type: 'warn'})
        return
      } else if (!this.rPassword) {
        this.showMessage({text: '请再输入一次密码', type: 'warn'})
        return
      }
      if (this.xPassword !== this.rPassword) {
        this.showMessage({text: '两次密码输入不一致', type: 'warn'})
        return
      }
      let param = {
        old_password: this.yPassword,
        new_password: this.xPassword,
        confirm_password: this.rPassword,
        email: this.userInfo.email
      }
      changePassword(param).then((res) => {
        if (res['error_code'] === 0) {
          this.showMessage({text: '修改成功', type: 'info'})
          this.showModel = false
          this.modelType = ''
        }
      }).catch((err) => {
        if (err['error_code'] === 10008) {
          this.showMessage({text: '原密码错误，请重试', type: 'warn'})
        } else if (err['error_code'] === 10000) {
          let msg = Object.keys(err['msg'])[0] && err['msg'][Object.keys(err['msg'])[0]][0] // 该邮箱已经注册过
          this.showMessage({text: msg, type: 'warn'})
          // this.showMessage({text: '未知错误', type: 'warn'})
        } else {
          this.showMessage({text: '未知错误', type: 'warn'})
        }
      })
    },
    verifyCourse: function () {
      let accountVerify = new RegExp(/^\d{5,10}$/)
      if (!accountVerify.test(this.account)) {
        this.showMessage({text: '慕课网ID号为5-10位数字', type: 'warn'})
        return
      }
      let param = {
        account: this.account,
        type: 300,
        cid: this.cId
      }
      courseVerify(param).then((res) => {
        if (res['error_code'] === 0) {
          this.showMessage({text: '验证成功', type: 'info'})
          getCourseList().then((res) => {
            this.course = res
          })
          getUserInfo().then((res) => {
            this.userInfo = res
          })
        }
        this.showModel = false
        this.modelType = ''
      }).catch((err) => {
        // this.showModel = false
        this.showMessage({text: stateCode[err['error_code'] + ''], type: 'warn'})
      })
    },
    outLogin() {
      localStorage.removeItem('wind')
      this.isLogin = false // 用户未登录
      this.$router.push('login')
    }
  },
  components: {
    'courseCard': courseCard,
    'v-header': vHeader,
    appOutline
  },
  activated: {}
}
</script>

<style scoped lang="stylus" type="text/stylus" rel="stylesheet/stylus">
  @import "~assets/stylus/variable";
  @import "~assets/stylus/mixin";
  .home
    .group-btn
      width 29px
      height 29px
      position absolute
      top 25px
      right 5%
      background-image url("../../assets/img/home/Group9@2x.png")
      background-size cover
      &:hover
        opacity .8
  .rectangle {
    width: 706px;
    background-color: $color-theme;
    margin: 0 auto;
  }

  .show-model {
    position: fixed;
    left 0;
    top 0;
    z-index 999
    width: 100%;
    height: 100%;
    background-color rgba(0, 0, 0, .5);
  }

  .show-model-main {
    width: 337px;
    height: 312px;
    margin: auto 0;
    background-color: #ffffff;
    border-radius: 4px;
    position: absolute;
    top: 50%;
    left: 50%;
    margin-top: -168px;
    margin-left: -168px;
    padding: 40px;
  }

  .display {
    display: none;
  }
  .show{
    display: block;
  }
  .model-main-name{
    width: 100%;
    height: 42px;
    font-family: HanziPenSC-W3;
    font-size: 30px;
    font-weight: normal;
    font-stretch: normal;
    line-height: 42px;
    letter-spacing: 0px;
    color: #2d61b4;
    text-align: center;
  }
  .item
    width: 100%;
    height: 38px;
    background-color: #f5f5f5;;
    border-radius 4px;
    margin-bottom 2px
    display flex
    align-items center
    overflow hidden
    input
      font-family: HanziPenSC-W3;
      font-size: 14px;
      font-weight: normal;
      font-stretch: normal;
      line-height: normal;
      letter-spacing: 0px;
      color: #333;
      padding-left 16px
      flex 1
      width 100%
      height 100%
      background-color: #f5f5f5;
  .imooc-uid{
  }
  .course-verify-note {
    width: 100%;
    height: 17px;
    font-family: PingFangSC-Regular;
    font-size: 12px;
    font-weight: normal;
    font-stretch: normal;
    line-height: 12px;
    letter-spacing: 0px;
    color: #40454a;
    text-align left;
  }
  .course-verify-do {
    width: 257px;
    height: 38px;
    background-color: #2c61b4;
    border-radius: 4px;
    margin: 0 auto;
    line-height: 38px;
    color: #fff;
    font-family: PingFangSC-Medium;
    font-size: 14px;
    font-weight: normal;
    font-stretch: normal;
    cursor: pointer;
  }
  .course-verify-do:hover{
    color rgba(255,255,255,.8)
  }
  .get-app-key {
    width: 100%;
    height: 17px;
    font-family: PingFangSC-Regular;
    font-size: 12px;
    font-weight: normal;
    font-stretch: normal;
    line-height: 17px;
    letter-spacing: 0px;
    color: #40454a;
    text-align: center;
  }
  // my-mask
  .my-mask
    position fixed
    left 0
    top 0
    z-index 999
    width 100%
    height 100%
    background-color rgba(0,0,0,.3)
    .menu
      position absolute
      top: 64px
      right 4%
      width: 191px;
      height: 186px;
      background-color: #ffffff;
      border-radius: 4px;
      padding 0 10px
      box-sizing border-box
      p
        font-family: PingFangSC-Regular;
        font-size: 14px;
        height 40px
        line-height 40px
        text-align center
        font-weight: normal;
        font-stretch: normal;
        letter-spacing: 0px;
        color: #363636;
        border-bottom 1px solid #dedede
      p.name
        height 1em
        line-height 1em
        margin-top 24px
        border-bottom none
      .p-hover:hover
        background-color $color-background
        color $color-blue
    .menu:before {
      content: "";
      display: block;
      width: 0;
      height: 0;
      border-bottom: 8px solid #fff;
      border-left: 6px solid transparent;
      border-right: 6px solid transparent;
      position: absolute;
      top: -8px;
      right 16px
    }

  @media screen and (max-width: $xs) {
    .rectangle {
      width: 100%;
      height: 100%;
    }
  }
</style>

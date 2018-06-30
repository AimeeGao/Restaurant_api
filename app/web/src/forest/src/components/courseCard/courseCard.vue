<template>
  <div class="container-course-card">
    <div class="rectangle-5">
      <div v-if="item.verify" class="success-verification">
        <img style="width: 100%; height: 100%;" src="../../assets/img/courseCard/Group3.png" alt="">
      </div>
      <div class="rectangle-9">
        <div class="course-card-name" :title="item.name">{{item.name}}</div>
        <div class="course-card-detail" :title="item.slogan">{{item.slogan}}</div>
        <div class="course-card-users">
          <div class="course-card-info">
            <div v-if="item.has_content" style="display: flex; flex-shrink: 0" >
              <div class="rectangle-7" v-if="item.verify && item.appkey" style="background-color: #bbbbbb; cursor: auto">
                已获取key
              </div>
              <div v-ripple class="rectangle-7" v-if="item.verify && !item.appkey" v-on:click="_getKey">
                获取开发者key
              </div>
              <div v-ripple class="rectangle-7" v-if="!item.verify" v-on:click="_courseVerify">
                若已购买，请验证
              </div>
            </div>
            <div v-else style="width: 100%; display: flex" >
              <div v-ripple class="rectangle-7" v-if="!item.verify" v-on:click="_courseVerify">
                若已购买，请验证
              </div>
              <div class="rectangle-7" v-else style="background-color: #bbbbbb; cursor: auto">
                已验证
              </div>
            </div>
            <div class="course-card-users-course-msg">
              <p class="text" v-if="item.has_content && !item.appkey && !item.verify">验证后可获取开发者key{{item.appkey}}</p>
              <div v-if="item.appkey">
                <slot></slot>
              </div>
            </div>
          </div>
          <div v-if="!item.verify">
            <a :href="item.link" target="_blank">
              <div class="course-card-buy">购买课程 ></div>
            </a>
          </div>
        </div>
      </div>
      <div class="rectangle-10">
        <img v-lazy="item.thumbnail" :alt="item.name">
      </div>
    </div>
  </div>
</template>

<script type="text/ecmascript-6">
export default {
  props: ['item', 'index'],
  name: 'courseCard',
  data() {
    return {
      'account': 'ff',
      'type': '',
      'cid': '',
      'test': 'success'
    }
  },
  created() {},
  methods: {
    _courseVerify() {
      let action = {
        'do': 'show',
        'type': 'courseVerify',
        'cId': this.item.id
      }
      this.$emit('action', action)
    },
    _getKey() {
      let action = {
        'do': 'show',
        'type': 'getKey',
        'cId': this.item.id,
        'index': this.index
      }
      this.$emit('action', action)
    }
  },
  components: {}
}
</script>

<style scoped lang="stylus" type="text/stylus" rel="stylesheet/stylus">
  @import "~assets/stylus/variable";
  @import "~assets/stylus/mixin";
  .container-course-card
    &:hover
      transition box-shadow .6s
      box-shadow 0px 3px 10px rgba(0,0,0,.1)
  .rectangle-5 {
    width: 100%;
    min-height: 137px;
    background-color: #ffffff;
    border-radius: 4px;
    padding: 6.3%;
    margin: 29px auto;
    display: flex;
    justify-content space-between
    position relative
  }
  .success-verification{
    position: absolute;
    width: 98px;
    /*height: 76px;*/
    right: -12px;
    top: -12px;
  }
  .rectangle-10
    width: 120px;
    height: auto;
    background-color: #f7f7f7;
    border-radius: 4px;
    overflow: hidden;
    margin: auto 0;
    flex-shrink 1
    img
      width: 100%;
      height: auto;

  .rectangle-9 {
    /*width: 100%;*/
    /*min-height: 137px;*/
    margin-right: 10.5%;
    text-align: left;
    flex 1
  }

  .course-card-name {
    width: 100%;
    min-height: 30px;
    font-family: CloudSongDaGBK;
    font-size: 20px;
    font-weight: normal;
    font-stretch: normal;
    line-height: 30px;
    letter-spacing: 0px;
    color: #40454a;
  }

  .course-card-detail {
    width: 100%;
    min-height: 17px;
    font-family: PingFangSC-Regular;
    font-size: 14px;
    font-weight: normal;
    font-stretch: normal;
    line-height: 17px;
    letter-spacing: 0px;
    color: #40454a;
    margin-top: 25px;
  }

  .course-card-users {
    width: 100%;
    height: 28px;
    margin-top: 38px;
    display: flex;
    align-items center
    justify-content space-between
    font-family: PingFangSC-Regular;
    font-size: 14px;
    font-weight: normal;
    font-stretch: normal;
    line-height: 28px;
    letter-spacing: 0px;
    color: #2d61b4;
  }

  .course-card-info
    display flex
    align-items center

  .rectangle-7 {
    /*width: 120px;*/
    width: auto;
    /*height: 28px;*/
    padding 0 14px
    display inline-block
    background-color: #2c61b4;
    border-radius: 100px;
    font-family: PingFangSC-Regular;
    font-size: 14px;
    font-weight: normal;
    font-stretch: normal;
    line-height: 28px;
    letter-spacing: 0px;
    color: #ffffff;
    text-align center;
    margin-right: 16px;
  }
  .rectangle-7:hover{
    cursor: pointer;
    color rgba(255,255,255,.8)
    box-shadow 0 2px 5px rgba(0,0,0,.3)
    transition all .3s
  }

  .course-card-users-course-msg {
    /*width: 228px;*/
    height: 17px;
    font-family: PingFangSC-Regular;
    font-size: 14px;
    font-weight: normal;
    font-stretch: normal;
    line-height: 17px;
    letter-spacing: 0px;
    color: #363636;
  }
  .course-card-users-course-msg .text{
    color: #888;
  }

  .course-card-buy {
    /*width: 65px;*/
    height: 17px;
    display flex
    align-items center
    font-family: PingFangSC-Regular;
    font-size: 14px;
    font-weight: normal;
    font-stretch: normal;
    line-height: 28px;
    letter-spacing: 0px;
    color: #2d61b4;
    margin: auto 0;
    float: right;
  }
  .course-card-buy:hover{
    color: rgba($color-blue, .8);
    text-decoration underline
  }

  @media screen and (max-width: $xs) {
    .container-course-card{
      width: 100%;
      padding: 10px;
    }
    .rectangle-5 {
      width: 100%;
      min-height: 100px;
      padding: 10px;
      margin: 0px;
    }

    .rectangle-9 {
      width: 70%;
      min-height: 100px;
      margin-right: 0px;
      padding-right: 10px;
    }

    .rectangle-10 {
      width: 30%;
      height: auto;
      background-color: #f7f7f7;
      border-radius: 4px;
      margin: auto 0px;
      overflow: hidden;
    }

    .rectangle-10 img {
      width: 100%;
      height: auto;
      cursor text
    }

    .course-card-name {
      width: 100%;
      min-height: 20px;
      font-family: CloudSongDaGBK;
      font-size: 14px;
      font-weight: normal;
      font-stretch: normal;
      line-height: 20px;
      letter-spacing: 0px;
      color: #40454a;
      overflow: hidden;
      padding: px;
    }

    .course-card-detail {
      display: none;
    }

    .course-card-users {
      width: 100%;
      min-height: 28px;
      margin-top: 10px;
      display: block;
      font-family: PingFangSC-Regular;
      font-size: 14px;
      font-weight: normal;
      font-stretch: normal;
      line-height: 28px;
      letter-spacing: 0px;
      color: #2d61b4;
    }

    .rectangle-7 {
      height: 28px;
      background-color: #2c61b4;
      border-radius: 100px;
      font-family: PingFangSC-Regular;
      font-size: 12px;
      font-weight: normal;
      font-stretch: normal;
      line-height: 28px;
      letter-spacing: 0px;
      color: #ffffff;
      text-align center;
      margin-right: 0px;
    }

    .course-card-users-course-msg {
      width: 100%;
      height: 17px;
      font-family: PingFangSC-Regular;
      font-size: 14px;
      font-weight: normal;
      font-stretch: normal;
      line-height: 17px;
      letter-spacing: 0px;
      color: #363636;
      margin: 10px 0;
    }

    .course-card-buy {
      height: 17px;
      font-family: PingFangSC-Regular;
      font-size: 14px;
      font-weight: normal;
      font-stretch: normal;
      line-height: 17px;
      letter-spacing: 0px;
      color: #2d61b4;
      padding-left: 0px;
      margin: auto 0;
      float: left;
    }

    .course-card-info{
      flex-direction column
      align-items flex-start
    }

    .success-verification{
      width 70px
    }

  }

</style>

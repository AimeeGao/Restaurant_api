<template style="z-index: 999999999999">
  <transition name="fade">
    <div class="message"
         :class="{success: type==='success', primary:type==='primary', info:type==='info', warn:type==='warn'}"
         @click="_hide()" style="z-index: 9999999999">
        <p class="text">{{text}}</p>
    </div>
  </transition>
</template>

<script type="text/ecmascript-6">
export default {
  props: {
    text: {
      type: String,
      default: ''
    },
    time: {
      type: Number,
      default: 2500
    },
    type: { // warn,info,primary,success
      type: String,
      default: 'info'
    },
    route: {
      type: String,
      default: ''
    }
  },
  name: 'message',
  data () {
    return {
    }
  },
  created () {
    if (this.time !== 0) {
      setTimeout(() => {
        this.hideMessage()
      }, this.time)
    }
    if (this.route) {
      setTimeout(() => {
        this.$router.push(this.route)
      }, this.time)
    }
  },
  methods: {
    _hide: function () {
      this.hideMessage()
    }
  },
  components: {}
}
</script>

<style scoped lang="stylus" type="text/stylus" rel="stylesheet/stylus">
  @import "~assets/stylus/variable";
  @import "~assets/stylus/mixin";
  .message
    width: 100%;
    height: 50px;
    line-height: 50px;
    background-color: #e56666;
    position fixed;
    left 0
    top: 0
    z-index 999
    .text
      line-height: 50px;
      text-align center
      font-family: PingFangSC-Regular;
      font-size: 14px;
      font-weight: normal;
      font-stretch: normal;
      letter-spacing: 0px;
      color: #ffffff;
  .message.success
    background-color $color-message-success
  .message.primary
    background-color $color-message-primary
  .message.info
    background-color $color-message-info
  .message.warn
    background-color $color-message-warn

</style>

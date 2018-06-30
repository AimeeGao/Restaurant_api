<template>
  <div class="my-outline">
    <div class="item" v-for="item of [0,1,2,3,4]" :key="item.value">
      <div class="item-box">
        <div class="info-box">
          <div class="title"></div>
          <div class="text"></div>
          <div class="btn-box">
            <div class="btn"></div>
            <div class="link"></div>
          </div>
        </div>
        <div class="img-box"></div>
      </div>
    </div>
  </div>
</template>

<script type="text/ecmascript-6">
export default {
  data () {
    return {}
  },
  created () {
  },
  methods: {},
  components: {}
}
</script>

<style scoped lang="stylus" type="text/stylus" rel="stylesheet/stylus">
    @import "~assets/stylus/variable";
    @import "~assets/stylus/mixin";

    .item
      width: 100%;
      min-height: 137px;
      box-sizing border-box
      background-color: #fff;
      border-radius: 4px;
      padding: 44px;
      margin: 29px auto;
      display: -ms-flexbox;
      display: flex;
      animation: opa 1.5s infinite;
      -webkit-animation: opa 1.5s infinite;
      .item-box
        flex 1
        width 100%
        display flex
        justify-content center
        align-items center
        .info-box
          flex 1
          height 100%
          padding-right 8%
          box-sizing border-box
          display flex
          flex-direction column
          justify-content space-between
          .title
            width 50%
            height 42px
            background-color $color-outline
          .text
            width 80%
            height 20px
            background-color $color-outline
          .btn-box
            width 100%
            height 30px
            display flex
            justify-content space-between
            align-items center
            .btn
              max-width 40%
              width 120px
              height 28px
              /*flex-grow 1*/
              flex-shrink 0
              border-radius 28px
              background-color $color-outline
            .link
              width 60px
              max-width 30%
              height 18px
              flex-shrink 1
              background-color $color-outline
        .img-box
          width 120px
          height 120px
          flex-shrink 0
          background-color $color-outline

    @keyframes opa
    {
      0%   {opacity: 1}
    //25%  {opacity: .75}
      50%  {opacity: .5}
    //75%  {opacity: .75}
      100% {opacity: 1}
    }
</style>

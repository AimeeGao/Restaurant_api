<template>
  <div class="header">
    <img src="../../assets/img/home/Group4.png" alt="">
  </div>
</template>

<script type="text/ecmascript-6">
export default {
  name: 'vHeader',
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
  .header{
    width: 100%
    max-height: 594px;
    align-items: cente;
    overflow: hidden;
  }
  .header img{
    width: 100%;
    height: auto;
    margin: auto 0;
  }
</style>

<template>
  <div id="app">
      <router-view></router-view>
      <vue-progress-bar></vue-progress-bar>
  </div>
</template>

<script>
// 
export default {
mounted () {
    this.$Progress.finish()
  },
  created () {
    this.$Progress.start()
    this.$router.beforeEach((to, from, next) => {
      if (to.meta.progress !== undefined) {
        let meta = to.meta.progress
        this.$Progress.parseMeta(meta)
      next()

      }else{
      this.$Progress.start()
      }
      next()
    })
    this.$router.afterEach((to) => {
      this.$Progress.finish()
      document.title=to.meta.title

    })
  }
}
</script>
<style scope>
    @import url('./assets/css/style.css');
</style>
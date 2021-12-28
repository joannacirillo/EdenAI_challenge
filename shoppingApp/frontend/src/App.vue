<template>
  <div class="outer">
    <div id="app">
      <nav-bar />
      <!-- <img src="./assets/logo.png"> -->
      <router-view/>
    </div>
  </div>
</template>

<script>
import NavBar from '@/components/NavBar/NavBar.vue'
export default {
  name: 'App',
  components: {
    NavBar
  }
}
</script>

<style src="./MainStyle.scss"></style>

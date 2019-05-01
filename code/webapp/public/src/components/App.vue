<template>
<div id="app">
  <Navbar></Navbar>
  <div class="container">
    <div class="row col-md-6 offset-md-3">
      <ListItems></ListItems>
    </div>
  </div>
</div>
</template>

<script>
import ListItems from './ListItems.vue';
import Navbar from './Navbar.vue';
export default {
  name: 'app',
  data() {
    return {}
  },
  components: {
    ListItems,
    Navbar
  },
}
</script>
<style>
.fade-enter-active,
.fade-leave-active {
  transition: opacity .5s
}

.fade-enter,
.fade-leave-active {
  opacity: 0
}
</style>

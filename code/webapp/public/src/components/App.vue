<template>
  <div id="app">
    <div class="container">
      <div class="row col-md-6 offset-md-3">
        <list-items></list-items>
      </div>
    </div>
  </div>
</template>


<script>
  import ListItems from './ListItems.vue';
  export default {
    name: 'app',
    data() {
      return {}
    },
    components: {ListItems},
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

<template>
<div id="app">
  <div class="container">
    <div class="row col-md-6 offset-md-3">
      <ViewButton></ViewButton>
      <ListItems></ListItems>
    </div>
  </div>
</div>
</template>


<script>
import ListItems from './ListItems.vue';
import ViewButton from './ViewButton.vue';
export default {
  name: 'app',
  data() {
    return {}
  },
  components: {
    ListItems,
    ViewButton
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

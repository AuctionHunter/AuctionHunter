<template>
<div id="app">
  <Navbar></Navbar>

  <modal
  v-if="showModal"
  :modalData="modalData">
  </modal>
  <div class="container" style="max-width: 100%;">
  <div class="row">
    <FilterForm></FilterForm>
    <ListItems></ListItems>
  </div>
  </div>
</div>
</template>

<script>
import ListItems from './ListItems.vue';
import Navbar from './Navbar.vue';
import Modal from './Modal.vue'
import FilterForm from './FilterForm.vue'
export default {
  name: 'app',
  data() {
    return {
      showModal: false,
      modalData: {}
    }
  },
  created: function() {
    var parent = this;
    this.$eventHub.$on('openModal', function(payload) {
        parent.showModal = true;
        parent.modalData = payload
    });
    this.$eventHub.$on('closeModal', function(payload) {
        parent.showModal = false;
    });
  },
  components: {
    ListItems,
    Modal,
    FilterForm,
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

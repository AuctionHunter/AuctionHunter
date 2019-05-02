<template>
  <div class="card" style="width: 18rem;">
    <div class="card-body">
      <h5 class="card-title">{{carName}}</h5>
      <img
      :src="carThumbnail"
      :alt="carName"
      class="img-thumbnail">
      <button type="button" v-on:click="toggle_modal" class="btn btn-info">More Info</button>
    </div>
  </div>
</template>

<script>
export default {
  name: 'DataCard',
  data() {
    return {}
  },
  updated() {
    console.log(this.index);
  },
  methods: {
    toggle_modal(){
      this.$eventHub.$emit('openModal', this.data);
    }
  },
  props: {
    carName: String,
    carThumbnail: String,
    index: Number,
    data: Object
  }
}
</script>

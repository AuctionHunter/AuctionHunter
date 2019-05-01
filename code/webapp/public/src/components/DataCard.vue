<template>
  <div class="card" style="width: 18rem;">
    <div class="card-body">
      <h5 class="card-title">{{carName}}</h5>
      <img
      :src="carThumbnail"
      :alt="carName"
      class="img-thumbnail">
      <a href="#" class="btn btn-primary">More Info</a>
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
  props: {
    carName: String,
    carThumbnail: String,
    index: Number
  }
}
</script>

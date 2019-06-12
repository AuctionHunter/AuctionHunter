<template>
<div class="card" style="width: 18rem;">
  <div class="card-body">
    <h5 class="card-title">{{carName}}</h5>
    <img :src="carThumbnail" :alt="carName" class="img-thumbnail">
    <p v-if="showPrices">
      ${{data.estimated_price}}
    </p>
    <p v-if="showMiles">
      {{data.miles}} miles
    </p>
    <p v-if="showValue">
      Value Estimate: {{data.value_est}}
    </p>
    <button type="button" v-on:click="toggle_modal" class="btn btn-info">More Info</button>
  </div>
  {{index}} of {{total}}
</div>
</template>

<script>
export default {
  name: 'DataCard',
  data() {
    return {
      showPrices: "",
      showMiles: "",
      showValue: "",
    }
  },
  created: function() {
    var parent = this;
    this.$eventHub.$on('togglePrice', function(payload) {
      parent.showPrices = payload;
    });
    this.$eventHub.$on('toggleMiles', function(payload) {
      parent.showMiles = payload;
    });
    this.$eventHub.$on('toggleValue', function(payload) {
      parent.showValue = payload;
    });
  },
  methods: {
    toggle_modal() {
      this.$eventHub.$emit('openModal', this.data);
    }
  },
  props: {
    carName: String,
    carThumbnail: String,
    index: Number,
    total: Number,
    data: Object
  }
}
</script>

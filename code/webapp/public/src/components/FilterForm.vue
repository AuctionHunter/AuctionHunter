<template>
<div style="margin-right:1%;">
  <h3>Filter Options</h3>
  <hr />
  <h4>Vehicle name search</h4>
  <input v-model="filterKey" placeholder="Vehicle name" />
  <hr />
  <ResetButton></ResetButton>
</div>
</template>

<script>
import ResetButton from './ResetButton.vue';
export default {
  name: 'FilterForm',
  data() {
    return {
      filterKey: this.message
    }
  },
  created: function() {
    var parent = this;
    this.$eventHub.$on('clearSearchForms', function(payload) {
      parent.filterKey = "";
    });
  },
  props: {
    message: String,
  },
  components: {
    ResetButton
  },
  watch: {
    filterKey: function(newVal, oldVal) { // watch it
      this.$eventHub.$emit('searchName', this.filterKey);
    }
  },
}
</script>

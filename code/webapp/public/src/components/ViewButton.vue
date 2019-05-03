<template>
<div>
  <button type="button" v-on:click="refresh" class="btn btn-info">Refresh</button>
</div>
</template>

<script>
export default {
  name: 'ViewButton',
  data() {
    return {}
  },
  methods: {
    refresh() {
       this.$eventHub.$emit('refreshList');
    }
  }
}
</script>

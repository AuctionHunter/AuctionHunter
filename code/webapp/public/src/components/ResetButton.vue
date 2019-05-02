<template>
<div>
  <button type="button" v-on:click="reset" class="btn btn-info">Reset</button>
</div>
</template>

<script>
export default {
  name: 'ResetButton',
  data() {
    return {}
  },
  methods: {
    reset() {
       this.$eventHub.$emit('resetSearch');
    }
  }
}
</script>

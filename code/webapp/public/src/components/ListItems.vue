<template>
<div>
  <div class="col-md-12" v-show="auctionItems.length>0">
    <h3>Auction Hunter</h3>
    <div class="row mrb-10" v-for="auctionItem in auctionItems">
      <div class="input-group m-b-5">
        <p>{{auctionItem.car_name}}</p>
        <p>{{auctionItem.body}}</p>
      </div>
    </div>
  </div>
</div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'ListItems',
  data() {
    return {
      auctionItems: []
    }
  },
  created: function() {
    this.fetchItems();
    var parent = this;
    this.$eventHub.$on('refreshTodo', function(payload) {
      parent.fetchItems();
    });
  },
  methods: {
    fetchItems() {
      let uri = 'http://localhost:8080/api/all';
      axios.get(uri).then((response) => {
        this.auctionItems = response.data;
        console.log("Fetch complete")
      });
    }
  }
}
</script>
<style scoped>
.delete__icon {}

.no_border_left_right {
  border-left: 0px;
  border-right: 0px;
}

.flat_form {
  border-radius: 0px;
}

.mrb-10 {
  margin-bottom: 10px;
}

.addon-left {
  background-color: none !important;
  border-left: 0px !important;
  cursor: pointer !important;
}

.addon-right {
  background-color: none !important;
  border-right: 0px !important;
}
</style>

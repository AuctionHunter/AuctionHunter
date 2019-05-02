<template>
<div class="card-columns">
  <div v-for="(auctionItem, index) in auctionItems">
    <DataCard
    :index="trackIndex(index)"
    :carName="auctionItem.car_name"
    :carThumbnail="auctionItem.car_image"
    :data="auctionItem">
    </DataCard>
  </div>
</div>
</template>

<script>
import axios from 'axios';
import DataCard from './DataCard.vue';

export default {
  name: 'ListItems',
  data() {
    return {
      auctionItems: []
    }
  },
  components: {
    DataCard
  },
  created: function() {
    this.fetchItems();
    var parent = this;
    this.$eventHub.$on('refreshTodo', function(payload) {
      parent.fetchItems();
    });
  },
  methods: {
    trackIndex: function(index) {
      return index + 1
    },
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
@media (min-width: 34em) {
    .card-columns {
        -webkit-column-count: 2;
        -moz-column-count: 2;
        column-count: 2;
    }
}

@media (min-width: 48em) {
    .card-columns {
        -webkit-column-count: 3;
        -moz-column-count: 3;
        column-count: 3;
    }
}

@media (min-width: 62em) {
    .card-columns {
        -webkit-column-count: 4;
        -moz-column-count: 4;
        column-count: 4;
    }
}

@media (min-width: 75em) {
    .card-columns {
        -webkit-column-count: 5;
        -moz-column-count: 5;
        column-count: 5;
    }
}
</style>

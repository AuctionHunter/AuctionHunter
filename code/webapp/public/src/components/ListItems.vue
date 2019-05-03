<template>
<div class="card-columns">
  <div v-for="(auctionItem, index) in auctionItems">
    <DataCard :index="trackIndex(index)"
    :carName="auctionItem.car_name"
    :carThumbnail="auctionItem.car_image"
    :data="auctionItem"
    :total="auctionItems.length"
    >
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
      auctionItems: [],
      masterList: [],
      airbagOptionsList: [],
      bodyOptionsList: [],
      fobOptionsList: [],
      codeOptionsList: [],
      sortedPrice: false,
      sortedMiles: false,
      sortedValue: false
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
    this.$eventHub.$on('searchName', function(payload) {
      parent.auctionItems = parent.nameSearch(payload.toUpperCase(), parent.auctionItems);
    });
    this.$eventHub.$on('searchAirbag', function(payload) {
      parent.auctionItems = parent.airbagSearch(payload, parent.auctionItems);
    });
    this.$eventHub.$on('searchBody', function(payload) {
      parent.auctionItems = parent.bodySearch(payload, parent.auctionItems);
    });
    this.$eventHub.$on('searchFob', function(payload) {
      parent.auctionItems = parent.fobSearch(payload, parent.auctionItems);
    });
    this.$eventHub.$on('searchCode', function(payload) {
      parent.auctionItems = parent.codeSearch(payload, parent.auctionItems);
    });
    this.$eventHub.$on('sortPrice', function(payload) {
      parent.sortedPrice = true;
      this.$eventHub.$emit('toggleMiles', false);
      this.$eventHub.$emit('toggleValue', false);
      parent.auctionItems = parent.sortPrice(payload, parent.auctionItems);
    });
    this.$eventHub.$on('sortMiles', function(payload) {
      parent.sortedMiles= true;
      this.$eventHub.$emit('togglePrice', false);
      this.$eventHub.$emit('toggleValue', false);
      parent.auctionItems = parent.sortMiles(payload, parent.auctionItems);
    });
    this.$eventHub.$on('sortValue', function(payload) {
      parent.sortedValue= true;
      this.$eventHub.$emit('togglePrice', false);
      this.$eventHub.$emit('toggleMiles', false);
      parent.auctionItems = parent.sortValue(payload, parent.auctionItems);
    });
    this.$eventHub.$on('resetSearch', function(payload) {
      parent.auctionItems = parent.masterList;
      parent.sortedPrice = false;
      parent.sortedMiles = false;
      parent.sortedValue = false;
      this.$eventHub.$emit('clearSearchForms');
      this.$eventHub.$emit('togglePrice', false);
      this.$eventHub.$emit('toggleMiles', false);
      this.$eventHub.$emit('toggleValue', false);
    });
  },
  methods: {
    trackIndex: function(index) {
      return index + 1
    },
    nameSearch(nameKey, myArray) {
      var resultArray = [];
      for (var i = 0; i < myArray.length; i++) {
        var curr_string = myArray[i].car_name
        if (curr_string.includes(nameKey)) {
          resultArray.push(myArray[i]);
        }
      }
      return resultArray;
    },
    airbagOptions(entries) {
      var flags = [],
        output = [],
        l = entries.length,
        i;
      for (i = 0; i < l; i++) {
        if (flags[entries[i].airbags]) continue;
        flags[entries[i].airbags] = true;
        output.push(entries[i].airbags);
      }
      return output;
    },
    airbagSearch(airbagKey, myArray) {
      var resultArray = [];
      for (var i = 0; i < myArray.length; i++) {
        var curr_string = myArray[i].airbags
        if (curr_string == airbagKey) {
          resultArray.push(myArray[i]);
        }
      }
      return resultArray;
    },
    bodyOptions(entries) {
      var flags = [],
        output = [],
        l = entries.length,
        i;
      for (i = 0; i < l; i++) {
        if (flags[entries[i].body]) continue;
        flags[entries[i].body] = true;
        output.push(entries[i].body);
      }
      return output;
    },
    bodySearch(bodyKey, myArray) {
      var resultArray = [];
      for (var i = 0; i < myArray.length; i++) {
        var curr_string = myArray[i].body
        if (curr_string == bodyKey) {
          resultArray.push(myArray[i]);
        }
      }
      return resultArray;
    },
    codeOptions(entries) {
      var flags = [],
        output = [],
        l = entries.length,
        i;
      for (i = 0; i < l; i++) {
        if (flags[entries[i].start_code]) continue;
        flags[entries[i].start_code] = true;
        output.push(entries[i].start_code);
      }
      return output;
    },
    codeSearch(codeKey, myArray) {
      var resultArray = [];
      for (var i = 0; i < myArray.length; i++) {
        var curr_string = myArray[i].start_code
        if (curr_string == codeKey) {
          resultArray.push(myArray[i]);
        }
      }
      return resultArray;
    },
    fobOptions(entries) {
      var flags = [],
        output = [],
        l = entries.length,
        i;
      for (i = 0; i < l; i++) {
        if (flags[entries[i].key_fob]) continue;
        flags[entries[i].key_fob] = true;
        output.push(entries[i].key_fob);
      }
      return output;
    },
    fobSearch(fobKey, myArray) {
      var resultArray = [];
      for (var i = 0; i < myArray.length; i++) {
        var curr_string = myArray[i].key_fob
        if (curr_string == fobKey) {
          resultArray.push(myArray[i]);
        }
      }
      return resultArray;
    },
    comparePrices(a, b) {
      if (parseInt(a.estimated_price, 10) < parseInt(b.estimated_price, 10)) {
        return -1;
      }
      if (parseInt(a.estimated_price, 10) > parseInt(b.estimated_price, 10)) {
        return 1;
      }
      return 0;
    },
    sortPrice(dir, myArray) {
      var sortedArray = [];
      this.$eventHub.$emit('togglePrice', true);
      sortedArray = myArray.sort(this.comparePrices);
      if (dir == "High to Low"){
        sortedArray = sortedArray.reverse()
      }
      return sortedArray;
    },
    compareMiles(a, b) {
      if (parseInt(a.miles.replace(/,/g,""), 10) < parseInt(b.miles.replace(/,/g,""), 10)) {
        return -1;
      }
      if (parseInt(a.miles.replace(/,/g,""), 10) > parseInt(b.miles.replace(/,/g,""), 10)) {
        return 1;
      }
      return 0;
    },
    sortMiles(dir, myArray) {
      var sortedArray = [];
      this.$eventHub.$emit('toggleMiles', true);
      sortedArray = myArray.sort(this.compareMiles);
      if (dir == "High to Low"){
        sortedArray = sortedArray.reverse()
      }
      return sortedArray;
    },
    compareValue(a, b) {
      if (a.value_est < b.value_est) {
        return -1;
      }
      if (a.value_est > b.value_est) {
        return 1;
      }
      return 0;
    },
    sortValue(dir, myArray) {
      var sortedArray = [];
      this.$eventHub.$emit('toggleValue', true);
      sortedArray = myArray.sort(this.compareValue);
      if (dir == "High to Low"){
        sortedArray = sortedArray.reverse()
      }
      return sortedArray;
    },
    fetchItems() {
      let uri = 'http://localhost:8080/api/all';
      axios.get(uri).then((response) => {
        this.auctionItems = response.data;
        this.masterList = response.data;
        this.$eventHub.$emit('setAirbagSearchOptions', this.airbagOptions(response.data));
        this.$eventHub.$emit('setBodySearchOptions', this.bodyOptions(response.data));
        this.$eventHub.$emit('setFobSearchOptions', this.fobOptions(response.data));
        this.$eventHub.$emit('setCodeSearchOptions', this.codeOptions(response.data));
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

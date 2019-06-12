<template>
<div style="margin-right:1%; margin-left:1%;">
  <h3>Filter Options</h3>
  <hr />
  <h4>Vehicle name search</h4>
  <input v-model="filterKey" placeholder="Vehicle name" />
  <hr />
  <h4>Airbags</h4>
  <select v-model="airbagKey">
    <option disabled value="">Select an option</option>
    <option v-for="airbagOption in airbagOptions">
      {{airbagOption}}
    </option>
  </select>
  <hr />
  <h4>Body Type</h4>
  <select v-model="bodyKey">
    <option disabled value="">Select an option</option>
    <option v-for="bodyOption in bodyOptions">
      {{bodyOption}}
    </option>
  </select>
  <hr />
  <h4>Key Fob</h4>
  <select v-model="fobKey">
    <option disabled value="">Select an option</option>
    <option v-for="fobOption in fobOptions">
      {{fobOption}}
    </option>
  </select>
  <hr />
  <h4>Start Code</h4>
  <select v-model="codeKey">
    <option disabled value="">Select an option</option>
    <option v-for="codeOption in codeOptions">
      {{codeOption}}
    </option>
  </select>
  <hr />
  <h4>Price</h4>
  <select v-model="priceKey">
    <option disabled value="">Select an option</option>
    <option>
      High to Low
    </option>
    <option>
      Low to High
    </option>
  </select>
  <hr />
  <h4>Miles</h4>
  <select v-model="mileKey">
    <option disabled value="">Select an option</option>
    <option>
      High to Low
    </option>
    <option>
      Low to High
    </option>
  </select>
  <hr />
  <h4>Estimated Value</h4>
  <select v-model="valueKey">
    <option disabled value="">Select an option</option>
    <option>
      High to Low
    </option>
    <option>
      Low to High
    </option>
  </select>
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
      filterKey: this.message,
      airbagKey: this.airbags,
      bodyKey: this.bodys,
      fobKey: this.fobs,
      priceKey: this.price,
      mileKey: this.miles,
      codeKey: this.codes,
      valueKey: this.values,
      airbagOptions: [],
      bodyOptions: [],
      fobOptions: [],
      codeOptions: []
    }
  },
  created: function() {
    var parent = this;
    this.$eventHub.$on('clearSearchForms', function(payload) {
      parent.filterKey = "";
      parent.airbagKey = "";
      parent.bodyKey = "";
      parent.fobKey = "";
      parent.codeKey = "";
      parent.priceKey = "";
      parent.mileKey = "";
      parent.valueKey = "";
    });
    this.$eventHub.$on('setAirbagSearchOptions', function(payload) {
      parent.airbagOptions = payload;
    });
    this.$eventHub.$on('setBodySearchOptions', function(payload) {
      parent.bodyOptions = payload;
    });
    this.$eventHub.$on('setFobSearchOptions', function(payload) {
      parent.fobOptions = payload;
    });
    this.$eventHub.$on('setCodeSearchOptions', function(payload) {
      parent.codeOptions = payload;
    });
  },
  props: {
    message: String,
    airbags: String,
    bodys: String,
    fobs: String,
    price: String,
    miles: String,
    values: String,
    codes: String
  },
  components: {
    ResetButton
  },
  watch: {
    filterKey: function(newVal, oldVal) {
      this.$eventHub.$emit('searchName', this.filterKey);
    },
    airbagKey: function(newVal, oldVal) {
      if (newVal) {
        this.$eventHub.$emit('searchAirbag', this.airbagKey);
      }
    },
    bodyKey: function(newVal, oldVal) {
      if (newVal) {
        this.$eventHub.$emit('searchBody', this.bodyKey);
      }
    },
    fobKey: function(newVal, oldVal) {
      if (newVal) {
        this.$eventHub.$emit('searchFob', this.fobKey);
      }
    },
    codeKey: function(newVal, oldVal) {
      if (newVal) {
        this.$eventHub.$emit('searchCode', this.codeKey);
      }
    },
    priceKey: function(newVal, oldVal) {
      if (newVal) {
        this.$eventHub.$emit('sortPrice', this.priceKey);
        this.mileKey = "";
        this.valueKey = "";
      }
    },
    mileKey: function(newVal, oldVal) {
      if (newVal) {
        this.$eventHub.$emit('sortMiles', this.mileKey);
        this.priceKey = "";
        this.valueKey = "";
      }
    },
    valueKey: function(newVal, oldVal) {
      if (newVal) {
        this.$eventHub.$emit('sortValue', this.valueKey);
        this.priceKey = "";
        this.mileKey = "";
      }
    }
  }
}
</script>

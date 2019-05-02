<template>
<transition name="modal">
  <div class="modal-mask">
    <div class="modal-wrapper">
      <div class="modal-container">

        <div class="modal-header">
          <slot name="header">
            {{modalData.car_name}}
            <img
            :src="modalData.car_image"
            class="img-thumbnail"/>
          </slot>
        </div>

        <div class="modal-body">
          <slot name="body">
            <ul>
              <li>
                Airbags: {{modalData.airbags}}
              </li>
              <li>
                Body: {{modalData.body}}
              </li>
              <li>
                Estimated Price: ${{modalData.estimated_price}}
              </li>
              <li>
                Key Fob: {{modalData.key_fob}}
              </li>
              <li>
                Miles: {{modalData.miles}}
              </li>
              <li>
                Damages: {{modalData.primary_damage}}, {{modalData.secondary_damage}}
              </li>
              <li>
                Start Code: {{modalData.start_code}}
              </li>
              <li>
                {{modalData.vin}}
              </li>
              <li>
                Estimated Value: {{modalData.value_est}}
              </li>
            </ul>
            <a :href="modalData.url" target="_blank">Auction Link</a>
          </slot>
        </div>

        <div class="modal-footer">
          <button class="btn btn-info" v-on:click="toggle_modal">
            Close
          </button>
        </div>

      </div>
    </div>
  </div>
</transition>
</template>

<script>
export default {
  name: 'Modal',
  data() {
    return {}
  },
  methods: {
    toggle_modal() {
      this.$eventHub.$emit('closeModal');
    }
  },
  props: {
    modalData: Object
  }
}
</script>

<style>
.modal-mask {
  position: fixed;
  z-index: 9998;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, .5);
  display: table;
  transition: opacity .3s ease;
}

.modal-wrapper {
  display: table-cell;
  vertical-align: middle;
}

.modal-container {
  width: 65%;
  margin: 0px auto;
  padding: 20px 30px;
  background-color: #fff;
  border-radius: 2px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, .33);
  transition: all .3s ease;
  font-family: Helvetica, Arial, sans-serif;
}

.modal-header h3 {
  margin-top: 0;
  color: #42b983;
}

.modal-body {
  margin: 20px 0;
}

.modal-default-button {
  float: right;
}

.modal-enter {
  opacity: 0;
}

.modal-leave-active {
  opacity: 0;
}

.modal-enter .modal-container,
.modal-leave-active .modal-container {
  -webkit-transform: scale(1.1);
  transform: scale(1.1);
}
</style>

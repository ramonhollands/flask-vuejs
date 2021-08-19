<template>
  <div @click="changeHandler" style="">
      <div class="small-button" :title="editable?'Toggle role':'Disabled'" style="float:left;" :style="label?'margin-right: 10px;':''">
        <i v-if="value" class="fas fa-check"></i> <!-- uses solid style -->
        <i v-else style="color: #006385" class="fas fa-check"></i> <!-- uses solid style -->
        <input class="checkbox" style="cursor: pointer; display: none" type="checkbox" :checked="value">
      </div>
      <div>{{label}}</div>
    </div>
</template>

<script>
export default {
  name: "Checkbox.vue",
  props: {
    'value': {required: true},
    'label': {default: ''},
    'editable': {default: true}
  },
  methods: {
    changeHandler () {
      if(!this.editable) {
        return;
      }
      this.$emit('input', !this.value);
    }
  }
}
</script>

<style scoped>
</style>
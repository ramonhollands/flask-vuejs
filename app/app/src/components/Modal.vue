import vSelect from 'vue-select'

<template>
    <div class="modal modal-active" style="display:block">
        <div class="modal-dialog modal-dialog-centered" style="max-width:80%">
            <div class="modal-content" style="min-height: 400px">
                <div v-if="loading" class="loading">Loading&#8230;</div>
                <div class="row">
                    <div class="col-md-12" style="position: relative;top: 0px;right: 0px;height: 28px;">
                      <div id="close" style="width: 40px" @click="close" class="medium button">X</div>
                    </div>
                </div>
                <div class="row" style="margin-top: 10px;">
                    <div class="col-md-12">
                       <slot name="content"></slot>
                    </div>
                </div>
                <div class="row">
                    <div class="col-md-12" style="position: relative;bottom: 16px;right: 0px;height: 28px;">
                      <slot name="buttons"></slot>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
export default {
  components: {},
  props: {
    'loading': {default: false}
  },
  data () {
    return {}
  },
  mounted () {
    $('.page-loader').show();
  },
  destroyed() {
    $('.page-loader').hide();
  },
  methods: {
      close() {
        this.$emit('close_modal')
      },
  },
}
</script>

<style scoped>
</style>
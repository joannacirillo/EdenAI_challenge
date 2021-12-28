<template>
  <b-card
    v-bind:title= prodName
    v-bind:img-src= imageSrc
    img-alt="Image"
    img-top
    tag="product"
    style="max-width: 20rem;"
    class="mb-2"
    >
      <b-row>
        <b-col>
            <b-card-text style="text-align:left">{{ price }}</b-card-text>
          </b-col>
          <b-col>
            <b-button>+</b-button>
          </b-col>
      </b-row>
    </b-card>
</template>
<script>
export default {
  name: 'ProductWidget',
  props: {
    price: {
      type: String,
      default: '0.00€',
      required: true
    },
    imageSrc: {
      type: String,
      default: '',
      required: false
    },
    prodName: {
      type: String,
      default: '',
      required: true
    }
  }
}
</script>
<style></style>

<template>
  <b-card
    title=productName
    img-src=imageSrc
    img-alt="Image"
    img-top
    tag="product"
    style="max-width: 20rem;"
    class="mb-2"
    ></b-card>
</template>
<script>
export default {
  name: 'ProductWidget',
  props: [
    'prodName',
    'imageSrc'
  ]
}
</script>
<style></style>

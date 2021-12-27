<template>
  <b-row>
    <b-col align="left">
      <b-link to="/">Accueil</b-link>
    </b-col>
    <b-col align="right">
      <b-button to="products">Produits</b-button>
      <b-button to="basket">Panier</b-button>
    </b-col>
  </b-row>
</template>
<script>
export default {
  props: {
  },
  name: 'NavBar'
}
</script>
<style></style>

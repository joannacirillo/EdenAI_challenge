import Vue from 'vue'
import Router from 'vue-router'
import Home from '@/components/Home/Home'
import Products from '@/components/Products/Products'
import Basket from '@/components/Basket/Basket'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Home',
      component: Home
    },
    {
      path: '/products',
      name: 'Products',
      component: Products
    },
    {
      path: '/basket',
      name: 'Basket',
      component: Basket
    }
  ]
})

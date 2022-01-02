import ProductWidget from './ProductWidget.vue'
import axios from 'axios';

export default {
  name : 'Products',
  components :{
      ProductWidget
    },
  data () {
    return {
      info: null
    }
  },
  methods: {
    mounted () {
      axios ({
        method:'get',
        url:'http://127.0.0.1:8000/api/products/'
      })
      .then(response => (this.info = response))
    }
  }
}
import { createApp } from 'vue'
import App from './App.vue'
import router from "./router"
import store from './store'

import 'normalize.css/normalize.css'

/* Global Components */
import Icon from '@/components/Global/GlobalIcon.vue'
import Button from '@/components/Global/GlobalButton.vue'
import Container from '@/components/Global/GlobalContainer.vue'
import Loading from '@/components/Global/GlobalLoading.vue'

/* Create App */
createApp(App)
    .use(store)
    .use(router)
    .component('Icon', Icon)
    .component('Button', Button)
    .component('Container', Container)
    .component('Loading', Loading)
    .mount('#app')
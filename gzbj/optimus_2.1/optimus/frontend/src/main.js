// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import VueMaterial from 'vue-material'
import 'vue-material/dist/vue-material.css'
import App from './App'
import router from './router'
import elementUi from 'element-ui'
import locale from 'element-ui/lib/locale/lang/en'
import 'element-ui/lib/theme-chalk/index.css'
import iView from 'iview';
import XEUtils from 'xe-utils'
import VXETable from 'vxe-table'
import  echarts from 'echarts'
import 'vxe-table/lib/index.css'
import 'iview/dist/styles/iview.css';
import _ from 'lodash';
import '@/assets/css/reset.css'
import '@/assets/sass/common.scss'
import '@/assets/sass/index.scss'
import util from '@/assets/utils/util'
import flexible from '@/assets/utils/flexible'
import AFTableColumn from 'af-table-column'



Vue.config.productionTip = false

// 路由跳转
Vue.prototype.$goRoute = function (index) {
  this.$router.push(index)
};
Vue.use(VueMaterial)
Vue.use(AFTableColumn)
Vue.use(elementUi, { locale })
Vue.use(VXETable)
Vue.use(iView)
Vue.use(util)
Vue.use(flexible)
Vue.prototype.$echarts=echarts;



// 全局获取缓存数据
// Vue.prototype.resetSetItem = function (key, newVal) {
//   if (key === 'watchStorage') {
//       // 创建一个StorageEvent事件
//       var newStorageEvent = document.createEvent('StorageEvent');
//       const storage = {
//           setItem: function (k, val) {
//               sessionStorage.setItem(k, val);

//               // 初始化创建的事件
//               newStorageEvent.initStorageEvent('setItem', false, false, k, null, val, null, null);

//               // 派发对象
//               window.dispatchEvent(newStorageEvent)
//           }
//       }
//       return storage.setItem(key, newVal);
//   }
// }

let Hub = new Vue();
Vue.prototype.$eventBus = Hub;//设立一个中转站
Vue.prototype.$XEUtils = XEUtils

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>'
})

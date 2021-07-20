import axios from 'axios'
import router from '../../router';
/**
 * 定义请求常量
 * TIME_OUT、ERR_OK
 */
export const TIME_OUT = 1500000000000000; // 请求超时时间
export const ERR_OK = true; // 请求成功返回状态，字段和后台统一
// 请求超时时间
axios.defaults.timeout = TIME_OUT;
// 引入基础路径，开发环境为了方便转发，值为空字符串
let baseURL = process.env.NODE_ENV === 'development' ? window.KYCFG.dapiUrl :  + ':80';//window.KYCFG.papiUrl;
axios.defaults.baseURL = baseURL;//process.env.baseUrl;
// 封装请求拦截
axios.interceptors.request.use(
  config => {
    //加时间戳  解决ie下不刷新问题
    if (config.method == 'post') {
      config.data = {
        ...config.data,
        _t: Date.parse(new Date()) / 1000
      }
    } else if (config.method == 'get') {
      config.params = {
        _t: Date.parse(new Date()) / 1000,
        ...config.params
      }
    }
    let token = sessionStorage.getItem('token'); // 获取token
    if (token != null) { // 如果token不为null，否则传token给后台
      config.headers['Authorization'] = token
    }else{
      router.replace({
        path: '/login' // 到登录页重新获取token
      });
    }
    return config
  },
  error => {
    return Promise.reject(error)
  }
)
// 封装响应拦截，判断token是否过期
axios.interceptors.response.use(
  response => {
    let {
      data
    } = response;
    if (data.code == 401) { // 如果后台返回的错误标识为token过期，则重新登录
      sessionStorage.removeItem('token'); // token过期，移除token
      sessionStorage.removeItem("user");//token过期，移除用户名
      router.replace({
        path: '/Login' // 到登录页重新获取token
      });
    }else if(data.code == 500){
      return Promise.reject(response)
    } else {
      return Promise.resolve(response)
    }
  },
  error => {
    return Promise.reject(error)
  }
)


export default axios
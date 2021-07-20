import axios from '@/assets/utils/axios'
import qs from 'qs'
let edition = 'v2.1'

// yamlGenerator默认列表
export function data_center_all (params) {
  return axios.get(`/api/ericic/${edition}/data_center`,params)
}

// yamlGenerator => current 上传
// export function current (params) {
//   let {site,cee_ver,project_name} = params;
//   return axios.post(`/api/v1/config/yaml_gen?site=${site}&cee_ver=${cee_ver}&pjt_name=${project_name}`)
// }


// yamlGenerator => history列表
export function yaml_gen_history () {
  return axios.get('/api/v1/config/yaml_gen/history')
}


// yamlGenerator => history 下载
export function down_history (id) {
  return axios.get(`/api/v1/config/yaml_gen/result?id=${id}`)
}


// yamlGenerator => history 删除
export function del_history (params) {
  return axios.delete(`/api/v1/config/yaml_gen/history`,params)
}




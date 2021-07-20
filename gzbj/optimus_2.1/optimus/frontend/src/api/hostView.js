import axios from '@/assets/utils/axios'
import qs from 'qs'
let edition = 'v2.1'

// 获得filter中tenant stack下来条件
export function getFilter (dc_id) {
  return axios.get(`/api/ericic/${edition}/host_config_data?dc_id=${dc_id}`)
}

// 获得Host View 表格数据
export function getTableData (params) {
  let {dc_id,limit,offset,query,sort,order,filter} = params;
  return axios.get(`/api/ericic/${edition}/host_data?dc_id=${dc_id}&limit=${limit}&offset=${offset}
  &query=${query}&sort=${sort}&order=${order}&filter=${filter}`)
}

// 获得Host Details 表格数据
export function getDetails (params) {
  let {cid,vid} = params;
  return axios.get(`/api/ericic/${edition}/${cid}/${vid}/network_port`)
}

// 获得Host Details CPU Layout
export function getLayout (params) {
  let {cid,hid} = params;
  return axios.get(`/api/ericic/${edition}/${cid}/cpu_layout/${hid}`)
}

// 获得Host Details Infra Resource State
export function getInfra (params) {
  let {cid,hid} = params;
  return axios.get(`/api/ericic/${edition}/${cid}/infra_resource/${hid}`)
}

// 获得Host Details Interface driver/firmware
export function getInterface (params) {
  let {cid,hid} = params;
  return axios.get(`/api/ericic/${edition}/${cid}/interface_driver/${hid}`)
}




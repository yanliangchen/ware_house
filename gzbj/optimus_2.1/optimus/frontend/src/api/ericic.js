import axios from '@/assets/utils/axios'
import qs from 'qs'
let edition = 'v2.1'

//DataCenter部分
// ericicLogin默认列表
export function data_center_all (params) {
  let {limit,offset} = params;
  return axios.get(`/api/ericic/${edition}/data_center?limit=${limit}&offset=${offset}`)
}

// ericicLogin默认列表 connection status
export function dc_connectionStatus (cid) {
  return axios.get(`/api/ericic/${edition}/connect_status?cid=${cid}`)
}

// ericicLogin => show
export function data_center_show (id) {
  return axios.get(`/api/ericic/${edition}/data_center?id=${id}`)
}

// ericicLogin => delete
export function data_center_delete (params) {
  return axios.delete(`/api/ericic/${edition}/data_center`,params)
}

// ericicLogin => edit
export function data_center_edit (params) {
  return axios.put(`/api/ericic/${edition}/data_center`,params)
}


// ericicLogin => edit => Verify connection 
export function verifyConnection (params) {
  return axios.post(`/api/ericic/${edition}/connect_status`,params)
}

// ericicLogin => new
export function data_center_new (params) {
  return axios.post(`/api/ericic/${edition}/data_center`,params)
}

// ericicContent =>get record
export function getRecord (params) {
  let {cid,limit,offset} = params;
  return axios.get(`/api/ericic/${edition}/record?cid=${cid}&limit=${limit}&offset=${offset}`)
}

// ericicContent =>save record
export function saveRecord (params) {
  return axios.post(`/api/ericic/${edition}/record`,params)
}

// ericicContent =>delete record
export function delRecord (params) {
  return axios.delete(`/api/ericic/${edition}/record`,params)
}

// ericicContent =>download record
export function down_history (dc_id) {
  return axios.get(`/api/ericic/${edition}/record/download?id=${dc_id}`)
}






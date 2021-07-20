import axios from '@/assets/utils/axios'
import qs from 'qs'
let edition = 'v2.1'

// 获得filter中tenant stack下来条件
export function getFilter (dc_id) {
  return axios.get(`/api/ericic/${edition}/config_data?dc_id=${dc_id}`)
}


// 获得VIM View 表格数据
export function getTableData (params) {
  let {dc_id,limit,offset,query,sort,order,filter} = params;
  return axios.get(`/api/ericic/${edition}/nova_data?dc_id=${dc_id}&limit=${limit}&offset=${offset}
  &query=${query}&sort=${sort}&order=${order}&filter=${filter}`)
}

// 获得VIM Details 表格数据
export function getDetails (params) {
  let {cid,vid} = params;
  return axios.get(`/api/ericic/${edition}/${cid}/${vid}/asdd/network_port`)
}



// 获得VIM Details 表格数据
export function getDetails1 (params) {
  let {cid,vid} = params;
  return axios.get(`/api/ericic/${edition}/${cid}/${vid}/uuuiiiddd/network_port`)
}





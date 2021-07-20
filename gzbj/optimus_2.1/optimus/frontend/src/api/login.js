import axios from '@/assets/utils/axios'
import qs from 'qs'
let edition = 'v2.1'

// 登录
export function login (params) {
  return axios.post(`/api/${edition}/login`,params)
}

// 注册
export function sign (params) {
  return axios.post(`/api/${edition}/sign`,params)
}

// Status
export function getStatus (cid) {
  return axios.get(`/api/ericic/${edition}/scheduler/task?cid=${cid}`)
}

// History
export function getSchedulerHistory (params) {
  let {cid,filter,limit,offset} = params;
  return axios.get(`/api/ericic/${edition}/scheduler/task/history?cid=${cid}&filter=${filter}&limit=${limit}&offset=${offset}`)
}

// seting
export function setSeting (params) {
  return axios.put(`/api/ericic/${edition}/scheduler/task`,params)
}


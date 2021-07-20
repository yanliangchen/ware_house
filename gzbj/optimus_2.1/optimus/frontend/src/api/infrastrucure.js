import axios from '@/assets/utils/axios'
import qs from 'qs'
let edition = 'v2.1'

// infra_resource
export function getEchartsData (cid) {
  return axios.get(`/api/ericic/${edition}/infrastructure?cid=${cid}`)
}

// tenant_quota
export function getQuota(params) {
  let {tid,cid} = params
  return axios.get(`/api/ericic/${edition}/${cid}/${tid}/tenant_quota`)
}




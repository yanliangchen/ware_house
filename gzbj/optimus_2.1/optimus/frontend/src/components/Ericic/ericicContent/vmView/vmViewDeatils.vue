<template>
  <div class="vmViewDeatils">
    <div class="header">
      <span class="title">VM:</span>
      <Select v-model="vid" style="width:200px" @on-change="changeVid" placeholder="">
        <Option v-for="item in idList" :value="item.value" :key="item.value">{{ item.label }}</Option>
      </Select>
      <Button class="button" @click="back">back</Button>
    </div>
    <div class="condition">
      <div class="title">
        Ports
      </div>
      <span class="s1">Traffic Static: </span>
      <Select v-model="time" style="width:60px" @on-change="changeTime" placeholder="">
        <Option v-for="item in timeList" :value="item.value" :key="item.value">{{ item.label }}</Option>
      </Select>
      <Button style="margin-left:10px" class="button" :disabled="disabled" @click="Start">Start</Button>
      <i v-show="disabled" class="el-icon-loading"></i>
    </div>
    <div class="tableBox"
          v-loading="loading"
        element-loading-text="Loading"
        element-loading-spinner="el-icon-loading">
      <el-table
        :data="tableData"
        :header-cell-style="{background:'#E6E9F2',color:'#8c8c8c'}"
        border
        empty-text="No data"
        ref="multipleTable"
        tooltip-effect="dark"
        style="width: 100%">
        <el-table-column
          label="ID"
          min-width="160"
          show-overflow-tooltip>
          <template slot-scope="scope">
            <a @click="handleId(scope.$index, scope.row)">{{scope.row.id}}</a>
          </template>
        </el-table-column>
        <el-table-column
          prop="name"
          label="Name"
          min-width="220"
          show-overflow-tooltip>
        </el-table-column>
        <el-table-column
          prop="ip_address"
          label="Ip Address"
          min-width="140"
          show-overflow-tooltip>
        </el-table-column>
        <el-table-column
          prop="vif_type"
          label="vif_type"
          width="100"
          show-overflow-tooltip>
        </el-table-column>
        <el-table-column
          prop="vhostuser"
          label="vhostuser"
          min-width="150"
          show-overflow-tooltip>
        </el-table-column>
        <el-table-column
          prop="mac"
          label="MAC"
          width="150"
          show-overflow-tooltip>
        </el-table-column>
        <el-table-column
          label="RX pkgs"
          width="120"
          show-overflow-tooltip>
          <template slot-scope="scope">
            <span>{{scope.row.rx_packets}}</span>
            <span v-if="scope.row.rx_packets_increase == '?' || scope.row.rx_packets_increase == '0' ">({{scope.row.rx_packets_increase}}) -</span>
            <span v-if="scope.row.rx_packets_increase < 0 "><span style="color:green">({{scope.row.rx_packets_increase}})</span>  <Icon style="color:green" size="14" type="md-arrow-round-down" /></span>
            <span v-if="scope.row.rx_packets_increase > 0 "><span style="color:red">({{scope.row.rx_packets_increase}})</span>  <Icon style="color:red" size="14" type="md-arrow-round-up" /></span>
          </template>
        </el-table-column>
        <el-table-column
          label="RX errors"
          width="120"
          show-overflow-tooltip>
          <template slot-scope="scope">
            <span>{{scope.row.rx_errors}}</span>
            <span v-if="scope.row.rx_errors_increase == '?' || scope.row.rx_errors_increase == '0' ">({{scope.row.rx_errors_increase}}) -</span>
            <span v-if="scope.row.rx_errors_increase < 0 "><span style="color:green">({{scope.row.rx_errors_increase}})</span>  <Icon style="color:green" size="14" type="md-arrow-round-down" /></span>
            <span v-if="scope.row.rx_errors_increase > 0 "><span style="color:red">({{scope.row.rx_errors_increase}})</span>  <Icon style="color:red" size="14" type="md-arrow-round-up" /></span>
          </template>
        </el-table-column>
        <el-table-column
          label="RX drop"
          width="120"
          show-overflow-tooltip>
          <template slot-scope="scope">
            <span>{{scope.row.rx_dropped}}</span>
            <span v-if="scope.row.rx_dropped_increase == '?' || scope.row.rx_dropped_increase == '0' ">({{scope.row.rx_dropped_increase}}) -</span>
            <span v-if="scope.row.rx_dropped_increase < 0 "><span style="color:green">({{scope.row.rx_dropped_increase}})</span>  <Icon style="color:green" size="14" type="md-arrow-round-down" /></span>
            <span v-if="scope.row.rx_dropped_increase > 0 "><span style="color:red">({{scope.row.rx_dropped_increase}})</span>  <Icon style="color:red" size="14" type="md-arrow-round-up" /></span>
          </template>
        </el-table-column>
        <el-table-column
          label="TX pkgs"
          width="120"
          show-overflow-tooltip>
          <template slot-scope="scope">
            <span>{{scope.row.tx_packets}}</span>
            <span v-if="scope.row.tx_packets_increase == '?' || scope.row.tx_packets_increase == '0' ">({{scope.row.tx_packets_increase}}) -</span>
            <span v-if="scope.row.tx_packets_increase < 0 "><span style="color:green">({{scope.row.tx_packets_increase}})</span> <Icon style="color:green" size="14" type="md-arrow-round-down" /></span>
            <span v-if="scope.row.tx_packets_increase > 0 "><span style="color:red">({{scope.row.tx_packets_increase}})</span> <Icon style="color:red" size="14" type="md-arrow-round-up" /></span>
          </template>
        </el-table-column>
        <el-table-column
          label="TX errors"
          width="120"
          show-overflow-tooltip>
          <template slot-scope="scope">
            <span>{{scope.row.tx_errors}}</span>
            <span v-if="scope.row.tx_errors_increase == '?' || scope.row.tx_errors_increase == '0' ">({{scope.row.tx_errors_increase}}) -</span>
            <span v-if="scope.row.tx_errors_increase < 0 "><span style="color:green">({{scope.row.tx_errors_increase}})</span>  <Icon style="color:green" size="14" type="md-arrow-round-down" /></span>
            <span v-if="scope.row.tx_errors_increase > 0 "><span style="color:red">({{scope.row.tx_errors_increase}})</span>  <Icon style="color:red" size="14" type="md-arrow-round-up" /></span>
          </template>
        </el-table-column>
        <el-table-column
          label="TX drop"
          width="120"
          show-overflow-tooltip>
          <template slot-scope="scope">
            <span>{{scope.row.tx_dropped}}</span>
            <span v-if="scope.row.tx_dropped_increase == '?' || scope.row.tx_dropped_increase == '0' ">({{scope.row.tx_dropped_increase}}) -</span>
            <span v-if="scope.row.tx_dropped_increase < 0 "><span style="color:green">({{scope.row.tx_dropped_increase}})</span>  <Icon style="color:green" size="14" type="md-arrow-round-down" /></span>
            <span v-if="scope.row.tx_dropped_increase > 0 "><span style="color:red">({{scope.row.tx_dropped_increase}})</span>  <Icon style="color:red" size="14" type="md-arrow-round-up" /></span>
          </template>
        </el-table-column>
      </el-table>
      <!-- <div class="pagination">
        <el-pagination
          background
          layout="total,prev, pager, next, jumper"
          @current-change="handleCurrentChange"
          :page-size="20"
          :total="total">
        </el-pagination>
      </div> -->
    </div>
  </div>
</template>

<script>
import { getDetails,getDetails1 } from "@/api/vmView"
export default {
  name: 'vmViewDeatils',
  data () {
    return {
      cid:'',
      vid:'',
      idList:[],
      tableData: [],
      total:0,
      loading:false,
      time:'6',
      timeList:[
        {
          label:'6s',
          value:'6'
        },
         {
          label:'10s',
          value:'10'
        },
         {
          label:'16s',
          value:'16'
        },
         {
          label:'30s',
          value:'30'
        }
      ],
      timer:'',
      value: 0,
      disabled:false,
      num:1
    }
  },
  mounted(){
    let dataCenter  = JSON.parse(sessionStorage.getItem('dataCenter'));
    this.cid = dataCenter.id;
    let vmViewIDs = JSON.parse(sessionStorage.getItem('vmViewIDs'));
    let tempList= [];
    vmViewIDs.forEach(res => {
      tempList.push({
        value:res.nova_uuid,
        label:res.nova_name,
      })
    });
    if(tempList.length>0){
      this.vid = tempList[0].value;
    }
    this.idList = tempList;
    this.getDetailsData();
  },
  methods:{
    async getDetailsData(){
      let {cid,vid} = this;
      let params = {
        cid:cid,
        vid:vid
      };
      this.loading = true;
      let res = await getDetails(params);
      let {data,code} = res.data;
      this.loading = false;
      // let res = {
      //   "code": 200,
      //   "data": [
      //       {
      //           "id": "06ff99d7-df78-4a71-a360-97ef0dbbb2ea",
      //           "ip_address": "fd00:5051::8:10",
      //           "mac": "fa:16:3e:54:19:de",
      //           "name": "worker-worker-4-ma9eda1-ma9eda1-worker-provisioning-net6-port-4",
      //           "rx_dropped": "2",
      //           "rx_errors": "?",
      //           "rx_packets": "7",
      //           "tx_dropped": "2",
      //           "tx_errors": "?",
      //           "tx_packets": "7",
      //           "vhostuser": "vhu06ff99d7-df",
      //           "vif_type": "vhostuser"
      //       },
      //       {
      //           "id": "0a7b9048-2074-4e65-83ee-91e8ce2c25bd",
      //           "ip_address": "10.191.28.19",
      //           "mac": "fa:16:3e:05:a5:c5",
      //           "name": "worker-worker-4-ma9eda1-ma9eda1-worker-oam-net4-port-4",
      //           "rx_dropped": "5",
      //           "rx_errors": "?",
      //           "rx_packets": "7",
      //           "tx_dropped": "5",
      //           "tx_errors": "?",
      //           "tx_packets": "7",
      //           "vhostuser": "vhu0a7b9048-20",
      //           "vif_type": "vhostuser"
      //       },
      //       {
      //           "id": "0ce1ef2e-4d10-4d37-8223-51d87bf4b344",
      //           "ip_address": "fd00:5052::b:3",
      //           "mac": "fa:16:3e:c6:2f:bb",
      //           "name": "worker-worker-4-ma9eda1-ma9eda1-worker-oam-net6-port-4",
      //           "rx_dropped": "2",
      //           "rx_errors": "?",
      //           "rx_packets": "5",
      //           "tx_dropped": "2",
      //           "tx_errors": "?",
      //           "tx_packets": "5",
      //           "vhostuser": "vhu0ce1ef2e-4d",
      //           "vif_type": "vhostuser"
      //       },
      //       {
      //           "id": "7d301b8a-89ea-4ae8-ad22-68194faeffeb",
      //           "ip_address": "fd00:5051::7:3",
      //           "mac": "fa:16:3e:d0:e1:a1",
      //           "name": "worker-worker-4-ma9eda1-ma9eda1-worker-traffic-net6-port-4",
      //           "rx_dropped": "2",
      //           "rx_errors": "?",
      //           "rx_packets": "7",
      //           "tx_dropped": "2",
      //           "tx_errors": "?",
      //           "tx_packets": "7",
      //           "vhostuser": "vhu7d301b8a-89",
      //           "vif_type": "vhostuser"
      //       },
      //       {
      //           "id": "8318eb81-bd50-41f7-87d1-c9ea807c7f49",
      //           "ip_address": "10.191.29.3",
      //           "mac": "fa:16:3e:83:49:64",
      //           "name": "worker-worker-4-ma9eda1-ma9eda1-worker-traffic-net4-port-4",
      //           "rx_dropped": "3",
      //           "rx_errors": "?",
      //           "rx_packets": "7",
      //           "tx_dropped": "3",
      //           "tx_errors": "?",
      //           "tx_packets": "7",
      //           "vhostuser": "vhu8318eb81-bd",
      //           "vif_type": "vhostuser"
      //       },
      //       {
      //           "id": "90c2d1b1-1808-47d6-ad7f-f60b0c27a489",
      //           "ip_address": "10.0.10.13",
      //           "mac": "fa:16:3e:95:6e:c5",
      //           "name": "worker-worker-4-ma9eda1-internal-port",
      //           "rx_dropped": "5",
      //           "rx_errors": "?",
      //           "rx_packets": "1",
      //           "tx_dropped": "5",
      //           "tx_errors": "?",
      //           "tx_packets": "1",
      //           "vhostuser": "vhu90c2d1b1-18",
      //           "vif_type": "vhostuser"
      //       },
      //       {
      //           "id": "e661ef7d-632c-45f0-b59a-04eb6418c56e",
      //           "ip_address": "10.191.29.19",
      //           "mac": "fa:16:3e:72:1b:4b",
      //           "name": "worker-worker-4-ma9eda1-ma9eda1-worker-provisioning-net4-port-4",
      //           "rx_dropped": "5",
      //           "rx_errors": "?",
      //           "rx_packets": "2",
      //           "tx_dropped": "5",
      //           "tx_errors": "?",
      //           "tx_packets": "2",
      //           "vhostuser": "vhue661ef7d-63",
      //           "vif_type": "vhostuser"
      //       }
      //   ],
      //   "status": true
      // }
      // let {data,code} = res;
      if(code == 200 && data.length>0){
        this.tableData = data;
      }
    },
    async getDetailsData1(){
      let {cid,vid,num} = this;
      if(this.value>=num){
        clearInterval(this.timer);
        this.disabled = false;
      }else{
        let params = {
          cid:cid,
          vid:vid
        };
        //this.loading = true;
        let res = await getDetails1(params);
        let {data,code} = res.data;
        //this.loading = false;
        if(code == 200 && data.length>0){
          this.tableData = data;
        }
      }
      this.value ++;
    },
    //分页
    handleCurrentChange(page){
      let tempOffset = (page-1)*20;
      this.offset = tempOffset;
      this.filterOk1();
    },
    //切换vid
    changeVid(id){
      this.disabled = false;
      this.value = 0;
      clearInterval(this.timer);
      this.vid = id;
      this.getDetailsData();
    },
    handleId(index,row){
      this.$goRoute('/neutronPort');
    },
    back(){
      this.$goRoute('/vmView')
    },
    changeTime(time){
      this.value = 0;
      this.time = time;
    },
    Start(){
      let {time} = this;
      this.num = time/2;
      this.disabled = true;
      this.timer = setInterval(this.getDetailsData1, (time/2)*1000);
    },
    getNewdata(){
      // this.value ++;
      // console.log(this.value);
      let res = {
        "code": 200,
        "data": [
            {
                "id": "06ff99d7-df78-4a71-a360-97ef0dbbb2ea",
                "ip_address": "fd00:5051::8:10",
                "mac": "fa:16:3e:54:19:de",
                "name": "worker-worker-4-ma9eda1-ma9eda1-worker-provisioning-net6-port-4",
                "rx_dropped": "2",
                "rx_dropped_increase": '?',
                "rx_errors": "?",
                "rx_errors_increase": "?",
                "rx_packets": "7",
                "rx_packets_increase": 3,
                "tx_dropped": "2",
                "tx_dropped_increase": 0,
                "tx_errors": "?",
                "tx_errors_increase": "10",
                "tx_packets": "7",
                "tx_packets_increase": 3,
                "vhostuser": "vhu06ff99d7-df",
                "vif_type": "vhostuser"
            },
            {
                "id": "0a7b9048-2074-4e65-83ee-91e8ce2c25bd",
                "ip_address": "10.191.28.19",
                "mac": "fa:16:3e:05:a5:c5",
                "name": "worker-worker-4-ma9eda1-ma9eda1-worker-oam-net4-port-4",
                "rx_dropped": "5",
                "rx_dropped_increase": 0,
                "rx_errors": "?",
                "rx_errors_increase": "0",
                "rx_packets": "7",
                "rx_packets_increase": -1,
                "tx_dropped": "5",
                "tx_dropped_increase": 0,
                "tx_errors": "?",
                "tx_errors_increase": "-12",
                "tx_packets": "7",
                "tx_packets_increase": -1,
                "vhostuser": "vhu0a7b9048-20",
                "vif_type": "vhostuser"
            },
            {
                "id": "0ce1ef2e-4d10-4d37-8223-51d87bf4b344",
                "ip_address": "fd00:5052::b:3",
                "mac": "fa:16:3e:c6:2f:bb",
                "name": "worker-worker-4-ma9eda1-ma9eda1-worker-oam-net6-port-4",
                "rx_dropped": "2",
                "rx_dropped_increase": 0,
                "rx_errors": "?",
                "rx_errors_increase": "12",
                "rx_packets": "5",
                "rx_packets_increase": 1,
                "tx_dropped": "2",
                "tx_dropped_increase": 0,
                "tx_errors": "?",
                "tx_errors_increase": "0",
                "tx_packets": "5",
                "tx_packets_increase": 1,
                "vhostuser": "vhu0ce1ef2e-4d",
                "vif_type": "vhostuser"
            },
            {
                "id": "7d301b8a-89ea-4ae8-ad22-68194faeffeb",
                "ip_address": "fd00:5051::7:3",
                "mac": "fa:16:3e:d0:e1:a1",
                "name": "worker-worker-4-ma9eda1-ma9eda1-worker-traffic-net6-port-4",
                "rx_dropped": "2",
                "rx_dropped_increase": '-11',
                "rx_errors": "?",
                "rx_errors_increase": "-2",
                "rx_packets": "7",
                "rx_packets_increase": 2,
                "tx_dropped": "2",
                "tx_dropped_increase": 0,
                "tx_errors": "?",
                "tx_errors_increase": "?",
                "tx_packets": "7",
                "tx_packets_increase": 2,
                "vhostuser": "vhu7d301b8a-89",
                "vif_type": "vhostuser"
            },
            {
                "id": "8318eb81-bd50-41f7-87d1-c9ea807c7f49",
                "ip_address": "10.191.29.3",
                "mac": "fa:16:3e:83:49:64",
                "name": "worker-worker-4-ma9eda1-ma9eda1-worker-traffic-net4-port-4",
                "rx_dropped": "3",
                "rx_dropped_increase": 0,
                "rx_errors": "?",
                "rx_errors_increase": "100",
                "rx_packets": "7",
                "rx_packets_increase": -2,
                "tx_dropped": "3",
                "tx_dropped_increase": 0,
                "tx_errors": "?",
                "tx_errors_increase": "0",
                "tx_packets": "7",
                "tx_packets_increase": -2,
                "vhostuser": "vhu8318eb81-bd",
                "vif_type": "vhostuser"
            },
            {
                "id": "90c2d1b1-1808-47d6-ad7f-f60b0c27a489",
                "ip_address": "10.0.10.13",
                "mac": "fa:16:3e:95:6e:c5",
                "name": "worker-worker-4-ma9eda1-internal-port",
                "rx_dropped": "5",
                "rx_dropped_increase": 10,
                "rx_errors": "?",
                "rx_errors_increase": "?",
                "rx_packets": "1",
                "rx_packets_increase": -7,
                "tx_dropped": "5",
                "tx_dropped_increase": 0,
                "tx_errors": "?",
                "tx_errors_increase": "22",
                "tx_packets": "1",
                "tx_packets_increase": -7,
                "vhostuser": "vhu90c2d1b1-18",
                "vif_type": "vhostuser"
            },
            {
                "id": "e661ef7d-632c-45f0-b59a-04eb6418c56e",
                "ip_address": "10.191.29.19",
                "mac": "fa:16:3e:72:1b:4b",
                "name": "worker-worker-4-ma9eda1-ma9eda1-worker-provisioning-net4-port-4",
                "rx_dropped": "5",
                "rx_dropped_increase": 0,
                "rx_errors": "?",
                "rx_errors_increase": "?",
                "rx_packets": "2",
                "rx_packets_increase": -7,
                "tx_dropped": "5",
                "tx_dropped_increase": 0,
                "tx_errors": "?",
                "tx_errors_increase": "-12",
                "tx_packets": "2",
                "tx_packets_increase": -7,
                "vhostuser": "vhue661ef7d-63",
                "vif_type": "vhostuser"
            }
        ],
        "status": true
      }
      let {data,code} = res;
      this.tableData = data;
    }
  },
  beforeDestroy() {
    clearInterval(this.timer);
  }
}
</script>

<style lang='scss'>
  .vmViewDeatils{
    .el-table--border td, .el-table--border th, .el-table__body-wrapper .el-table--border.is-scrolling-left~.el-table__fixed{
      border-right: none;
    }
  }
</style>
<style scoped lang="scss">
  .vmViewDeatils{
    width: 100%;
    height: 100%;
    .header{
      width: 100%;
      height: 50px;
      padding: 0 1rem;
      line-height: 50px;
      .title{
        font-size: 16px;
        font-weight: 700;
        margin-right: 10px;
      }
      .button{
        float:right;
        margin-top: 10px;
      }
    }
    .condition{
      width: 100%;
      height: 60px;
      .title{
        width: 100%;
        height: 30px;
        font-size: 16px;
        font-weight: 700;
        margin-left: 17px;
      }
      .s1{
        font-size: 12px;
        font-weight: 700;
        margin-left: 27px;
        margin-right: 10px;
      }

    }
    .tableBox{
      width: 100%;
      height: calc(100% - 115px);
      margin-top: 5px;
      padding: 0.5rem 1rem;
      .pagination{
        width: 100%;
        height: 60px;
        padding: 5px 0 10px 0;
        display: flex;
        align-items: center;
        justify-content: flex-end;
      }
    }
  }
</style>

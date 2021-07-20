<template>
  <div class="history">
    <div class="header">
      <Icon type="ios-book" />
      <span class="title">History</span>
    </div>
    <div class="tableBox">
      <el-table
        :data="tableData"
        :header-cell-style="{background:'#E6E9F2',color:'#8c8c8c'}"
        border
        empty-text="No data"
        ref="multipleTable"
        tooltip-effect="dark"
        style="width: 100%">
        <el-table-column
          prop="name"
          label="Name"
          show-overflow-tooltip>
        </el-table-column>
        <el-table-column
          prop="dc_name"
          label="Datacenter"
          width="110"
          show-overflow-tooltip>
        </el-table-column>
        <el-table-column
          prop="cee_version"
          label="CEE Version"
          width="100"
          show-overflow-tooltip>
        </el-table-column>
        <el-table-column
          prop="lcm_ip"
          label="LCM IP"
          width="140"
          show-overflow-tooltip>
        </el-table-column>
        <el-table-column
          prop="system_name"
          label="System Name"
          width="120"
          show-overflow-tooltip>
        </el-table-column>
        <el-table-column
          prop="openrc_path"
          label="OpenstackRC Dir"
          show-overflow-tooltip>
        </el-table-column>
        <el-table-column
          prop="timestamp"
          label="Create Time"
          width="140"
          show-overflow-tooltip>
        </el-table-column>
        <el-table-column
          prop="status"
          label="Status"
          width="100"
          show-overflow-tooltip>
        </el-table-column>
        <el-table-column
          label="Export"
          width="90"
          align="center"
          show-overflow-tooltip>
          <template slot-scope="scope">
            <span v-if="scope.row.status == 'successful'">
              <Icon style="color:green;cursor:pointer;font-size:17px" @click="downHistory(scope.$index,scope.row)" type="md-archive" />
            </span>
            <span v-else>
              <span style="color:red">waiting</span>
            </span>
          </template>
        </el-table-column>
        <el-table-column
          width="70"
          align="center"
          show-overflow-tooltip>
          <template slot-scope="scope">
            <Icon style="color:red;cursor:pointer;font-size:17px" @click="del(scope.$index,scope.row)" type="ios-close-circle" />
          </template>
        </el-table-column>
      </el-table>
      <div class="pagination"> 
        <el-pagination
          background
          layout="total,prev, pager, next, jumper"
          @current-change="handleCurrentChange"
          :total="total">
        </el-pagination>
      </div>
    </div>
    <Modal
      class-name="vertical-center-modal deleteModal"
      v-model="deleteModal"
      width="450px">
      <div class="icon">
        <Icon type="ios-alert-outline" size="22" style="color:#cf9236" />
      </div>
      <div class="errMsg">
        <div>Record DELETE ALERT</div>
        <div>Are you sure to delete this data of <span style="font-weight:500;font-size:16px;">{{fileName}}</span> (This operation can not be rollback.)</div>
      </div>
      <div class="soltFooter">
        <Button type="primary" @click="delConfirm()" style="margin:0 15px 0  8px;">OK</Button>
        <Button @click="delCancel()">Cancel</Button>
      </div>
    </Modal>
  </div>
</template>

<script>
import downloadjs from 'downloadjs';
import { getRecord,delRecord,down_history } from "@/api/ericic";
export default {
  name: 'history',
  data () {
    return {
      total:0,
      limit:10,
      offset:0,
      tableData: [],
      deleteModal:false,
      id:'',
      cid:'',
      fileName:''
    }
  },
  mounted(){
    let dataCenter  = JSON.parse(sessionStorage.getItem('dataCenter'));
    this.cid = dataCenter.id;
    this.getTableData();
  },
  methods:{
    async getTableData(){
      let _this = this;
      let {cid,limit,offset} = this;
      // let res = {
      //   "code": 200,
      //   "data": [
      //     {
      //       "cee_version": "drop28",
      //       "cid": "d9fd0c83a9a243adab8fe97087ab9d62",
      //       "data_center": "gaofzhan",
      //       "id": "de8c46a08b244793b7472e462718da48",
      //       "lcm_ip": "fd00:7070:0:2bd::17",
      //       "name": "gaofzhan_record_test_2",
      //       "openrc_path": "/home/ceeinfra/admin-openrc.sh",
      //       "pid": "65062673e1344c47af7ae80d64cfeb57",
      //       "status": "successful",
      //       "system_name": "DL33",
      //       "timestamp": 1614678997,
      //       "traceback": null
      //     },
      //     {
      //       "cee_version": "drop28",
      //       "cid": "d9fd0c83a9a243adab8fe97087ab9d62",
      //       "data_center": "gaofzhan",
      //       "id": "de8c46a08b244793b7472e462718da48",
      //       "lcm_ip": "fd00:7070:0:2bd::17",
      //       "name": "gaofzhan_record_test_2",
      //       "openrc_path": "/home/ceeinfra/admin-openrc.sh",
      //       "pid": "65062673e1344c47af7ae80d64cfeb57",
      //       "status": "error",
      //       "system_name": "DL33",
      //       "timestamp": 1614678997,
      //       "traceback": null
      //     }
      //   ],
      //   "status": true,
      //   "total": 1
      // };
      let params = {
        limit:limit,
        offset:offset,
        cid:cid
      }
      let res = await getRecord(params);
      let {code,data} = res.data;
      if(code == 200 && data.length>0){
        data.forEach(val=>{
          val.timestamp = _this.$util.formatDate(val.timestamp*1000,'yyyy-MM-dd HH:mm')
        })
      }
      this.tableData = data;
    },
    //跳转分页
    handleCurrentChange(page){
      let tempOffset = (page-1)*10;
      this.offset = tempOffset;
      this.getTableData();
    },
    del(index,row){
      this.deleteModal = true;
      let {id,name} = row;
      this.fileName = name;
      this.id = id;
    },
    delConfirm(){
      let _this = this;
      let params ={
        id : this.id
      }
      delRecord({data:params}).then(res=>{
        let {code} = res.data;
        if(code == 200){
          _this.$Message.success({
            duration: 2.5,
            content: 'Deletion succeeded!'
          });
          _this.getTableData();//刷新列表
        }else{
          _this.$Message.error({
            duration: 2.5,
            content: 'Deletion failed!'
          });
        };
        _this.deleteModal = false;
      })
    },
    delCancel(){
      this.deleteModal = false;
    },
    //History 表格中下载
    downHistory(index,row){
      down_history(row.id).then(res=>{
        let {code,data} = res.data;  
        if(code == 200){
          const blob = this.$util.base64ToBlob('data:application/x-zip-compressed;base64,' + data)
          downloadjs(blob,`${row.name}.xlsx`)
        };
      })
    },
    back(){
      this.$goRoute('/vmView')
    }
  }
}
</script>

<style lang='scss'>
  .history{
    .el-table--border td, .el-table--border th, .el-table__body-wrapper .el-table--border.is-scrolling-left~.el-table__fixed{
      border-right: none;
    }
  }
</style>
<style scoped lang="scss">
  .history{
    width: 100%;
    height: 100%;
    .header{
      width: 100%;
      height: 40px;
      padding: 0 1rem;
      line-height: 40px;
      color: rgb(77, 74, 74);
      padding-top: 5px;
      i{
        margin-bottom: 3px;
        font-size: 16px;
      }
      .title{
        font-size: 16px;
        font-weight: 700;
        margin-right: 10px;
      }
    }
    
    .tableBox{
      width: calc(100% - 30);
      height: calc(100% - 70px);
      margin: 10px 15px 15px 15px;
      box-shadow: 0 0 2px 2px #ddd;
      border-radius: 5px;
      .pagination{
        width: 100%;
        height: 60px;
        padding: 5px 0;
        display: flex;
        align-items: center;
        justify-content: flex-end;
      }
    }
  }
</style>

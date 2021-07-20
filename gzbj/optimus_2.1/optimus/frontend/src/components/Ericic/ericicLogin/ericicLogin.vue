<template>
  <div class="ericicLogin">
    <div class="tableBox">
      <el-table
        :header-cell-style="{background:'#E6E9F2',color:'#8c8c8c'}"
        v-loading="loading"
        element-loading-text="Loading"
        element-loading-spinner="el-icon-loading"
        empty-text="No data"
        ref="multipleTable"
        :data="tableData"
        tooltip-effect="dark"
        style="width: 100%">
        <el-table-column
          prop="name"
          label="Name"
          show-overflow-tooltip>
          <template slot-scope="scope">
            <a @click="handleSelect(scope.$index, scope.row)">{{scope.row.name}}</a>
          </template>
        </el-table-column>
        <el-table-column
          label="Connection Status"
          show-overflow-tooltip>
          <template slot-scope="scope">
            <span v-if="scope.row.connectionStatus == 0">
              <el-tag size="small" type="danger">failed</el-tag>
            </span>
            <span v-else-if="scope.row.connectionStatus == 1">
              <el-tag size="small" type="success">success</el-tag>
            </span>
            <span v-else-if="scope.row.connectionStatus == 3">
              <i class="vxe-icon--refresh roll"></i>
            </span>
            <span v-else-if="scope.row.connectionStatus == 4">

            </span>
          </template>
        </el-table-column>
        <el-table-column
          prop="Mode"
          label="Mode"
          show-overflow-tooltip>
        </el-table-column>
        <el-table-column
          label="AccessMgmt"
          width="300"
          align="left">
          <template slot-scope="scope">
            <span v-if="scope.row.type == 1 && scope.row.Mode == 'online'">
              <Button type="primary" class="ivu-btn-table" @click="handleShow(scope.$index, scope.row)">Show</Button>
              <Button type="error"  class="DELETE ivu-btn-table" @click="handleDelete(scope.$index, scope.row)">Delete</Button>
              <Button type="info" class="ivu-btn-table" @click="handleSelect(scope.$index, scope.row)">Select</Button>
            </span>
            <span v-if="scope.row.type == 1 && scope.row.Mode == 'offline'">
              <Button type="primary" class=" ivu-btn-table" @click="handleShow(scope.$index, scope.row)">Show</Button>
              <Button type="error"  class="DELETE ivu-btn-table" @click="handleDelete(scope.$index, scope.row)">Delete</Button>
              <Button type="info" class="ivu-btn-table" @click="handleSelect(scope.$index, scope.row)">Select</Button>
              <Button type="success" icon="ios-download-outline" class="ivu-btn-table upload" @click="handleUpload(scope.$index, scope.row)">
                <el-upload
                  multiple
                  ref="upload"
                  :show-file-list="false"
                  class="upload-demo"
                  action
                  accept= '.json'
                  :http-request="uploadSectionFile">
                  <span>Upload</span>
                </el-upload>
              </Button>
            </span>
            <span v-if="scope.row.type == 0">
              <Button  class="ivu-btn-table"  @click="handleNew(scope.$index, scope.row)">
                New<Icon type="ios-add" size="16" />
              </Button>
            </span>
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
        <div>DATACENTER DELETE ALERT</div>
        <div>Are you sure to delete all datas of <span style="font-weight:500;font-size:16px;">{{fileName}}</span> (This operation can not be rollback.)</div>
      </div>
      <div class="soltFooter">
        <Button type="primary" @click="delConfirm()" style="margin:0 15px 0  8px;">OK</Button>
        <Button @click="delCancel()">Cancel</Button>
      </div>
    </Modal>
  </div>
</template>

<script>
import $ from 'jquery';
import _ from 'lodash';
import axios from 'axios'
import { data_center_all,dc_connectionStatus,data_center_delete,data_center_upload } from "@/api/ericic"
export default {
  name: 'ericicLogin',
  data () {
    return {
      tempData:[],
      tableData:[],
      total:0,
      limit:10,
      offset:0,
      loading:false,
      deleteModal:false,
      fileName:'',
      id:'',
      promiseAll:[],
      connectionStatusBox:[]
    }
  },
  mounted(){
    this.getList();
  },
  methods:{
    //table 列表
    async getList(){
      let _this = this;
      this.loading = true;
      let {limit,offset}= this;
      let params = {
        limit:limit,
        offset:offset
      };
      let res = await data_center_all(params);
      this.loading = false;
      let {data,total,code} = res.data;
      if(code == 200){
        let tempoffset = this.offset;
        if(data.length == 0 && tempoffset != 0){
          this.offset = tempoffset -10;
          this.getList();
          return false;
        }
        data.forEach(res=>{
          res.type = 1;
          if(res.mode){
            res.Mode = 'online'
          }else{
            res.Mode = 'offline'
          }
        })
        data.forEach(res=>{
          let {id} = res;
          if(res.mode){
            res.connectionStatus = '3'
            //this.promiseAll.push(_this.getConnectionStatus(id))
          }
        })
        //this.getAllConnectionStatus();
        data.push({
          Name:'',
          ConnectionStatus:'',
          type:0
        });
        this.tableData = data;
        this.total = total;
        this.tempData = data;
        data.forEach(res=>{
          let {id} = res;
          if(res.mode){
            _this.getConnectionStatus(id)
          }
        })
      }
    },
    //跳转分页
    handleCurrentChange(page){
      let tempOffset = (page-1)*10;
      this.offset = tempOffset;
      this.getList();
    },
    //获得 Connection Status
    getConnectionStatus(id){
      let _this = this;
      dc_connectionStatus(id).then(res=>{
        let {code,data,message} = res.data;
        if(code == 200){
          let tempData = _this.tempData;
          for(var j=0;j<tempData.length;j++){
              if(id === tempData[j].id){
                tempData[j].connectionStatus = data;
              }
          }
          tempData.forEach(res=>{
            if(res.connectionStatus == false){
              res.connectionStatus = '0'
            }else if(res.connectionStatus == true){
              res.connectionStatus = '1'
            }else if(res.connectionStatus == '3'){
              res.connectionStatus = '3'
            }else if(res.Mode == 'offline'){
              res.connectionStatus = '4'
            }
          });
          // console.log(new Date().getTime()+'-----' + id)
          _this.tableData = tempData;
        }
      });
      // return new Promise((resolve,reject)=>{
      //   dc_connectionStatus(id).then(res=>{
      //     let {code,data,message} = res.data;
      //     if(code == 200){
      //       _this.connectionStatusBox.push({
      //         id:id,
      //         connectionStatus:data
      //       })
      //       resolve();
      //     }else{
      //       reject();
      //     }
      //   });
      // });
    },
    //循环调用 接口 获得 Connection Status
    getAllConnectionStatus(){
      Promise.all(this.promiseAll).then((res)=>{
        let connectionS = this.connectionStatusBox;
        let tempData = this.tempData;
        for(var i=0;i<connectionS.length;i++){
          for(var j=0;j<tempData.length;j++){
              if(connectionS[i].id === tempData[j].id){
                tempData[j].connectionStatus = connectionS[i].connectionStatus;
              }
          }
        }
        tempData.forEach(res=>{
          if(res.connectionStatus == false){
            res.connectionStatus = '0'
          }else if(res.connectionStatus == true){
            res.connectionStatus = '1'
          }else{
            res.connectionStatus = '4'
          }
        })
        this.tableData = tempData;
        // 调用完所有接口需要做的事情
      })
    },
    //show
    handleShow(index,row){
      sessionStorage.setItem('dataCenter',JSON.stringify(row));
      this.$goRoute(`/ericicShow`);
    },
    //upload
    handleUpload(index,row){
      let {id} = row;
      this.id = id;
    },
    //upload file
    uploadSectionFile(file){
      let _this = this;
      let fileId = this.id;
      let formData = new FormData();  //  用FormData存放上传文件
      formData.append("json_file",file.file);
      formData.append("id",fileId);
      if(/\.json$/.test(file.file.name)){
        let baseURL  = process.env.NODE_ENV === 'development' ? window.KYCFG.dapiUrl : + '';
        let uploadUrl =  `/api/ericic/v1/data_center/upload`;
        $.ajax({
          type: "post", // 数据提交类型
          url: uploadUrl, // 发送地址
          data: formData, //发送数据
          async: true, // 是否异步
          processData: false, //processData 默认为false，当设置为true的时候,jquery ajax 提交的时候不会序列化 data，而是直接使用data
          contentType: false, //
          success:function(res){
            let {code,message} = res;
            if(code == 200){
              _this.$Message.success({
                duration: 2.5,
                content: message
              });
            }
          },
          error:function(XMLHttpRequest, textStatus, errorThrown){
            _this.$Message.error({
              duration: 2.5,
              content: 'Upload failed!'
            });
            // let {code,message} = res.responseJSON;
            // if(code == 400){
            //   _this.$Message.error({
            //     duration: 2.5,
            //     content: message
            //   });
            // }else if(code == 500){
            //   _this.$Message.error({
            //     duration: 2.5,
            //     content: 'Server error!'
            //   });
            // }
          }
        });
      }else{
        this.$Message.error({
          duration: 2.5,
          content: 'This type of file is not supported!'
        });
      };
    },
    //表格中delete
    handleDelete(index,row){
      let {id,name} = row;
      this.fileName = name;
      this.id = id;
      this.deleteModal = true;
    },
    //表格中select
    handleSelect(index,row){
      this.$goRoute('/vmView');
      sessionStorage.setItem('dataCenter',JSON.stringify(row));
      this.$eventBus.$emit('headerKey',1);//控制表头按钮显示
    },
    //跳转到新增页面
    handleNew(index,row){
      this.$goRoute(`/ericicNew`);
    },
    //delete 确定
    delConfirm(){
      let _this = this;
      let params ={
        id : this.id
      }
      data_center_delete({data:params}).then(res=>{
        let {data,code} = res.data;
        if(code == 200){
          _this.$Message.success({
            duration: 2.5,
            content: 'Deletion succeeded!'
          });
          _this.getList();//刷新列表
        }else{
          _this.$Message.error({
            duration: 2.5,
            content: 'Deletion failed!'
          });
        };
        _this.deleteModal = false;
      }).catch(error => {
        let response = error.response;
        if(response.status == 400){
          _this.$Message.error({
            duration: 3.5,
            content: response.data.message
          });
        }else if(response.status == 500){
          _this.$Message.error({
            duration: 2.5,
            content: 'Server error!'
          });
        }
      });
      
    },
    //delete 取消
    delCancel(){
      this.deleteModal = false;
    }
  },
  destroyed(){}
}
</script>

<style scoped lang="scss">
  .ericicLogin{
    width: 100%;
    height: 100%;
    overflow: auto;
    padding: 20px;
    .tableBox{
      box-shadow: 0 0 2px 2px #ddd;
      border-radius: 5px;
      .ivu-btn-table{
        padding: 1.4px 8px 2.5px !important;
      }
      .upload{
        background-color: #002561 !important;
        border-color: #002561 !important;
        &:hover{
          background-color: #4259C1 !important;
          border-color: #4259C1 !important;
        }
      }
      .ivu-btn{
        margin-right: .5rem;    
      }
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

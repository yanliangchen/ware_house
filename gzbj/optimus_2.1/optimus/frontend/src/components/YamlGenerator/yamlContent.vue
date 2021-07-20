<template>
  <div class="yamlContent">
    <div class="Homepage">
      <Tabs active-key="key1"  type="card" v-model="tabName" @on-click='changeTabs'>
        <Tab-pane label="Current" key="Current" name="Current">
          <div class="tab_content_iptarea">
            <div class="part">
              <div class="tab-form-title">site</div>
              <div class="tab-form-select">
                <Select v-model="site" style="width:90%" placeholder="site">
                  <Option v-for="item in siteList" :value="item.value" :key="item.value">{{ item.label }}</Option>
                </Select>
              </div>
            </div>
            <div class="part">
              <div class="tab-form-title">cee version</div>
              <div class="tab-form-select">
                <Select v-model="cee" style="width:90%" placeholder="cee version">
                  <Option v-for="item in ceeList" :value="item.value" :key="item.value">{{ item.label }}</Option>
                </Select>
              </div>
            </div>
            <div class="part">
              <div class="tab-form-title">project name</div>
              <div class="tab-form-input">
                <Input v-model="projectName" placeholder="Eproject name" style="width: 90%" />
              </div>
            </div>
          </div>
          <div class="tab_content_upload">
            <div class="fileBox">
              <span v-show="fileNameList.length == 0">upload input files(at least 1 excel and 1 config yaml file)</span>
              <el-tag  v-show="fileNameList.length != 0" style="margin-right:10px;" :type="tag.type == 'yaml' ? '' : 'success'" :key="tag.FILE_NAME" v-for="tag in fileNameList" size="small" :disable-transitions="false">{{tag.FILE_NAME}}</el-tag>
            </div>
            <div class="tab_upload_btn_grp">
              <Button type="primary" class="upload btn">
                <el-upload
                  multiple
                  ref="upload"
                  :show-file-list="false"
                  :auto-upload="false"
                  class="upload-demo"
                  action
                  accept= '.yaml,.xls,.xlsx'
                  :on-change="handleChange">
                  <span>Upload</span>
                </el-upload>
                <!-- <input type="file" id="file"   accept=".xls,.xlsx,.yaml"  @change="changeFile"  multiple="true">  -->
              </Button>
              <Button type="primary" class="btn" @click="reset">Reset</Button>
            </div>
          </div>
          <div class="tableBox">
            <el-table
              :header-cell-style="{background:'#E6E9F2',color:'#8c8c8c'}"
              border
              empty-text="No data"
              :data="fileNameList"
              tooltip-effect="dark"
              :max-height="maxTableHeight1"
              style="width: 100%">
              <el-table-column
                type="index"
                label="ID"
                width="70">
              </el-table-column>
              <el-table-column
                prop="FILE_NAME"
                label="FILE_NAME"
                show-overflow-tooltip>
              </el-table-column>
              <el-table-column label="OPERATION" width="200" align="center">
                <template slot-scope="scope">
                  <Icon type="md-trash" style="cursor: pointer;" size="16"   @click="deleteFile(scope.$index, scope.row)" />
                </template>
              </el-table-column>
            </el-table>
          </div>
          <div class="tab_content_generator_btn">
            <Button class="Generator"  @click="uploadGenerator">Generator Config</Button>
          </div>
        </Tab-pane>
        <Tab-pane label="History" key="History" name="History">
          <div class="tab_content_delete_btn">
            <Button type="error"  class="DELETE" @click="deleteAll">DELETE</Button>
          </div>
          <div>
            <el-table
              :header-cell-style="{background:'#E6E9F2',color:'#8c8c8c'}"
              border
              empty-text="No data"
              ref="multipleTable"
              :data="historyData"
              tooltip-effect="dark"
              style="width: 100%"
              :max-height="maxTableHeight"
              @selection-change="handleSelectionChange">
              <el-table-column
                type="selection"
                width="55">
              </el-table-column>
              <el-table-column
                type="index"
                label="ID"
                width="70">
              </el-table-column>
              <el-table-column
                prop="project_name"
                label="Project_Name"
                show-overflow-tooltip>
              </el-table-column>
              <el-table-column
                prop="cee_version"
                label="CEE_Version"
                show-overflow-tooltip>
              </el-table-column>
              <el-table-column
                prop="timestamp"
                label="RUN_TIME"
                show-overflow-tooltip>
              </el-table-column>
              <el-table-column
                label="TASK_STATUS"
                align="center"
                width="150">
                <template slot-scope="scope">
                  <span v-if="scope.row.status == 'success'">
                    <el-tag size="small" type="success">{{scope.row.status}}</el-tag>
                  </span>
                  <span v-else>
                    <el-tag size="small" type="danger">{{scope.row.status}}</el-tag>
                  </span>
                </template>
              </el-table-column>
              <el-table-column label="OPERATION" width="150" align="center">
                <template slot-scope="scope">
                  <span v-if="scope.row.status == 'success'">
                    <i class="el-icon-download"   style="cursor: pointer;margin-right:10px;" @click="downHistory(scope.$index, scope.row)"></i>
                  </span>
                  <Icon type="md-trash" style="cursor: pointer;" size="16"   @click="deleteHistory(scope.$index, scope.row)" />
                </template>
              </el-table-column>
            </el-table>
            <div class="pagination">
              <el-pagination background layout="total,prev, pager, next, jumper" :total="totalNum" :current-page="pageNum"  :page-size='pageSize'  @current-change="pageClick">
              </el-pagination>
            </div>
          </div>
        </Tab-pane>
      </Tabs>
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
    <Modal
      class-name="vertical-center-modal deleteModal"
      v-model="deleteAllModal"
      width="450px">
      <div class="icon">
        <Icon type="ios-alert-outline" size="22" style="color:#cf9236" />
      </div>
      <div class="errMsg">
        <div>DATACENTER DELETE ALERT</div>
        <div>Are you sure to delete all datas  (This operation can not be rollback.)</div>
      </div>
        <div class="soltFooter">
          <Button type="primary" @click="delAllConfirm()" style="margin:0 15px 0  8px;">OK</Button>
          <Button @click="delAllCancel()">Cancel</Button>
        </div>
    </Modal>
  </div>
</template>

<script>
import _ from 'lodash';
import axios from 'axios'
import downloadjs from 'downloadjs';
import { yaml_gen_history,down_history,del_history } from "@/api/yamlGenerator"
export default {
  name: 'yamlContent',
  data () {
    return {
      tabName:'Current',
      siteList:[
        {
          value:'GZ',
          label:'GZ'
        },
        {
          value:'ZZ',
          label:'ZZ'
        }
      ],
      site:'',
      ceeList:[
        {
          value:'drop22',
          label:'drop22'
        },
        {
          value:'drop25',
          label:'drop25'
        },
        {
          value:'drop26',
          label:'drop26'
        },
        {
          value:'drop28',
          label:'drop28'
        },
        {
          value:'drop35',
          label:'drop35'
        }
      ],
      cee:'',
      projectName:'',
      fileNameList:[],
      fileList:[],
      chunkData:[],
      historyData:[],
      totalNum:0,
      pageSize:10,
      pageNum:1,
      maxTableHeight:200,
      maxTableHeight1:200,
      multipleSelection:[],
      deleteModal:false,
      deleteAllModal:false,
      fileName:'',
      id:''
    }
  },
  mounted(){
    //动态设置table高度
    this.$nextTick(()=>{
      let screenHeight = document.body.clientHeight;//浏览器高度
      let tempHeight = screenHeight - 241;
      this.maxTableHeight = tempHeight;
      this.maxTableHeight1 = tempHeight - 130;
    });
  },
  methods:{
    changeFile(){},
    //重置
    reset(){
      this.site = '';
      this.cee = '';
      this.projectName = '';
      this.fileNameList = [];
    },
    handleChange(file){
      this.addNewFile(file);
    },
    //Generator Config 上传
    uploadGenerator(){
      let _this = this;
      let {site,cee,projectName} = this;
      if(site == '' || cee == '' || projectName == '' || this.fileNameList.length == 0){
        this.$Message.error({
          duration: 2,
          content: 'Please complete the form!'
        });
        return false;
      }
      let typeBox = [];
      this.fileNameList.forEach(res=>{
        typeBox.push(res.type)
      })
      if((typeBox.indexOf('xlsx') == -1 && typeBox.indexOf('xls') == -1) || typeBox.indexOf('yaml') == -1){
        this.$Message.error({
          duration: 2,
          content: 'Please upload least 1 excel and 1 config yaml file!'
        });
        return false;
      };
     

      const formData = new FormData();  //  用FormData存放上传文件
      let tempfileList = this.fileList;
      this.fileNameList.forEach((res,index)=>{
        if(res.type == 'yaml'){
          formData.append("yaml",tempfileList[index].raw)
        }else{
          formData.append("excel",tempfileList[index].raw)
        }
      });
      // this.fileList.forEach(res=>{
      //   formData.append("file",res.raw)
      // });
      let baseURL = process.env.NODE_ENV === 'development' ? window.KYCFG.dapiUrl : window.KYCFG.papiUrl;
      $.ajax({
        type: "POST", // 数据提交类型
        url: baseURL + `/api/v1/config/yaml_gen?site=${site}&cee_ver=${cee}&pjt_name=${projectName}`, // 发送地址
        data: formData, //发送数据
        async: true, // 是否异步
        processData: false, //processData 默认为false，当设置为true的时候,jquery ajax 提交的时候不会序列化 data，而是直接使用data
        contentType: false, //
        success:function(res){
          _this.tabName = 'History'  //上传完成后切换到History页
        },
        error:function(res){
          let {code,message} = res.responseJSON;
          if(code == 400){
            _this.$Message.error({
              duration: 2.5,
              content: message
            });
          }else if(code == 500){
            _this.$Message.error({
              duration: 2.5,
              content: 'Server error!'
            });
          }
        }
      });
//       axios({
// 　　　　url:baseURL + `/api/v1/config/yaml_gen?site=${site}&cee_ver=${cee}&pjt_name=${projectName}`,
// 　　　　data:formData, //在此处上传文件
// 　　　　method: "post",
// 　　　　headers:{
// 　　　　　　'Content-Type':'multipart/form-data' //值得注意的是，这个地方一定要把请求头更改一下
// 　　　　}
// 　　　　}).then(function(res){
//           _this.tabName = 'History'  //上传完成后切换到History页
// 　　　　}).catch(function(req){
// 　　　　　 console.log(req,"请求失败的回调，自己看看为啥失败")
// 　　　　})
      
    },
    //选择多个文件逻辑处理 只能上传一个xsl文件和多个yaml文件 不能有其他的文件类型
    addNewFile(file){
      let _this = this;
      let name = file.name;
      let type = name.split('.').pop();
      let repeatExcel,repeatFile=true;
      if(this.fileNameList.length>0){
        this.fileNameList.forEach(res=>{
          if(res.type == type && (type == 'xlsx' || type == 'xls')){
            repeatExcel = true;
            return false;
          }
          if(res.FILE_NAME == name){
            _this.$Message.error({
              duration: 2.5,
              content: 'Duplicate file cannot be uploaded!'
            });
            repeatFile = false;
            return false;
          }
        });
      }
      if(repeatFile){
        // 上传excel
        if(/\.(xlsx|xls)$/.test(name)){
          if(repeatExcel){
            this.$Message.warning({
              duration: 2.5,
              content: 'Excel has been uploaded and the previous file has been replaced!'
            });
          }else{
            this.$Message.success('New file added success!');
            this.fileNameList.push({'FILE_NAME':name,'type':type});
            this.fileList.push(file);
          }
        }else if(/\.yaml$/.test(name)){// 上传yaml
          this.$Message.success('New file added success!');
          this.fileNameList.push({'FILE_NAME':name,'type':type});
          this.fileList.push(file);
        }else{
          this.$Message.error({
            duration: 2.5,
            content: 'This type of file is not supported!'
          });
        };
      }
    },
    //Current表格中删除文件
    deleteFile(index,row){
      let {FILE_NAME,type} = row;
      let tempList = this.fileNameList;
      for(var i = 0; i < tempList .length; i++) {
        if(tempList[i].FILE_NAME == FILE_NAME) {
          tempList.splice(i, 1);
          break;
        }
      };
      this.fileNameList = tempList;
      
      //保存得file列表
      let tempFileList = this.fileList;
      for(var i = 0; i < tempList .length; i++) {
        if(tempFileList[i].name == FILE_NAME) {
          tempFileList.splice(i, 1);
          break;
        }
      };
      this.fileList = tempFileList;
    },
    //切换tabs
    changeTabs(name){
      if(name == 'History'){
        this.getHistoryList();
      }
    },
    //History 列表
    getHistoryList(){
      let _this = this;
      yaml_gen_history().then(res=>{
        let {code,data} = res.data;
        if(code == 200){
          _this.totalNum = data.length;
          _this.chunkData = _.chunk(data,10);
          _this.historyData = this.chunkData[0];
        }
      }).catch(error => {
        let response = error.response;
        this.verifyDisabled = false;
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
    pageClick(page){//跳转分页
      this.historyData = this.chunkData[page-1];
    },
    //History 表格中下载
    downHistory(index,row){
      let {id} = row;
      down_history(id).then(res=>{
        let {code,data} = res.data;  
        if(code == 200){
          const blob = this.$util.base64ToBlob('data:application/x-zip-compressed;base64,' + data)
          downloadjs(blob,`${id}.zip`)
        };
      })
    },
    //History 表格中删除
    deleteHistory(index,row){
      this.deleteModal = true;
      let {id,project_name} = row;
      this.fileName = project_name;
      this.id = id;
    },
    //删除 确定
    async delConfirm(){
      let {id} = this;
      let params = {'id':[id]};
      let res = await del_history({data:params});
      let {code} = res.data;
      if(code == 200){
        this.$Message.success({
          duration: 2.5,
          content: 'Deletion succeeded!'
        });
        this.getHistoryList();
      }else{
        this.$Message.error({
          duration: 2.5,
          content: 'Deletion failed!'
        });
      }
      this.deleteModal = false;
    },
    //删除 取消
    delCancel(){
      this.deleteModal = false;
    },
    //History 表格多选
    handleSelectionChange(val){
      this.multipleSelection = val;
    },
    //History 批量删除
    deleteAll(){
      let {multipleSelection} = this;
      if(multipleSelection.length == 0){
        this.$Message.error({
          duration: 2.5,
          content: 'Please select the data to be deleted!'
        });
      }else{
        this.deleteAllModal = true;
      }
    },
    //删除全部 确定
    async delAllConfirm(){
      let delData = this.multipleSelection;
      let idBox = [];
      delData.forEach(res=>{
        idBox.push(res.id);
      })
      let params = {'id':idBox};
      let res = await del_history({data:params});
      let {code} = res.data;
      if(code == 200){
        this.$Message.success({
          duration: 2.5,
          content: 'Deletion succeeded!'
        });
        this.getHistoryList();
      }else{
        this.$Message.error({
          duration: 2.5,
          content: 'Deletion failed!'
        });
      }
      this.deleteAllModal = false;
    },
    //删除全部 取消
    delAllCancel(){
      this.deleteAllModal = false;
    },
  }
}
</script>

<style scoped lang="scss">
  .yamlContent{
    width: 100%;
    height: calc(100% - 2.5rem);
    overflow: auto;
    padding:1rem 2rem 0 2rem;
    .Homepage{
      width: 100%;
      height: 100%;
      overflow: auto;
      // background-color: #F9FAFF;
      .tab_content_iptarea{
        max-width: 38rem;
        width: 100%;
        display: flex;
        .part{
          margin-bottom: 24px;
          .tab-form-title{
            color: #8c8c8c !important;
            margin-bottom: 0.2rem;
            margin-left: 0.3rem;
            height: 1.5rem;
          }
          .tab-form-select{
            width: 12rem;
          }
          .tab-form-input{
            width: 18rem;
          }
        }
      }
      .tab_content_upload{
        display: flex;
        margin-top: 0.4rem;
        margin-bottom: 1.6rem;
        width: 100%;
        .tab_upload_btn_grp{
          display: flex;
          align-items: center;
          .upload{
            background-color: #002561 !important;
            border-color: #002561 !important;
            margin: 0 10px 0 20px;
            &:hover{
              background-color: #4259C1 !important;
              border-color: #4259C1 !important;
            }
          }
          .btn{
            height: 2rem;
          }
        }
        .fileBox{
          width: 40.2rem;
          height: auto;
          line-height: 2rem;
          min-height: 2rem;
          background-color: #fff;
          border: 1px solid #d9d9d9;
          border-radius: 2px;
          // display: flex;
          // align-items: center;
          padding-left: 10px;
          color: #d9d9d9;
          word-wrap: break-word; 
          word-break: normal;
          &:hover{
            border-color: #465AB0;
          }
        }
      }
      .tab_content_delete_btn{
        width: 100%;
        margin: 0 0 0.75rem 0;
        display: block;
        text-align: right;
      }
      .tab_content_generator_btn{
        margin: 1.5rem 0 1.5rem 0;
        float: right;
        .Generator{
          color: #e6fffb;
          background-color: #006d75;
          border-color: #006d75;
        }
      }
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

<template>
  <div class="hostView">
    <div class="header">
      <div class="buttonBox">
        <div class="tabs">
          <div @click="change(1)">VM View</div>
          <div>|</div>
          <div @click="change(0)" class="activedBut" >Host View</div>
        </div>
        <div class="s_button" @click="showFilter">Filter</div>
        <div class="s_button" @click="selectData">Select</div>
      </div>
    </div>
    <el-collapse-transition>
      <div class="filterStatus" v-show="filterStatus">
        <Tabs :value="filterName"  @on-click='changeTabs'>
          <TabPane label="Host" name="host">
            <div class="line">
              <span>Host:</span>
              <span>
                <Input v-model="fhost" @keyup.enter.native="filterOk" placeholder="Host" style="width: 200px" />
              </span>
            </div>
          </TabPane>
          <TabPane label="Host Aggregate" name="host_aggregate">
            <div class="line">
              <span>Host Aggregate:</span>
              <span>
                <Select :transfer="true" v-model="aggregate" style="width:200px" placeholder="Please select">
                  <Option v-for="(item,index) in aggregateList" size="small" :value="item.value" :key="index">{{ item.label }}</Option>
                </Select>
              </span>
            </div>
          </TabPane>
          <TabPane label="Availability Zone" name="availability_zone">
            <div class="line">
              <span>Availability Zone:</span>
              <span>
                <Select :transfer="true" v-model="availability" style="width:200px" placeholder="Please select">
                  <Option v-for="(item,index) in availabilityList" size="small" :value="item.value" :key="index">{{ item.label }}</Option>
                </Select>
              </span>
            </div>
          </TabPane>
          <TabPane label="Host State" name="state">
            <div class="line">
              <span>Host State:</span>
              <span>
                <Input v-model="hostState" @keyup.enter.native="filterOk" placeholder="Host State" style="width: 200px" />
              </span>
            </div>
          </TabPane>
        </Tabs>
        <div class="line line_l">
          <div class="button" @click="filterOk">Ok</div>
          <div class="button" @click="filterReset">Reset</div>
        </div>
      </div>
    </el-collapse-transition>
    <div class="sortBox">
      <div class="title">Sorting by:</div>
      <div class="selectBox">
        <Dropdown trigger="click"  @on-click="clickDropdown">
          <a href="javascript:void(0)">
            {{vmAmount}}
            <Icon type="ios-arrow-down"></Icon>
          </a>
          <DropdownMenu slot="list">
            <DropdownItem name="time_asc" :selected="selectedDrop == 'lowest'?true:false">lowest to highest</DropdownItem>
            <DropdownItem name="time_desc" :selected="selectedDrop == 'highest'?true:false">highest from lowest</DropdownItem>
          </DropdownMenu>
        </Dropdown>
      </div>
      <div class="pagination">
        <el-pagination
          background
          layout="total,sizes,prev, pager, next, jumper"
          :page-sizes="[20, 40, 60, 100,200]"
          @size-change="handleSizeChange"
          @current-change="handleCurrentChange"
          :page-size="20"
          :total="total">
        </el-pagination>
      </div>
    </div>
    <div class="tableBox">
      <el-table
        :row-class-name="tableRowClassName"
        :height="tableHeight"
        :data="tableData"
        :header-cell-style="{background:'#E6E9F2',color:'#8c8c8c'}"
        border
        empty-text="No data"
        ref="multipleTable"
        tooltip-effect="dark"
        style="width: 100%"
        @selection-change="handleSelectionChange">
        <el-table-column
          type="selection"
          width="55">
        </el-table-column>
        <el-table-column
          prop="host"
          width="auto"
          label="Host"
          show-overflow-tooltip>
        </el-table-column>
        <el-table-column
          prop="host_aggregate"
          width="130"
          show-overflow-tooltip
          label="Host Aggregate">
        </el-table-column>
        <el-table-column
          prop="availability_zone"
          width="140"
          show-overflow-tooltip
          label="Availability Zone">
        </el-table-column>
        <el-table-column
          prop="state"
          width="65"
          show-overflow-tooltip
          label="Host State">
        </el-table-column>
        <el-table-column
          min-width="250"
          style="padding-right:5px;"
          label="VM UUID">
          <template slot-scope="scope">
            <!-- <el-tooltip class="item" effect="dark" placement="top">
              <div v-html="scope.row.vmUuid" slot="content"></div>
              <div style="font-size:12px" v-html="scope.row.vmUuid" ></div>
            </el-tooltip> -->
            <div style="font-size:12px;" v-html="scope.row.vmUuid"></div>
          </template>
        </el-table-column>
        <el-table-column
          width="200"
          label="VM Name">
          <template slot-scope="scope">
            <div style="font-size:12px" v-html="scope.row.vmName"></div>
          </template>
        </el-table-column>
        <el-table-column
          width="100"
          label="VM Status">
          <template slot-scope="scope">
            <div style="font-size:12px" v-html="scope.row.vmStatus"></div>
          </template>
        </el-table-column>
        <el-table-column
          width="120"
          label="VM Tenant">
          <template slot-scope="scope">
            <div style="font-size:12px" v-html="scope.row.vmTenant"></div>
          </template>
        </el-table-column>
      </el-table>
      
    </div>
  </div>
</template>

<script>
import { getFilter,getTableData } from "@/api/hostView"
export default {
  name: 'hostView',
  data () {
    return {
      limit:20,
      offset:0,
      nowPage:1,
      dc_id:'',
      total:0,
      query:'host',
      filter:'',
      sort:'vm_num',
      order:'desc',
      vmAmount:'VM amount',
      selectedDrop:'',
      filterStatus:false,
      filterName:'host',
      aggregate:'',
      aggregateList:[],
      availability:'',
      availabilityList:[],
      fhost:'',
      hostState:'',
      tableData: [],
      multipleSelection:[],
      tableHeight:400
    }
  },
  mounted(){
    this.$nextTick(()=>{
      let screenHeight = document.body.clientHeight;//浏览器高度
      let tempHeight = screenHeight - 150;
      this.tableHeight = tempHeight;
    });
    this.dataCenterDetails = JSON.parse(sessionStorage.getItem('dataCenter'));
    let {cee_version,data_center,id,name,Mode} = this.dataCenterDetails;
    this.dc_id = id;
    this.getFilterList();
    this.filterOk();
  },
  methods:{
    //table斑马纹
    tableRowClassName({ rowIndex }) {
      if (rowIndex % 2 === 0) {
        return "warning-row";
      } else if (rowIndex % 2 === 1) {
        return "success-row";
      }
      return "";
    },
    //获得筛选条件中 tenant stack条件下拉列表
    getFilterList(){
      let {dc_id} = this;
      getFilter(dc_id).then(res=>{
        let {code,data} = res.data;
        if(code == 200 && data.length>0){
          let {host_az,host_ha} = data[0];
          let tempHa = [],tempAz = [];
          host_ha.forEach(ele=>{
            tempHa.push(
              {
                value:ele.aggregate_name,
                label:ele.aggregate_name
              }
            )
          })
          host_az.forEach(ele=>{
            tempAz.push(
              {
                value:ele.availability_zone,
                label:ele.availability_zone
              }
            )
          });
          this.aggregateList = tempHa;
          this.availabilityList = tempAz;
        }
      })
    },
    showFilter(){
      this.filterStatus = !this.filterStatus;
    },
    change(type){
      if(type == 1){
        this.$goRoute('/vmView');
      }else{
        this.$goRoute('/hostView');
      }
    },
    //点击sorting by下拉菜单
    clickDropdown(name){
      let temp = name.split('_');
      //this.sort = temp[0];
      this.order = temp[1];
      if(temp[1] == 'asc'){
        this.selectedDrop = 'lowest'
      }else{
        this.selectedDrop = 'highest'
      }
      this.filterOk();
    },
    //筛选确定
    filterOk(){
      let _this = this;
      let {dc_id,limit,offset,query,sort,order} = this;
      if(query == 'host'){
        this.filter = this.fhost;
      }else if(query == 'host_aggregate'){
        this.filter = this.aggregate;
      }else if(query == 'availability_zone'){
        this.filter = this.availability;
      }else if(query == 'state'){
        this.filter = this.hostState;
      }
      let params={
        dc_id:dc_id,
        query:query,
        filter:this.filter != undefined ? this.filter : '',
        sort:sort,
        order:order,
        limit:limit,
        offset:0
      };
      getTableData(params).then(res=>{
        let {code,data,total} = res.data;
        if(code == 200 && data.length>0){
          data.forEach(val=>{
            // let {host,hz,nova_data,state,status,timestamp,update_at} = val;
            let {host,host_aggregate,nova_data,state,status,timestamp,update_at,
            availability_zone,vm_info} = val;
            val.timestamp = _this.$util.formatDate((val.timestamp)*1000,'yyyy-MM-dd HH:mm');
            val.update_at = _this.$util.formatDate((val.update_at)*1000,'yyyy-MM-dd HH:mm');
            let tepmUUid = '',tepmName = '',tepmStatus = '',tepmTenant = '';
            if(vm_info && vm_info.length>0){
              vm_info.forEach(res=>{
                let {name,status,id,tenant_name} = res;
                tepmUUid = _this.$util.formatString(id) + '<br/>' + tepmUUid;
                tepmName = _this.$util.formatString(name) + '<br/>' + tepmName;
                tepmStatus = _this.$util.formatString(status) + '<br/>' + tepmStatus;
                tepmTenant = _this.$util.formatString(tenant_name) + '<br/>' + tepmTenant;
              })
            };
            val.vmUuid = tepmUUid;
            val.vmName = tepmName;
            val.vmStatus= tepmStatus;
            val.vmTenant = tepmTenant;
          });
          // debugger
          // data.forEach(res=>{
          //   let teNum = res.host.split('-')[2].split('.')[0];
          //   res.sortNum = teNum;
          // })
          // function compare(property){
          //   return function(a,b){
          //       var value1 = a[property];
          //       var value2 = b[property];
          //       return value1 - value2;
          //   }
          // }
          // let newData = data.sort(compare('sortNum'));
          this.tableData = data;
          //console.log('第一个'+newData[0].host+'.......'+'第二个'+newData[1].host)
          this.total = total;
        }else{
          this.tableData = [];
          this.total = 0;
        }
      })
      
      this.filterStatus = false;
    },
    //筛选确定
    filterOk1(){
      let _this = this;
      let {dc_id,limit,offset,query,sort,order} = this;
      if(query == 'host'){
        this.filter = this.fhost;
      }else if(query == 'host_aggregate'){
        this.filter = this.aggregate;
      }else if(query == 'availability_zone'){
        this.filter = this.availability;
      }else if(query == 'state'){
        this.filter = this.hostState;
      }
      let params={
        dc_id:dc_id,
        query:query,
        filter:this.filter != undefined ? this.filter : '',
        sort:sort,
        order:order,
        limit:limit,
        offset:offset
      };
      getTableData(params).then(res=>{
        let {code,data,total} = res.data;
        if(code == 200 && data.length>0){
          data.forEach(val=>{
            // let {host,hz,nova_data,state,status,timestamp,update_at} = val;
            let {host,host_aggregate,nova_data,state,status,timestamp,update_at,
            availability_zone,vm_info} = val;
            val.timestamp = _this.$util.formatDate((val.timestamp)*1000,'yyyy-MM-dd HH:mm');
            val.update_at = _this.$util.formatDate((val.update_at)*1000,'yyyy-MM-dd HH:mm');
            let tepmUUid = '',tepmName = '',tepmStatus = '',tepmTenant = '';
            if(vm_info && vm_info.length>0){
              vm_info.forEach(res=>{
                let {name,status,id,tenant_name} = res;
                tepmUUid = _this.$util.formatString(id) + '<br/>' + tepmUUid;
                tepmName = _this.$util.formatString(name) + '<br/>' + tepmName;
                tepmStatus = _this.$util.formatString(status) + '<br/>' + tepmStatus;
                tepmTenant = _this.$util.formatString(tenant_name) + '<br/>' + tepmTenant;
              })
            };
            val.vmUuid = tepmUUid;
            val.vmName = tepmName;
            val.vmStatus= tepmStatus;
            val.vmTenant = tepmTenant;
          });
          this.tableData = data;
          this.total = total;
        }else{
          this.tableData = [];
          this.total = 0;
        }
      })
      this.filterStatus = false;
    },
    //分页
    handleCurrentChange(page){
      this.nowPage = page;
      let tempOffset = (page-1)*20;
      this.offset = tempOffset;
      this.filterOk1();
    },
    handleSizeChange(num){
      let {nowPage}  = this;
      let tempOffset = (nowPage-1)*num;
      this.limit = num;
      this.offset = tempOffset;
      this.filterOk1();
    },
    //筛选重置
    filterReset(){
      this.fhost = '';
      this.hostState = '';
      this.aggregate = '';
      this.availability = '';
      this.selectedDrop = '';
    },
    //切换tabs
    changeTabs(name){
      this.query = name;
    },
    //History 表格多选
    handleSelectionChange(val){
      this.multipleSelection = val;
    },
    //强制多选表格
    selectData(){
      let {multipleSelection} = this;
      if(multipleSelection.length == 0){
        this.$Message.warning({
          duration: 2.5,
          content: 'Please select the data !'
        });
      }else{
        sessionStorage.setItem('hostViewIDs',JSON.stringify(multipleSelection))
        this.$goRoute('/hostViewDetails')
      }
    },
  },
  beforeDestroy(){

  }
}
</script>

<style lang="scss">
  .hostView{
    .el-table--border td, .el-table--border th, .el-table__body-wrapper .el-table--border.is-scrolling-left~.el-table__fixed{
      border-right: none;
    }
  }
  .hostView{
    .el-table td .cell{
      font-size: 12px !important;
    }
  }
</style>
<style scoped lang="scss">
  .hostView{
    width: 100%;
    height: 100%;
    .header{
      width: 100%;
      height: 55px;
      .buttonBox{
        width: 100%;
        height: 55px;
        display: flex;
        align-items: center;
        .tabs{
          width: 12rem;
          height: 30px;
          border: 1px solid #ddd;
          border-radius: .4rem;
          float: left;
          margin-left: 1rem;
          div{
            font-size: .7rem;
            width: 89px;
            float: left;
            height: 30px;
            line-height: 30px;
            text-align: center;
            font-weight: 400;
            cursor: pointer;
          }
          div:nth-child(2){
            width: 10px;
            text-align: center;
          }
          .activedBut{
            font-weight: 500;
            color: #409eff;
          }
        }
        .s_button{
          padding: 0 .7rem;
          height: 2rem;
          border: 1px solid #ddd;
          border-radius: .4rem;
          float: left;
          display: flex;
          justify-content: center;
          align-items: center;
          cursor: pointer;
          margin-left: 10px;
          &:hover{
            border: 1px solid #409eff;
            color: #409eff;
          }
        }
      }
    }
    .filterStatus{
      width: calc(100% - 2rem);
      height: 11rem;
      margin: 0 1rem;
      border:1px dashed #dee0e4;
      border-radius: .4rem;
      .ivu-tabs{
        padding: 0 .5rem;
      }
      .ivu-tabs .ivu-tabs-tabpane{
        height: 4.5rem;
      }
      .line{
        width: 100%;
        height: 2.5rem;
        display: flex;
        align-items: center;
        span:nth-child(1){
          font-size: 14px;
          font-weight: 500;
          width: 150px;
          text-align: left;
          padding: 0 10px 0 20px;
        }
        .button{
          padding: 0 .7rem;
          height: 2rem;
          border: 1px solid #ddd;
          border-radius: .4rem;
          float: left;
          display: flex;
          justify-content: center;
          align-items: center;
          cursor: pointer;
          margin-left: 10px;
        }
        .button:nth-child(1){
          margin-left: 30px;
        }
      }
      .line_l{
        height: 3rem;
        border-top: 1px dashed #dee0e4;
      }
    }
    
    .sortBox{
      width: 100%;
      height: 2rem;
      display: flex;
      align-items: center;
      color: #000;
      position: relative;
      .title{
        height: 100%;
        font-size: .9rem;
        font-weight: 600;
        margin-right: .6rem;
        margin-left: 1rem;
        display: flex;
        align-items: center;
        float: left;
      }
      .selectBox{
        float: left;
        .ivu-dropdown{
          margin-right: 30px;
          .ivu-icon{
            display: none;
          }
          .ivu-dropdown-rel a{
            color: #000 !important;
          }
        }
        .ivu-dropdown:nth-child(1){
          margin-left: 10px;
        }
      }
      
      .pagination{
        max-width: 500px;
        height: 60px;
        padding: 5px 0 10px 0;
        display: flex;
        align-items: center;
        justify-content: flex-end;
        position: absolute;
        right: 10px;
      }
    }
    .tableBox{
      width: 100%;
      height: calc(100% - 90px);
      padding: 0.5rem 1rem;
    }
  }
</style>

<template>
  <div class="vmView">
    <div class="header">
      <div class="buttonBox">
        <div class="tabs">
          <div @click="change(1)" class="activedBut" >VM View</div>
          <div>|</div>
          <div @click="change(0)">Host View</div>
        </div>
        <div class="s_button" @click="showFilter">Filter</div>
        <div class="s_button" @click="selectData">Select</div>
        <div class="advanceBox">
          <Button @click="showHideAdvance">Advance</Button>
          <div class="cBox" v-show="advanceS">
            <CheckboxGroup v-model="AdvanceGroup">
              <Checkbox label="Flavor" ></Checkbox>
              <Checkbox label="Volume" ></Checkbox>
              <Checkbox label="Host"></Checkbox>
              <Checkbox label="Created Time"></Checkbox>
              <Checkbox label="Tenant"></Checkbox>
            </CheckboxGroup>
            <el-button class="bt" size="mini"  @click="advanceOk">OK</el-button>
            <el-button size="mini"  @click="advanceCancel">Cancel</el-button>
          </div>
        </div>
      </div>
    </div>
    <el-collapse-transition>
      <div class="filterStatus" v-show="filterStatus">
        <Tabs :value="filterName" @on-click='changeTabs'>
          <TabPane label="Name" name="nova_name">
            <div class="line">
              <span>Name:</span>
              <span>
                <Input v-model="fName" @keyup.enter.native="filterOk" placeholder="Name" style="width: 200px" />
              </span>
            </div>
          </TabPane>
          <TabPane label="VM Status" name="nova_status">
            <div class="line">
              <span>Status:</span>
              <span>
                <Select :transfer="true" v-model="fStatus" style="width:200px"  placeholder="Please select">
                  <Option v-for="item in statusList" size="small" :value="item.value" :key="item.value">{{ item.label }}</Option>
                </Select>
              </span>
            </div>
          </TabPane>
          <TabPane label="Host" name="nova_host">
            <div class="line">
              <span>Host:</span>
              <span>
                <Input v-model="fHost" @keyup.enter.native="filterOk" placeholder="Host" style="width: 200px" />
              </span>
            </div>
          </TabPane>
          <TabPane label="Tenant" name="nova_tenant">
            <div class="line">
              <span>Tenant:</span>
              <span>
                <Select :transfer="true" v-model="fTenant" style="width:200px" placeholder="Please select">
                  <Option v-for="item in tenantList" size="small" :value="item.label" :key="item.value">{{ item.label }}</Option>
                </Select>
              </span>
            </div>
          </TabPane>
          <TabPane label="Stack" name="stack_id">
            <div class="line">
              <span>Stack:</span>
              <span>
                <Select :transfer="true" v-model="fStack" style="width:200px" placeholder="Please select">
                  <Option v-for="item in stackList" size="small" :value="item.value" :key="item.value">{{ item.label }}</Option>
                </Select>
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
        <Dropdown trigger="click" divided @on-click="clickDropdown">
          <a href="javascript:void(0)">
            Created Time
            <Icon type="ios-arrow-down"></Icon>
          </a>
          <DropdownMenu slot="list">
            <DropdownItem name="time_desc" :selected="selectedDrop == 'time_desc'?true:false">start from latest</DropdownItem>
            <DropdownItem name="time_asc" :selected="selectedDrop == 'time_asc'?true:false">start from oldest</DropdownItem>
          </DropdownMenu>
        </Dropdown>
      </div>
      <div class="selectBox">
          <Dropdown trigger="click" @on-click="clickDropdown1">
          <a href="javascript:void(0)">
            Flavor Size
            <Icon type="ios-arrow-down"></Icon>
          </a>
          <DropdownMenu slot="list">
            <DropdownItem name="vcpu_asc"  :selected="selectedDrop1 == 'vcpu_asc'?true:false">vcpu increazing</DropdownItem>
            <DropdownItem name="vcpu_desc" :selected="selectedDrop1 == 'vcpu_desc'?true:false">vcpu decreazing</DropdownItem>
            <DropdownItem name="memory_asc" :selected="selectedDrop1 == 'memory_asc'?true:false">mem increazing</DropdownItem>
            <DropdownItem name="memory_desc" :selected="selectedDrop1 == 'memory_desc'?true:false">mem decreazing</DropdownItem>
            <DropdownItem name="disk_asc" :selected="selectedDrop1 == 'disk_asc'?true:false">disk increazing</DropdownItem>
            <DropdownItem name="disk_desc" :selected="selectedDrop1 == 'disk_desc'?true:false">disk decreazing</DropdownItem>
          </DropdownMenu>
        </Dropdown>
      </div>
      <div class="pagination">
        <el-pagination
          background
          layout="total,sizes,prev, pager, next, jumper"
          @current-change="handleCurrentChange"
          @size-change="handleSizeChange"
          :page-sizes="[20, 40, 60, 100,200]"
          :page-size="20"
          :total="total">
        </el-pagination>
      </div>
    </div>
    <div class="tableBox">
      <el-table
        :row-class-name="tableRowClassName"
        :data="tableData"
        :header-cell-style="{background:'#E6E9F2',color:'#8c8c8c'}"
        empty-text="No data"
        ref="multipleTable"
        tooltip-effect="dark"
        style="width: 100%"
        :height="tableHeight"
        @selection-change="handleSelectionChange">
        <el-table-column
          type="selection"
          width="55">
        </el-table-column>
        <el-table-column
          prop="nova_uuid"
          label="UUID"
          min-width="150"
          show-overflow-tooltip>
        </el-table-column>
        <el-table-column
          prop="nova_name"
          label="Name"
          min-width="150"
          show-overflow-tooltip>
        </el-table-column>
        <el-table-column
          prop="nova_status"
          label="Status"
          min-width="70"
          show-overflow-tooltip>
        </el-table-column>
        <el-table-column
          prop="nova_power_state"
          label="Power State"
          width="70"
          show-overflow-tooltip>
        </el-table-column>
        <el-table-column
          label="Networks"
          min-width="350">
          <template slot-scope="scope">
            <!-- <div style="font-size:12px" v-html="scope.row.oNetworks"></div> -->
            <el-tooltip class="item" effect="dark" placement="top">
              <div v-html="scope.row.oNetworks" slot="content"></div>
              <div style="font-size:12px" v-html="scope.row.oNetworks1" ></div>
            </el-tooltip>
          </template>
        </el-table-column>
        <el-table-column label="Flavor" :key="Math.random()" v-if="this.AdvanceStatus.indexOf('Flavor') != -1" align="center">
          <el-table-column
            prop="flavor_vcpu"
            label="vCPU"
            width="60"
          show-overflow-tooltip>
          </el-table-column>
          <el-table-column
            prop="flavor_memory"
            label="Mem(Gb)"
            width="60"
          show-overflow-tooltip>
          </el-table-column>
          <el-table-column
            prop="flavor_disk"
            label="Disk"
            width="60"
            show-overflow-tooltip>
          </el-table-column>
        </el-table-column>
        <el-table-column label="Volume" :key="Math.random()" v-if="this.AdvanceStatus.indexOf('Volume') != -1"  align="center">
          <el-table-column
            label="Name"
            width="350">
            <template slot-scope="scope">
              <!-- <div style="font-size:12px" v-html="scope.row.volumename"></div> -->
              <el-tooltip class="item" effect="dark" placement="top">
                <div v-html="scope.row.volumename" slot="content"></div>
                <div style="font-size:12px" v-html="scope.row.volumename1" ></div>
              </el-tooltip>
            </template>
          </el-table-column>
          <el-table-column
            label="status"
            width="75"
            show-overflow-tooltip>
            <template slot-scope="scope">
              <div style="font-size:12px" v-html="scope.row.volumestatus"></div>
            </template>
          </el-table-column>
          <el-table-column
            prop="volumesize"
            label="size"
            width="75"
            show-overflow-tooltip>
            <template slot-scope="scope">
              <div style="font-size:12px" v-html="scope.row.volumesize"></div>
            </template>
          </el-table-column>
          <el-table-column
            prop="volumetype"
            label="type"
            width="100"
            show-overflow-tooltip>
            <template slot-scope="scope">
              <div style="font-size:12px" v-html="scope.row.volumetype"></div>
            </template>
          </el-table-column>
          <el-table-column
            prop="volumebootable"
            label="bootable"
            width="85"
            show-overflow-tooltip>
            <template slot-scope="scope">
              <div style="font-size:12px" v-html="scope.row.volumebootable"></div>
            </template>
          </el-table-column>
        </el-table-column>
        <el-table-column
          prop="host"
          :key="Math.random()"
          v-if="this.AdvanceStatus.indexOf('Host') != -1" 
          show-overflow-tooltip
          width="180"
          label="Host">
        </el-table-column>
        <el-table-column
          prop="created_time"
          :key="Math.random()"
          v-if="this.AdvanceStatus.indexOf('Created Time') != -1" 
          label="Created Time"
          width="120"
          show-overflow-tooltip>
        </el-table-column>
        <el-table-column
          prop="tenant"
          label="Tenant"
          :key="Math.random()"
          v-if="this.AdvanceStatus.indexOf('Tenant') != -1" 
          width="120"
          show-overflow-tooltip>
        </el-table-column>
      </el-table>
    </div>
  </div>
</template>

<script>
import { getFilter,getTableData } from "@/api/vmView"
export default {
  name: 'vmView',
  data () {
    return {
      limit:20,
      offset:0,
      nowPage:1,
      dc_id:'',
      selectedDrop:'',
      selectedDrop1:'',
      filterStatus:false,
      query:'nova_name',
      filter:'',
      sort:'time',
      order:'desc',
      filterName:'nova_name',
      fName:'',
      fStatus:'',
      statusList:[
        {
          value:'ACTIVE',
          label:'ACTIVE'
        },
        {
          value:'BUILD',
          label:'BUILD'
        },
        {
          value:'SHUTOFF',
          label:'SHUTOFF'
        },
        {
          value:'PAUSED',
          label:'PAUSED'
        },
        {
          value:'SUSPENDED',
          label:'SUSPENDED'
        },
        {
          value:'RESCUE',
          label:'RESCUE'
        },
        {
          value:'ERROR',
          label:'ERROR'
        },
        {
          value:'RESIZE',
          label:'RESIZE'
        },
        {
          value:'SOFT_DELETED',
          label:'SOFT_DELETED'
        },
        {
          value:'HARD_DELETED',
          label:'HARD_DELETED'
        }
      ],
      fHost:'',
      fTenant:'',
      tenantList:[],
      fStack:'',
      stackList:[],
      tableData: [],
      total:0,
      multipleSelection:[],
      tableHeight:600,
      AdvanceStatus:['Flavor','Volume','Host','Created Time','Tenant'],
      AdvanceGroup:['Flavor','Volume','Host','Created Time','Tenant'],
      advanceS:false
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
    //控制table列
    showHideAdvance(){
      this.advanceS = !this.advanceS;
    },
    advanceOk(){
      this.AdvanceStatus = this.AdvanceGroup;
      this.advanceS = false;
      this.$nextTick(()=>{
        this.$refs.multipleTable.doLayout()
      })
    },
    advanceCancel(){
      this.AdvanceGroup = [];
      this.advanceS = false;
    },
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
        if(code == 200 && data && data.length>0){
          let {stack,tenant} = data[0];
          let tempStack = [],tempTenant = [];
          stack.forEach(ele => {
            tempStack.push(
              {
                value:ele.stack_id,
                label:ele.stack_name
              }
            )
          });
          tenant.forEach(ele => {
            tempTenant.push(
              {
                value:ele.tenant_id,
                label:ele.tenant_name
              }
            )
          });
          this.stackList = tempStack;
          this.tenantList = tempTenant;
        }
      })
    },
    //显示隐藏筛选条件
    showFilter(){
      this.filterStatus = !this.filterStatus;
    },
    //切换vm view 和 host view
    change(type){
      if(type == 1){
        this.$goRoute('/vmView');
      }else{
        this.$goRoute('/hostView');
      }
    },
    //筛选确定
    filterOk(){
      let _this = this;
      let {dc_id,limit,offset,query,sort,order} = this;
      if(query == 'nova_name'){
        this.filter = this.fName;
      }else if(query == 'nova_status'){
        this.filter = this.fStatus;
      }else if(query == 'nova_host'){
        this.filter = this.fHost;
      }else if(query == 'nova_tenant'){
        this.filter = this.fTenant;
      }else{
        this.filter = this.fStack;
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
        if(code == 200 && data && data.length>0){
          data.forEach(val=>{
            let {networks,volume} = val;
            val.created_time = _this.$util.formatDate((val.created_time)*1000,'yyyy-MM-dd HH:mm');
            val.flavor_memory = _this.$util.formatNmuber1(val.flavor_memory);
            //volume
            let tempbootable='-',tempname='-',tempname1='-',tempsize='-',tempstatus='-',temptype='-';
            if(volume && volume.length>0){
              volume.forEach(res=>{
                let {volume_bootable,volume_name,volume_size,volume_status,volume_type} = res;
                tempbootable = _this.$util.formatString(volume_bootable) + '<br/>' + tempbootable;
                tempname = _this.$util.formatString(volume_name) + '<br/>' + tempname;
                tempname1 = _this.$util.formatString(volume_name).substring(0.20)+'...' + '<br/>' + tempname1;
                tempsize = _this.$util.formatString(volume_size) + '<br/>' + tempsize;
                tempstatus = _this.$util.formatString(volume_status) + '<br/>' + tempstatus;
                temptype = _this.$util.formatString(volume_type) + '<br/>' + temptype;
              })
            };
            val.volumebootable = tempbootable;
            val.volumename = tempname;
            val.volumename1 = tempname1;
            val.volumesize = tempsize;
            val.volumestatus = tempstatus;
            val.volumetype = temptype;

            //networks
            let tempNetworks = '',tempNetworks1 = '';
            if(networks && networks && networks.length>0){
              networks.forEach(res=>{
                let {ip,name} = res;
                let temp =  name + ' = ' + ip;
                tempNetworks1 =  temp.substring(0,45)+'...' + '<br/>' + tempNetworks1;
                tempNetworks =  temp + '<br/>' + tempNetworks;
              })
            }
            val.oNetworks = tempNetworks;
            val.oNetworks1 = tempNetworks1;
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
    ToBreak (val) {
      return val.replace('\n', '<br />')
    },
    //筛选确定
    filterOk1(){
      let _this = this;
      let {dc_id,limit,offset,query,sort,order} = this;
      if(query == 'nova_name'){
        this.filter = this.fName;
      }else if(query == 'nova_status'){
        this.filter = this.fStatus;
      }else if(query == 'nova_host'){
        this.filter = this.fHost;
      }else if(query == 'nova_tenant'){
        this.filter = this.fTenant;
      }else{
        this.filter = this.fStack;
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
        if(code == 200 && data && data.length>0){
          data.forEach(val=>{
            let {networks,volume} = val;
            val.created_time = _this.$util.formatDate((val.created_time)*1000,'yyyy-MM-dd HH:mm');
            val.flavor_memory = _this.$util.formatNmuber1(val.flavor_memory);
            //volume
            // let tempbootable='-',tempname='-',tempsize='-',tempstatus='-',temptype='-';
            // if(volume && volume.length>0){
            //   volume.forEach(res=>{
            //     let {volume_bootable,volume_name,volume_size,volume_status,volume_type} = res;
            //     tempbootable = _this.$util.formatString(volume_bootable) + '<br/>' + tempbootable;
            //     tempname = _this.$util.formatString(volume_name) + '<br/>' + tempname;
            //     tempsize = _this.$util.formatString(volume_size) + '<br/>' + tempsize;
            //     tempstatus = _this.$util.formatString(volume_status) + '<br/>' + tempstatus;
            //     temptype = _this.$util.formatString(volume_type) + '<br/>' + temptype;
            //   })
            // };
            // val.volumebootable = tempbootable;
            // val.volumename = tempname;
            // val.volumesize = tempsize;
            // val.volumestatus = tempstatus;
            // val.volumetype = temptype;
            let tempbootable='-',tempname='-',tempname1='-',tempsize='-',tempstatus='-',temptype='-';
            if(volume && volume.length>0){
              volume.forEach(res=>{
                let {volume_bootable,volume_name,volume_size,volume_status,volume_type} = res;
                tempbootable = _this.$util.formatString(volume_bootable) + '<br/>' + tempbootable;
                tempname = _this.$util.formatString(volume_name) + '<br/>' + tempname;
                tempname1 = _this.$util.formatString(volume_name).substring(0.20)+'...' + '<br/>' + tempname1;
                tempsize = _this.$util.formatString(volume_size) + '<br/>' + tempsize;
                tempstatus = _this.$util.formatString(volume_status) + '<br/>' + tempstatus;
                temptype = _this.$util.formatString(volume_type) + '<br/>' + temptype;
              })
            };
            val.volumebootable = tempbootable;
            val.volumename = tempname;
            val.volumename1 = tempname1;
            val.volumesize = tempsize;
            val.volumestatus = tempstatus;
            val.volumetype = temptype;

            // //networks
            // let tempNetworks = '';
            // if(networks && networks && networks.length>0){
            //   networks.forEach(res=>{
            //     let {ip,name} = res;
            //     let temp =  name + ' = ' + ip;
            //     tempNetworks =  temp + '<br/>' + tempNetworks;
            //   })
            // }
            // val.oNetworks = tempNetworks;
            //networks
            let tempNetworks = '',tempNetworks1 = '';
            if(networks && networks && networks.length>0){
              networks.forEach(res=>{
                let {ip,name} = res;
                let temp =  name + ' = ' + ip;
                tempNetworks1 =  temp.substring(0,45)+'...' + '<br/>' + tempNetworks1;
                tempNetworks =  temp + '<br/>' + tempNetworks;
              })
            }
            val.oNetworks = tempNetworks;
            val.oNetworks1 = tempNetworks1;
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
      this.fName = '';
      this.fStatus = '';
      this.fHost = '';
      this.fTenant = '';
      this.fStack = '';
      this.sort = 'time';
      this.order = 'desc';
      this.selectedDrop = '';
      this.selectedDrop1 = '';
    },
    //切换tabs
    changeTabs(name){
      this.query = name;
    },
    //点击sorting by下拉菜单
    clickDropdown(name){
      let temp = name.split('_');
      this.sort = temp[0];
      this.order = temp[1];
      if(temp[1] == 'asc'){
        this.selectedDrop = 'time_asc'
      }else{
        this.selectedDrop = 'time_desc'
      }
      this.selectedDrop1 = '';
      this.filterOk();
    },
    clickDropdown1(name){
      let temp = name.split('_');
      this.sort = temp[0];
      this.order = temp[1];
      if(temp[1] == 'asc' && temp[0] == 'vcpu'){
        this.selectedDrop1 = 'vcpu_asc'
      }else if(temp[1] == 'desc' && temp[0] == 'vcpu'){
        this.selectedDrop1 = 'vcpu_desc'
      }else if(temp[1] == 'asc' && temp[0] == 'memory'){
        this.selectedDrop1 = 'memory_asc'
      }else if(temp[1] == 'desc' && temp[0] == 'memory'){
        this.selectedDrop1 = 'memory_desc'
      }else if(temp[1] == 'asc' && temp[0] == 'disk'){
        this.selectedDrop1 = 'disk_asc'
      }else{
        this.selectedDrop1 = 'disk_desc'
      }
      this.selectedDrop = '';
      this.filterOk();
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
        sessionStorage.setItem('vmViewIDs',JSON.stringify(multipleSelection));
        this.$goRoute('/vmViewDeatils')
      }
    }
  },
  beforeDestroy(){

  }
}
</script>

<style lang="scss">
  .vmView{
    .el-table--border td, .el-table--border th, .el-table__body-wrapper .el-table--border.is-scrolling-left~.el-table__fixed{
      border-right: none;
    }
    .el-table--border th, .el-table__fixed-right-patch{
      border-bottom: none;
    }
  }
  .vmView{
    .el-table td .cell{
      font-size: 12px !important;
    }
  }
</style>
<style scoped lang="scss">
  .vmView{
    width: 100%;
    height: 100%;
    .header{
      width: 100%;
      height: 55px;
      position: relative;
      .buttonBox{
        width: 100%;
        height: 55px;
        display: flex;
        align-items: center;
        .tabs{
          width: 12rem;
          height: 2rem;
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
        .advanceBox{
          position: absolute;
          right: 30px;
          cursor: pointer;
          .cBox{
            position: absolute;
            z-index: 9999;
            right: -25px;
            top: 40px;
            background: #fff;
            width: 150px;
            padding: 5px 0;
            border: 1px solid #ddd;
            .bt{
              margin-left: 5px;
            }
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
        border-bottom:1px dashed #dee0e4;
        display: flex;
        align-items: center;
        span:nth-child(1){
          font-size: 14px;
          font-weight: 500;
          width: 120px;
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
      .line:nth-last-child(1){
        border-bottom: none;
      }
      .line_l{
        height: 3rem;
        border-top: 1px dashed #dee0e4;
        .button{
          &:hover{
            border: 1px solid #409eff;
            color: #409eff;
          }
        }
      }
    }
    .sortBox{
      width: 100%;
      height: 30px;
      display: flex;
      align-items: center;
      margin-top: 5px;
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
        width: 130px;
        float: left;
        .ivu-dropdown{
          margin-right: 10px;
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

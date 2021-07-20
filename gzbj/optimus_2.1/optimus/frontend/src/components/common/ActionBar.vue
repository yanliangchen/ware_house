<template>
  <div class="ActionBar">
    <div class="title">
      <img src="/static/img/logo2.png" v-show="!controlStatus" />
      <span v-show="!controlStatus">OPTIMUS</span>
      <el-tooltip   content="Menu" placement="bottom" effect="light" v-show="controlStatus">
        <Icon type="md-list" class="menuList" size="20" @click="showDrawer" />
      </el-tooltip>
    </div>
    <div class="ebSystemBar-admin">
      <span class="el-dropdown-link" @click="clickNotification" v-show="controlStatus">
        <span class="user setting">
          <Icon type="ios-warning" style="margin-right: 1px;" />
        </span>
      </span>
      <span class="el-dropdown-link" @click="clickSet" v-show="controlStatus">
        <span class="user setting">
          <Icon type="ios-settings" />
        </span>
      </span>
      <el-dropdown>
        <span class="el-dropdown-link">
          <span class="user">
            <Icon type="ios-home" /> 
          </span>
        </span>
        <el-dropdown-menu slot="dropdown">
          <el-dropdown-item @click.native="YamlGenerator"><Icon type="ios-cube aIcon" size="16" />Yaml Generator</el-dropdown-item>
          <el-dropdown-item @click.native="Ericic"><Icon type="ios-construct aIcon" size="16" />EriCIC</el-dropdown-item>
          <el-dropdown-item @click.native="Setting"><Icon type="ios-exit aIcon" size="16" />Home</el-dropdown-item>
        </el-dropdown-menu>
      </el-dropdown>
      <a href="javascript:void(0)">
        <span class="user home" @click="signOut">
          <el-tooltip   content="Sign out" placement="bottom" effect="light">
            <Icon type="md-person"  />
          </el-tooltip>
        </span>
      </a>
    </div>
    <Modal
      class-name="vertical-center-modal modalNotifica"
      v-model="modalNotifica"
      transfer
      width="600px">
      <div class="title">
        Notification
      </div>
      <div class="content">
        <Tabs ref="tabs" :value="noName">
          <TabPane label="Status" name="oStatus">
            <div>
              dynamic task<span class="block"></span>{{statusData.dJop_id}}<span class="block"></span>will be synced at
              <span class="block"></span>"{{statusData.dTime}}"。
            </div>
            <div>
              static task<span class="block"></span>{{statusData.sJop_id}}<span class="block"></span>will be synced at
              <span class="block"></span>"{{statusData.sTime}}"。
            </div>
          </TabPane>
          <TabPane label="History" name="oHistory">
            <div v-for="(item,index) in historyList"  :key="index">
              {{item.task_name}}<span class="block"></span>is<span class="block"></span>{{item.status}} to synced action<span class="block"></span>{{item.time}}。
            </div>
            <div v-if="historyList.length==0">No data!</div>
          </TabPane>
      </Tabs>
      </div>
      <div class="soltFooter">
        <Button type="primary" @click="notificaOk()">OK</Button>
      </div>
    </Modal>
    <Modal
      class-name="vertical-center-modal modalSeting"
      v-model="modalSeting"
      width="600px">
      <div class="title">
        Setting
      </div>
      <div class="content">
        <div class="part">
          <div class="name">
            Auto-Update
          </div>
          <div class="describe">
            <span>Host/VM Info</span>
            <span>Infra/Tenant Stastic</span>
          </div>
          <div class="switch">
            <span class="sw">
              <el-switch
                v-model="dtask"
                active-color="#13ce66"
                inactive-color="#ff4949">
              </el-switch>
            </span>
            <span class="sw">
              <el-switch
                v-model="stask"
                active-color="#13ce66"
                inactive-color="#ff4949">
              </el-switch>
            </span>
          </div>
        </div>
        <div class="part part2">
          <div class="name">
            Update Interval
          </div>
          <div class="describe">
            <span>Host/VM Info</span>
            <span>Infra/Tenant Stastic</span>
          </div>
          <div class="switch">
            <span class="sw">
              <Select v-model="dinterval"  placeholder="" size="small" style="width:60px">
                <Option v-for="item in timeList" :value="item.value" :key="item.value">{{ item.label }}</Option>
              </Select>
              <span class="company">Min</span>
            </span>
            <span class="sw">
              <Select v-model="sinterval"  placeholder="" size="small" style="width:60px">
                <Option v-for="item in timeList" :value="item.value" :key="item.value">{{ item.label }}</Option>
              </Select>
              <span class="company">Min</span>
            </span>
          </div>
        </div>
        <div class="part part2">
          <div class="name">
            Auto-Update Period
          </div>
          <div class="describe">
            <span>Host/VM Info</span>
            <span>Infra/Tenant Stastic</span>
          </div>
          <div class="switch">
            <span class="sw">
              <span style="margin-left:5px;">Start</span>
              <Select v-model="dstart"  placeholder=""  size="small" style="width:60px">
                <Option v-for="item in timeList1" :value="item.value" :key="item.value">{{ item.label }}</Option>
              </Select>
              <span style="margin-left:5px;">End</span>
              <Select v-model="dend"  placeholder=""  size="small" style="width:60px">
                <Option v-for="item in timeList1" :value="item.value" :key="item.value">{{ item.label }}</Option>
              </Select>
            </span>
            <span class="sw">
              <span style="margin-left:5px;">Start</span>
              <Select v-model="sstart"  placeholder=""  size="small" style="width:60px">
                <Option v-for="item in timeList1" :value="item.value" :key="item.value">{{ item.label }}</Option>
              </Select>
              <span style="margin-left:5px;">End</span>
              <Select v-model="send"  placeholder=""  size="small" style="width:60px">
                <Option v-for="item in timeList1" :value="item.value" :key="item.value">{{ item.label }}</Option>
              </Select>
            </span>
          </div>
        </div>
      </div>
      <div class="soltFooter">
        <Button @click="setBack()">Cancel</Button>
        <Button type="primary" @click="setOk()" style="margin:0 15px 0  8px;">OK</Button>
      </div>
    </Modal>
    <Drawer title="" placement="left" width="200" :closable="false" v-model="drawerStatus">
      <p @click="jumpRouter('ToolSelection')">Home</p>
      <p @click="jumpRouter('Infrastrucure')">Infrastructure Status</p>
      <p @click="jumpRouter('tenant')">Tenant Status</p>
      <p @click="jumpRouter('vmView')">VM View</p>
      <p @click="jumpRouter('hostView')">Host View</p>
      <p @click="jumpRouter('record')">Record</p>
      <p @click="jumpRouter('history')">History/Download</p>
    </Drawer>
  </div>
</template>

<script>
import { getStatus,getSchedulerHistory,getSetting,setSeting } from "@/api/login"
export default {
  name: 'ActionBar',
  data () {
    return {
      status:0,
      controlStatus:false,
      drawerStatus:false,
      modalSeting:false,
      setStatus:false,
      modalNotifica:false,
      noName:'oStatus',
      timeList:[
        {
          value:'30',
          label:'30'
        },
        {
          value:'45',
          label:'45'
        },
        {
          value:'60',
          label:'60'
        },
        {
          value:'120',
          label:'120'
        }
      ],
      timeList1:[
        {
          value:'0',
          label:'0'
        },
        {
          value:'1',
          label:'1'
        },
        {
          value:'2',
          label:'2'
        },
        {
          value:'3',
          label:'3'
        },
        {
          value:'4',
          label:'4'
        },
        {
          value:'5',
          label:'5'
        },
        {
          value:'6',
          label:'6'
        },
        {
          value:'7',
          label:'7'
        },
        {
          value:'8',
          label:'8'
        },
        {
          value:'9',
          label:'9'
        },
        {
          value:'10',
          label:'10'
        },
        {
          value:'11',
          label:'11'
        },
        {
          value:'12',
          label:'12'
        },
        {
          value:'13',
          label:'13'
        },
        {
          value:'14',
          label:'14'
        },
        {
          value:'15',
          label:'15'
        },
        {
          value:'16',
          label:'16'
        },
        {
          value:'17',
          label:'17'
        },
        {
          value:'18',
          label:'18'
        },
        {
          value:'19',
          label:'19'
        },
        {
          value:'20',
          label:'20'
        },
        {
          value:'21',
          label:'21'
        },
        {
          value:'22',
          label:'22'
        },
        {
          value:'23',
          label:'23'
        }
      ],
      hostM:'30',
      infraM:'30',
      cid:'',
      statusData:{
        dJop_id :'  -  ',
        dTime : '  -  ',
        sJop_id :'  -  ',
        sTime :'  -  '
      },
      temphistoryList:[],
      historyList:[],
      dtask:false,
      stask:false,
      dinterval:'30',
      sinterval:'30',
      dstart:'0',
      dend:'0',
      sstart:'0',
      send:'0'
    }
  },
  mounted(){
    let _this = this;
    let dataCenterDetails = JSON.parse(sessionStorage.getItem('dataCenter'));
    if(dataCenterDetails){
      let {cee_version,data_center,id,name,Mode} = dataCenterDetails;
      this.cid = id;
    };
    this.$eventBus.$on('headerKey',res=>{
      if(res == 0){
        _this.controlStatus = false;
      }else{
        _this.controlStatus = true;
      }
    });
  },
  methods:{
    showDrawer(){
      this.drawerStatus = true;
    },
    jumpRouter(path){
      if(path == 'tenant'){
        this.$eventBus.$emit('vmViewS',1);
        sessionStorage.setItem('vmViewS',1);
      }else{
        this.$eventBus.$emit('vmViewS',0);
        sessionStorage.setItem('vmViewS',0);
      }
      this.$goRoute(`/${path}`);
      this.drawerStatus = false;
    },
    //切换到Tool Selection页
    Setting(){
      this.$goRoute('/ToolSelection');
    },
    //切换到YamlGenerator页
    YamlGenerator(){
      this.$goRoute('/YamlGenerator');
    },
    //切换到Ericic页
    Ericic(){
      this.controlStatus = false;
      this.$goRoute('/Ericic');
    },
    //退出登录
    signOut(e){
      this.$goRoute('/Login');
      sessionStorage.clear();
    },
    //setting
    clickSet(){
      this.getSettingData();
      this.modalSeting = true;
    },
    async getSettingData(){
      let dataCenterDetails = JSON.parse(sessionStorage.getItem('dataCenter'));
      if(dataCenterDetails){
        let {id} = dataCenterDetails;
        this.cid = id;
      };
      let {cid} = this;
      let res  = await getStatus(cid);
      let {code,data} = res.data;
      if(code == 200 && data  && data.length>0){
        let {cid,dynamic_task,static_task} = data[0];
        if(dynamic_task && dynamic_task.end){
          this.dtask = dynamic_task.next_run_time == null ? false : true;
          this.dinterval = String((dynamic_task.interval)/60);
          this.dstart = String((dynamic_task.start)/3600);
          this.dend = String((dynamic_task.end)/3600);
        }
        if(static_task && static_task.end){
          this.stask = static_task.next_run_time == null ? false : true;
          this.sinterval = String((static_task.interval)/60);
          this.sstart = String((static_task.start)/3600);
          this.send = String((static_task.end)/3600);
        }
      }
    },
    async setOk(){
      let dataCenterDetails = JSON.parse(sessionStorage.getItem('dataCenter'));
      if(dataCenterDetails){
        let {id} = dataCenterDetails;
        this.cid = id;
      };
      let {cid,dtask,stask,dinterval,sinterval,dstart,dend,sstart,send} = this;
      let params = {
        cid:cid,
        interval:Number(sinterval)*60,
        task:"static",
        start:Number(sstart)*3600,
        end:Number(send)*3600,
        action:stask ? "resume" :'pause'
      };
      
      let params1 = {
        cid:cid,
        interval:Number(dinterval)*60,
        task:"dynamic",
        start:Number(dstart)*3600,
        end:Number(dend)*3600,
        action:dtask ? "resume" :'pause'
      };
      let res = await setSeting(params);
      let res1 = await setSeting(params1);
      if(res.data.code == 201 && res1.data.code == 201){
        this.$Message.success({
          duration: 2.5,
          content: 'Set successfully!'
        });
        this.modalSeting = false;
      }else{
        this.$Message.error({
          duration: 2.5,
          content: 'Set failed!'
        });
      }
    },
    setBack(){
      this.modalSeting = false;
    },

    //Notification
    clickNotification(){
      let _this = this;
      this.$refs.tabs.activeKey = 'oStatus';
      let dataCenterDetails = JSON.parse(sessionStorage.getItem('dataCenter'));
      if(dataCenterDetails){
        let {id} = dataCenterDetails;
        this.cid = id;
      };
      let {cid} = this;
      getStatus(cid).then(res=>{
        let {code,data} = res.data;
        if(code == 200 && data && data.length>0){
          let {dynamic_task,static_task} = data[0];
          let temp = {
            dJop_id :dynamic_task != null ? dynamic_task.job_id : '  -  ',
            dTime : dynamic_task != null ?  dynamic_task.next_run_time : '  -  ',
            sJop_id : static_task != null ?  static_task.job_id : '  -  ',
            sTime : static_task != null ?  static_task.next_run_time : '  -  '
          }
          this.statusData = temp;
        }
      });
      let params={
        cid:cid,
        filter:'static',
        limit:10,
        offset:0
      };
      getSchedulerHistory(params).then(res=>{
        let {code,data,total_num} = res.data;
        if(code == 200 && data){
          _this.temphistoryList = data;
        }
      });
      let params1={
        cid:cid,
        filter:'dynamic',
        limit:10,
        offset:0
      };
      
      getSchedulerHistory(params1).then(res=>{
        let {code,data,total_num} = res.data;
        if(code == 200 && data){
          let temp  = _this.temphistoryList;
          let temp1 = temp.concat(data);
          temp1.forEach(res=>{
            res.time = _this.$util.formatDate((res.timestamp)*1000,'yyyy-MM-dd HH:mm');
          });
          _this.historyList = temp1;
        }
      })
      this.modalNotifica = true;
    },
    notificaOk(){
      this.modalNotifica = false;
    }
  },
  destroyed(){
    this.$eventBus.$off('headerKey');
  }
}
</script>
<style lang="scss">
  .ActionBar{
    .el-dropdown-menu{
      padding: 0 !important;
      box-shadow: 0 2px 6px rgba(0,0,0,.2)
    }
  }
  .modalSeting{
    color: #000;
    .title{
      height: 25px;
      width: 100%;
      font-size: 1rem;
      font-weight: 600;
    }
    .content{
      min-height: 1.5rem;
      width: 100%;
      color: #000;
      margin-top: 5px;
      margin-bottom: 15px;
      .part{
        width: 100%;
        height: 60px;
        .name{
          font-weight: 600;
          margin: 0 15px 0 10px;
          width: 140px;
          height: 60px;
          padding-top: 5px;
          float: left;
        }
        .describe{
          height: 100%;
          width: 150px;
          line-height: 30px;
          font-size: .55rem;
          float: left;
          span{
            display: inline-block;
            height: 30px;
            line-height: 30px;
          }
        }
        .switch{
          margin: 0 .5rem;
          height: 60px;
          width: 200px;
          float: left;
          .sw{
            height: 30px;
            line-height: 30px;
            display: inline-block;
            width: 200px;
            padding-top: 5px;
          }
          .company{
            margin-left:5px;
            position: relative;
          }
        }
      }
      .part2{
        margin-top: 5px;
      }
    }
  }
  .modalNotifica{
    color: #000;
    .title{
      height: 25px;
      width: 100%;
      font-size: 1rem;
      font-weight: 600;
    }
    .content{
      min-height: 10rem;
      margin-top: 5px;
      .ivu-tabs-tabpane{
        color: #000;
        max-height: 200px;
        overflow-y: auto;
      }
      .block{
        display: inline-block;
        width: 7px;
        height: 5px;
      }
    }
  }
  .ivu-drawer-content{
    z-index: 99999999999999999;
    .ivu-drawer-body{
      p{
        cursor: pointer;
        height: 25px;
        line-height: 25px;
        &:hover{
          color: #409eff;
        }
      }
    }
  }
</style>
<style scoped lang="scss">
  .ActionBar{
    width: 100%;
    height: 2.5rem;
    display: flex;
    align-items: center;
    padding: 0 1rem;
    border-bottom: 0;
    background: #4259C1;
    .title{
      font-weight: 500;
      color: #fff;
      display: flex;
      justify-content: center;
      align-items: center;
      img{
        width: 22px;
      }
      span{
        font-size: 1.1rem;
        margin-left: 10px;
      }
      .menuList{
        cursor: pointer;
        &:hover{
          color: #2b85e4;
        }
      }
    }
    .home{
      margin: 0 3px;
    }
    .setting{
      margin-right: 5px;
    }
    .user{
      width: 20px;
      height: 20px;
      display: inline-block;
      border-radius: 12px;
      background: #fff;
      text-align: center;
      line-height:16px ;
      padding-left: 1px;
      .ivu-icon{
        color:#1890ff;
      }
    }
    .ActionBar_btn{
      cursor: pointer;
      display: flex;
      align-items: center;
      color: #465AB0;
    }
    .ebSystemBar-admin{
      position: absolute;
      top: 10px;
      right: 0.5rem;
      cursor: pointer;
      .aIcon{
        margin-right:10px;
      }
    }
  }
</style>

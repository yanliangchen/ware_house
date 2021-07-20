<template>
  <div class="record">
    <div class="box">
      <div class="name">
        <span>Record</span>
      </div>
      <div class="nameBox">
        <span>name</span>
        <Input v-model="cName" placeholder="" style="width: 300px" />
        <Button class="button" @click="save">save</Button>
      </div>
      <div class="title">
        <Icon size="20" type="ios-information-circle" />
        <span>Datacenter Information</span>
      </div>
      <div class="content">
        <ul>
          <li>
            <span>Datacenter</span>
            <span>{{datacenter}}</span>
          </li>
          <li>
            <span>CEE Version</span>
            <span>{{ceeversion}}</span>
          </li>
          <li>
            <span>LCM IP</span>
            <span>{{lcmip}}</span>
          </li>
          <li>
            <span>System Name</span>
            <span>{{systemname}}</span>
          </li>
          <li>
            <span>rc file</span>
            <span>{{rcfile}}</span>
          </li>
        </ul>
      </div>
    </div>
  </div>
</template>

<script>
import { getRecord,saveRecord } from "@/api/ericic"
export default {
  name: 'record',
  data () {
    return {
      name:'',
      cid:'',
      datacenter:'',
      ceeversion:'',
      lcmip:'',
      systemname:'',
      rcfile:'',
      cName:''
    }
  },
  mounted(){
    let dataCenter  = JSON.parse(sessionStorage.getItem('dataCenter'));
    let {data_center,system_name,name,cee_version,lcm_ip,openstackrc_dir,id} = dataCenter;
    this.datacenter = data_center;
    this.ceeversion = cee_version;
    this.lcmip = lcm_ip;
    this.systemname = system_name;
    this.rcfile = openstackrc_dir;
    this.name = name;
    this.cid = id;
  },
  methods:{
    save(){
      let _this = this;
      let {cName} = this;
      if(cName.trim() == ''){
        this.$Message.warning({
          duration: 2.5,
          content: 'Name is required !'
        });
      }else{
        let {cName,cid} = this;
        let params={
          name:cName,
          cid:cid
        };
        saveRecord(params).then(res=>{
          let {code} = res.data;
          if(code == 201){
             _this.$Message.success({
              duration: 2.5,
              content: 'Saved successfully'
            });
            _this.$goRoute('/history');
          }else{
            _this.$Message.error({
              duration: 2.5,
              content: 'Save failed!'
            });
          }
        })
      }
    }
  }
}
</script>

<style scoped lang="scss">
  .record{
    width: 100%;
    height: 100%;
    color: #000;
    .box{
      padding: 10px;
      .name{
        width: 100%;
        height: 40px;
        line-height: 40px;
        padding-left: 25px;
        padding-top: 5px;
        span{
          font-size: 20px;
          font-weight: 600;
        }
      }
      .nameBox{
        font-size: 16px;
        font-weight: 600;
        width: 100%;
        height: 50px;
        line-height: 50px;
        padding-left: 35px;
        .button{
          margin-left: 10px;
        }
      }
      .title{
        padding: 10px 0 10px 35px;
        span{
          font-size: 16px;
          font-weight: 600;
          position: relative;
          top: 2px;
        }
      }
      .content{
        width: 700px;
        padding: 0 45px;
        ul{
          padding: 10px 0;
          li{
            height: 30px;
            border-bottom: 1px solid #ddd;
            line-height: 30px;
            span:nth-child(1){
              font-size: 13px;
              font-weight: 600;
              width: 120px;
              display: inline-block;
            }
          }
        }
      }
    }
  }
</style>

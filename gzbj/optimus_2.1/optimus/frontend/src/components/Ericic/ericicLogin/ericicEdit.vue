<template>
  <div class="ericicEdit">
    <div class="tableBox">
      <el-form :model="ruleForm" :rules="rules" ref="ruleForm" label-position="left" label-width="160px" class="demo-ruleForm">
        <el-form-item label="Name" prop="name">
          <el-input v-model="ruleForm.name" size="small" disabled></el-input>
        </el-form-item>
        <el-form-item label="Mode" prop="Mode">
          <el-select size='small' style="width:100%" @change="changeMode" v-model="ruleForm.Mode" placeholder="">
            <el-option label="online" value="1"></el-option>
            <el-option label="offline" value="0"></el-option>
          </el-select>
        </el-form-item>
        <el-form-item label="Country/Province/City" prop="location">
          <el-input v-model="ruleForm.location" size="small"></el-input>
        </el-form-item>
        <el-form-item label="SystemName" prop="SystemName">
          <el-input v-model="ruleForm.SystemName" size="small"></el-input>
        </el-form-item>
        <el-form-item label="CEE version" prop="cee_version">
          <el-select size='small' style="width:100%" v-model="ruleForm.cee_version" placeholder="Please select">
            <el-option v-for="item in ceeList" :value="item.value" :key="item.value">{{ item.label }}</el-option>
          </el-select>
          <!-- <el-input v-model="ruleForm.cee_version" size="small"></el-input> -->
        </el-form-item>
        <el-form-item label="LCM IP" prop="lcm_ip">
          <el-input v-model="ruleForm.lcm_ip" size="small" :disabled="disabledBtn"></el-input>
        </el-form-item>
        <el-form-item label="LCM Usr" prop="lcm_user">
          <el-input v-model="ruleForm.lcm_user" size="small" :disabled="disabledBtn"></el-input>
        </el-form-item>
        <el-form-item label="LCM Pwd" prop="lcm_pwd">
          <el-input v-model="ruleForm.lcm_pwd" size="small" :disabled="disabledBtn"></el-input>
        </el-form-item>
        <el-form-item label="openstackrc dir" prop="openrc_dir">
          <el-input v-model="ruleForm.openrc_dir" size="small" :disabled="disabledBtn"></el-input>
        </el-form-item>
        <el-form-item label="lcmrc dir" prop="lcmrc_dir">
          <el-input v-model="ruleForm.lcmrc_dir" size="small" :disabled="disabledBtn"></el-input>
        </el-form-item>
        <el-form-item style="text-align:right;">
          <el-button  size="small"  type="primary" style="margin-right:10px;" :disabled="disabledBtn || verifyDisabled" @click="connectionVerify">Verify connection</el-button>
          <el-button  size="small" style="width:70px;" type="primary" @click="Save()">Save</el-button>
          <el-button  size="small" style="width:70px;" @click="Cancel()">Cancel</el-button>
        </el-form-item>
      </el-form>
    </div>
  </div>
</template>
<script>
import { data_center_show,data_center_edit,verifyConnection } from "@/api/ericic"
export default {
  name: 'ericicEdit',
  data () {
    return {
      // ceeList:[
      //   {
      //     value:'drop22',
      //     label:'drop22'
      //   },
      //   {
      //     value:'drop25',
      //     label:'drop25'
      //   },
      //   {
      //     value:'drop26',
      //     label:'drop26'
      //   },
      //   {
      //     value:'drop28',
      //     label:'drop28'
      //   },
      //   {
      //     value:'drop35',
      //     label:'drop35'
      //   }
      // ],
      ceeList:[
        {
          value:'CEE neXt',
          label:'CEE neXt'
        }
      ],
      ruleForm: {
        name: '',
        Mode:'',
        location:'',
        SystemName:'',
        cee_version:'',
        lcm_ip:'',
        lcm_pwd:'',
        lcm_user:'',
        openrc_dir:'',
        lcmrc_dir:''
      },
      rulesOnline: {
        name: [
          { required: true, trigger: 'blur' }
        ],
        location: [
          { required: true, trigger: 'blur' }
        ],
        Mode: [
          { required: true, trigger: 'change' }
        ],
        SystemName: [
          { required: true, trigger: 'change' }
        ],
        cee_version: [
          { required: true, trigger: 'change' }
        ],
        lcm_ip: [
          { required: true, trigger: 'blur' }
        ],
        lcm_user: [
          { required: true, trigger: 'blur' }
        ],
        lcm_pwd: [
          { required: true, trigger: 'blur' }
        ],
        openrc_dir: [
          { required: true, trigger: 'blur' }
        ],
        lcmrc_dir: [
          { required: true, trigger: 'blur' }
        ]
      },
      rulesOffline: {
        name: [
          { required: true, trigger: 'blur' }
        ],
        Mode: [
          { required: true, trigger: 'blur' }
        ],
        SystemName: [
          { required: true, trigger: 'change' }
        ],
        location: [
          { required: true, trigger: 'blur' }
        ],
        cee_version: [
          { required: true, trigger: 'blur' }
        ],
        lcm_ip: [
          { required: false, trigger: 'blur' }
        ],
        lcm_user: [
          { required: false, trigger: 'blur' }
        ],
        lcm_pwd: [
          { required: false, trigger: 'blur' }
        ],
        openrc_dir: [
          { required: false, trigger: 'blur' }
        ],
        lcmrc_dir: [
          { required: false, trigger: 'blur' }
        ]
      },
      rules:{
        name: [
          { required: true, trigger: 'blur' }
        ],
        location: [
          { required: true, trigger: 'blur' }
        ],
        Mode: [
          { required: true, trigger: 'change' }
        ],
        SystemName: [
          { required: true, trigger: 'change' }
        ],
        cee_version: [
          { required: true, trigger: 'change' }
        ],
        lcm_ip: [
          { required: true, trigger: 'blur' }
        ],
        lcm_user: [
          { required: true, trigger: 'blur' }
        ],
        lcm_pwd: [
          { required: true, trigger: 'blur' }
        ],
        openrc_dir: [
          { required: true, trigger: 'blur' }
        ],
        lcmrc_dir: [
          { required: true, trigger: 'blur' }
        ]
      },
      disabledBtn:false,
      verifyDisabled:false,
      Mode:0
    }
  },
  mounted(){
    let {id} = JSON.parse(sessionStorage.getItem('dataCenter'));
    this.getShow(id);
    let {Mode} = this.ruleForm;
    if(Mode == 'online'){
      this.disabledBtn = false;
    }else{
      this.disabledBtn = true;
    }
  },
  methods:{
    //改变 Mode
    changeMode(mode){
      this.Mode = mode;
      if(mode == 0){
        this.rules = this.rulesOffline;
        this.disabledBtn = true;
      }else{
        this.rules = this.rulesOnline;
        this.disabledBtn = false;
      }
    },
    Cancel(){
      this.$goRoute('/ericicShow');
    },
    //保存
    Save(type){
      let _this = this;
      let {id} = JSON.parse(sessionStorage.getItem('dataCenter'));
      let {name,Mode,SystemName,cee_version,lcm_ip,lcm_pwd,lcm_user,lcmrc_dir,openrc_dir,location} = this.ruleForm;
      let tempLocation = location.split('/');
      let params = {
        id: id,
        name: name,
        mode:Mode == '1' || Mode == 'online' ? true : false,
        country: tempLocation[0],
        province: tempLocation[1],
        city: tempLocation[2],
        system_name:SystemName,
        cee_version: cee_version,
        lcm_ip: lcm_ip,
        lcm_user: lcm_user,
        lcm_pwd: lcm_pwd,
        openstackrc_dir:openrc_dir,
        lcmrc_dir: lcmrc_dir
      };
      this.$refs.ruleForm.validate((valid) => {
        if (valid) {
          data_center_edit(params).then(res=>{
            let {code,message} = res.data;
            if(code == 200){
              _this.$Message.success({
                duration: 2.5,
                content: 'modified success!'
              });
              
              if(_this.Mode == 0){
                _this.disabledBtn = true;
              }else{
                _this.disabledBtn = false;
              }
              _this.getShow(id);
              //_this.$goRoute('/ericicLogin');
            }else{
              _this.$Message.error({
                duration: 2.5,
                content: 'modified failed!'
              });
            }
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
        } else {
          return false;
        }
      });
    },
    //connectionVerify
    connectionVerify(){
      let _this = this;
      this.verifyDisabled = true;
      let {lcm_ip,lcm_pwd,lcm_user} = this.ruleForm;
      let params = {
        lcm_ip: lcm_ip,
        lcm_user: lcm_user,
        lcm_pwd: lcm_pwd,
      }
      verifyConnection(params).then(res=>{
        let {code,data,message} = res.data;
        this.verifyDisabled = false;
        if(code == 200){
          if(data){
            _this.$Message.success({
              duration: 2.5,
              content: 'connect success!'
            });
          }else{
            _this.$Message.error({
              duration: 2.5,
              content: message
            });
          }
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
    async getShow(id){
      let res = await data_center_show(id);
      let {code} = res.data;
      if(code == 200){
        let {mode,cee_version,country,province,city,system_name,lcm_ip,id,lcm_pwd,lcm_user,name,openstackrc_dir,lcmrc_dir} =  res.data.data;
        this.ruleForm.Mode = mode ? 'online' : 'offline';
        this.ruleForm.cee_version = cee_version;
        this.ruleForm.location = country + '/' + province + '/' + city;
        this.ruleForm.lcm_ip = lcm_ip;
        this.ruleForm.lcm_pwd = lcm_pwd;
        this.ruleForm.lcm_user = lcm_user;
        this.ruleForm.openrc_dir = openstackrc_dir;
        this.ruleForm.name = name;
        this.ruleForm.SystemName = system_name;
        this.ruleForm.lcmrc_dir = lcmrc_dir;
        if(!mode){
          this.rules = this.rulesOffline;
          this.disabledBtn = true;
        }else{
          this.rules = this.rulesOnline;
          this.disabledBtn = false;
        };
        sessionStorage.setItem('dataCenter',JSON.stringify(res.data.data))
      }
    }
  }
}
</script>

<style scoped lang="scss">
  .ericicEdit{
    width: 100%;
    height: calc(100% - 3rem);
    padding: 1rem 14rem;
    background-color: #F9FAFF;
  }
</style>

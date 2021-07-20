<template>
  <div class="ericicShow">
    <div class="tableBox">
      <el-form :model="ruleForm"  ref="ruleForm" label-position="left" label-width="160px" class="demo-ruleForm">
        <el-form-item label="Name" prop="name">
          <el-input v-model="ruleForm.name" size="small" disabled></el-input>
        </el-form-item>
        <el-form-item label="Mode" prop="Mode">
          <el-select size='small' style="width:100%" disabled v-model="ruleForm.Mode" placeholder="">
            <el-option label="online" value="online"></el-option>
            <el-option label="offline" value="offline"></el-option>
          </el-select>
        </el-form-item>
        <el-form-item label="Country/Province/City" prop="location">
          <el-input v-model="ruleForm.location" size="small" disabled></el-input>
        </el-form-item>
        <el-form-item label="SystemName" prop="SystemName">
          <el-input v-model="ruleForm.SystemName" size="small" disabled></el-input>
        </el-form-item>
        <el-form-item label="CEE version" prop="cee_version">
          <el-input v-model="ruleForm.cee_version" size="small" disabled></el-input>
        </el-form-item>
        <el-form-item label="LCM IP" prop="lcm_ip">
          <el-input v-model="ruleForm.lcm_ip" size="small" disabled></el-input>
        </el-form-item>
        <el-form-item label="LCM Usr" prop="lcm_user">
          <el-input v-model="ruleForm.lcm_user" size="small" disabled ></el-input>
        </el-form-item>
        <el-form-item label="LCM Pwd" prop="lcm_pwd">
          <el-input v-model="ruleForm.lcm_pwd" size="small" disabled></el-input>
        </el-form-item>
        <el-form-item label="openstackrc dir" prop="openrc_dir">
          <el-input v-model="ruleForm.openrc_dir" size="small" disabled></el-input>
        </el-form-item>
        <el-form-item label="lcmrc dir" prop="lcmrc_dir">
          <el-input v-model="ruleForm.lcmrc_dir" size="small" disabled></el-input>
        </el-form-item>
        <el-form-item style="text-align:right;">
          <el-button  size="small" style="width:70px;" type="primary" @click="edit()">edit</el-button>
          <el-button  size="small" style="width:70px;" @click="back()">back</el-button>
        </el-form-item>
      </el-form>
    </div>
  </div>
</template>
<script>
import { data_center_show,data_center_edit } from "@/api/ericic"
export default {
  name: 'ericicShow',
  data () {
    return {
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
      }
    }
  },
  mounted(){
    let dataCenter = sessionStorage.getItem('dataCenter');
    this.getShow(dataCenter);
  },
  methods:{
    edit(){
      this.$goRoute('/ericicEdit');
    },
    back(){
      this.$goRoute('/ericicLogin');
    },
    getShow(dataCenter){
      let {mode,cee_version,country,province,city,system_name,lcm_ip,id,lcm_pwd,lcm_user,name,openstackrc_dir,lcmrc_dir} =  JSON.parse(dataCenter);
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
    }
  }
}
</script>

<style scoped lang="scss">
  .ericicShow{
    width: 100%;
    height: calc(100% - 3rem);
    padding: 1rem 14rem;
    background-color: #F9FAFF;
  }
</style>

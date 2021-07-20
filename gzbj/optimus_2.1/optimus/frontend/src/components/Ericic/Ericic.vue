<template>
  <div class="Ericic">
    <div class="main_content" :style='style'>
      <Action-bar></Action-bar>
      <div class="contentBox">
        <router-view></router-view>
      </div>
    </div>
  </div>
</template>

<script>
import ActionBar from '@/components/common/ActionBar'
export default {
  components:{
    ActionBar
  },
  name: 'Ericic',
  data () {
    return {
      msg:{
        title:'Ericic',
        describe:'NFVI Resource Checker',
        icon:'ios-stats'
      },
      status:0
    }
  },
  computed:{
    style(){
      let {status} = this;
      return{
        width:status?'100%':'100%'
      }
    }
  },
  mounted(){
    let dataCenterDetails = JSON.parse(sessionStorage.getItem('dataCenter'));
    if(dataCenterDetails){
      if(this.$route.name == 'ericicLogin'){
        this.$eventBus.$emit('headerKey',0);//控制表头按钮显示
      }else{
        this.$eventBus.$emit('headerKey',1);//控制表头按钮显示
      }
      
    };
  },
}
</script>

<style scoped lang="scss">
  .Ericic{
    width: 100%;
    height: 100%;
    .main_content{
      transition: all 0.2s ease;
      // width: calc(100% - 200px);
      height: 100%;
      float: right;
      .contentBox{
        width: 100%;
        height: calc(100% - 2.5rem);
        // padding: 0 2rem;
        overflow: auto;
        // background-color: #F9FAFF;
      }
    }
  }
</style>

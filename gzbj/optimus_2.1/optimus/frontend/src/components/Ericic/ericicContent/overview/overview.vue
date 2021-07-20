<template>
  <div class="overview">
    <div class="header">
      <div class="tabs">
        <div @click="change(1)" :class="{ 'activedBut': isActive }">Infra Resource</div>
        <div>|</div>
        <div @click="change(0)" :class="{ 'activedBut': !isActive }">Tenant Quota</div>
      </div>
    </div>
    <div class="content">
      <router-view></router-view>
    </div>
  </div>
</template>

<script>
export default {
  name: 'overview',
  data () {
    return {
      isActive:true
    }
  },
  mounted(){
    let _this = this;
    this.$eventBus.$on('vmViewS',res=>{
      if(res == 1){
        _this.isActive = false;
      }else{
        _this.isActive = true;
      }
    });
    let s = sessionStorage.getItem('vmViewS');
    if(s == 1){
      _this.isActive = false;
    }else{
      _this.isActive = true;
    }
  },
  methods:{
    change(type){
      if(type == 1){
        this.isActive = true;
        this.$goRoute('/Infrastrucure');
      }else{
        this.isActive = false;
        this.$goRoute('/tenant');
      }
    }
  },
  beforeDestroy(){
    this.$eventBus.$off('vmViewS');
  }
}
</script>

<style scoped lang="scss">
  .overview{
    width: 100%;
    height: 100%;
    .header{
      width: 100%;
      height: 50px;
      line-height: 50px;
      padding-top: 5px;
      .activedBut{
        font-weight: 500;
        color: #409eff;
      }
      .tabs{
        width: 190px;
        height: 28px;
        border: 1px solid #ddd;
        border-radius: 3px;
        position: relative;
        top: 6px;
        left: 10px;
        div{
          font-size: .7rem;
          width: 89px;
          float: left;
          height: 26px;
          line-height: 26px;
          text-align: center;
          font-weight: 400;
          cursor: pointer;
        }
        div:nth-child(2){
          width: 10px;
          text-align: center;
        }
      }
    }
    .content{
      width: 100%;
      height: calc(100% - 51px);
      border-top: 1px solid #ddd;
    }
  }
</style>

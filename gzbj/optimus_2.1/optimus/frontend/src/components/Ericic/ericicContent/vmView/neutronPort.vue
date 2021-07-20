<template>
  <div class="neutronPort">
    <div class="box">
      <div class="name">
        <span>Neutron Port</span>
        <Button class="button" @click="back">back</Button>
      </div>
      <div class="title">
        Port Information
      </div>
      <div class="content">
        <ul>
          <li>
            <span>ID</span>
            <span>{{idName}}</span>
          </li>
          <li>
            <span>Name</span>
            <span>{{idName}}</span>
          </li>
          <li>
            <span>IP Address</span>
            <span>{{idName}}</span>
          </li>
          <li>
            <span>MAC</span>
            <span>{{idName}}</span>
          </li>
          <li>
            <span>vif_type</span>
            <span>{{idName}}</span>
          </li>
          <li>
            <span>vhostuser</span>
            <span>{{idName}}</span>
          </li>
        </ul>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'neutronPort',
  data () {
    return {
      idName:'1'
    }
  },
  methods:{
    back(){
      this.$goRoute('/vmViewDeatils')
    }
  }
}
</script>

<style scoped lang="scss">
  .neutronPort{
    width: 100%;
    height: 100%;
    color: #000;
    .box{
      .name{
        font-size: 16px;
        font-weight: 600;
        width: 100%;
        height: 50px;
        line-height: 50px;
        padding-left: 10px;
        position: relative;
        .button{
          position: absolute;
          right: 10px;
          top: 9px;
        }
      }
      .title{
        font-size: 16px;
        font-weight: 600;
        padding-left: 30px;
      }
      .content{
        width: 100%;
        padding: 0 35px;
        ul{
          padding: 10px 0;
          li{
            height: 30px;
            border-bottom: 1px solid #ddd;
            line-height: 30px;
            span:nth-child(1){
              font-size: 13px;
              font-weight: 600;
              width: 80px;
              display: inline-block;
            }
          }
        }
      }
    }
  }
</style>

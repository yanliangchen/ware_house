<template>
  <div class="YamlGenerator">
    <div class="main_content" :style='style'> 
      <Action-bar></Action-bar>
      <yaml-content></yaml-content>
    </div>
  </div>
</template>

<script>
import ActionBar from '@/components/common/ActionBar'
import yamlContent from '@/components/YamlGenerator/yamlContent'
export default {
  components:{
    ActionBar,
    yamlContent
  },
  name: 'YamlGenerator',
  data () {
    return {
      msg:{
        title:'CONFIG',
        describe:'Yaml Generator',
        icon:'md-settings'
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
  mounted(){},
  methods:{

  }
}
</script>

<style scoped lang="scss">
  .YamlGenerator{
    width: 100%;
    height: 100%;
    .main_content{
      transition: all 0.2s ease;
      // width: calc(100% - 200px);
      height: 100%;
      float: right;
    }
  }
</style>

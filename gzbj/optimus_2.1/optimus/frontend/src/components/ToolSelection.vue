<template>
  <div class="ToolSelection">
    <div class="selectTitle">
      <div class="selectBg">
        <div>OPTIMUS</div>
        <span>CEE neXt automation tools.</span>
      </div>
    </div> 
    <div class="selectBox">
        <div class="part" v-for="(item,index) in items" :key="index" :value="item.vaue" @click="changePart(item)">
          <div class="content">
            <div>{{item.title}}</div>
            <div>{{item.content}}</div>
          </div>
          <div class="img"  :style="{ 'background-image': 'url(../../static/img/' + item.src + '.jpg)'}"></div>
        </div>
        <div class="part1"></div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'ToolSelection',
  data () {
    return {
      items:[
        {
          title:'Yaml Generator',
          path:'YamlGenerator',
          src:'bg2',
          content:'Design: Generator CEE neXt yaml files.'
        },
        {
          title:'EriCIC',
          path:'ericic',
          src:'bg1',
          content:'Maintenance: Monitor & Summary CEE neXt services and VNF status.'
        },
        {
          title:'Scripts Runtime (in progress)',
          path:'toolBox',
          src:'bg3',
          content:'Integration: Run-time environment for CEE neXt integration related tools.'
        }
      ]
    }
  },
  mounted(){

  },
  methods:{
    changePart(item){
      let path = item.path;
      this.$goRoute(`/${path}`);
    }
  }
}
</script>
<style scoped lang="scss">
  .ToolSelection{
    width: 100%;
    height: 100vh;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    padding:0;
    z-index: 9999;
    background-color: rgb(31, 41, 90);

    .selectTitle{
      width: 100%;
      height: 40%;
      padding: 1.5rem 3rem;
      .selectBg{
        width: 100%;
        height: 100%;
        padding: 2rem 4rem 0 4rem;
        background-image: url(../../static/img/timg.jpg);
        background-repeat: no-repeat;
        background-size: 100% auto;
        border-radius: 4px;
        color: #fff;
        div{    
          font-size: 2.125rem;
          font-family: "Roboto", "Helvetica", "Arial", sans-serif;
          font-weight: 400;
          line-height: 1.235;
          letter-spacing: 0.00735em;
          margin: 1rem 0 2.49rem 0;
        }
        span{
          font-size: 1.08rem;
        }
      }
    }
    .selectBox{
      background-color: #F9FAFF;
      width: 100%;
      height: 60%;
      display: flex;
      justify-content: center;
      flex-wrap: wrap;
      .part{
        width: calc(50% - 4rem);
        cursor: pointer;
        height: 40%;
        margin: 1rem 1rem 0 1rem;
        display: flex;
        background-color: #fff;
        border-radius: 2px;
        box-shadow: 0 3px 1px -2px rgba(0,0,0,.2), 0 2px 2px 0 rgba(0,0,0,.14), 0 1px 5px 0 rgba(0,0,0,.12);
        float: left;
        &:hover{
          .content{
            background: #e0e9f7;
          }
        }
        div{
          float: left;
        }
        .content{
          width: 65%;
          display: flex;
          flex-direction: column;
          padding: 16px;
          div:nth-child(1){
            color: rgba(0, 0, 0, 0.9);
            font-size: 1.5rem;
            font-family: "Roboto", "Helvetica", "Arial", sans-serif;
            font-weight: 400;
            height: 2rem;
            line-height: 2rem;
          }
          div:nth-child(2){
            color: rgba(0, 0, 0, 0.5);
            font-size: 1rem;
            font-family: "Roboto", "Helvetica", "Arial", sans-serif;
            font-weight: 400;
            line-height: 1.75;
            letter-spacing: 0.00938em;
          }
        }
        .img{
          width: 40%;
          display: block;
          background-size: cover;
          background-repeat: no-repeat;
          background-position: center;
        }
      }
      .part1{
        width: calc(50% - 4rem);
        height: 40%;
        margin: 1rem 1rem 0 1rem;
      }
    }
  }
</style>

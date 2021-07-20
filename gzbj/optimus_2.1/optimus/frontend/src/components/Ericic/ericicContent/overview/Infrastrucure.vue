<template>
  <div class="Infrastrucure">
    <div class="content">
      <div class="title">
        Infrastrucure Resource:
      </div>
      <div class="echartsBox">
        <div class="common">
          <div class="changeType">
            <span v-for="(item,index) in cpuTypeBox" @click="changeCpu(index)" :class="{active:index==cpucurrent}" :key="index">{{item}}</span>
          </div>
          <div class="cpuBox cBox" id="cpuBox"></div>
          <div class="cpuData" v-if="cpuStatus">
            <div>
              <span>used:</span>
              <span>{{cpu_used}} vCPU</span>
            </div>
            <div>
              <span>free:</span>
              <span>{{cpu_free}} vCPU</span>
            </div>
            <div>
              <span>total:</span>
              <span>{{cpu_total}} vCPU</span>
            </div>
          </div>
          <div class="cpuData cpuData_f" v-else>
            <div>
              <span>{{cpu_tenant_name}}</span>
              <span>{{cpu_tenant_value}}</span>
            </div>
          </div>
          <div class="legendContent">
            <div class="titleName" v-show="cpuStatus">Infra Resource</div>
            <div class="part" v-show="cpuStatus">
              <span style="background: #ff8033;"></span>
              <span>used</span>
            </div>
            <div class="part" v-show="cpuStatus">
              <span style="background: #A9D18E;"></span>
              <span>free</span>
            </div>
            <div class="titleName" v-show="!cpuStatus">Tenant Resource</div>
            <div class="tenantBox">
              <div class="part"  v-show="!cpuStatus" v-for="(item,index) in cpu_legendBox"  :key="index">
                <span :style="{background: item.color}"></span>
                <span :title="item.name1">{{item.name}}</span>
              </div>
            </div>
          </div>
        </div>
        <div class="common">
          <div class="changeType">
           <span v-for="(item,index) in cpuTypeBox" @click="changeMem(index)" :class="{active:index==memcurrent}" :key="index">{{item}}</span>
          </div>
          <div class="memBox cBox" id="memBox"></div>
          <div class="cpuData" v-if="memStatus">
            <div>
              <span>used:</span>
              <span>{{memory_used}} Gb</span>
            </div>
            <div>
              <span>free:</span>
              <span>{{memory_free}} Gb</span>
            </div>
            <div>
              <span>total:</span>
              <span>{{memory_total}} Gb</span>
            </div>
          </div>
          <div class="cpuData cpuData_f" v-else>
             <div>
              <span>{{mem_tenant_name}}</span>
              <span>{{mem_tenant_value}}</span>
            </div>
          </div>
          <div class="legendContent">
            <div class="titleName" v-show="memStatus">Infra Resource</div>
            <div class="part" v-show="memStatus">
              <span style="background: #ff8033;"></span>
              <span>used</span>
            </div>
            <div class="part" v-show="memStatus">
              <span style="background: #A9D18E;"></span>
              <span>free</span>
            </div>
            <div class="titleName" v-show="!memStatus">Tenant Resource</div>
            <div class="tenantBox">
              <div class="part"  v-show="!memStatus" v-for="(item,index) in mem_legendBox"  :key="index">
                <span :style="{background: item.color}"></span>
                <span :title="item.name1">{{item.name}}</span>
              </div>
            </div>
          </div>
        </div>
        <div class="common">
          <div class="localBox cBox" id="localBox"></div>
          <div class="cpuData">
            <div>
              <span>used:</span>
              <span>{{disk_used}}T</span>
            </div>
            <div>
              <span>free:</span>
              <span>{{disk_free}}T</span>
            </div>
            <div>
              <span>total:</span>
              <span>{{disk_total}}T</span>
            </div>
          </div><div class="legendContent">
            <div class="titleName">Infra Resource</div>
            <div class="part">
              <span style="background: #ff8033;"></span>
              <span>used</span>
            </div>
            <div class="part">
              <span style="background: #A9D18E;"></span>
              <span>free</span>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="details">
      <div class="left common">
        <div class="title">Compute Host:</div>
        <div class="box">
          <div class="div1"><Icon style="margin-right:7px;" size="16" type="logo-codepen" />Compute Hosts Overview</div>
          <div>
            <span>Compute(total)</span>
            <span class="span1">{{host_info.total}}</span>
          </div>
          <div>
            <span>Compute(nova-compute up)</span>
            <span class="span1 span1_1"><Icon size="18" style="margin-right:7px;" type="ios-checkmark-circle-outline" />{{host_info.up}}</span>
          </div>
          <div>
            <span>Compute(nova-compute down)</span>
            <span class="span1 span1_2"><Icon size="18" style="margin-right:7px;" type="ios-close-circle-outline" />{{host_info.down}}</span>
          </div>
        </div>
      </div>
      <div class="right common">
        <div class="title">Volume Pool:</div>
        <div class="box1">
          <div class="div1"><Icon style="margin-right:7px;" size="16" type="ios-photos" />Volume Pools Overview</div>
          <div class="div1">
            <span>Volume Pool</span>
            <span>Volume Backend Name</span>
          </div>
          <div class="newBox">
            <div class="PoolBox">
              <span v-for="(item,index) in poolBoxData" :key="index">{{item.name}}</span>
            </div>
            <div class="NameBox">
              <span v-for="(item,index) in nameBoxData" :key="index">{{item.name}}</span>
            </div>
            <div class="noData" v-if="poolBoxData.length == 0">no data!</div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { getEchartsData } from "@/api/infrastrucure"
export default {
  name: 'Infrastrucure',
  data () {
    return {
      cpu_free:'0',
      cpu_total:'0',
      cpu_used:'0',
      cpu_tenant_name:'',
      cpu_tenant_value:'',
      cpuTypeBox:['Infra','Tenant'],
      cpucurrent:0,
      cpu_legendBox:[],
      disk_free:'0',
      disk_total:'0',
      disk_used:'0',
      memory_free:'0',
      memory_total:'0',
      memory_used:'0',
      mem_tenant_name:'',
      mem_tenant_value:'',
      mem_legendBox:[],
      memcurrent:0,
      cpuData:[],
      memData:[],
      cpuStatus:true,
      memStatus:true,
      lengendColor:['#F08080','#A52A2A','#FF4D40','#FF8033','#E69966','#F4A460','#F5DEB3','#FFA500','#B8860B','#FFBF00',
      '#CCCC4D','#FFFF4D','#808000','#556B2F','#8FBC8F','#00FF00','#00FA9A','#66CDAA','#20B2AA','#008080',
      '#4798B3','#00BFFF','#4682B4','#6495ED','#004D99','#0033FF','#191970','#483D8B','#5000B8'],
      host_info:{},
      tenant_info:[],
      poolBoxData:[],
      nameBoxData:[]
    }
  },
  mounted(){
    let dataCenterDetails = JSON.parse(sessionStorage.getItem('dataCenter'));
    let {id} = dataCenterDetails;
    this.getData(id);
  },
  methods:{
    getData(id){
      let _this = this;
      getEchartsData(id).then(res=>{
        let {code,data} = res.data;
        //let ress = {"code":200,"data":{"host_info":{"down":0,"total":34,"up":34},"tenant_info":[{"core_used":236,"id":"2175917dfdad4bb8a8818e73cad45008","name":"ma9eda2ma9eda2ma9eda2ma9eda2ma9eda2","ram_used":1228800},{"core_used":102,"id":"b40ff84cc38e4d7da66d444fdf5dd4a2","name":"ma9nrf1","ram_used":614400},{"core_used":114,"id":"a461881b75b84215bba5142a15255599","name":"ma9ccsm2","ram_used":630784},{"core_used":0,"id":"e1e36038c9664640a9d35ac568182f2f","name":"service","ram_used":0},{"core_used":318,"id":"7f4ae3e07ff64a54a2f54cadf6237f57","name":"ma9ccsm1","ram_used":1777664},{"core_used":0,"id":"d764060ea5bf4ca684f53cff8544840f","name":"ma9ccdm2","ram_used":0},{"core_used":280,"id":"608f83114b2c409dbfbb0341aa7788af","name":"ma9ccdm1","ram_used":1458176},{"core_used":0,"id":"97c2dbef64974126a2930cc93a8c5f7e","name":"admin","ram_used":0},{"core_used":228,"id":"3ce3894bede2418997311a19ee941842","name":"ma9eda1","ram_used":1212416}],"total_memory":13103906,"total_storage":12208,"total_vcpus":1904,"used_memory":5129216,"used_storage":0,"used_vcpus":924,"volume_info":[{"id":"1e935851-ab62-41bd-bee4-d983eeb82bc8","name":"h3c"}]},"status":true}
        if(code == 200 && data){
          let {host_info,tenant_info,total_memory,total_storage,total_vcpus,used_memory,used_storage
          ,used_vcpus,volume_info} = data;
          this.host_info = host_info;
          this.tenant_info = tenant_info;
          this.cpu_total = total_vcpus;
          this.cpu_free = total_vcpus - used_vcpus;
          this.cpu_used = used_vcpus;
          this.disk_total = _this.$util.formatNmuber(total_storage);
          this.disk_used = _this.$util.formatNmuber(used_storage);
          this.disk_free = _this.disk_total - _this.disk_used;
          this.memory_total = _this.$util.formatNmuber(total_memory);
          this.memory_used = _this.$util.formatNmuber(used_memory);
          this.memory_free = _this.memory_total - this.memory_used;
          this.drawCpu();
          this.drawMem();
          this.drawLocal();
          if(volume_info && volume_info.length>0){
            let tN=[],tP=[];
            volume_info.forEach(res=>{
              tN.push({
                name:'-'
              })
              tP.push({
                name:res.name
              })
            });
            _this.nameBoxData =tN;
            _this.poolBoxData =tP;
          }
        }else{
          this.host_info = {
            "down": 0,
            "total": 0,
            "up": 0
          };
          this.tenant_info = 0;
          this.cpu_total = 0;
          this.cpu_free = 0;
          this.cpu_used = 0;
          this.disk_total = 0;
          this.disk_free = 0;
          this.disk_used = 0;
          this.memory_total = 0;
          this.memory_free = 0;
          this.memory_used = 0;
          this.drawCpu();
          this.drawMem();
          this.drawLocal();
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
    },
    changeCpu(index){
      this.cpucurrent = index;
      if(index == 0){
        this.drawCpu();
        this.cpu_tenant_name = '';
        this.cpu_tenant_value = '';
      }else{
        this.drawCpuDetails();
      }
    },
    drawCpu(){
      this.cpuStatus = true;
      let {cpu_free,cpu_total,cpu_used} = this;
      let myChart = this.$echarts.init(document.getElementById('cpuBox'));
      myChart.off('click') // 这里很重要！！！
      let option = {
        title: {
          text: 'CPU',
          left: 'center',
          top:20
        },
        tooltip: {
          trigger: 'item',
          formatter: '{b}: {c} ({d}%)',
          confine: true
        },
        grid:{
          left: 24, // 默认10%，给24就挺合适的。
          top: 24, // 默认60
          right: 24, // 默认10%
          bottom: 24, // 默认60
        },
        // legend: {
        //   orient: 'vertical',
        //   left: '70%',  //图例距离左的距离
        //   y: 'center',  //图例上下居中
        //   selectedMode: false,
        //   data: ['used', 'free']
        // },
        color:['#ff8033','#A9D18E'],
        series: [
          {
            name: 'CPU',
            type: 'pie',
            radius: ['35%', '55%'],
            center: ['35%', '50%'], //图的位置，距离左跟上的位置
            itemStyle:{
              borderWidth:2, //设置border的宽度有多大
              borderColor:'#fff',
            },
            label: {
              formatter: '{d}%',
              show : false   //隐藏标示文字
            },
            labelLine: {
                show: false
            },
            data: [
              {value: cpu_used, name: 'used'},
              {value: cpu_free, name: 'free'}
            ]
          }
        ]
      }
      myChart.setOption(option,true);
    },
    drawCpuDetails(){
      let _this = this;
      this.cpuStatus = false;
      let {cpu_free,cpu_total,cpu_used,tenant_info,lengendColor} = this;
      let legendBox = [],seriesBox = [];
      tenant_info.forEach((res,index)=>{
        let {core_used,name} = res;
        legendBox.push({
          name:name.length>7 ?name.substring(0,7)+'...':name,
          name1:name,
          color:lengendColor[index]
        });
        seriesBox.push({
          value:core_used,
          name:name
        })
      });
      this.cpu_legendBox = legendBox;
      // seriesBox.shift({
      //   value: cpu_free, name: 'free'
      // });
      let myChart = this.$echarts.init(document.getElementById('cpuBox'));
      myChart.off('click') // 这里很重要！！！
      let option = {
        title: {
          text: 'CPU',
          left: 'center',
          top:20
        },
        tooltip: {
          trigger: 'item',
          formatter: '{b}: {c} ({d}%)',
          confine: true
        },
        grid:{
          left: 24, // 默认10%，给24就挺合适的。
          top: 24, // 默认60
          right: 24, // 默认10%
          bottom: 24, // 默认60
        },
        // legend: {
        //   orient: 'vertical',
        //   type: 'scroll',
        //   left: '70%',  //图例距离左的距离
        //   y: 'center',  //图例上下居中
        //   selectedMode: false,
        //   data: legendBox
        // },
        color:['#F08080','#A52A2A','#FF4D40','#E69966','#F4A460','#F5DEB3','#FFA500','#B8860B','#FFBF00',
      '#CCCC4D','#FFFF4D','#808000','#556B2F','#8FBC8F','#00FF00','#00FA9A','#66CDAA','#20B2AA','#008080',
      '#4798B3','#00BFFF','#4682B4','#6495ED','#004D99','#0033FF','#191970','#483D8B','#5000B8'],
        series: [
          // {
          //   name: 'Infra',
          //   type: 'pie',
          //   radius: ['30%', '44%'],
          //   center: ['35%', '50%'], //图的位置，距离左跟上的位置
          //   itemStyle:{
          //     borderWidth:2, //设置border的宽度有多大
          //     borderColor:'#fff',
          //   },
          //   label: {
          //     formatter: '{d}%',
          //     show : false   //隐藏标示文字
          //   },
          //   labelLine: {
          //       show: false
          //   },
          //   data: [
          //     {value: cpu_used, name: 'used'},
          //     {value: cpu_free, name: 'free'}
          //   ]
          // },
          {
            name: 'Tenant',
            type: 'pie',
            radius: ['35%', '55%'],
            center: ['35%', '50%'], //图的位置，距离左跟上的位置
            label: {
              formatter: '{d}%',
              show : false   //隐藏标示文字
            },
            labelLine: {
                show: false
            },
            itemStyle:{
              borderWidth:2, //设置border的宽度有多大
              borderColor:'#fff',
            },
            data: seriesBox
          }
        ]
      }
      myChart.setOption(option,true);
      // myChart.on("click", pieConsole);
      // function pieConsole(param) {
      //   let {data,seriesName} = param;
      //   if(seriesName == 'Tenant'){
      //     let {name,value} = data;
      //     _this.cpu_tenant_name = name + ':';
      //     _this.cpu_tenant_value = value;
      //   }
      // }
    },
    changeMem(index){
      this.memcurrent = index;
      if(index == 0){
        this.drawMem();
        this.mem_tenant_name = '';
        this.mem_tenant_value = '';
      }else{
        this.drawMemDetails();
      }
    },
    drawMem(){
      let _this = this;
      this.memStatus = true;
      let {memory_free,memory_total,memory_used,memData} = this;
      let myChart = this.$echarts.init(document.getElementById('memBox'));
      let option = {
        title: {
          text: 'Mem',
          left: 'center',
          top:10
        },
        tooltip: {
          trigger: 'item',
          formatter: '{b}: {c} ({d}%)',
          confine: true
        },
        grid:{
          left: 24, // 默认10%，给24就挺合适的。
          top: 24, // 默认60
          right: 24, // 默认10%
          bottom: 24, // 默认60
        },
        // legend: {
        //   orient: 'vertical',
        //   left: '70%',  //图例距离左的距离
        //   y: 'center',  //图例上下居中
        //   selectedMode: false,
        //   data: ['used', 'free']
        // },
        color:['#ff8033','#A9D18E'],
        series: [
          {
            name: 'Mem',
            type: 'pie',
            radius: ['35%', '55%'],
            center: ['35%', '50%'], //图的位置，距离左跟上的位置
            label: {
              formatter: '{d}%',
              show : false   //隐藏标示文字
            },
            labelLine: {
                show: false
            },
            itemStyle:{
              borderWidth:2, //设置border的宽度有多大
              borderColor:'#fff',
            },
            data: [
              {value: memory_used, name: 'used'},
              {value: memory_free, name: 'free'}
            ]
          }
        ]
      }
      myChart.setOption(option,true);
    },
    drawMemDetails(){
      let _this = this;
      this.memStatus = false;
      let {memory_free,memory_total,memory_used,tenant_info,lengendColor} = this;
      let legendBox = [],seriesBox = [];
      tenant_info.forEach((res,index)=>{
        let {ram_used,name} = res;
        legendBox.push({
          name:name.length>7 ?name.substring(0,7)+'...':name,
          name1:name,
          color:lengendColor[index]
        });
        seriesBox.push({
          value:_this.$util.formatNmuber(ram_used),
          name:name
        })
      });
      this.mem_legendBox = legendBox;
      // seriesBox.shift({
      //   value: memory_free, name: 'free'
      // });
      let myChart = this.$echarts.init(document.getElementById('memBox'));
      let option = {
        title: {
          text: 'Mem',
          left: 'center',
          top:10
        },
        tooltip: {
          trigger: 'item',
          formatter: '{b}: {c} ({d}%)',
          confine: true
        },
        grid:{
          left: 24, // 默认10%，给24就挺合适的。
          top: 24, // 默认60
          right: 24, // 默认10%
          bottom: 24, // 默认60
        },
        // legend: {
        //   orient: 'vertical',
        //   left: '70%',  //图例距离左的距离
        //   y: 'center',  //图例上下居中
        //   selectedMode: false,
        //   data: legendBox
        // },
        color:['#F08080','#A52A2A','#FF4D40','#E69966','#F4A460','#F5DEB3','#FFA500','#B8860B','#FFBF00',
      '#CCCC4D','#FFFF4D','#808000','#556B2F','#8FBC8F','#00FF00','#00FA9A','#66CDAA','#20B2AA','#008080',
      '#4798B3','#00BFFF','#4682B4','#6495ED','#004D99','#0033FF','#191970','#483D8B','#5000B8'],
        series: [
          // {
          //   name: 'Infra',
          //   type: 'pie',
          //   radius: ['30%', '44%'],
          //   center: ['35%', '50%'], //图的位置，距离左跟上的位置
          //   label: {
          //     formatter: '{d}%',
          //     show : false   //隐藏标示文字
          //   },
          //   labelLine: {
          //       show: false
          //   },
          //   itemStyle:{
          //     borderWidth:2, //设置border的宽度有多大
          //     borderColor:'#fff',
          //   },
          //   data: [
          //     {value: memory_used, name: 'used'},
          //     {value: memory_free, name: 'free'}
          //   ]
          // },
          {
            name: 'Tenant',
            type: 'pie',
            radius: ['35%', '55%'],
            center: ['35%', '50%'], //图的位置，距离左跟上的位置
            label: {
              formatter: '{d}%',
              show : false   //隐藏标示文字
            },
            labelLine: {
                show: false
            },
            itemStyle:{
              borderWidth:2, //设置border的宽度有多大
              borderColor:'#fff',
            },
            data: seriesBox
          }
        ]
      }
      myChart.setOption(option,true);
      myChart.on("click", pieConsole);
      function pieConsole(param) {
        let {data,seriesName} = param;
        if(seriesName == 'Tenant'){
          let {name,value} = data;
          _this.mem_tenant_name = name + ':';
          _this.mem_tenant_value = value+ 'G';
        }
      }
    },
    drawLocal(){
      let _this = this;
      let {disk_free,disk_total,disk_used} = this;
      let myChart = this.$echarts.init(document.getElementById('localBox'));
      let option = {
        title: {
          text: 'Local Disk',
          left: 'center',
          top:10
        },
        tooltip: {
          trigger: 'item',
          formatter: '{b}: {c} ({d}%)',
          confine: true
        },
        grid:{
          left: 24, // 默认10%，给24就挺合适的。
          top: 24, // 默认60
          right: 24, // 默认10%
          bottom: 24, // 默认60
        },
        // legend: {
        //   orient: 'vertical',
        //   left: '70%',  //图例距离左的距离
        //   y: 'center',  //图例上下居中
        //   selectedMode: false,
        //   data: ['used', 'free']
        // },
        color:['#ff8033','#A9D18E'],
        series: [
          {
            name: 'Local Disk',
            type: 'pie',
            radius: ['35%', '55%'],
            center: ['35%', '50%'], //图的位置，距离左跟上的位置
            label: {
              formatter: '{d}%',
              show : false   //隐藏标示文字
            },
            labelLine: {
                show: false
            },
            itemStyle:{
              borderWidth:2, //设置border的宽度有多大
              borderColor:'#fff',
            },
            data: [
              {value: disk_used, name: 'used'},
              {value: disk_free, name: 'free'}
            ]
          }
        ]
      }
      myChart.setOption(option,true);
    }
  },
  beforeDestroy(){

  }
}
</script>

<style scoped lang="scss">
  .Infrastrucure{
    width: 100%;
    height: 100%;
    overflow: auto;
    color: #000;
    .content{
      width: 100%;
      height: 500px;
      border-bottom: 1px solid #ddd;
      .title{
        height: 30px;
        line-height: 30px;
        padding-top: 5px;
        font-size: 18px;
        font-weight: 500;
        color: #000;
        padding-left: 15px;
      }
      .echartsBox{
        width: 100%;
        height: calc(100% - 30px);
        .changeType{
          width: 110px;
          height: 20px;
          position: absolute;
          left: 29%;
          bottom: 20px;
          margin-left: -30px;
          z-index: 999;
          text-align: center;
          span{
            display: inline-block;
            width: 50px;
            height: 20px;
            border-radius: 5px;
            font-size: .6rem;
            line-height: 19px;
            text-align: center;
            cursor: pointer;
            background: #ddd;
            &:hover{
              background: #A9D18E;
            }
          }
          .active{
            background: #A9D18E;
          }
          span:nth-child(1){
            margin-right: 10px;
          }
        }
        .common{
          width: calc(33.3% - 30px);
          height: 90%;
          margin: 15px;
          border: 1px solid #ddd;
          position: relative;
          float: left;
          box-shadow: 0 0 2px 2px #ddd;
          border-radius: 5px;
        }
        .common:nth-child(2){
          width: calc(33.4% - 30px);
        }
        .cBox{
          width: 100%;
          height: 100%;
          padding: 5% 0;
        }
        .cpuData{
          width: 110px;
          height: 100px;
          position: absolute;
          z-index: 99;
          top: 50%;
          left: 35%;
          margin-top: -50px;
          margin-left: -50px;
          overflow: auto;
          div{
            width: 100%;
            height: 20px;
            line-height: 20px;
            display: flex;
            justify-content: center;
            overflow: auto;
            span:nth-child(1){
              display: block;
              float: left;
            }
            span:nth-child(2){
              display: block;
              text-align: center;
              float: left;
            }
          }
          div:nth-child(1){
            color: #000;
            margin-top: 20px;
          }
          div:nth-child(2){
            color: #000;
          }
          div:nth-child(3){
            color: #000;
          }
          span{
            font-size: .7rem;
            font-weight: 500;
          }
        }
        .cpuData_f{
          div{
            margin-top: 0 !important;
          }
          display: flex;
          justify-content: center;
          align-items: center;
        }
        .legendContent{
          width: 130px;
          height: 100%;
          position: absolute;
          right: 10px;
          top: 0;
          overflow: auto;
          display: flex;
          align-items: center;
          flex-direction: column;
          justify-content: center;
          div{
            width: 100%;
            height: 20px;
            line-height: 20px;
          }
          .titleName{
            font-size: 14px;
            font-weight: 800;
            margin-bottom: 5px;
          }
          .tenantBox{
            width: 100%;
            height: auto;
            max-height: 280px;
            overflow: auto;
          }
          .part{
            width: 100%;
            height: 25px;
            display: flex;
            align-items: center;
            span:nth-child(1){
              width: 25px;
              height: 15px;
              display: inline-block;
              margin-right: 10px;
              border-radius: 2px;
            }
            span:nth-child(2){
              margin-bottom: 5px;
            }
          }
        }
      }
    }
    .details{
      width: 100%;
      min-height: 300px;
      overflow: auto;
      padding:0 15px;
      .common{
        width: 50%;
        height: 100%;
        float: left;
        .title{
          width: 100%;
          height: 50px;
          line-height: 50px;
          font-size: 18px;
          font-weight: 600;
        }
        .box{
          width: 90%;
          margin-left: 5%;
          border: 1px solid #ddd;
          max-height: 270px;
          box-shadow: 0 0 2px 2px #ddd;
          border-radius: 5px;
          div{
            width: 100%;
            padding: 0 15px;
            height: 35px;
            line-height: 35px;
            font-size: 12px;
            font-weight: 400;
            border-bottom: 1px solid #ddd;
            span{
              font-size: 11px;
            }
            span:nth-child(1){
              width: 50%;
              display: block;
              float: left;
            }
            span:nth-child(2){
              width: 50%;
              display: block;
              float: right;
            }
            .span1{
              text-align: right;
            }
            .span1_1{
              cursor: pointer;
              .ivu-icon{
                color: green;
              }
            }
            .span1_2{
              cursor: pointer;
              .ivu-icon{
                color: red;
              }
            }
          }
          .div1{
            font-size: 14px;
            font-weight: 500;
          }
        }
        .box1{
          width: 90%;
          margin-left: 5%;
          border: 1px solid #ddd;
          height: 270px;
          margin-bottom: 20px;
          box-shadow: 0 0 2px 2px #ddd;
          border-radius: 5px;
          .div1{
            width: 100%;
            padding: 0 15px;
            height: 35px;
            line-height: 35px;
            font-size: 12px;
            font-weight: 400;
            border-bottom: 1px solid #ddd;
            span{
              font-size: 11px;
            }
            span:nth-child(1){
              width: 50%;
              display: block;
              float: left;
            }
            span:nth-child(2){
              width: 50%;
              display: block;
              float: right;
            }
          }
          .div1{
            font-size: 14px;
            font-weight: 500;
          }
          .newBox{
            width: 100%;
            max-height: 200px;
            overflow: auto;
            .PoolBox{
              width: 50%;
              float: left;
              overflow: auto;
              font-size: 12px;
              font-weight: 400;
              border-bottom: 1px solid #ddd;
              span{
                display: block;
                width: 100%;
                font-size: 12px;
                font-weight: 400;
                border-bottom: 1px solid #ddd;
                height: 35px;
                line-height: 35px;
                padding-left: 10px;
              }
            }
            .NameBox{
              width: 50%;
              float: left;
              overflow: auto;
              span{
                display: block;
                width: 100%;
                font-size: 12px;
                font-weight: 400;
                border-bottom: 1px solid #ddd;
                height: 35px;
                line-height: 35px;
                padding-left: 10px;
              }
            }
            .noData{
              width: 100%;
              height: 190px;
              display: flex;
              align-items: center;
              justify-content: center;
              font-size: 14px;
              font-weight: 600;
            }
          }
        }
      }
    }
  }
</style>

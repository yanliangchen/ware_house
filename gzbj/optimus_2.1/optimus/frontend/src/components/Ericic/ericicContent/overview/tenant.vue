<template>
  <div class="tenant">
    <div class="content">
      <div class="echartsBox">
        <div class="title">
          <span>Tenant:</span>
          <Select v-model="tenantHid" style="width:200px" @on-change="changeTenant">
            <Option v-for="(item,index) in tenantList" :value="item.tenant_name" :key='index'>{{ item.tenant_name }}</Option>
          </Select>
          <!-- <span>{{item.name}}</span> -->
        </div>
        <div 
          style="height:800px;width:100%;"
          v-loading="loading"
        element-loading-text="Loading"
        element-loading-spinner="el-icon-loading">
          <div class="common">
            <div class="cBox" :id="tenantData.n1"></div>
            <div class="cpuData">
              <div>
                <span >quota:</span>
                <span >{{tenantData.cores.limit == -1 ? 'no limit' : tenantData.cores.limit}} vCPU</span>
              </div>
              <div>
                <span >total:</span>
                <span >{{tenantData.cores.total}} vCPU</span>
              </div>
            </div>
            <div class="cpuData_s">
              <div>
                <span >used quota:</span>
                <span >{{tenantData.cores.in_use}} vCPU</span>
              </div>
              <div>
                <span >available quota:</span>
                <span >{{tenantData.cores.availability}} vCPU</span>
              </div>
              <div>
                <span >other:</span>
                <span >{{tenantData.cores.other}} vCPU</span>
              </div>
            </div>
            <div class="legendContent">
              <div class="titleName">Quota</div>
              <div class="part">
                <span style="background: #ff8033;"></span>
                <span>quota</span>
              </div>
              <div class="part">
                <span style="background: #A6A6A6;"></span>
                <span>other</span>
              </div>
            </div>
            <div class="legendContent1">
              <div class="titleName">Quota Statistic</div>
              <div class="part">
                <span style="background: #FFA500;"></span>
                <span>used quota</span>
              </div>
              <div class="part">
                <span style="background: #A9D18E;"></span>
                <span>available quota</span>
              </div>
              <div class="part">
                <span style="background: #A6A6A6;"></span>
                <span>other</span>
              </div>
            </div>
          </div>
          <div class="common">
            <div class="cBox" :id="tenantData.n2"></div>
            <div class="cpuData">
              <div>
                <span >quota:</span>
                <span >{{tenantData.ram.limit == -1 ? 'no limit' : tenantData.ram.limit}} Gb</span>
              </div>
              <div>
                <span >total:</span>
                <span >{{tenantData.ram.total}} Gb</span>
              </div>
            </div>
            <div class="cpuData_s">
              <div>
                <span >used quota:</span>
                <span >{{tenantData.ram.in_use}} Gb</span>
              </div>
              <div>
                <span >available quota:</span>
                <span >{{tenantData.ram.availability}} Gb</span>
              </div>
              <div>
                <span >other:</span>
                <span >{{tenantData.ram.other}} Gb</span>
              </div>
            </div>
            <div class="legendContent">
              <div class="titleName">Quota</div>
              <div class="part">
                <span style="background: #ff8033;"></span>
                <span>quota</span>
              </div>
              <div class="part">
                <span style="background: #A6A6A6;"></span>
                <span>other</span>
              </div>
            </div>
            <div class="legendContent1">
              <div class="titleName">Quota Statistic</div>
              <div class="part">
                <span style="background: #FFA500;"></span>
                <span>used quota</span>
              </div>
              <div class="part">
                <span style="background: #A9D18E;"></span>
                <span>available quota</span>
              </div>
              <div class="part">
                <span style="background: #A6A6A6;"></span>
                <span>other</span>
              </div>
            </div>
          </div>
          <div class="common" style="margin-bottom:15px;">
            <div class="cBox" :id="tenantData.n3"></div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { getFilter } from "@/api/vmView"
import { getQuota } from "@/api/infrastrucure"
export default {
  name: 'tenant',
  data () {
    return {
      tenantList:[],
      tenantHid:'admin',
      lengendColor:['#ff8033','#A6A6A6','#FFA500','#A9D18E','#A6A6A6','#F08080','#A52A2A','#FF4D40','#E69966','#F4A460','#F5DEB3','#FFA500','#B8860B','#FFBF00',
      '#CCCC4D','#FFFF4D','#808000','#556B2F','#8FBC8F','#00FF00','#00FA9A','#66CDAA','#20B2AA','#008080',
      '#4798B3','#00BFFF','#4682B4','#6495ED','#004D99','#0033FF','#191970','#483D8B','#5000B8'],
      tenantData:{},
      cid:'',
      loading:false
    }
  },
  mounted(){
    let dataCenterDetails = JSON.parse(sessionStorage.getItem('dataCenter'));
    if(dataCenterDetails){
      let {cee_version,data_center,id,name,Mode} = dataCenterDetails;
      this.cid = id;
      this.getFilterList();
    }
  },
  methods:{
    getFilterList(){
      let _this = this;
      let {cid} = this;
      getFilter(cid).then(res=>{
        let {code,data} = res.data;
        if(code == 200 && data.length>0){
          let {tenant} = data[0];
          if(tenant && tenant.length>0){
            _this.tenantList = tenant;
            _this.drawEcharts(tenant[0]);
          }
        }
      })
    },
    changeTenant(item){
      let _this = this;
      let tenantList = this.tenantList;
      tenantList.forEach(res=>{
        if(res.tenant_name == item){
          _this.drawEcharts(res);
        }
      });
    },
    drawEcharts(tenant){
      let {tenant_id} = tenant;
      let _this = this;
      let {cid} = this; 
      _this.loading = true;
      let params = {
        cid:cid,
        tid:tenant_id
      };
      getQuota(params).then(res=>{
        let {code,data} = res.data;
        _this.loading = false;
        if(code == 200 && data){
          if(data.volume.default != undefined){
            data.n1 = 'cores' + Math.random(100000);
            data.n2 = 'ram' + Math.random(100000);
            data.n3 = 'volume' + Math.random(100000);
            let {ram,cores} = data;
            if(ram){
              let {limit,total} = ram;
              if(ram.limit == -1){
                data.ram.limit = 'no limit';
                data.ram.total = total;
              }else{
                data.ram.limit = limit;
                data.ram.total = total - limit;
              }
              _this.tenantData = data;
            }
            if(cores){
              let {limit,total} = cores;
              if(limit == -1){
                data.cores.limit = 'no limit';
                data.cores.total = total;
              }else{
                data.cores.limit = limit;
                data.cores.total = total - limit;
              }
              _this.tenantData = data;
            }
          _this.drawCpu(data);
          }
        }
      });
      // let dat = {
      //   "code": 200,
      //   "data": {
      //       "cores": {
      //           "in_use": 13413,
      //           "limit": -1,
      //           "total": 122,
      //           "other": 21,
      //           "availability": 1412,
      //       },
      //       "ram": {
      //           "in_use": 1555,
      //           "limit": 21,
      //           "total": 311,
      //           "other": 12,
      //           "availability": 132,
      //       },
      //       "volume": { // 当有多个volume 信息时， 会存在多个key， default 信息一定存在
      //           "default": {
      //               "in_use": 20,
      //               "limit": -1
      //           },
      //           "pool_2": {
      //               "in_use": 10,
      //               "limit": 100
      //           },
      //           "pool_3": {
      //               "in_use": 110,
      //               "limit": 1100
      //           }
      //       }
      //   },
      //   "status": true
      // };
      // let {code,data} = dat;
      //   if(code == 200 && data){
      //     if(data.volume.default != undefined){
      //       data.n1 = 'cores' + Math.random(100000);
      //       data.n2 = 'ram' + Math.random(100000);
      //       data.n3 = 'volume' + Math.random(100000);
      //       let {ram,cores} = data;
      //       if(ram){
      //         let {limit,total} = ram;
      //         if(ram.limit == -1){
      //           data.ram.limit = 'no limit';
      //           data.ram.total = total;
      //         }else{
      //           data.ram.limit = limit;
      //           data.ram.total = total - limit;
      //         }
      //         _this.tenantData = data;
      //       }
      //       if(cores){
      //         let {limit,total} = cores;
      //         if(limit == -1){
      //           data.cores.limit = 'no limit';
      //           data.cores.total = total;
      //         }else{
      //           data.cores.limit = limit;
      //           data.cores.total = total - limit;
      //         }
      //         _this.tenantData = data;
      //       }
      //     _this.drawCpu(data);
      //     }
      //   }
    },
    drawCpu(res){
      this.$nextTick(function(){
        let {n1,n2,n3,cores,ram,volume} = res;
        //let {availability,in_use,limit,other,total} = cores;
        let tempCoresLimit,tempCoresOther,tempRamLimit,tempRamother;
        if(cores){
          let {limit,total} = cores;
          if(limit == 'no limit'){
            tempCoresLimit = total;
            tempCoresOther = 0;
          }else{
            tempCoresLimit = limit;
            tempCoresOther = total - limit;
          }
        }
        if(ram){
          let {limit,total,in_use,availability,other} = ram;
          if(limit == 'no limit'){
            tempRamLimit = ram.total;
            tempRamother = 0;
          }else{
            tempRamLimit = limit;
            tempRamother = total - limit;
          }
          ram.in_use = this.$util.formatNmuber(in_use);
          ram.availability = this.$util.formatNmuber(availability);
          ram.other = this.$util.formatNmuber(other);
        }
        let myChart = this.$echarts.init(document.getElementById(n1));
        let option = {
          title: {
            text: 'CPU',
            left: 'center',
            top:20
          },
          tooltip: {
            trigger: 'item',
            formatter: '{b}: {c} ({d}%)',
            formatter: function (params) {
              let {value,name} = params.data;
              if(cores.total == value){
                return name + ':    ' +' no limit';
              }else{
                return name + ':    ' +value;
              }
            }
          },
          grid:{
            left: 24, // 默认10%，给24就挺合适的。
            top: 24, // 默认60
            right: 24, // 默认10%
            bottom: 24, // 默认60
          },
          color:this.lengendColor,
          series: [
            {
              name: 'CPU',
              type: 'pie',
              radius: ['52%', '75%'],
              center: ['30%', '50%'], //图的位置，距离左跟上的位置
              label: {
                formatter: '{d}%'
              },
              itemStyle:{
                borderWidth:2, //设置border的宽度有多大
                borderColor:'#fff',
              },
              data: [
                {value: tempCoresLimit, name: 'quota'},
                {value: tempCoresOther, name: 'other'}
              ],
              left: '-15%',
              top: 0,
              bottom: 0
            },
            // {
            //   name: 'Infra',
            //   type: 'pie',
            //   radius: ['45%', '60%'],
            //   center: ['-5%', '50%'], //图的位置，距离左跟上的位置
            //   label: {
            //     show:false
            //   },
            //   itemStyle:{
            //     borderWidth:2, //设置border的宽度有多大
            //     borderColor:'#fff',
            //   },
            //   data: [
            //     {value: tempCoresLimit, name: 'quota'},
            //     {value: tempCoresOther, name: 'other'}
            //   ],
            //   left: '65%',
            //   right: 0,
            //   top: 0,
            //   bottom: 0
            // },
            {
              name: 'Tenant',
              type: 'pie',
              radius: ['52%', '75%'],
              center: ['-5%', '50%'], //图的位置，距离左跟上的位置
              label: {
                formatter: '{d}%'
              },
              itemStyle:{
                borderWidth:2, //设置border的宽度有多大
                borderColor:'#fff',
              },
              data: [
                {value: cores.in_use, name: 'used quota'},
                {value: cores.availability, name: 'available quota'},
                {value: cores.other, name: 'other'}
              ],
              left: '65%',
              right: 0,
              top: 0,
              bottom: 0
            }
          ]
        }
        myChart.setOption(option,true);
        
        let myChart1 = this.$echarts.init(document.getElementById(n2));
        let option1 = {
          title: {
            text: 'Mem',
            left: 'center',
            top:20
          },
          tooltip: {
            trigger: 'item',
            formatter: '{b}: {c} ({d}%)',
            formatter: function (params) {
              let {value,name} = params.data;
              if(ram.total == value){
                return name + ':    ' +' no limit';
              }else{
                return name + ':    ' +value;
              }
            }
          },
          grid:{
            left: 24, // 默认10%，给24就挺合适的。
            top: 24, // 默认60
            right: 24, // 默认10%
            bottom: 24, // 默认60
          },
          color:this.lengendColor,
          series: [
            {
              name: 'Mem',
              type: 'pie',
              radius: ['52%', '75%'],
              center: ['30%', '50%'], //图的位置，距离左跟上的位置
              label: {
                formatter: '{d}%'
              },
              itemStyle:{
                borderWidth:2, //设置border的宽度有多大
                borderColor:'#fff',
              },
              data: [
                {value: tempRamLimit, name: 'quota'},
                {value: tempRamother, name: 'other'}
              ],
              left: '-15%',
              top: 0,
              bottom: 0
            },
            // {
            //   name: 'Infra',
            //   type: 'pie',
            //   radius: ['45%', '60%'],
            //   center: ['-5%', '50%'], //图的位置，距离左跟上的位置
            //   label: {
            //     show:false
            //   },
            //   itemStyle:{
            //     borderWidth:2, //设置border的宽度有多大
            //     borderColor:'#fff',
            //   },
            //   data: [
            //     {value: tempRamLimit, name: 'quota'},
            //     {value: tempRamother, name: 'other'}
            //   ],
            //   left: '65%',
            //   right: 0,
            //   top: 0,
            //   bottom: 0
            // },
            {
              name: 'Tenant',
              type: 'pie',
              radius: ['52%', '75%'],
              center: ['-5%', '50%'], //图的位置，距离左跟上的位置
              label: {
                formatter: '{d}%'
              },
              itemStyle:{
                borderWidth:2, //设置border的宽度有多大
                borderColor:'#fff',
              },
              data: [
                {value: ram.in_use, name: 'used quota'},
                {value: ram.availability, name: 'available quota'},
                {value: ram.other, name: 'other'}
              ],
              left: '65%',
              right: 0,
              top: 0,
              bottom: 0
            }
          ]
        }
        myChart1.setOption(option1,true);
        
        let myChart2 = this.$echarts.init(document.getElementById(n3));
        let emphasisStyle = {
          itemStyle: {
            barBorderWidth: 1,
            shadowBlur: 10,
            shadowOffsetX: 0,
            shadowOffsetY: 0,
            shadowColor: 'rgba(0,0,0,0.5)'
          }
        };
        let legendBox = ['used','quota'];
        let xAxis = [],useddata = [],quotadata=[];
        for(let key  in volume){
          let {in_use,limit} = volume[key];
          xAxis.push(key);
          useddata.push(in_use);
          quotadata.push(limit);
        };
        let tempquotadata = [],tempquotadata1 = [];
        if(quotadata.length>0){
          quotadata.forEach(res=>{
            if(res != -1){
              tempquotadata.push(res)
            }
          })
          quotadata.forEach(res=>{
            if(res != -1){
              tempquotadata1.push(res)
            }else{
              tempquotadata1.push(Math.max.apply(null,tempquotadata)+100)
            }
          })
        }
        let option2 = {
          title: {
            text: 'Volume',
            left: 'center',
            top:20
          },
          tooltip: {
            trigger: 'axis',
            axisPointer: {
              type: 'shadow'
            },
            formatter: function (params) {
              let p1 = params[0];
              let p2 = params[1];
              let {data} = params[1];
              if(Math.max.apply(null,tempquotadata)+100 == data){
                return p1.name+ '<br>'+ p1.marker + '   ' + p1.seriesName + ':    ' + p1.data + '<br>'
                + p2.marker + '   ' + p2.seriesName + ':    ' +' no limit' ;
              }else{
                return p1.name+ '<br>'+ p1.marker + '   ' + p1.seriesName + ':    ' + p1.data + '<br>'
                + p2.marker + '   ' + p2.seriesName + ':    ' +p2.data ;
              }
            }
          },
          legend: {
            data: legendBox,
            top:'60px'
          },
          color:this.lengendColor,
          grid: {
            top:'100px',
            left: '4%',
            right: '5%',
            bottom: '3%',
            containLabel: true
          },
          xAxis: {
            boundaryGap: [0, 0.01],
            type: 'value'
          },
          yAxis: {
            data: xAxis,
            type: 'category'
          },
          series: [
            {
              name: legendBox[0],
              type: 'bar',
              // stack: 'two',
              // emphasis: emphasisStyle,
              data: useddata
            },
            {
              name: legendBox[1],
              type: 'bar',
              // stack: 'two',
              // emphasis: emphasisStyle,
              data: tempquotadata1
            }
          ]
        };
        myChart2.setOption(option2,true);
      })
    }
  },
  beforeDestroy(){

  }
}
</script>

<style scoped lang="scss">
  .tenant{
    width: 100%;
    height: 100%;
    .content{
      width: 100%;
      height: 100%;
      border-top: 1px solid #ddd;
      overflow: auto;
      .title{
        height: 30px;
        line-height: 30px;
        color: #000;
        padding-left: 15px;
        margin-top: 10px;
        span{
          font-size: 18px;
          font-weight: 600;
          margin-right: 5px;
        }
      }
      .echartsBox{
        width: 100%;
        height: 800px;
        .common{
          width: 100%;
          height: 350px;
          position: relative;
          float: left;
          border-bottom: 1px solid #ddd;
        }
        .cBox{
          width: 100%;
          height: 100%;
        }
        .cpuData{
          width: 160px;
          height: 100px;
          position: absolute;
          z-index: 99;
          top: 50%;
          left: 19.2%;
          margin-top: -50px;
          margin-left: -80px;
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
              min-width: 70px;
              text-align: right;
              margin-right: 5px;
            }
            span:nth-child(2){
              display: block;
              float: left;
              width: 100px;
              text-align: left;
            }
          }
          div:nth-child(1){
            color: #000;
            margin-top: 30px;
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
        .cpuData_s{
          width: 180px;
          height: 100px;
          position: absolute;
          z-index: 99;
          top: 50%;
          left: 63%;
          margin-top: -50px;
          margin-left: -90px;
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
              min-width: 90px;
              text-align: right;
              margin-right: 5px;
            }
            span:nth-child(2){
              display: block;
              float: left;
              text-align: left;
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
        .legendContent{
          width: 140px;
          height: 100%;
          position: absolute;
          left: 40%;
          margin-left: -50px;
          top: 0;
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
        .legendContent1{
          width: 140px;
          height: 100%;
          position: absolute;
          left: 85%;
          margin-left: -50px;
          top: 0;
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
  }
</style>

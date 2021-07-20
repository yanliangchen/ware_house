<template>
  <div class="hostViewDetails">
    <div class="header">
      <span class="title">HOST:</span>
      <Select v-model="hid" style="width:200px" @on-change="changeVid">
        <Option v-for="(item,index) in idList" :value="item.value" :key='index'>{{ item.label }}</Option>
      </Select>
      <Button class="button" @click="back">back</Button>
    </div>
    <div class="common"  v-loading="loading3"
        element-loading-text="Loading"
        element-loading-spinner="el-icon-loading">
      <div class="title">CPU Layout</div>
      <div class="content">
        <div class="cpu-content">
          <div class="socket_info">
            <div class="title">
              <span v-for="(item,index) in coreList"  :key="index">{{item}}</span>
            </div>
            <ul class="left" >
              <li v-for="(item,index) in socketList"  :key="index">{{item}}</li>
            </ul>
            <ul class="right" v-for="(val,index) in socketNumList"  :key="index">
              <li  v-for="(item,index) in val"  :key="index">
                <span>
                  [
                    <span style="color:red;font-weight:900" v-if="item.c1.type == 1">{{item.c1.value}}</span>
                    <span style="color:green;font-weight:900" v-if="item.c1.type == 2">{{item.c1.value}}</span>
                    <span style="color:blue;font-weight:900" v-if="item.c1.type == 3">{{item.c1.value}}</span>
                    <span v-if="item.c1.type == 0">{{item.c1.value}}</span>
                    ,
                    <span style="color:red;font-weight:900" v-if="item.c2.type == 1">{{item.c2.value}}</span>
                    <span style="color:green;font-weight:900" v-if="item.c2.type == 2">{{item.c2.value}}</span>
                    <span style="color:blue;font-weight:900" v-if="item.c2.type == 3">{{item.c2.value}}</span>
                    <span v-if="item.c2.type == 0">{{item.c2.value}}</span>
                  ]
                </span>
              </li>
            </ul>
          </div>
          <div class="instance_info">
            <el-table
              :data="instanceData"
              stripe
              border
              style="width: 100%">
              <el-table-column
                label=""
                width="40">
                <template slot-scope="scope">
                  <div v-if='scope.row.type == "free"' style="width:10px;height:10px;background:green"> </div>
                  <div v-if='scope.row.type == "ovs"' style="width:10px;height:10px;background:blue"> </div>
                  <div v-if='scope.row.type == "cpu"' style="width:10px;height:10px;background:red"> </div>
                </template>
              </el-table-column>
              <el-table-column
                prop="vm"
                label="VM"
                show-overflow>
              </el-table-column>
              <el-table-column
                prop="instance"
                label="Instance"
                width="200"
                show-overflow>
              </el-table-column>
              <el-table-column
                prop="vcpu"
                label="vCPU"
                width="200"
                show-overflow>
              </el-table-column>
            </el-table>
          </div>
        </div>
      </div>
    </div>
    <div class="common" v-loading="loading1"
        element-loading-text="Loading"
        element-loading-spinner="el-icon-loading">
      <div class="title">Infra Resource State</div>
      <div class="infraContent">
        <div class="cpart">
          <div class="cpuBox cBox" id="cpuBox"></div>
          <div class="cpuData">
            <div>
              <span>total:</span>
              <span>{{cpu_total}}</span>
            </div>
            <div>
              <span>used:</span>
              <span>{{cpu_used}}</span>
            </div>
            <div>
              <span>free:</span>
              <span>{{cpu_free}}</span>
            </div>
          </div>
        </div>
        <div class="cpart">
          <div class="memBox cBox" id="memBox"></div>
          <div class="cpuData">
            <div>
              <span>total:</span>
              <span>{{mem_total}} MB</span>
            </div>
            <div>
              <span>used:</span>
              <span>{{mem_used}} MB</span>
            </div>
            <div>
              <span>free:</span>
              <span>{{mem_free}} MB</span>
            </div>
          </div>
        </div>
        <div class="cpart">
          <div class="diskBox cBox" id="diskBox"></div>
          <div class="cpuData">
            <div>
              <span>total:</span>
              <span>{{disk_total}} GB</span>
            </div>
            <div>
              <span>used:</span>
              <span>{{disk_used}} GB</span>
            </div>
            <div>
              <span>free:</span>
              <span>{{disk_free}} GB</span>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="common" v-loading="loading2"
        element-loading-text="Loading"
        element-loading-spinner="el-icon-loading">
      <div class="title">Interface driver/firmware</div>
      <div class="content Interface">
        <div class="Interface_header">
          <div class="tabs">
            <div @click="changeInterface(1)" :class="{ 'activedBut': isActive }">statistics</div>
            <div>|</div>
            <div @click="changeInterface(0)" :class="{ 'activedBut': !isActive }">driver/firmware</div>
          </div>
        </div>
        <div class="Interface_content" v-show="isActive">
          <div class="tableBox">
            <el-table
              :data="staticData"
              :header-cell-style="{background:'#E6E9F2',color:'#8c8c8c'}"
              border
              empty-text="No data"
              ref="multipleTable"
              tooltip-effect="dark"
              style="width: 100%">
              <el-table-column
                prop="interface"
                min-width="90"
                label="Interface"
                show-overflow-tooltip>
              </el-table-column>
              <el-table-column
                prop="mac"
                min-width="130"
                show-overflow-tooltip
                label="Mac">
              </el-table-column>
              <el-table-column
                prop="pci_number"
                min-width="130"
                show-overflow-tooltip
                label="PCI Number">
              </el-table-column>
              <el-table-column
                prop="rx_packets"
                show-overflow-tooltip
                label="rx_packets">
              </el-table-column>
              <el-table-column
                prop="rx_errors"
                show-overflow-tooltip
                label="rx_errors">
              </el-table-column>
              <el-table-column
                prop="rx_dropped"
                show-overflow-tooltip
                label="rx_dropped">
              </el-table-column>
              <el-table-column
                prop="tx_packets"
                show-overflow-tooltip
                label="tx_packets">
              </el-table-column>
              <el-table-column
                prop="tx_errors"
                show-overflow-tooltip
                label="tx_errors">
              </el-table-column>
              <el-table-column
                prop="tx_dropped"
                show-overflow-tooltip
                label="tx_dropped">
              </el-table-column>
            </el-table>
          </div>
        </div>
        <div class="Interface_content" v-show="!isActive">
          <div class="tableBox">
            <el-table
              :data="firmwareData"
              :header-cell-style="{background:'#E6E9F2',color:'#8c8c8c'}"
              border
              empty-text="No data"
              ref="multipleTable"
              tooltip-effect="dark"
              style="width: 100%">
              <el-table-column
                prop="interface"
                width="100"
                label="Interface"
                show-overflow-tooltip>
              </el-table-column>
              <el-table-column
                prop="mac"
                width="150"
                show-overflow-tooltip
                label="Mac">
              </el-table-column>
              <el-table-column
                prop="pci_number"
                width="150"
                show-overflow-tooltip
                label="PCI Number">
              </el-table-column>
              <el-table-column
                prop="driver"
                width="120"
                show-overflow-tooltip
                label="driver">
              </el-table-column>
              <el-table-column
                prop="driver_info"
                width="120"
                show-overflow-tooltip
                label="driver info">
              </el-table-column>
              <el-table-column
                prop="firmware_version"
                show-overflow-tooltip
                label="firmware version">
              </el-table-column>
              <el-table-column
                prop="desc"
                show-overflow-tooltip
                label="Description">
              </el-table-column>
            </el-table>
          </div>
        </div>
      </div>
    </div>
    <!-- <div class="common">
      <div class="title">Iptables</div>
      <div class="content">

      </div>
    </div>
    <div class="common">
      <div class="title">Docker Services</div>
      <div class="content"></div>
    </div> -->
  </div>
</template>

<script>
import { getLayout,getInfra,getInterface } from "@/api/hostView"
export default {
  name: 'hostViewDetails',
  data () {
    return {
      cid:'',
      hid:'',
      idList:[],
      instanceData:[],
      socketNumList:[],
      coreList:[],
      cpu_total:'0',
      cpu_used:'0',
      cpu_free:'0',
      mem_total:'0',
      mem_used:'0',
      mem_free:'0',
      disk_total:'0',
      disk_used:'0',
      disk_free:'0',
      isActive:true,
      staticData:[],
      socketList:[],
      firmwareData:[],
      loading1:false,
      loading2:false,
      loading3:false
    }
  },
  mounted(){
    let dataCenter  = JSON.parse(sessionStorage.getItem('dataCenter'));
    this.cid = dataCenter.id;
    let hostViewIDs = JSON.parse(sessionStorage.getItem('hostViewIDs'));
    let tempList= [];
    hostViewIDs.forEach(res => {
      tempList.push({
        value:res.id,
        label:res.host,
      })
    });
    if(tempList.length>0){
      this.hid = tempList[0].value;
    }
    this.idList = tempList;
    this.getLayoutData();
    this.getInfraData();
    this.getInterfaceData();
  },
  methods:{
    //切换hid
    changeVid(id){
      this.hid = id;
      this.getLayoutData();
      this.getInfraData();
      this.getInterfaceData();
    },
    //CPU Layout
    async getLayoutData(){
      let {cid,hid} = this;
      let params = {
        cid:cid,
        hid:hid
      };
      this.loading3 = true;
      let res = await getLayout(params);

      let dat = {
        "code": 200,
        "data": {
          "cpu_free_info": {
              "socket 0": [
                  "3",
                  "35"
              ],
              "socket 1": [
                  "51",
                  "19"
              ]
          },
          "instance_info": [
              {
                  "instance": "instance-00000737",
                  "vcpu": [
                      "21",
                      "53",
                      "29",
                      "61",
                      "22",
                      "54",
                      "31",
                      "63",
                      "20",
                      "52",
                      "28",
                      "60",
                      "23",
                      "55",
                      "25",
                      "57",
                      "24",
                      "56",
                      "30",
                      "62",
                      "26",
                      "58",
                      "18",
                      "50",
                      "27",
                      "59"
                  ],
                  "vm": "worker-worker-1-ma9eda1"
              },
              {
                  "instance": "instance-00000734",
                  "vcpu": [
                      "13",
                      "45",
                      "47",
                      "15",
                      "5",
                      "37",
                      "38",
                      "6",
                      "44",
                      "12",
                      "36",
                      "4",
                      "10",
                      "42",
                      "39",
                      "7",
                      "46",
                      "14",
                      "9",
                      "41",
                      "8",
                      "40",
                      "43",
                      "11",
                      "2",
                      "34"
                  ],
                  "vm": "worker-worker-0-ma9eda1"
              }
          ],
          "ovs_info": {
              "socket 0": [
                  "1",
                  "33"
              ],
              "socket 1": [
                  "49",
                  "17"
              ]
          },
          "socket_info": {
              "socket 0": {
                  "Core0": [
                      0,
                      32
                  ],
                  "Core1": [
                      1,
                      33
                  ],
                  "Core10": [
                      10,
                      42
                  ],
                  "Core11": [
                      11,
                      43
                  ],
                  "Core12": [
                      12,
                      44
                  ],
                  "Core13": [
                      13,
                      45
                  ],
                  "Core14": [
                      14,
                      46
                  ],
                  "Core15": [
                      15,
                      47
                  ],
                  "Core2": [
                      2,
                      34
                  ],
                  "Core3": [
                      3,
                      35
                  ],
                  "Core4": [
                      4,
                      36
                  ],
                  "Core5": [
                      5,
                      37
                  ],
                  "Core6": [
                      6,
                      38
                  ],
                  "Core7": [
                      7,
                      39
                  ],
                  "Core8": [
                      8,
                      40
                  ],
                  "Core9": [
                      9,
                      41
                  ]
              },
              "socket 1": {
                  "Core0": [
                      16,
                      48
                  ],
                  "Core1": [
                      17,
                      49
                  ],
                  "Core10": [
                      26,
                      58
                  ],
                  "Core11": [
                      27,
                      59
                  ],
                  "Core12": [
                      28,
                      60
                  ],
                  "Core13": [
                      29,
                      61
                  ],
                  "Core14": [
                      30,
                      62
                  ],
                  "Core15": [
                      31,
                      63
                  ],
                  "Core2": [
                      18,
                      50
                  ],
                  "Core3": [
                      19,
                      51
                  ],
                  "Core4": [
                      20,
                      52
                  ],
                  "Core5": [
                      21,
                      53
                  ],
                  "Core6": [
                      22,
                      54
                  ],
                  "Core7": [
                      23,
                      55
                  ],
                  "Core8": [
                      24,
                      56
                  ],
                  "Core9": [
                      25,
                      57
                  ]
              }
          }
        },
        "status": true
      }
      let {data,code} = res.data;
      //let {data,code} = dat;
      this.loading3 = false;
      if(code == 200 && data){
        let tempData = data;
        //右侧
        let tempInstance = tempData.instance_info;
        let {cpu_free_info,ovs_info} = tempData;
        tempInstance.forEach(res=>{
          res.vcpu = res.vcpu.join(',')
          res.type="cpu";
        });
        let tcpu_free_info =[],tovs_info =[],t=[],b=[],t1=[],b1=[];
        Object.keys(tempData.cpu_free_info).forEach(function(key){
          t.push(tempData.cpu_free_info[key]);
        });
        t.forEach(res=>{
          if(res.length>0){
            b.push(res.join(','))
          }
        })
        tcpu_free_info.push({
          type:'free',
          instance:'',
          vm:'free for VM',
          vcpu:b.join(',')
        });
        Object.keys(tempData.ovs_info).forEach(function(key){
          t1.push(tempData.ovs_info[key]);
        });
        t1.forEach(res=>{
          if(res.length>0){
            b1.push(res.join(','))
          }
        })
        tovs_info.push({
          type:'ovs',
          instance:'',
          vm:'ovs',
          vcpu:b1.join(',')
        });
        let tempO = tempInstance.concat(tcpu_free_info);
        tovs_info.forEach(res=>{
          tempO.unshift(res)
        });
        this.instanceData = tempO;

        let redCpu = [],tempRedcpu=[],blueOvs = [],tempblueOvs=[],greenFree = [],tempgreenFree=[];
        tempInstance.forEach(res=>{
          redCpu.push(res.vcpu);
        });
        redCpu.forEach(res=>{
          tempRedcpu = tempRedcpu.concat(res.split(","));
        });
        tcpu_free_info.forEach(res=>{
          greenFree.push(res.vcpu);
        });
        greenFree.forEach(res=>{
          tempgreenFree = tempgreenFree.concat(res.split(","));
        });
        tovs_info.forEach(res=>{
          blueOvs.push(res.vcpu);
        });
        blueOvs.forEach(res=>{
          tempblueOvs = tempblueOvs.concat(res.split(","));
        });
        //左侧
        let tempCore = Object.keys(tempData.socket_info);
        
        let newTempCore = [],newTempCore1 = [];
        tempCore.forEach(res=>{
          newTempCore.push(res.substring(6))
        })
        function compare(a, b) {
          return a - b;
        }
        newTempCore = newTempCore.sort(compare);
        newTempCore.forEach(res=>{
          newTempCore1.push('socket' + res);
        });
        if(newTempCore1.length>0){
          let tempsocket = tempData.socket_info[newTempCore1[0]];
          let socketList = Object.keys(tempsocket);
          let tempsocketList = [],tempsocketList1 = [];
          socketList.forEach(res=>{
            tempsocketList.push(res.substring(4))
          })
          tempsocketList = tempsocketList.sort(compare);
          tempsocketList.forEach(res=>{
            tempsocketList1.push('Core' + res);
          });
          this.socketList = tempsocketList1;
          let tempNumList = [];
          newTempCore1.forEach(function(key){
            let temp =tempData.socket_info[key];
            socketList.forEach(val=>{
              let cpuNum = {
                c1:{
                  value:temp[val][0],
                  type:0
                },
                c2:{
                  value:temp[val][1],
                  type:0
                }
              };
              tempNumList.push(cpuNum)
            })
          });
          //分割数组
          function chunkArray(array, size) {
            //获取数组的长度，如果你传入的不是数组，那么获取到的就是undefined
            const length = array.length
            //判断不是数组，或者size没有设置，size小于1，就返回空数组
            if (!length || !size || size < 1) {
              return []
            }
            //核心部分
            let index = 0 //用来表示切割元素的范围start
            let resIndex = 0 //用来递增表示输出数组的下标
          
            //根据length和size算出输出数组的长度，并且创建它。
            let result = new Array(Math.ceil(length / size))
            //进行循环
            while (index < length) {
              //循环过程中设置result[0]和result[1]的值。该值根据array.slice切割得到。
              result[resIndex++] = array.slice(index, (index += size))
            }
            //输出新数组
            return result
          }
          if(tempRedcpu.length > 0){
            let numLength = tempNumList.length;
            let cpuLength = tempRedcpu.length;
            let freeLength =tempgreenFree.length;
            let ovsLength =tempblueOvs.length;
            for(let i = 0; i < numLength; i++) {
              let numItem = tempNumList[i];
              for (let j = 0; j < cpuLength; j++) {
                  let cpuItem = tempRedcpu[j]
                  let {c1,c2} = numItem;
                  if (c1.value == cpuItem) {
                      c1.type = 1;
                  }else if(c2.value == cpuItem) {
                      c2.type = 1;
                  }
              }
              for (let k = 0; k <freeLength ; k++) {
                  let freeItem =tempgreenFree[k]
                  let {c1,c2} = numItem;
                  if (c1.value == freeItem) {
                      c1.type = 2;
                  }else if(c2.value == freeItem) {
                      c2.type = 2;
                  }
              }
              for (let w = 0; w <ovsLength; w++) {
                  let ovsItem =tempblueOvs[w]
                  let {c1,c2} = numItem;
                  if (c1.value == ovsItem) {
                      c1.type = 3;
                  }else if(c2.value == ovsItem) {
                      c2.type = 3;
                  }
              }
            }
            this.socketNumList =  chunkArray(tempNumList,socketList.length);
          }else{
            this.socketNumList = chunkArray(tempNumList,socketList.length);
          };
        }
        this.coreList = newTempCore1;
      }
    },
    //Infra Resource State
    async getInfraData(){
      let {cid,hid} = this;
      let params = {
        cid:cid,
        hid:hid
      };
      this.loading1 = true;
      let res = await getInfra(params);
      this.loading1 = false;
      this.$nextTick(function(){
        let {data,code} = res.data;
        if(code == 200 && data){
          let {total_cpu,total_ram,total_rom,used_cpu,used_ram,used_rom} = data;
          total_cpu = this.$util.formatString(total_cpu);
          total_ram = this.$util.formatString(total_ram);
          total_rom = this.$util.formatString(total_rom);
          used_cpu = this.$util.formatString(used_cpu);
          used_ram = this.$util.formatString(used_ram);
          used_rom = this.$util.formatString(used_rom);
          this.cpu_total = total_cpu;
          this.cpu_used = used_cpu;
          this.cpu_free = total_cpu - used_cpu;

          this.mem_total = total_rom;
          this.mem_used = used_rom;
          this.mem_free = total_rom - used_rom;
          
          this.disk_total = total_ram;
          this.disk_used = used_ram;
          this.disk_free = total_ram - used_ram;

          //cpu
          let myChart = this.$echarts.init(document.getElementById('cpuBox'));
          let option = {
            title: {
              text: 'CPU',
              left: 'center',
              top:0
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
            legend: {
              y: 'bottom',  //图例上下居中
              selectedMode: false,
              data: ['used', 'free']
            },
            color:['#A9D18E','#A6A6A6'],
            series: [
              {
                name: 'CPU',
                type: 'pie',
                radius: ['50%', '70%'],
                center: ['50%', '50%'], //图的位置，距离左跟上的位置
                label: {
                  formatter: '{d}%'
                },
                itemStyle:{
                  borderWidth:2, //设置border的宽度有多大
                  borderColor:'#fff',
                },
                data: [
                  {value: total_cpu - used_cpu, name: 'free'},
                  {value: used_cpu, name: 'used'}
                ]
              }
            ]
          }
          myChart.setOption(option,true);
          //memory
          let myChart1 = this.$echarts.init(document.getElementById('memBox'));
          let option1 = {
            title: {
              text: 'Memory',
              left: 'center',
              top:0
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
            legend: {
              y: 'bottom',  //图例上下居中
              selectedMode: false,
              data: ['used', 'free']
            },
            color:['#A9D18E','#A6A6A6'],
            series: [
              {
                name: 'CPU',
                type: 'pie',
                radius: ['50%', '70%'],
                center: ['50%', '50%'], //图的位置，距离左跟上的位置
                label: {
                  formatter: '{d}%'
                },
                itemStyle:{
                  borderWidth:2, //设置border的宽度有多大
                  borderColor:'#fff',
                },
                data: [
                  {value: total_ram - used_ram, name: 'free'},
                  {value: used_ram, name: 'used'}
                ]
              }
            ]
          }
          myChart1.setOption(option1,true);
          //disk
          let myChart2 = this.$echarts.init(document.getElementById('diskBox'));
          let option2 = {
            title: {
              text: 'Local disk',
              left: 'center',
              top:0
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
            legend: {
              y: 'bottom',  //图例上下居中
              selectedMode: false,
              data: ['used', 'free']
            },
            color:['#A9D18E','#A6A6A6'],
            series: [
              {
                name: 'CPU',
                type: 'pie',
                radius: ['50%', '70%'],
                center: ['50%', '50%'], //图的位置，距离左跟上的位置
                label: {
                  formatter: '{d}%'
                },
                itemStyle:{
                  borderWidth:2, //设置border的宽度有多大
                  borderColor:'#fff',
                },
                data: [
                  {value: total_rom - used_rom, name: 'free'},
                  {value: used_rom, name: 'used'}
                ]
              }
            ]
          }
          myChart2.setOption(option2,true);
        };
      })
    },
    //Interface driver/firmware
    async getInterfaceData(){
      let {cid,hid} = this;
      let params = {
        cid:cid,
        hid:hid
      };
      this.loading2 = true;
      let res = await getInterface(params);
      this.loading2 = false;
      let {code,data} = res.data;
      if(code == 200 && data){
        let tempfirmware = data.firmware;
        let tempstatic = data.static;
        if(tempfirmware){
          let newtempstatic = [],newtempfirmware = [];
          Object.keys(tempstatic).forEach(function(key){
            newtempstatic.push(tempstatic[key])
          });
          newtempstatic.forEach(res=>{
            res.rx_dropped = (res.rx_dropped).toString();
            res.rx_errors = (res.rx_errors).toString();
            res.tx_dropped = (res.tx_dropped).toString();
            res.tx_errors = (res.tx_errors).toString();
            res.tx_packets = (res.tx_packets).toString();
          })
          this.staticData = newtempstatic;

          
          Object.keys(tempfirmware).forEach(function(key){
            newtempfirmware.push(tempfirmware[key])
          });
          this.firmwareData = newtempfirmware;
        }
      }
    },
    changeInterface(type){
      if(type == 1){
        this.isActive = true;
      }else{
        this.isActive = false;
      }
    },
    back(){
      this.$goRoute('/hostView')
    }
  }
}
</script>

<style lang="scss">
  .hostViewDetails{
    .el-table--border td, .el-table--border th, .el-table__body-wrapper .el-table--border.is-scrolling-left~.el-table__fixed{
      border-right: none;
    }
  }
</style>
<style scoped lang="scss">
  .hostViewDetails{
    width: 100%;
    height: 100%;
    color: #000;
    .header{
      width: 100%;
      height: 50px;
      padding: 0 1rem;
      line-height: 50px;
      .title{
        font-size: 16px;
        font-weight: 700;
        margin-right: 10px;
      }
      .button{
        float:right;
        margin-top: 10px;
      }
    }
    
    .common{
      width: 100%;
      height: 400px;
      min-height: 400px;
      border-bottom: 1px solid #ddd;
      .title{
        width: 100%;
        height: 40px;
        line-height: 40px;
        font-size: 16px;
        font-weight: 500;
        padding-left: 20px;
      }
      .content{
        width: 100%;
        height: 100%;
        .cpu-content{
          width: 100%;
          height: 70%;
          .socket_info{
            height: 100%;
            width: 44.5%;
            float: left;
            margin-right: 1%;
            border: 1px solid #ddd;
            margin-top: 20px;
            overflow: auto;
            .title{
              width: 100%;
              height: 30px;
              line-height: 30px;
              padding-left: 130px;
              span{
                width: 80px;
                text-align: center;
                display: inline-block;
              }
            }
            .left{
              width: 120px;
              height: calc(100% - 30px);
              text-align: center;
              float: left;
              padding-left: 15px;
              text-align: right;
              padding-right: 20px;
              li{
                width: 100%;
                height: 20px;
                line-height: 20px;
              }
            }
            .right{
              width: 85px;
              padding-left: 10px;
              height: calc(100% - 30px);
              text-align: center;
              float: left;
              li{
                width: 80px;
                float: left;
                height: 20px;
                line-height: 20px;
              }
            }
          }
          .instance_info{
            height: 100%;
            width: 54.5%;
            float: left;
            border: 1px solid #ddd;
            margin-top: 20px;
            overflow: auto;
          }
        }
      }
      .infraContent{
        width: 100%;
        height: calc(100% - 40px);
        .cpart{
          width: calc(33.3% - 30px);
          height: 90%;
          margin: 10px;
          border: 1px solid #ddd;
          position: relative;
          float: left;
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
            left: 50%;
            margin-top: -50px;
            margin-left: -50px;
            overflow: auto;
            div{
              width: 100%;
              height: 20px;
              line-height: 20px;
              display: flex;
              justify-content: center;
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
              color: #A9D18E;
            }
            div:nth-child(3){
              color: #A6A6A6;
            }
            span{
              font-size: .7rem;
              font-weight: 500;
            }
          }
        }
      }
      .Interface{
        width: 100%;
        height: 100%;
        .Interface_header{
          width: 100%;
          height: 40px;
          line-height: 40px;
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
            left: 30px;
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
        .Interface_content{
          width: 100%;
          height: 320px;
          .tableBox{
            padding: 10px;
          }
        }
      }
    }
  }
</style>

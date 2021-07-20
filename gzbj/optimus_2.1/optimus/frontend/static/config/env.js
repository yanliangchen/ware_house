/**
 * 项目环境配置
 * 在 index.html 中引入
 * 用于解决webpack根据引用，会打包一切被引用资源的问题
 */
(function () {
  "use strict";
  if (!("KYCFG" in window)) {
    window.KYCFG = {
      dapiUrl: 'http://localhost:9000', // 开发环境api 地址
      //dapiUrl: 'http://10.196.36.29:9000', // 开发环境api 地址
      papiUrl: 'http://100.98.97.86:9000', // 生成环境api 地址
    }
  }
})();

import Vue from 'vue'
import Router from 'vue-router'


Vue.use(Router)

// const originalPush = Router.prototype.push
// Router.prototype.push = function push(location) {
//   return originalPush.call(this, location).catch(err => err)
// }

//首页
const Home = ()=>import("@/components/Home");

//登录
const Login = ()=>import("@/components/Login");

//ToolSelection
const ToolSelection = ()=>import("@/components/ToolSelection");

//YamlGenerator
const YamlGenerator = ()=>import("@/components/YamlGenerator/yamlGenerator");

//Toolbox
const Toolbox = ()=>import("@/components/Toolbox/Toolbox");

//Ericic
const Ericic = ()=>import("@/components/Ericic/Ericic");

//ericicLogin
const ericicLogin = ()=>import("@/components/Ericic/ericicLogin/ericicLogin");

//ericicLogin => show
const ericicShow = ()=>import("@/components/Ericic/ericicLogin/ericicShow");

//ericicLogin => edit
const ericicEdit = ()=>import("@/components/Ericic/ericicLogin/ericicEdit");

//ericicLogin => new
const ericicNew = ()=>import("@/components/Ericic/ericicLogin/ericicNew");

//ericicContent => overview
const overview = ()=>import("@/components/Ericic/ericicContent/overview/overview");

//ericicContent => Infrastrucure
const Infrastrucure = ()=>import("@/components/Ericic/ericicContent/overview/Infrastrucure");

//ericicContent => tenant
const tenant = ()=>import("@/components/Ericic/ericicContent/overview/tenant");

//vmView
const vmView = ()=>import("@/components/Ericic/ericicContent/vmView/vmView");

//vmViewDeatils
const vmViewDeatils = ()=>import("@/components/Ericic/ericicContent/vmView/vmViewDeatils");

//neutronPort
const neutronPort = ()=>import("@/components/Ericic/ericicContent/vmView/neutronPort");

//hostView
const hostView = ()=>import("@/components/Ericic/ericicContent/hostView/hostView");

//hostViewDetails
const hostViewDetails = ()=>import("@/components/Ericic/ericicContent/hostView/hostViewDetails");

//history
const history = ()=>import("@/components/Ericic/ericicContent/history");

//record
const record = ()=>import("@/components/Ericic/ericicContent/record");

const router = new Router({
  routes: [
    {
      path: '/Login',
      name: 'Login',
      component: Login
    },
    {
      path: '/Home',
      name: 'Home',
      component: Home,
      redirect: '/ToolSelection',
      children: [
        {
          path: '/ToolSelection',
          name:'ToolSelection',
          component: ToolSelection
        },
        {
          path: '/YamlGenerator',
          name:'YamlGenerator',
          component: YamlGenerator
        },
        {
          path: '/Toolbox',
          name:'Toolbox',
          component: Toolbox
        },
        {
          path: '/Ericic',
          name:'Ericic',
          component: Ericic,
          redirect: '/ericicLogin',
          children:[
            {
              path: '/ericicLogin',
              name:'ericicLogin',
              component: ericicLogin
            },
            {
              path: '/ericicShow',
              name:'ericicShow',
              component: ericicShow
            },
            {
              path: '/ericicEdit',
              name:'ericicEdit',
              component: ericicEdit
            },
            {
              path: '/ericicNew',
              name:'ericicNew',
              component: ericicNew
            },
            {
              path: '/overview',
              name:'overview',
              component: overview,
              redirect: '/Infrastrucure',
              children:[
                {
                  path: '/Infrastrucure',
                  name:'Infrastrucure',
                  component: Infrastrucure
                },
                {
                  path: '/tenant',
                  name:'tenant',
                  component: tenant
                }
              ]
            },
            {
              path: '/vmView',
              name:'vmView',
              component: vmView
            },
            {
              path: '/vmViewDeatils',
              name:'vmViewDeatils',
              component: vmViewDeatils
            },
            {
              path: '/neutronPort',
              name:'neutronPort',
              component: neutronPort
            },
            {
              path: '/hostView',
              name:'hostView',
              component: hostView
            },
            {
              path: '/hostViewDetails',
              name:'hostViewDetails',
              component: hostViewDetails
            },
            {
              path: '/history',
              name:'history',
              component: history
            },
            {
              path: '/record',
              name:'record',
              component: record
            }
          ]
        }
      ]
    },
  ]
})

//注册全局前置守卫  未登录或失去登录信息时 跳转到登录页面
router.beforeEach((to, from, next) => {
  if (to.path == '/Login') {
    sessionStorage.removeItem('user');
    sessionStorage.removeItem('token');
  }
  let user = sessionStorage.getItem('user');

  if (!user && to.path != '/Login') {
    next({
      path: '/Login'
    })
  } else {
    //Vue.prototype.resetSetItem('watchStorage', true);//全局触发 监听sessionStorge
    next()
  }
});

export default router;

<template>
  <div class="loginBox">
    <div class="login_logo"></div>
    <div class="login_showboard_bg"></div>
    <div class='login_logo_optimus'></div>
    <div class="login_ipt_area">
      <div class="login_title">{{key ? 'Enterprise sign in' :'Register'}}</div>
      <md-field md-clearable>
        <label>{{key ? 'User Id' :'New User Name'}}</label>
        <md-input v-model="initial"></md-input>
        <span class="md-error tip1" v-if="errUserStatus">{{key ?errUser :errUser1}}</span>
      </md-field>
      <md-field>
        <label>{{key ? 'Password' :'New Password'}}</label>
        <md-input v-model="password" type="password" @keyup.enter.native="login"></md-input>
        <span class="md-error tip2" v-if="errPasswordStatus">{{key ?errPassword :errPassword1}}</span>
      </md-field>
      <md-button class="md-raised md-primary custom-button signButton"  @click="login">{{key ? 'Sign In' :'CREATE ACCOUNT'}}</md-button>
      <div class="login_bottom_help">
        <span>{{key ? "Don't have an account?" :'Have an account already?'}}</span>
        <a class="hand" @click="changeStatus">{{key ? 'Sign up' :'Back to login'}}</a>
      </div>
    </div>
  </div>
</template>
<script>
import { login,sign } from "@/api/login"
export default {
  name: 'Login',
  data () {
    return {
      initial: '',
      password: '',
      key:true,
      errUserStatus:false,
      errUser:'User Id is empty!',
      errUser1:'New User Name is empty!',
      errPasswordStatus:false,
      errPassword:'Password is empty!',
      errPassword1:'New Password is empty!'
    }
  },
  watch:{
    // initial(e){
    //   if(e.trim() == ''){
    //     this.errUserStatus = true;
    //   }else{
    //     this.errUserStatus = false;
    //   }
    // }
  },
  mounted(){
  },
  methods: {
    //登录
    login(){
      let _this = this;
      let {initial,password,key} = this;
      if(initial.trim() == ''){
        this.errUserStatus = true;
      }else{
        this.errUserStatus = false;
      }
      if(password.trim() == ''){
        this.errPasswordStatus = true;
      }else{
        this.errPasswordStatus = false;
      }
      if(initial.trim() != '' && password.trim() != ''){
        let params = {
          name:initial,
          password:password
        }
        if(key){//key = true ;登录 key = false; 注册页面
          login(params).then(res=>{
            let {code,data} = res.data;
            if(code == 200){
              let {access_token} = data;
              sessionStorage.setItem("token", access_token); //存一个请求头
              sessionStorage.setItem("user", initial);//存用户名 
              _this.$goRoute('/Home');
            }else{
              _this.$message({
                message: 'Login failed!',
                duration:1800,
                type: 'error',
                center: true
              });
            }
          })
        }else{
          sign(params).then(res=>{
            let {code} = res.data;
            if(code == 201){
              _this.$message({
                message: 'Sign success!',
                duration:1800,
                type: 'success',
                center: true
              });
              _this.key = true;
            }else{
              _this.$message({
                message: 'Sign failed!',
                duration:1800,
                type: 'error',
                center: true
              });
            }
          })
        }
      }
    },
    changeStatus(){
      this.key = !this.key;
    }
  },
}
</script>

<style scoped  lang="scss">
  .loginBox{
    width: 100vw;
    height: 100vh;
    overflow: hidden;
    display: flex;
    justify-content: flex-end;
    align-items: center;
    background-color: #1a1a1a;
    .login_showboard_bg{
        display: block;
        .login_slide{
          width: 100%; 
          background-color: rgba(255,255,255, .7);
          .login_slideItem{
            display: flex;
            justify-content: center;
            width:100%;
            height:100%;
            padding: 1rem 1rem 1rem 3rem;
            overflow: hidden;
            .login_slideItemCard{
              width:100%;
              height:100%;
              padding: 2rem 2rem;
            }
          }
        }

        padding:0;
        width:calc(100% - 420px);
        height:100vh;
        overflow: auto;
        // display: flex;
        flex-direction: column;
        &::-webkit-scrollbar {/*隐藏滚轮*/
          display: none;
        }
        @media screen and (min-width:600px){
            
        }
        @media screen and (max-width: 600px){
          display: none;
        }
        background-image:url('/static/img/bg_img.jpg');
        // &::after{
        //     content:'';
        //     position: fixed;
        //     display:block;
        //     z-index: 999;
        //     width:calc(100% - 420px);
        //     height: 100%;
        //     background-color: rgba(255, 255, 255, .6);
        // }
    }
    
    .login_logo{
      z-index: 9999;
      background-size:100% 100%;
      background-repeat:no-repeat;
      @media screen and (min-width:600px){
        background-image: url('/static/img/elogo-dark.svg');
      }
      @media screen and (max-width: 600px){
        background-image: url('/static/img/elogo-light.svg');
      }
      position: absolute;
      top:1.5rem;
      left: 1.5rem;
      width: 2.4rem;
      height: 2.4rem;
      img{
        width: 100%;
        height: 100%;
      }
    }

    .login_logo_optimus{
      width: 40rem;
      height: 12rem;
      position: absolute;
      top: 5rem;
      left: 4rem;
      background-size:100% 100%;
      background-repeat:no-repeat;
      z-index: 99998;
      background-image:url('/static/img/optimus_light.png');
    }

    .login_footer{
      padding:2rem 0;
      position: relative;
      left: 0;
      bottom: 0;
      @media screen and (min-width:600px){
        width:100%;
        height:20rem;
        background-color: #030852;
      }
      @media screen and (max-width: 600px){
        display: none;
      }
      .login_footer_img{
        margin-left: 4rem;
        margin-bottom: 1rem;
        width: 2rem;
        height: 2rem;
        background-size:100% 100%;
        background-repeat:no-repeat;
        background-image: url('/static/img/elogo-light.svg');
      }
      .login_footer_content{
        background-color: #030852;
        display: flex;
        .login_footer_p{
          margin: 0 0 0 4rem;
          p{
            font-size: 1.1rem;
            color: #fafafa;
          }
        }
      }   
    }
    
    .login_ipt_area{
      background-color: #1a1a1a;
      height:100vh;
      display: flex;
      flex-direction: column;
      justify-content: center;
      z-index: 99999;
      @media screen and (min-width:600px){
        width:420px;
        padding:0 3rem;
      }
      @media screen and (max-width: 600px){
        width:100vw;
        padding:0 5rem;
      }
      .login_title{
        padding:0 0 1.5rem 0;
        font-size: 1.6rem;
        color: #FFF;
        font-family: Montserrat,sans-serif,Helvetica Neue,Arial;
      }
      /* 帮助文字 */
      .login_bottom_help{
        display: flex;
        padding-top: 1rem;
        // justify-content: center;
        // padding-left: 2rem;
        span{
          color:#bfbfbf;
          font-family: Montserrat,sans-serif,Helvetica Neue,Arial;
        }
        a{
          margin-left: .5rem;
        }
      }
      /* 底部提示文字 */
      .login_bottom_span{
        white-space: wrap;
        color:#8c8c8c;
        padding-top: 1.5rem;
        font-size: .7rem;
        min-height: 5rem;
      }
      .login_ipt{
        height: 4rem;
        width:100%;
        padding:.5rem 0;
        /* 报错情况下 */
        .Mui-error{
          .MuiOutlinedInput-notchedOutline{
            border-color:#f44336!important;
          }
          .MuiOutlinedInput-input{
            color:#f44336!important;
          }
          & + p{
            color:red;
          }
        }
        /* 正常情况下 */
        .Mui-focused{
          color:#FFF;
        }
        .MuiFormLabel-root{
          color:#595959;
        }
        .MuiInputBase-root{
          .MuiOutlinedInput-input{
            color:#FAFAFA;
          }
          .MuiOutlinedInput-notchedOutline{
            border-color:#FAFAFA;
          }
        }
      }
      
      .signButton{
        margin-top: 10px !important;
      }
    }
  }
</style>

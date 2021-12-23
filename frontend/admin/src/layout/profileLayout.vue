<template>
<div :style="opacity">
<section v-if="accountActive==true">

<div class="container-fluid header">
<div class="row p-1">
<div class="col-md p-0">
</div>
</div>
</div>

<div class="container-fluid">
<div class="row p-1">
<div class="col-md p-0">
   <nav class="navbar navbar-expand-lg p-1 m-1 mt-0 mb-0">
<a class="navbar-brand" href="/app/secure/dashboard" :style="appinfo.css.headercolor"><img src="" :width="appinfo.logoWidth" :height="appinfo.logoHeight"  alt=" "> &nbsp; {{appinfo.appname}}</a>
<span class="navbar-toggler" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
<i class="bi-list"></i>
</span>
<div class="collapse navbar-collapse" id="navbarSupportedContent">
<div style="border-top:1.5px solid #eee"></div>
    <ul class="navbar-nav m-0 p-0 ms-auto">
    </ul>
    <ul class="navbar-nav m-0 p-0 ms-auto">
    <li class="nav-item p-1 pt-0 pb-0"> <a v-bind:class="'nav-link ' + appinfo.f_color" href="/app/site/help"><i class="bi-question-circle" role="img" aria-label="Help" style="font-size: 1.4rem; color: black;"></i></a> </li>
    <li class="nav-item p-1 pt-0 pb-0"> <a v-bind:class="'nav-link ' + appinfo.f_color" href="#"><i class="bi-list" role="img" aria-label="Apps" style="font-size: 1.4rem; color: black;"></i></a> </li>
  
    </ul>
</div>
</nav>
</div>
</div>
</div>

<div class="container">
<div class="row">
    <div class="col-md-2 sidebar p-2 border-end">
        <div class="row">
            <div class="col-md-12">
                <a class="navbar-brand text-white" href="/app/secure/dashboard"> &nbsp; {{appinfo.appname}} </a><img class="float-right" src="" 
                :width="appinfo.logoWidth" :height="appinfo.logoHeight"  alt=" ">
            </div>
        <div class="col-md-12 mt-4 text-center">
            <div class="dp mt-2 mx-auto"></div>
        <big>Welcome, {{userdata['surname']}} </big>
        <big class="text-black">{{userdata['businessName']}} </big>
        <small class="text-black">Administrator</small>

        </div>
        </div>

      <ul class="navbar-nav sidebar-list mt-4">
        <li class="nav-item active"><router-link to="/app/secure/dashboard" class="nav-link"><i class="bi-house m-2 ml-0 mt-0 mb-0" style="font-size: 1.1rem; "></i> Dashboard </router-link></li>
        <hr>
        <!-- <li class="nav-item"><router-link to="/app/secure/dashboard" class="nav-link "><i class="bi-credit-card" style="font-size: 1.1rem;"></i> Subscriptions </router-link></li>
        <li class="nav-item active"><router-link to="#" class="nav-link text-warning"> <strong>Free services</strong> </router-link></li>
        
        <li class="nav-item"><router-link to="/app/secure/dashboard" class="nav-link "><i class="bi-house-fill" style="font-size: 1.1rem;"></i> Production details </router-link></li>
        <li class="nav-item"><router-link to="/app/secure/dashboard" class="nav-link "><i class="bi-credit-card-2-front" style="font-size: 1.1rem;"></i> Financial statistics </router-link></li>
        <li class="nav-item"><router-link to="/app/secure/dashboard" class="nav-link "><i class="bi-cloud" style="font-size: 1.1rem;"></i> Temperature checks </router-link></li>
        <li class="nav-item"><router-link to="/app/secure/dashboard" class="nav-link "><i class="bi-mailbox" style="font-size: 1.1rem;"></i> Reports </router-link></li>
        <li class="nav-item"><router-link to="/app/secure/dashboard" class="nav-link "><i class="bi-house" style="font-size: 1.1rem;"></i> Your farms </router-link></li>
        <hr>
        <li class="nav-item active"><router-link to="#" class="nav-link text-warning"> <strong>Premium services</strong> </router-link></li>
        <li class="nav-item"><router-link to="/app/secure/dashboard" class="nav-link "><i class="bi-camera-video" style="font-size: 1.1rem;"></i> Live stream </router-link></li>
        <li class="nav-item"><router-link to="/app/secure/dashboard" class="nav-link "><i class="bi-people" style="font-size: 1.1rem;"></i> Join community </router-link></li>
        <li class="nav-item"><router-link to="/app/secure/dashboard" class="nav-link "><i class="bi-people" style="font-size: 1.1rem;"></i> Hire experts </router-link></li>
        <li class="nav-item"><router-link to="/app/secure/dashboard" class="nav-link "><i class="bi-bar-chart-steps" style="font-size: 1.1rem;"></i> Suggestions </router-link></li>
        <hr>
        <li class="nav-item"><router-link to="/app/secure/dashboard" class="nav-link "><i class="bi-gear" style="font-size: 1.1rem;"></i> Settings </router-link></li>
       -->

    </ul>
      <ul class="navbar-nav sidebar-list mt-2" v-for="(d, index) in menus" :key="index">
    <li class="nav-item"><router-link :to="'/app/secure/'+d['menuName']" class="nav-link"><i :class="'m-2 ml-0 mt-0 mb-0 '+d['menu_icon']" style="font-size: 1.1rem;"></i> {{d['menu_description']}} </router-link></li>
   </ul>
    
    <ul class="navbar-nav sidebar-list mt-2">
    <li class="nav-item"><router-link to="/app/site/logout" class="nav-link "><i class="m-2 ml-0 mt-0 mb-0 bi-power" style="font-size: 1.1rem;"></i> Logout </router-link></li>
   </ul>
</div>
<div class="col-md-10 offset-md-2 maindiv mt-2 p-0">
<section v-if="ifUserHasAccess=='true'">
    <slot></slot>
</section>
<section v-else>
   <div class="container-fluid">
       <div class="row mt-5 text-center ">
           <div class="col-8 mt-5 mx-auto d-flex justify-content-center">
   <p class="lead mt-2 text-danger" style="line-height:1.5">{{norecord}}</p>
           </div>
 <div class="col-8 mt-5 mx-auto d-flex justify-content-center">
<!-- <p class="m-2" @click="$router.go(-1)" ><a href="#" class="btn btn-outline-primary text-center">  <i class="bi-arrow-left"></i> Back </a></p> -->
           </div>
       </div>
   </div>
</section>
</div>
</div>
</div>
</section>
<section v-else>
   <div class="container-fluid mt-5">
       <div class="row mt-5 text-center ">
           <div class="col-8 mt-5 mx-auto d-flex justify-content-center">
   <p class="lead mt-2 text-danger" style="line-height:1.5">{{norecord}}</p>
           </div>
 <div class="col-8 mt-5 mx-auto d-flex justify-content-center">
<!-- <p class="m-2" @click="$router.go(-1)" ><a href="#" class="btn btn-outline-primary text-center">  <i class="bi-arrow-left"></i> Back </a></p> -->
           </div>
       </div>
   </div>
</section>

</div>
</template>


<style scoped>
.sidebar, .header{
    background: #010314;
    color: #fff;
}

.sidebar-list a{ 
color: #fff;

}
.sidebar-list a i{ 
color: rgb(231, 235, 29);

}
.list-group-item{
    padding-left:4px;
}

.list-group-item i{
    margin-right: 5px;
}
.userlink{
    text-decoration: none;
    color: rgb(59, 56, 56);
}
.active{
border-top-left-radius: 5px;
border-top-right-radius: 5px;
}
</style>
<script>
import appsettings from '../json/myapp.json'
import axios from 'axios'
export default {
    data(){
        return {
            info:[],
            userdata:[],
            menus:[],
            "media":appsettings.media,
            "appinfo":appsettings.appinfo,
            networkerror:appsettings.error.networkerror,
            progress:null,
            accountActive:false,
            ifUserHasAccess:false,
            userid:null,
            page: '',
            pwd:'',
            classname:'',
            isDisabled: false,
            error_btn: null,
            errormodal: null,
            record:false,
            norecord: '',
            loader:false,
            loaderstatus:'',
            
            counter:'0',
            pagename: this.$route.name,
            opacity_enable:'opacity:0.7; pointer-events: none;',
            opacity_disable:'opacity:1; pointer-events:All;',
            opacity:'',
            }
    },
        created(){
        this.setStorage()
        this.auth_check()
        },
    methods:{
       setStorage: function(){
            localStorage.setItem('error', this.networkerror)
        },
     listmenu: function(){
            this.$Progress.start()
            this.isDisabled = true
            this.opacity = this.opacity_enable
        axios.get(process.env.VUE_APP_API+'/api/adminmenu/menus/',{
            params:{

                'pagename':this.pagename
            }
        })
        .then(response => {
            if(response.data.status == response.data.statusmsg){
            this.norecord=response.data.msg
            this.alert=''
            this.classname=''
            this.menus = response.data.result
            this.ifUserHasAccess=response.data.ifUserHasAccess
            this.accountActive = true
            this.$Progress.finish()
            this.isDisabled = false
            this.opacity = this.opacity_disable
            }else{
            this.alert=''
            this.norecord=response.data.msg
            this.classname=''
            this.$Progress.finish()
            this.isDisabled = false
            this.opacity = this.opacity_disable
            }
        
        }).catch(()=>{
            
            this.alert=''
            this.classname=''
            this.norecord=localStorage.getItem('error')
            this.$Progress.finish()
            this.isDisabled = false
            this.opacity = this.opacity_disable
        })
    },

    auth_check: function(){
    this.$Progress.start()
    this.isDisabled = true
    this.opacity = this.opacity_enable
    axios.get(process.env.VUE_APP_API+'/auth/auth_check/')
        .then(response => {
            if(response.data.status==response.data.statusmsg){
                this.userdata = response.data.userdata
                this.accountActive = true
                this.$Progress.finish()
                this.isDisabled = false
                this.opacity = this.opacity_disable
                this.listmenu()
                localStorage.setItem("userdata", response.data.userdata);
                }else{
                this.$Progress.finish()
                this.isDisabled = false
                this.opacity = this.opacity_disable
                this.accountActive = false
                localStorage.removeItem('userdata');
                window.location.href='/app/site/logout'
            }
        }).catch(()=>{
            this.$Progress.finish()
            this.isDisabled = false
            this.opacity = this.opacity_disable
            this.accountActive = false
            this.alert = localStorage.getItem('error')
            localStorage.removeItem("userdata");
            window.location.href='/app/site/logout'
        })
    },



    },

}
</script>
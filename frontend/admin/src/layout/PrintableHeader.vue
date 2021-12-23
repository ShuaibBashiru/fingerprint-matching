<template>
<div :style="opacity">
<section v-if="isSession==true">
<div class="container-fluid menuheader border-bottom borderStyle">
<div class="row">
<div class="col-md-12">
<nav class="navbar navbar-expand-lg">
<span class="navbar-toggler" data-bs-toggle="collapse" data-bs-target="#navbar" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
<i class="bi-list" style="font-size: 2rem; color: black;"></i>
</span>

<a class="navbar-brand p-0 m-0 me-3 ms-md-2 siteStyle" href="/app/secure/dashboard"><img src="@/assets/icons/logo.png" :width="appinfo.logoWidth" :height="appinfo.logoHeight"  alt=" "> &nbsp; {{appinfo.appname}}</a>
<ul class="navbar-nav p-0 m-3 mb-0 mt-0 d-md-none">
    <li class="nav-item"> 
     <div class="dp-top mx-auto">
            <img :src="getEnvUrl+'/userassets/passports/'+passport" alt=".">
        </div>    
    </li>
</ul>
<div class="collapse navbar-collapse" id="navbar">
<div class="pb-1 mt-2 menudivider d-md-none"></div>
 <ul class="navbar-nav ms-auto m-0 p-0 d-md-none d-lg-none" v-for="(d, index) in mainMenu" :key="index">
        <li class="nav-item m-3 mb-1 mt-1 mb-md-0 mt-md-0 me-md-2"> <router-link :to="'/app/secure/'+d['menuName']" class="link-dark nav-link"> {{d['menu_description']}} </router-link></li>
</ul>
<ul class="navbar-nav m-0 p-0 ms-auto">
        <li class="nav-item m-3 mb-md-0 mt-md-0 me-md-2"> <a v-bind:class="'gradient_txt' + appinfo.f_color" href="/app/site/logout"><i class="bi-power" role="img" aria-label="Help" style="font-size: 1.2rem;"></i></a> </li>
        <li class="nav-item m-3 mb-md-0 mt-md-0 me-md-3"> <a v-bind:class="'gradient_txt' + appinfo.f_color" href="/app/site/contact"><i class="bi-question-circle" role="img" aria-label="Help" style="font-size: 1.2rem;"></i></a> </li>
    </ul>
</div>

</nav>
</div>
</div>
</div>

        <div class="container-fluid">
        <div class="row">
        <div class="col-md-2 sidebar shadow mt-5">
        <div class="wrapper p-2 mt-1">
        <div class="row">
        <div class="col-md-12 mt-4 mb-2 text-center position-static">
        <div class="dp mt-2 mx-auto mb-1">
            <img :src="getEnvUrl+'/userassets/passports/'+passport" alt=".">
        </div>
        <p class="lead m-0 p-0 text-primary">Applicant</p> 
        <big>Welcome, {{usersession['surname']}} </big>
        <small>{{usersession['applicant_number']}} </small>
        </div>
        <div class="col-md-12 mt-5">
        <h5 class="pb-1"> <a href="/app/secure/dashboard"><strong>Dashboard</strong> </a></h5>
        </div>
        <div class="border-top"></div>
        <div class="col-md-12 mt-3">
        <ul class="list-unstyled ps-0 ms-1">
        <li class="mb-2">
        <p class="pb-0 mb-1 align-items-center rounded collapsed" data-bs-toggle="collapse" data-bs-target="#application" aria-expanded="false">
        <i class="bi-globe me-1"></i>    Application
        <i class="bi-chevron-down  float-end"></i>
        </p>
        <div class="collapse" id="application">
        <ul class="btn-toggle-nav list-unstyled fw-normal pb-1 small" v-for="(d, index) in application" :key="index">
        <li> <router-link :to="'/app/secure/'+d['menuName']" class="link-dark nav-link"><i class="bi-dash"></i> {{d['menu_description']}} </router-link></li>
        </ul>
        </div>
        </li>  
        </ul>
  
       <div class="border-top my-3"></div>
        <ul class="list-unstyled ps-0 ms-1">
        <li class="mb-1">
        <p class=" pb-0 mb-1 align-items-center rounded collapsed" data-bs-toggle="collapse" data-bs-target="#settings" aria-expanded="false">
        <i class="bi-gear me-1"></i> Settings
        <i class="bi-chevron-down float-end"></i>
        </p>
        <div class="collapse" id="settings">
        <ul class="btn-toggle-nav list-unstyled fw-normal pb-1 small" v-for="(d, index) in settingMenu" :key="index">
        <li> <router-link :to="'/app/secure/'+d['menuName']" class="link-dark nav-link"><i class="bi-dash"></i> {{d['menu_description']}} </router-link></li>
        </ul>
        </div>
        </li>  
        </ul>  
        </div>
        </div>

        </div>

        </div>
        <div class="col-md-10 offset-md-2">
        <div class="col-md-12 mb-3 mt-1">
            <section v-if="alert!=''">
            <div v-bind:class="'alert '+ classname +' p-2 ps-3 pe-3 m-0 mb-1 mt-1 text-center border-0'"> <span></span> {{alert}} </div>
            </section>
       </div>
        <section v-if="ifUserHasAccess==true">
        <div class="ms-md-3 me-md-3 p-md-3">
                <slot></slot>
        </div>
        </section>
        <section v-else>
        <div class="container-fluid">
        <div class="row mt-5 text-center ">
        <div class="col-8 mt-5 mx-auto d-flex justify-content-center">
        <p class="lead mt-2 text-primary"><span>{{norecord}}</span></p>
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
        <div class="col-md-8 mt-5 mx-auto d-flex justify-content-center">
        <p class="mt-2 text-primary"><span>{{norecord}}</span></p>
        </div>
        </div>
        </div>
        </section>

</div>
</template>


<script>
import appsettings from '../json/myapp.json'
import axios from 'axios'
export default {
        data(){
        return {
        info:[],
        alert: '',
        isSession: false,
        formStatus: false,
        usersession:'',
        getEnvUrl: process.env.VUE_APP_API,
        passport: '',
        menus:[],
        mainMenu: [
            {"menuName":'dashboard', 'menu_description':'Dashboard'},
            {"menuName":'downloadappform', 'menu_description':'Download form'},
            // {"menuName":'dashboard', 'menu_description':'Settings'},
            ],
        application: [
            {"menuName":'applicationform', 'menu_description':'Download form'},
            ],
        webcontent:[],
        users:[],
        admin:[],
        settingMenu:[],
        mailing:[],
        loan:[],
        payment:[],
        upload:[],
        "settings":appsettings.settings,
        "appinfo":appsettings.appinfo,
        networkerror:appsettings.error.networkerror,
        progress:null,
        accountActive:false,
        ifUserHasAccess:true,
        userid:null,
        page: '',
        pwd:'',
        classname:'alert-danger',
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
        interval: '',
        }
        },

        mounted: function(){
        this.checkSession()
        this.setStorage()
        this.auth_check()
        this.preview()
      
        },
        methods:{
        checkSession: function(){
        if (!this.$session.exists()) {
            window.location='/app/site/logout'
            }else{
                if(this.$session.get('usersession')){
                this.isSession = true
                   this.usersession = this.$session.get('usersession')
                    this.passport = this.usersession['applicant_number'].toLowerCase()+'.png'
                }else{
                    window.location='/app/site/logout'
                }
            }
    },
        setStorage: function(){
        localStorage.setItem('error', this.networkerror)
        },
       
        auth_check: function(){
        this.$Progress.start()
        this.isDisabled = true
        this.opacity = this.opacity_enable
        axios.get(process.env.VUE_APP_API+'/auth/auth_check/auth_check',{
        params: {
        pagename: this.pagename,
        userid: this.usersession['email_one'],
        }
        })
        .then(response => {
        if(response.data.status==response.data.statusmsg){
        this.accountActive = true
        this.$Progress.finish()
        this.isDisabled = false
        this.opacity = this.opacity_disable
        }else{
        this.classname=response.data.classname
        this.alert=response.data.msg
        this.$Progress.finish()
        this.isDisabled = false
        this.opacity = this.opacity_disable
        this.accountActive = false
        this.$session.destroy()
        setTimeout(function(){
            window.location.href=response.data.redirect
        },3000)
        }
        }).catch(()=>{
        this.$Progress.finish()
        this.isDisabled = false
        this.opacity = this.opacity_disable
        this.accountActive = false
        this.alert = 'Your session has expired, logging you out...'
        this.$session.destroy()
        setTimeout(function(){
            window.location.href='/app/site/logout'
        },3000)
        })
        },


        },

}
</script>
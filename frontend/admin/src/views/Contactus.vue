<template>
    <div>
         <GeneralHeader>
        <div class="container mb-5">
            <div class="row mb-md-5">
                <div class="col-md-12 ps-2">
                     <div class="m-md-4 mt-5">
                    <h2 class="display-3"> Hi, how can we help? </h2>
                     </div>
                    </div>
            </div>

                   <div class="row">
        <div class="col-md-6">
                   <div class="m-md-4 mt-5">
                        <h3>Help & Support</h3>
                    <p class="lead">Have questions or need to report an issue with our services, suggestions and enquiries? We've got you covered. </p>
                <a class="nav-link ps-0" :href="'mailto:' + settings['email_one']"><button class="btn btn-outline-primary">Write us a message</button></a>
               </div>
                </div>

                <div class="col-md-6">
             <div class="m-md-4 mt-5">
                <h3>Contacts</h3>
                <p class="lead"></p>
                <a class="nav-link ps-0" :href="'mailto:'+settings['email_one']">Email:  {{settings['email_one']}}</a>
                <a class="nav-link ps-0" :href="'tel:'+settings['phone_one']">Phone: {{settings['phone_one']}}</a>
             </div>
                </div>
            </div>
        <div class="row">
                <div class="col-md-6">
                  <div class="m-md-4 mt-5">
                        <h3> Address </h3>
                    <p class="lead">
                    {{settings['address']}}</p>
                  </div>
                </div>
            </div>

            <div class="row">
                <div class="col-md-12">
                     <div class="mt-md-5 mt-4">
                     <button type="button" class="m-2 btn btn-outline-primary float-end" @click="$router.go('-1')"> <i class="bi-arrow-90deg-left"></i> Back</button>
                     </div>
                </div>
            </div>

        </div>
         </GeneralHeader>
    </div>
</template>

<style>
.lead{
  color: #0a010196;
font-size: 18px;

}
</style>
<script>
import appsettings from '../json/myapp.json'
// import axios from 'axios'
export default {
    data (){
        return{
        "settings":appsettings.settings,
        "appinfo":appsettings.appinfo,
        networkerror:appsettings.error.networkerror,
        alert: '',
        classname: '',
        record:false,
        norecord: '',
        toggle:null,
        opacity_enable:'opacity:0.7; pointer-events: none;',
        opacity_disable:'opacity:1; pointer-events:All;',
        opacity:'',
    }
    },

    created(){
    }, 
    methods:{
    },


    }
</script>
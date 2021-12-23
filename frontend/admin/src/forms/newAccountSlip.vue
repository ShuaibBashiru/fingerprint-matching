<template>
<div :style="opacity">
    <section v-if="usersession==true">
    <AdminHeader>
<div class="container-fluid mt-1 p-0">
<div class="row d-flex justify-content-center p-0">
    <div class="col-md-12 ps-0">
        <VueHtml2pdf style="margin: auto;"
        :show-layout="true"
        :float-layout="false"
        :enable-download="true"
        :preview-modal="false"
        :paginate-elements-by-height="1400"
        :filename="'Pre-Registration Slip For_'+accountSlip['surname']+'_'+accountSlip['firstname']"
        :pdf-quality="2"
        :manual-pagination="false"
        pdf-format="a4"
        pdf-orientation="portrait"
        pdf-content-width="100%"
        @progress="onProgress($event)"
        @hasStartedGeneration="hasStartedGeneration()"
        @hasGenerated="hasGenerated($event)"
        ref="html2Pdf"
        >
<section slot="pdf-content" class="m-md-5 mb-3 p-3">
    <div class="col-md-12 ps-0 text-center mb-5">
        <img src="@/assets/icons/logo.png" class="img-fluid" alt="" width="80">
    <h5 class="text-primary mb-2 ps-2">{{appinfo.appname}} REGISTRATION</h5>
    </div>
    <div class="col-md-12 ps-0 m-2 mt-4">
    <h4 class="mb-2 pb-2 border border-top-0 border-start-0 border-end-0">Registration Confirmation Slip</h4>
    <p class="mb-2 pb-2 text-dark pt-2"><strong>Basic Information </strong></p>
    <div class="table-responsive">
    <table class="table table-striped">
        <tbody>
            <tr><td>Application Number</td><td class="text-uppercase">{{accountSlip['applicant_number']}}</td></tr>
            <tr><td>Lastname</td><td class="text-uppercase">{{accountSlip['surname']}}</td></tr>
            <tr><td>Firstname</td><td class="text-uppercase">{{accountSlip['firstname']}}</td></tr>
            <tr><td>Email</td><td class="text-lowercase">{{accountSlip['email_one']}}</td></tr>
            <tr><td>Phone Number</td><td class="">{{accountSlip['phoneCode']}}{{accountSlip['phone_one']}}</td></tr>
            <tr><td>Registration date</td><td class="">{{accountSlip['date_created']}}</td></tr>
        </tbody>
    </table>
 </div>

    </div>
 <div class="col-md-12">
<p class="text-danger ps-2"><strong>Note: </strong>You are advised to download or save this Registration slip before you continue. Application number or Email provided and the password will be required at login.</p>
 </div>
    <div class="row mb-2">
         <div class="col-md-12">
             <div class="border pt-2 text-center"> <p> &copy; Copyright {{appinfo.year}} by {{appinfo.appname}}. All Rights Reserved</p> </div>
         </div>
    </div>
</section>
</VueHtml2pdf>
 <div class="col-md-12 ">
     <div class="ms-md-5 me-0 mt-0 p-3 pt-0">
     <button class="btn btn-outline-primary float-end me-5" @click="printPdf">Download pdf</button>
     </div>
 </div>
</div>
</div>
</div>
  </AdminHeader>
  </section>
</div>
</template>
<style>

</style>
<script>
import appsettings from '../json/myapp.json'
export default {
    data (){
        return{
        accountSlip:'',
        surname: '',
        alert: '',
        classname: '',
        record:false,
        norecord: '',
        toggle:'',
        usersession: false,
        appinfo: appsettings.appinfo,
        opacity_enable:'opacity:0.7; pointer-events: none;',
        opacity_disable:'opacity:1; pointer-events:All;',
        opacity:'',
    }
    },

    mounted (){
        this.checkSession()
    }, 
    methods:{
    checkSession: function(){
     if (!this.$session.exists) {
        window.location='/app/site/signin'
        }else{
            if(this.$session.get('accountSlip')){
             this.usersession = true
                this.getSession()
            }else{
                window.location='/app/site/signin'
            }
        }
    },
   printPdf: function(){
       this.$refs.html2Pdf.generatePdf()
   },
   getSession: function(){
      this.accountSlip = this.$session.get('accountSlip')
       }

    },


    }
</script>
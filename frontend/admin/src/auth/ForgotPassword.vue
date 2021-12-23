<template>
<div :style="opacity">
    <GeneralHeader>
<div class="col-md-9 mt-5 ms-auto">
<div class="container">
<div class="border">
<div class="row">
<div class="col-md-8">
    <div class="p-2">
            <form @submit.prevent="formCheck" class="needs-validation">
            <fieldset class="border p-2">
                <legend class="w-auto" style="float: none; padding: inherit;">Forgot password</legend>
            <div class="row">

            <div class="col-md-12">
                <div class="m-1 mt-2">
                        <input type="hidden" class="d-none" v-model="token" required readonly>
                    <label for="sname" class="pb-1 text-dark">Your email</label>
                <div class="input-group">
                    <span class="input-group-text"><i class="bi-briefcase"></i></span>
                    <input type="text" v-model="email" :disabled="isDisabled" id="email" class="form-control" required placeholder="Email address">
                </div>
                <small class="form-text text-muted">{{error}}</small>
                
                </div>
            </div>

            <div class="col-md-12 mt-2 text-center d-flex justify-content-end">
                <div class="m-1">
                    <label for=""></label>
                <div class="input-group">
                    <button type="submit" :disabled="isDisabled" class="btn btn-primary">{{submit}}</button>
                </div>
            </div>
            <small class="pb-2 text-danger text-center">{{error_btn}}</small>
            </div>
                </div>
                </fieldset>
            </form>
                <div class="col-md-12 mt-4 d-flex justify-content-end">
                <p class=""><a href="/app/site/signin">Sign in instead</a></p>
            </div>
        
    </div>
</div>

</div>
</div>
</div>

</div>

 </GeneralHeader>
</div>
</template>
<script>
import axios from 'axios'
import axios from 'axios'
export default {

    data (){
        return{
        email: null,
        record: false,
        alert:null,
                    token: '',
            isToken: false,
            tryAgain: 'd-none',
            validationClass: 'text-primary',
            validationMsg: 'Please wait while validating and redirecting to the requested page...',
        password: null,
        cpassword: null,
        languageCode: null,
        phone: null,
        countryCode: null,
        account_type: null,
        gender: null,
        selectDefault:"Select",
        classname:null,
        submit:'Proceed',
        submittxt:'Proceed',
        isDisabled:false,
        error: null,
        error_btn: null,
        opacity_enable:'opacity:0.7; pointer-events: none;',
        opacity_disable:'opacity:1; pointer-events:All;',
        opacity:'',
    }
    },
    created(){
    this.tokenize()
    },
    methods:{
        validEmail: function (email) {
    var re = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
    return re.test(email);
    },
    formCheck: function(e){
        if (!this.validEmail(this.email)) {
        this.err_email="Valid email is required.";
        }else{
            this.error="";
        this.submit="Please wait.."
        this.preview()
        }
    e.preventDefault();
    },
        preview: function(){
        this.norecord = 'Synchronizing...'
        this.$Progress.start()
        this.isDisabled = true
        this.opacity = this.opacity_enable
        const form = new FormData();
        form.append('email', this.email)
        form.append('csrfmiddlewaretoken', this.token)
        axios.post(process.env.VUE_APP_API_URL+'/posts/validate_email_id/', form)
        .then(response => {
            if(response.data.status == response.data.statusmsg){
            this.classname=response.data.classname
            this.alert=response.data.msg
            this.norecord=''
            this.record = true
            this.$Progress.finish()
            this.isDisabled = false
            this.opacity = this.opacity_disable 
            this.submit = this.submittxt
            setInterval(function(){
            window.location.href=response.data.redirect
            },3000)
            }else{
            this.record = false
            this.classname=response.data.classname
            this.alert=response.data.msg
            this.$Progress.finish()
            this.isDisabled = false
            this.opacity = this.opacity_disable
            this.submit = this.submittxt

            }
        }).catch(()=>{
            this.record = false
            this.classname='alert-danger p-2'
            this.alert=localStorage.getItem('error')
            this.$Progress.fail()
            this.isDisabled = false
            this.opacity = this.opacity_disable
            this.submit = this.submittxt

        })
    },


     tokenize: function(){
        this.$Progress.start()
    axios.get(process.env.VUE_APP_API_URL+'/auth/tokenize/',{
    params:{
      'token': Math.random(9, 9999)
    }
  }).then(response => {
      if(response.data.status==response.data.statusmsg){
      this.token=response.data.key
      axios.defaults.headers.common['X-CSRF-TOKEN'] = response.data.key;
      this.$Progress.finish()
      this.isDisabled = false
      }else{
      this.$Progress.finish()
      this.isDisabled = false
     this.classname='text-danger p-1 text-center'
      this.alert=localStorage.getItem('error')
      }
    
  }).catch(()=>{
      this.$Progress.fail()
      this.isDisabled = false
      this.classname='text-danger p-1 text-center'
      this.alert=localStorage.getItem('error')
  })
  },
    }


    }
</script>
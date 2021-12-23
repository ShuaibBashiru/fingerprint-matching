<template>
<div :style="opacity">
    <GeneralHeader>
<div class="container-fluid mt-2 p-0">
<section v-if="isToken">
<div class="row d-flex justify-content-center p-0 mt-2">
    <div class="col-md-5 mt-2 ps-0 m-2">
    <h5 class="text-primary mb-2 ps-3">Admin login</h5>
  <form @submit.prevent="signIn" role="form">
    <div class="m-1 mt-3">
  <div class="form-row p-3 border pt-2 pe-md-4 ps-md-4 pb-4 rounded m-2">
    <div class="form-group mt-4 col">
        <label for="userid" class="text-muted pb-2">Email</label>
        <input type="hidden" v-model="token" required>
      <input type="email" class="form-control form-control-md form-control-sm-lg" v-model="userid" placeholder="Enter your email address" id="userid" required maxlength="100" minlength="10">
    </div>
<!-- form-control form-control-md form-control-sm-lg -->
    <div class="form-group mt-4 col">
        <label for="pwd" class="text-muted pb-2">Password</label>
        <small class="float-end pb-2"><a href="#/app/site/forgotpassword" class="text-left">Forgot password?</a></small>
      <div class="input-group">
        <input :type="pass_type" class="form-control form-control-md form-control-sm-lg" v-model="pwd" placeholder="Password" id="pwd" required maxlength="50" minlength="3">
        <small class="input-group-text">
        <input class="form-check-input d-none" type="checkbox" id="showpass"
           v-model="toggle"
           true-value="yes"
          false-value="no" @change="showpassword">
        <label class="form-check-label" for="showpass">
        <small style=""> <i class="bi-eye"></i> </small>
        </label>
        </small>
      </div>
      <small class="text-muted"><strong>Note:</strong> Please note that your password is case sensitive </small>
    </div>

    <div class="form-group mt-2 col">
        <input class="form-check-input" type="checkbox" id="rememberme"
           v-model="rememberme_val"
           true-value="yes"
          false-value="no" @change="rememberme">
        <label class="form-check-label" for="rememberme">
        <small class="ps-2"> Remember me </small>
        </label>
    </div>


      <div class="form-group mt-4 col">
     <div class="row">
       <div class="col-md-12 mb-3 mt-1">
        <section v-if="alert!=''">
      <div v-bind:class="'alert '+ classname +' p-2 ps-3 pe-3 m-0 mb-1 mt-1 text-center border-0'"> <span></span> {{alert}} </div>
      </section>
       </div>
       <div class="col-md-12">
         <button type="submit" name="login" class="btn btn-primary form-control border-0" :disabled="isDisabled">{{button}}</button></div>
     </div>
    </div>

  </div>
  </div>
</form>
<!-- <div class="p-2 ps-0">
      <p class="ps-3">I do not have an account? <a href="/app/site/newaccount" class="text-right">
        Create an Account
      </a></p>
</div> -->
    </div>
</div>
</section>
<section v-else>
<div class="row mt-5">
  <div class="col-md-6 m-auto">
    <div class="card">
  <div class="card-header text-dark">
    Authentication
  </div>
  <div class="card-body">
    <p :class="'card-text '+ validationClass">{{validationMsg}}</p>
    <a @click="$router.go(0)" :class="'btn btn-primary float-end '+tryAgain">Try again</a>
  </div>
</div>
  </div>
</div>
</section>
</div>

  </GeneralHeader>
</div>
</template>
<style>

</style>
<script>
import axios from 'axios'
export default {
data(){
  return{
            info:[],
            alert:'',
            progress:null,
            userid:null,
            pwd:'',
            classname:'',
            rememberme: '',
            rememberme_val: '',
            token: '',
            isToken: false,
            tryAgain: 'd-none',
            validationClass: 'text-primary',
            validationMsg: 'Please wait while validating and redirecting to the requested page...',
            btntxt: 'Sign in',
            button: 'Sign in',
            isDisabled: false,
            toggle:null,
            pass_type:'password',
            opacity_enable:'opacity:0.7; pointer-events: none;',
            opacity_disable:'opacity:1; pointer-events:All;',
            opacity: this.opacity_disable,
         }

},
created(){
this.tokenize()
},

  methods:{
  tokenize: function(){
        this.$Progress.start()
    axios.get(process.env.VUE_APP_API+'/auth/tokenize/',{
    params:{
      'token': Math.random(9, 9999)
    }
  }).then(response => {
      if(response.data.status==response.data.statusmsg){
      this.token=response.data.key
      this.isToken=true
      this.tryAgain='d-none'
      axios.defaults.headers.common['X-CSRF-TOKEN'] = response.data.key;
      this.$Progress.finish()
      }else{
      this.$Progress.finish()
      this.isToken=false
      this.tryAgain=''
      this.validationClass = response.data.classname
      this.validationMsg=localStorage.getItem('error')
      } 
    
  }).catch(()=>{
      this.$Progress.fail()
      this.validationClass='text-danger p-2'
      this.validationMsg='Network error! refresh and try again or report this error on our contact page.'
      this.isToken=false
      this.tryAgain=''


  })
  },

       
        signIn(){
          this.button='Please wait...'
          this.$Progress.start()
          this.isDisabled = true
          this.opacity = this.opacity_enable
          const form = new FormData();
          form.append('userid', this.userid)
          form.append('password', this.pwd)
          form.append('csrfmiddlewaretoken', this.token)
          axios.post('/auth/signin/', form)
          .then(response => {
            if(response.data.status==response.data.statusmsg){
            this.classname=response.data.classname
            this.alert=response.data.msg
            this.button=this.btntxt
            this.$Progress.finish()
            this.isDisabled = false
            this.opacity = this.opacity_disable
            this.$session.start()
            this.$session.set('usersession', response.data.result)
            this.$session.set('chatSessionID', response.data.chatSessionID)
            setTimeout(function(){
            window.location.href=response.data.redirect
            },2000)
            }else{
            this.alert=response.data.msg
            this.classname=response.data.classname
            this.button=this.btntxt
            this.$Progress.finish()
            this.isDisabled = false
            this.opacity = this.opacity_disable
            }
          
        }).catch(()=>{
            this.alert=localStorage.getItem('error')
            this.classname='alert-danger p-2'
            this.button=this.btntxt
            this.$Progress.fail()
            this.isDisabled = false
            this.opacity = this.opacity_disable

        })
    },
    showpassword: function(){
      if(this.toggle=="yes"){
      this.pass_type = 'text'
      }else{
      this.pass_type = 'password'
      }
    },
    
   


},
// End of methods

}

</script>

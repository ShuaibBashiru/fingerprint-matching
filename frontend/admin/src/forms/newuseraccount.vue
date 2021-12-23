<template>
<div :style="opacity">
    <GeneralHeader>
<div class="container-fluid mt-2 p-0">
    <section v-if="isToken">
<div class="row d-flex justify-content-center p-0">
    <div class="col-md-8 ps-0 m-2 mt-2">
    <h5 class="text-primary mb-2 ps-2">Create an account</h5>
  <form @submit.prevent="formCheck" role="form">
      <div class="row border pt-2 pe-md-4 ps-md-4 pb-4 rounded m-2">
 <div class="col-md-6 mt-1">
                <div class="m-1 mt-3">
                        <input type="hidden" class="d-none" v-model="token" required readonly>
                    <label for="sname" class="pb-1 text-muted">Surname</label>
                <div class="input-group">
                    <span class="input-group-text"><i class="bi-person"></i></span>
                    <input type="text" v-model="surname"  id="sname" minlength="3" maxlength="40" class="form-control form-control-md form-control-sm-lg" required placeholder="Surname">
                </div>
                <small class="form-text text-muted"></small>
                
                </div>
            </div>

            <div class="col-md-6">
                <div class="m-1 mt-3">
                    <label for="fname" class="pb-1 text-muted">First Name</label>
                <div class="input-group">
                    <span class="input-group-text"><i class="bi-person"></i></span>
                    <input type="text" v-model="firstname"  minlength="3" maxlength="40" id="fname" class="form-control form-control-md form-control-sm-lg" required placeholder="First Name">
                </div>
                <small class="form-text text-muted"></small>
                
                </div>
            </div>

            <div class="col-md-6">
                <div class="m-1 mt-3">
                    <label for="email" class="pb-1 text-muted">Email</label>
                <div class="input-group">
                    <span class="input-group-text"><i class="bi-mailbox"></i></span>
                    <input type="email" v-model="email_one"  minlength="10" maxlength="100" id="email" class="form-control form-control-md form-control-sm-lg" required placeholder="Email address">
                </div>
                    <small class="form-text text-muted"></small>
                </div>
            </div>

        <div class="col-md-6">
                <div class="m-1 mt-3">
                    <label for="code" class="pb-1 text-dark">Phone Number</label>
                <div class="row">
                    <div class="col-4 pe-1">
                <div class="input-group">
                    <select class="form-control form-control-md form-control-sm-lg" v-model="phoneCode" id="code" required>
                       <option disabled value="" selected>Code</option>
                    <option :value="d['mcode']" v-for="(d, index) in phoneCodes" :key="index">{{d['ccode']}} {{d['mcode']}}</option>
                    </select>
                    </div>
                    </div>
                <div class="col-8 ps-0">
                <div class="input-group">
                    <input type="text" @change="checkPhone" v-model="phone_one" minlength="7" maxlength="15" id="phone" class="form-control form-control-md form-control-sm-lg" required placeholder="Number only">
                    </div>
                    <small class="pb-2 text-danger">{{phone_error}}</small>
                </div>
                    </div>
            
                </div>
            </div>

            <div class="col-md-6">
                <div class="m-1 mt-3">
               <label for="password" class="text-muted pb-2">Password</label>
      <div class="input-group">
        <input :type="pass_type" class="form-control form-control-md form-control-sm-lg" v-model="password" placeholder="Password" id="password" required maxlength="50" minlength="3">
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
      <small class="text-muted">A stong password is required to protect your account </small>
                </div>
            </div>
    
        <div class="col-md-6">
                <div class="m-1 mt-3">
               <label for="confirm_password" class="text-muted pb-2">Confirm password</label>
      <div class="input-group">
        <input :type="pass_type" @change="checkPass" class="form-control form-control-md form-control-sm-lg" v-model="confirm_password" placeholder="Re-type passsword" id="password" required maxlength="50" minlength="3">
      </div>
                    <small class="pb-2 text-danger text-center">{{password_error}}</small>

                </div>
            </div>

      <div class="col-md-12 mb-3 mt-1">
        <section v-if="alert!=''">
      <div v-bind:class="'alert '+ classname +' p-2 ps-3 pe-3 m-0 mb-1 mt-1 text-center border-0'"> <span></span> {{alert}} </div>
      </section>
       </div>

          <div class="col-md-9">
              <div class="mb-0 mt-3 ps-0">
            <p class="">By creating an account you agree to our <a href="">Terms of Service </a> & <a href="">Privacy policy.</a> </p>
              </div>
            </div>
      
   
        <div class="col-md-3 mt-3">
                <div class="m-1">
                    <button type="submit" :disabled="isDisabled" class="btn btn-primary float-end">{{submit}}</button>
                </div>
            </div>

  </div>
</form>
<div class="p-2 ps-0">
<p class="ps-2">I already have an account, log in instead? <a href="/app/site/signin" class="text-right">Log in</a></p>
</div>
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
import phonecodes from '../json/phoneCode'
import axios from 'axios'
export default {
    data (){
        return{
        formSuccess: 0,
        auth_check: false,
        token: '',
        isToken: false,
        tryAgain: 'd-none',
        validationClass: 'text-primary',
        validationMsg: 'Please wait while validating and redirecting to the requested page...',
        alert: '',
        alertmodal: '',
        phoneCodes: phonecodes.codes,
        error: '',
        info: [],
        checked: true,
        surname: '',
        firstname: '',
        email_one: '',
        phone_one: '',
        phoneCode: '+234',
        sessionid: '1',
        dob: '',
        mob: '',
        yob: '',
        othername: '',
        gender: '',
        personalId: '',
        password: '',
        confirm_password: '',
        loader: false,
        selectDefault:"Select",
        classname: 'alert-danger',
        submit: 'Create',
        submittxt:'Create',
        isDisabled: false,
        opacity_enable:'opacity:0.7; pointer-events: none;',
        opacity_disable:'opacity:1; pointer-events:All;',
        opacity:'',
        phone_error: '',
        password_error: '',
        form_error: '',
        errormodal: '',
        record:false,
        norecord: '',
        toggle:'',
        max_year: new Date().getFullYear() - 10,
        pass_type:'password',
        mob_list: [
            {"dm":'01', 'm':'January'},{"dm":'02', 'm':'February'},
            {"dm":'03', 'm':'March'},{"dm":'04', 'm':'April'},
            {"dm":'05', 'm':'May'},{"dm":'06', 'm':'June'},
            {"dm":'07', 'm':'July'},{"dm":'08', 'm':'August'},
            {"dm":'09', 'm':'September'},{"dm":'10', 'm':'October'},
            {"dm":'11', 'm':'November'},{"dm":'12', 'm':'December'},
            ],
        dob_list: ['01', '02', '03', '04', '05', '06', 
        '07', '08', '09', '10', '11', '12', '13', '14',
        '15', '16', '17', '18', '19', '20', '21', '22',
        '23', '24', '25', '26', '27', '28', '29', '30',
        '31']
    }
    },

    created(){
    this.tokenize()
    }, 

    methods:{
   tokenize: function(){
        this.$Progress.start()
    axios.get(process.env.VUE_APP_API+'/auth/token/tokenize/',{
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

        showpassword: function(){
      if(this.toggle=="yes"){
      this.pass_type = 'text'
      }else{
      this.pass_type = 'password'
      }
    },
    validEmail: function (email) {
    var re = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
    return re.test(email);
    },
    validDigit: function (digits) {
    var re = /^\d+$/;
    return re.test(digits);
    },

    checkPhone: function(){
    if(this.phone_one.startsWith(0)){
        this.phone_error="Kindly remove the leading ZERO";
    }else if(this.phone_one==''){
        this.phone_error="";
    }else{
        this.phone_error="";
        }
    },
     checkPass: function(){
   if(!this.password.match(/[a-z]+/) || !this.password.match(/[A-Z]+/) || !this.password.match(/[0-9]+/)){
        this.password_error="Weak password";
    } else if(this.password != this.confirm_password){
        this.password_error="Your password do not match";
    }else{
        this.password_error="";
        }
    },
    formCheck: function(e){
      if (!this.validEmail(this.email_one)) {
        this.alert="A valid email is required.";
        }else if(!this.validDigit(this.phone_one)){
        this.alert="A valid phone number is required.";
        }if(this.phone_one.startsWith(0)){
        this.alert="Kindly remove the leading ZERO from Phone number provided";
        }else if(!this.password.match(/[a-z]+/) || !this.password.match(/[A-Z]+/) || !this.password.match(/[0-9]+/)){
        this.alert="Weak password! Please use combination of uppercase, lowercase and number";
        }else if(this.password != this.confirm_password){
        this.alert="Your password do not match";
        }else{
              this.error_btn="";
            this.alert="";
            this.$confirm("You are about to submit this form, click Ok to continue or Cancel to go back?").then(() => {
            this.submit="Please wait.."
            this.addNew()
            });
        }
    e.preventDefault();
    },
    addNew: function(){
        this.$Progress.start()
        this.isDisabled = true
        this.opacity = this.opacity_enable
        this.submit='Please wait..'
        const form = new FormData();
        form.append('surname', this.surname)
        form.append('firstname', this.firstname)
        form.append('email', this.email_one)
        form.append('phoneCode', this.phoneCode)
        form.append('phone', this.phone_one)
        form.append('password', this.password)
        form.append('csrf_test_name', this.token)
        axios.post(process.env.VUE_APP_API+'/form/account/addnew', form)
        .then(response => {
        if(response.data.status==response.data.statusmsg){
        this.classname=response.data.classname
        this.alert=response.data.msg
        this.submit=this.submittxt
        this.$Progress.finish()
        this.isDisabled = false
        this.opacity = this.opacity_disable
        this.formSuccess = 1
        this.$session.start()
        this.$session.set('accountSlip', response.data.result)
        setInterval(function(){
        window.location=response.data.redirect
        },3000)
        }else{
        this.classname=response.data.classname
        this.alert=response.data.msg
        this.submit=this.submittxt
        this.$Progress.finish()
        this.isDisabled = false
        this.opacity = this.opacity_disable
        this.formSuccess = 2

        }
    }).catch(()=>{
        this.classname='alert-danger p-2'
        this.alert=localStorage.getItem('error')
        this.submit=this.submittxt
        this.$Progress.fail()
        this.isDisabled = false
        this.opacity = this.opacity_disable
        this.formSuccess = 2

    })  
    },

   


    },


    }
</script>
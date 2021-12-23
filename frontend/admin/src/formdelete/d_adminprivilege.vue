
<template>
<div :style="opacity">
<AdminHeader>
<div class="container p-0">
<div class="row">
<div class="col-6">
<div class="p-1 pb-0 ml-0 pl-0">
    <h5 class="mt-2 text-danger"> Trash </h5>
</div>
</div>
<div class="col-6 p-0 d-flex justify-content-end">
<div class="btn-toolbar m-1" role="toolbar" aria-label="Toolbar with button groups">
<div class="btn-group m-2" role="group" aria-label="First group" @click="$router.go(-1)"><button class="btn btn-outline-primary text-center">  <i class="bi-arrow-left"></i> Back </button></div>
</div>

</div>
</div>
</div>
  <section v-if="alert!=''">
      <div v-bind:class="'alert '+ classname +' p-2 ps-3 pe-3 m-0 mb-1 mt-1 text-center border-0'"> <span></span> {{alert}} </div>
  </section>
<section v-if="record==true">
<div class="container p-0">
<div class="border">
<div class="row">
<div class="col-md-12">
    <div class="p-2">
 <p class="text-danger p-3 pb-0 pt-0">Are you sure you want to delete this?! Please confirm before you take this unrecoverable action.</p>
    <section v-if="formSuccess == 0">
<form @submit.prevent="formCheck" class="needs-validation">
            <fieldset class="p-2 pt-0">
                    <div class="row m-md-0">
            <div class="col-md-5">
                <div class="m-1 mt-3">
                        <input type="hidden" class="d-none" v-model="token" required readonly>
                        <input type="hidden" class="d-none" v-model="keyid" required readonly>
                <div class="input-group">
                    <span class="input-group-text">User ID</span>
                    <input type="text" v-model="email" class="form-control" disabled readonly>
                </div>
                <small class="form-text text-muted"></small>
                
                </div>
            </div>
         <div class="col-md-5">
                <div class="m-1 mt-3">
                <div class="input-group">
                    <span class="input-group-text">Name</span>
                    <input type="text" v-model="menuname" class="form-control" required readonly placeholder="Name">
                </div>
                <small class="form-text text-muted"></small>
                <small class="text-danger"></small>
                
                </div>
            </div>

            <div class="col-md-2 d-flex justify-content-end">
                <div class="m-1 mt-3">
                <div class="input-group">
                    <button type="submit" :disabled="isDisabled" class="btn btn-danger">{{submit}}</button>
                </div>
                </div>
                    <small class="pb-2 text-danger text-center">{{error_btn}}</small>
            </div>

                </div>
                </fieldset>
            </form>
                    </section>
       
          <section v-else-if="formSuccess == 1" >
        <div class="container mt-5 mb-4">
            <div class="row">
            <div class="col-12">
            </div>
            <div class="col-12 mt-2 d-flex justify-content-center">
            <div class="btn-group">
                <button class="btn btn-primary m-2" @click="$router.go(-1)"> Go Back </button>
                </div>
            </div>
            </div>
        </div>
          </section>
           <section v-else>
        <div class="container mt-5 mb-4">
            <div class="row">
            <div class="col-12">
            </div>
            <div class="col-12 mt-2 d-flex justify-content-center">
            <div class="btn-group">
                <button class="btn btn-warning m-2" @click="$router.go(-1)"> Close this page </button>
                <button class="btn btn-primary m-2" @click="$router.go(0)">Try again</button>

                </div>
            </div>
            </div>
        </div>
          </section>
        
    </div>

</div>
</div>
</div>
</div>
</section>
<section v-else>
<div class="container">
    <div class="row">
    <div class="col-12 mt-2 d-flex justify-content-center">
    <div class="btn-group">
        <button class="btn btn-warning m-2" @click="$router.go(-1)"> Close this page </button>
        </div>
    </div>
    </div>
</div>
</section>

</AdminHeader>

</div>
</template>

<script>
import axios from 'axios'
import axios from 'axios'
export default {
    data (){
        return{
        formSuccess: 0,
         info:[],
        auth_check: false,
        alert: '',
        checked: true,
        keyid_validate: this.$route.params.id,
        keyid:'',
        selectToggleValue:'',
        isChecked:false,
        alertmodal: '',
                    token: '',
            isToken: false,
            tryAgain: 'd-none',
            validationClass: 'text-primary',
            validationMsg: 'Please wait while validating and redirecting to the requested page...',
        email: null,
        menuname: null,
        loader: false,
        selectDefault:"Select",
        classname: '',
        submit:'Delete',
        submittxt:'Delete',
        isDisabled: false,
        error_btn: null,
        record:null,
        norecord:null,
        opacity_enable:'opacity:0.7; pointer-events: none;',
        opacity_disable:'opacity:1; pointer-events:All;',
        opacity:'',
    }
    },

    created(){
    this.preview()
    this.tokenize()
    }, 

    methods:{
        showForm: function(){
        this.formSuccess = 0
        },
          formCheck: function(e){
         this.error_btn="";
            this.alert="";
            this.$confirm("Are you sure you want to delete this?, click Ok to continue or Cancel to go back?").then(() => {
            this.submit="Please wait.."
            this.delete()
            });
    e.preventDefault();
    },

       preview: function(){
        this.norecord = 'Synchronizing...'
        this.$Progress.start()
        this.isDisabled = true
        this.opacity = this.opacity_enable
        axios.get(process.env.VUE_APP_API_URL+'/api/adminprivilege/validate_id/', {
            params:{
                'keyid': this.keyid_validate
            },
        })
        .then(response => {
            if(response.data.status == response.data.statusmsg){
            this.alert=''
            this.classname=''
            this.norecord=''
            this.record = true
            this.info = response.data.result
            this.email = this.info['email_one']
            this.menuname = this.info['menu_description']
            this.keyid = this.info['keyid']
            this.$Progress.finish()
            this.isDisabled = false
            this.opacity = this.opacity_disable 
            }else{
            this.record = false
            this.alert=response.data.msg
            this.norecord=response.data.msg
            this.classname=response.data.classname
            this.$Progress.finish()
            this.isDisabled = false
            this.opacity = this.opacity_disable
            }
        }).catch(()=>{
            this.record = false
            this.classname='alert-danger p-2'
            this.alert=localStorage.getItem('error')
            this.norecord=localStorage.getItem('error')
            this.$Progress.fail()
            this.isDisabled = false
            this.opacity = this.opacity_disable
        })
    },

    delete: function(){
        this.$Progress.start()
        this.isDisabled = true
        this.opacity = this.opacity_enable
        const form = new FormData();
        form.append('title', this.title)
        form.append('keyid', this.keyid)
        form.append('itemName', this.info['uniqueCode'])
        form.append('csrfmiddlewaretoken', this.token)
        axios.post(process.env.VUE_APP_API_URL+'/posts/adminprivilege/delete/', form,{
        }).then(response => {
        if(response.data.status==response.data.statusmsg){
        this.classname=response.data.classname
        this.alert=response.data.msg
        this.submit=this.submittxt
        this.$Progress.finish()
        this.isDisabled = false
        this.formSuccess = 1
        this.opacity = this.opacity_disable
        setInterval(function(){
        window.history.back()
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
        this.classname='alert-danger p-2'
      this.alert=localStorage.getItem('error')
        this.opacity = this.opacity_enable
      } 
    
  }).catch(()=>{
      this.$Progress.fail()
      this.isDisabled = false
      this.classname='alert-danger p-2'
      this.alert=localStorage.getItem('error')
      this.opacity = this.opacity_enable

  })
  },


    },


    }
</script>
<template>
<div :style="opacity">
<AdminHeader>
<div class="container-fluid p-0">
<div class="row">
      <div class="col-md-12 mb-1">
        <section v-if="alert!=''">
      <div v-bind:class="'alert '+ classname +' p-2 ps-3 pe-3 m-0 mb-1 mt-1 text-center border-0'"> <span></span> {{alert}} </div>
      </section>
       </div>
</div>
<div class="row p-0">
    <div class="col-md-12 mb-3">
        <h4 class="text-primary">Identical Fingerprints Similarity (Male)</h4>
        <hr>
    </div>

    <div class="row">
        <div class="col-md-12">
            <div class="row">
                <div class="col-md"><h4 class="text-primary">Captured</h4></div>
                <div class="col-md"><button class="btn btn-primary mb-2 float-end" @click="preview">Reload</button></div>
                <div class="col-md"><button class="btn btn-outline-primary mb-2 float-end" @click="$router.push('/secure/classify')">Evaluation</button></div>
            </div>
            
            <section v-if="record==true">
            <div class="table-responsive">
                <table class="table table-hover table-bordered" id="myTable">
                    <thead>
                        <tr>
                            <th scope="col">s/n</th>
                            <th scope="col">Gender</th>
                            <th scope="col"></th>
                            <th scope="col" class="text-center">Date Created</th>
                        </tr>
                      </thead>
                      <tbody>
                    <tr v-for="(d, index) in info" :key="index">
                    <td> {{index + 1}} </td>
                    <td> {{d['Category']}} </td>
                    <td class="text-center"> <img src="@/assets/icons/fingericon.png" alt="" width="50"> </td>
                    <td class="text-center"> {{d['CreatedDate']}} </td>

                       </tr>
                            
                      </tbody>
                </table>
            </div>
</section>
<section v-else>
    <hr>
    <p class="text-danger mt-2">No record found</p>
</section>
    </div>
    </div>



</div>
</div>
</AdminHeader>
</div>
</template>

<style scoped>

</style>

<script>
import axios from 'axios'
export default {
    data (){
        return{
        auth_check: false,
        usersession: '',
        userdata:'',
        applicationMsg: 'Please wait while checking your application status',
        applicationStatus:null,
        token: '',
        isToken: false,
        tryAgain: 'd-none',
        validationClass: 'text-primary',
        validationMsg: 'Please wait while validating and redirecting to the requested page...',
        alert: '',
        alertmodal: '',
        error: '',
        info: [],
        info2: [],
        loader: false,
        loadermodal: false,
        classname: '',
        classnamemodal: null,
        submit: 'Submit',
        submittxt:'Submit',
        isDisabled: false,
        btntxt: 'Send',
        button: 'Send',
        opacity_enable:'opacity:0.7; pointer-events: none;',
        opacity_disable:'opacity:1; pointer-events:All;',
        opacity:'',
        errormodal: null,
        record:false,
        norecord: '',
        chatMessage: '',
        chatSessionID: '',
        currentChat: '',
        countPending: '',
        countClosed: '',
        person_one: '',
        person_two: '',
    }
    },

   created(){
        this.setStorage()
        this.checkSession()
        this.preview()
        },
        methods:{
            
        setStorage: function(){
        localStorage.setItem('error', this.networkerror)
        },

       checkSession: function(){
        if (this.$session.exists()) {
            this.usersession = this.$session.get('usersession')
            }else{
                return false
                }
        },



        formCheck: function(e){
            this.addNew()
    e.preventDefault();
    },


 preview: function(){
        this.$Progress.start()
        this.isDisabled = true
        this.opacity = this.opacity_enable
        axios.get(process.env.VUE_APP_API+'/api/list/getenrolled/',{
              params:{
                userid: this.usersession['email_one'],
            }
        })
        .then(response => {
            if(response.data.status == response.data.statusmsg){
            this.info = response.data.result
            this.$Progress.finish()
            this.isDisabled = false
            this.opacity = this.opacity_disable
            this.record = true
            }else{
            this.norecord = response.data.msg
            this.alert = response.data.msg
            this.classname = response.data.classname
            this.$Progress.finish()
            this.isDisabled = false
            this.opacity = this.opacity_disable
            this.record = false

            }
        
        }).catch(()=>{
            this.classname='alert-danger p-2'
            this.alert=localStorage.getItem('error')
            this.$Progress.fail()
            this.isDisabled = true
            this.opacity = this.opacity_disable
            this.record = false

        })
    },


    },



    }
</script>
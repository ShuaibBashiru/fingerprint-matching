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
        <h4 class="text-primary">Identical Fingerprints Similarity(Male)</h4>
        <hr>
    </div>

    <div class="row">
        <div class="col-md-12">
            <div class="row">
                <div class="col-md"><h4 class="text-dark">Finger templates</h4></div>
                <div class="col-md"><button class="btn btn-outline-primary mb-2 float-end" @click="formCheck">Compare</button></div>
            </div>
            
            <section v-if="record==true">
                
                <div class="row">

                    <div class="col-md-4">
                        <div class="row">
                <div class="col-md-12">
                        <div class="border">
                              <div class="m-1">
                <div class="input-group">
                   <span class="input-group-text">Person One</span>
                    <select v-model="finger_id_one" class="form-control" id="category" required>
                        <option disabled value="" selected>Select</option>
                        <option v-for="(d, index) in info" :key="index" :value="d['id']">{{d['Category']}} (Finger {{index+1}})</option>
                   </select>
                </div>
                </div>
                        </div>
                    </div>

                    <div class="col-md-12">
                        <div class="border">
                              <div class="m-1">
                <div class="input-group">
                   <span class="input-group-text">Person Two</span>
                    <select v-model="finger_id_two" class="form-control" id="category" required>
                        <option disabled value="" selected>Select</option>
                        <option v-for="(d, index) in info2" :key="index" :value="d['id']">{{d['Category']}} (Finger {{index+1}})</option>
                   </select>
                </div>
                </div>
                        </div>
                    </div>
                        </div>
                    </div>

                    <div class="col-md-2 text-center">
                         <img src="@/assets/icons/fingericon.png" alt="" width="80">
                    </div>

                    <div class="col-md-6">
                                     <div class="col-md-12">
                        <div class="border">
                              <div class="m-1">
                                 <div class="table-responsive">
                <table class="table table-hover table-bordered" id="myTable">
                <thead>
                        <tr>
                            <th scope="col">Gender</th>
                            <th scope="col">Identical(%)</th>
                            <th scope="col">Threshold</th>
                        </tr>
                </thead>
                 <tbody>
                    <tr>
                    <td> {{result['Category']}} </td>
                    <td> {{result['identical']}} </td>
                    <td> {{result['threshold']}} </td>
                       </tr>
                            
                      </tbody>
                </table>

                </div>

                                  
                        </div>
                        </div>
                    </div>

                    </div>


                  <div class="col-md-12">
                     <p class="text-muted mt-3"> Threshold: Recall that the algorithm used in this project to measure the matching score of the fingerprint templates is Levenshtein distance. </p>
                  </div>


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
        result: [],
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
        finger_id_one: '',
        finger_id_two: '',
        gender:'',
        identical:'',
        threshold:'',
    }
    },

   created(){
        this.setStorage()
        this.checkSession()
        this.preview()
        this.preview2()
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
            if (this.finger_id_one=='' || this.finger_id_two=='') {
                this.alert="Please select from person one and two"
            }else{
                this.classify()
            }
    e.preventDefault();
    },

 classify: function(){
        this.$Progress.start()
        this.opacity = this.opacity_enable
        axios.get(process.env.VUE_APP_API+'/api/list/classify2/',{
              params:{
                userid: this.usersession['email_one'],
                finger_id_one: this.finger_id_one,
                finger_id_two: this.finger_id_two,
            }
        })
        .then(response => {
            if(response.data.status == response.data.statusmsg){
            this.result = response.data.result
            this.$Progress.finish()
            this.opacity = this.opacity_disable
            }else{
            this.norecord = response.data.msg
            this.alert = response.data.msg
            this.classname = response.data.classname
            this.$Progress.finish()
            this.opacity = this.opacity_disable

            }
        
        }).catch(()=>{
            this.classname='alert-danger p-2'
            this.alert=localStorage.getItem('error')
            this.$Progress.fail()
            this.opacity = this.opacity_disable

        })
    },

 preview: function(){
        this.$Progress.start()
        this.isDisabled = true
        this.opacity = this.opacity_enable
        axios.get(process.env.VUE_APP_API+'/api/list/user/',{
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

    preview2: function(){
        this.$Progress.start()
        this.isDisabled = true
        this.opacity = this.opacity_enable
        axios.get(process.env.VUE_APP_API+'/api/list/user2/',{
              params:{
                userid: this.usersession['email_one'],
            }
        })
        .then(response => {
            if(response.data.status == response.data.statusmsg){
            this.info2 = response.data.result
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
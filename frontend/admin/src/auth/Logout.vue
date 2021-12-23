<template>
    <div>
    <GeneralHeader/>
<section v-if="loader==false">
</section>
<section v-else>
   <div class="container-fluid">
       <div class="row mt-5">
           <div class="col text-center">
               <p class="lead text-primary"><small>{{message}}</small></p>
           </div>
       </div>
   </div>
</section>

    </div>
</template>
<script>
import axios from 'axios'
export default {
data(){
    return{
        message: 'Logging out, please wait .....',
        statusMsg: null,
        error_found: false,
    }
},
created(){
   this.logout(); 
},
    methods:{
    logout: function(){
             this.$Progress.start()
          axios.get(process.env.VUE_APP_API+'/auth/logout/logmeout/')
        .then(response => {
            if(response.data.status==response.data.statusmsg){
                this.alert = response.data.msg
                this.message = 'You will be logged out in 3 seconds'
                this.classname = response.data.classname
                this.error_found = false
                this.$session.remove('chatSessionID')
                this.$session.remove('usersesseion')
                this.$session.destroy()
                this.$Progress.finish()
                setTimeout(function(){
                window.location.href=response.data.redirect
                },2000)
            }else{
                this.alert = response.data.msg
                this.classname = response.data.classname
                this.message = 'You will be logged out in 3 seconds'
                this.error_found = false
                this.$session.remove('chatSessionID')
                this.$session.remove('usersesseion')
                this.$session.destroy()
                this.$Progress.finish()
                 setTimeout(function(){
                window.location.href='/app/site/signin'
                },2000)
            }
        }).catch(()=>{
            this.alert = localStorage.getItem('error')
            this.classname = 'alert-danger'
            this.message = 'You will be logged out in 3 seconds'
            this.error_found = true
            this.$session.remove('chatSessionID')
            this.$session.remove('usersesseion')
            this.$session.destroy()
            this.$Progress.finish()
            setTimeout(function(){
            window.location.href='/app/site/signin'
            },2000)

        })
    },

}
}
</script>
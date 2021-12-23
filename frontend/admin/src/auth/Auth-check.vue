<template>
    <div>
    </div>
</template>
<script>
// import axios from 'axios'
export default {
data(){
    return{
        message: 'Please wait a moment..',
        statusMsg: null,
        error_found: false,
        loader:true,
        classname: 'text-primary',
        pagename: this.$route.name,
        alert: 'Please wait a moment..'

    }
},
created(){
//    this.checkSession(); 
},
    methods:{
                 checkSession: function(){
        if (!this.$session.exists()) {
            window.location='/app/site/logout'
                alert()
            }else{
                alert()
                if(this.$session.get('usersession')){
                this.isSession = true
                    this.getSession()
                    this.passport = this.usersession['applicant_number'].toLowerCase()+'.png'
                }else{
                    window.location='/app/site/logout'
                }
            }
    },

}
}
</script>
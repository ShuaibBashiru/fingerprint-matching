<template>
<div :style="opacity">
<div class="container-fluid menuheader border-bottom borderStyle">
<div class="row">
<div class="col-md-12">
<nav class="navbar navbar-expand-lg p-1 m-1 mt-0 mb-0">
<a class="navbar-brand" href="/app/" :style="appinfo.css.headercolor"><img src="@/assets/icons/logo.png" :width="appinfo.logoWidth" :height="appinfo.logoHeight"  alt=""> &nbsp; {{appinfo.appname}}</a>
<span class="navbar-toggler" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
<i class="bi-list text-white"></i>
</span>
<div class="collapse navbar-collapse" id="navbarSupportedContent">
<div style="border-top:1.5px solid #eee"></div>
    <ul class="navbar-nav m-0 p-0 ms-auto">
    <li class="nav-item"> <a class="nav-link" href="#/app/site/contact">HOW IT WORKS</a> </li>
    <li class="nav-item"> <a class="nav-link" href="#/app/site/contact">MEMBERS</a> </li>
    <li class="nav-item"> <a class="nav-link" href="#/app/site/contact">SAVINGS</a> </li>
    <li class="nav-item"> <a class="nav-link" href="#/app/site/contact">LOAN</a> </li>
    <li class="nav-item"> <a class="nav-link" href="#/app/site/contact">COMMODITIES</a> </li>
    <li class="nav-item"> <a class="nav-link" href="#/app/site/contact">TERMS & CONDITIONS</a> </li>
    </ul>
    <ul class="navbar-nav m-0 p-0 ms-auto">
    <li class="nav-item"> <a class="nav-link" href="/app/site/contact">CHAT US</a> </li>
    </ul>
</div>
</nav>
</div>
</div>
</div>
</div>
</template>
<style scoped>
.navbar-nav .nav-item a{
color:#ffffff;
font-size: 14px;
font-family: 'Geomanist book webfont',Arial,sans-serif;
}
</style>
<script>
import appsettings from '../json/myapp.json'
// import axios from 'axios'
export default {
data(){
return {
"media":appsettings.media,
"appinfo":appsettings.appinfo
}
}
}
</script>

var link = "http://127.0.0.1:8000/"
module.exports = {
  publicPath: process.env.VUE_APP_BASE_URL,
  outputDir: 'dist',
  devServer: {
    proxy: {
    "^/assets": {
        target: link,
        pathRewrite: { "^/passports/": "/passports/" },
        changeOrigin: true,
        logLevel: "debug"
      },
      // End user
      "^/auth": {
        target: link,
        pathRewrite: { "^/auth/": "/auth/" },
        changeOrigin: true,
        logLevel: "debug"
      },
      
      "^/admin": {
        target: link,
        pathRewrite: { "^/admin/": "/admin/" },
        changeOrigin: true,
        logLevel: "debug"
      },
      "^/user": {
        target: link,
        pathRewrite: { "^/user/": "/user/" },
        changeOrigin: true,
        logLevel: "debug"
      },
      "^/pub": {
        target: link,
        pathRewrite: { "^/pub/": "/pub/" },
        changeOrigin: true,
        logLevel: "debug"
      },
      "^/api": {
        target: link,
        pathRewrite: { "^/api/": "/api/" },
        changeOrigin: true,
        logLevel: "debug"
      },
      "^/upload": {
        target: link,
        pathRewrite: { "^/upload/": "/upload/" },
        changeOrigin: true,
        logLevel: "debug"
      },

    }
  }
};
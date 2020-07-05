const {verify} = require('hcaptcha');
 require("dotenv").config()
const secret = process.env.RECAPTCHA_SECRET_KEY// 'my hcaptcha secret from hcaptcha.com';
const token = process.env.RECAPTCHA_SITE_KEY;
 
verify(secret, token)
  .then((data) => console.log('success!', data))
  .catch(console.error);
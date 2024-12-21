const validator = require("validator");

console.log(validator.isEmail("ad@gmail.com"));
console.log(validator.isMobilePhone("081234567", "id-ID"));
console.log(validator.isNumeric("081234567"));

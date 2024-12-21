// console.log("Hello");

// const nama = "Ahmad Dani";

// const cetakNama = (nama) => `Hai, nama saya ${nama}`;

// console.log(cetakNama(nama));

// const fs = require(fs); //core modul
// const moment = require("moment"); // third party module / npm module / node_module

// const cetakNama = require("./coba"); //local modul

// console.log("Hello");

const coba = require("./coba");

// console.log(coba);

console.log(
  coba.cetakNama("Ahmad Dani"),
  coba.PI,
  coba.mahasiswa.cetatMhs(),
  new coba.Orang()
);

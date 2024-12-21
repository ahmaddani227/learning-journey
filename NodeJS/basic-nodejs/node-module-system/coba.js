// console.log("Hello World");

function cetakNama(nama) {
  return `Halo nama saya ${nama}`;
}

const mahasiswa = {
  nama: "Ahmad Dani",
  umur: 18,
  cetatMhs() {
    return `Halo, nama saya ${this.nama} dan saya berumur ${this.umur} tahun`;
  },
};

const PI = 3.14;

class Orang {
  constructor() {
    console.log("Objek orang telah dibuat");
  }
}

// module.exports.cetakNama = cetakNama;
// module.exports.PI = PI;
// module.exports.mahasiswa = mahasiswa;
// module.exports.Orang = Orang;

// module.exports = {
//   cetakNama: cetakNama,
//   PI: PI,
//   mahasiswa: mahasiswa,
//   Orang: Orang
// }

module.exports = {
  cetakNama,
  PI,
  mahasiswa,
  Orang,
};

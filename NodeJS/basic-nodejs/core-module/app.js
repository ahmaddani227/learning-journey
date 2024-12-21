// core module

// File System
const fs = require("fs");

// menulis string ke file secara synchronus

// try {
//   fs.writeFileSync("data/test.txt", "Hello World secara synchronus!");
// } catch (e) {
//   console.log(e);
// }

// menulis string ke file secara asynchronus

// fs.writeFile("data/test.txt", "Hello World secara asynchronus", (err) => {
//   console.log(err);
// });

// Membaca isi file (synchronus)

// const data = fs.readFileSync("data/test.txt", "utf-8");
// console.log(data);

// Membaca isi file (asynchronus)
// fs.readFile("data/test.txt", "utf-8", (err, data) => {
//   if (err) throw err;
//   console.log(data);
// });

// READLINE
const readline = require("readline");
const rl = readline.Interface({
  input: process.stdin,
  output: process.stdout,
});

// rl.question("Masukkan nama Anda : ", (nama) => {
//   console.log(`Terima Kasih ${nama}`);

//   rl.close();
// });
rl.question("Masukkan nama Anda : ", (nama) => {
  rl.question("Masukkan nomer Hp Anda : ", (noHp) => {
    const contact = { nama, noHp };

    const file = fs.readFileSync("data/contacts.json", "utf-8");

    const contacts = JSON.parse(file);
    contacts.push(contact);

    fs.writeFileSync("data/contacts.json", JSON.stringify(contacts));

    console.log("Terima Kasih sudah memasukkan data");

    rl.close();
  });
});
